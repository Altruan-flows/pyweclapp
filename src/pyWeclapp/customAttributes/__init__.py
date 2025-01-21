from .. import weclapp
import logging
import json
from .kitty import KITTY_Generator
import os
from . import config
from typing import Tuple, List


class CAT_Generator:
    def __init__(self, entityName: str, entityId: str, targetDirectory: str):
        """Creates or updated a CAT Class for a givern weclapp entity in a predefined directory
        it will use the
            - entityName:       as the name of the weclapp entity
            - entityId:         as the id of the weclapp entity
            - targetDirectory   desired directory to save the file in
            - StaticOrExcludedIDs.json File - Schema: {catId: catName}; Method to manually rename or exclude (catName=null) a cat
            - cat_Settings.py File: File to manually save other constants related to cats.
        """
        self.entityName = entityName
        self.entityId = entityId
        self.targetDirectory = targetDirectory
        self.entity = weclapp.GET(entity_name=entityName, entity_id=entityId)
        self.customAttributes = set()
        self.defaultCustomAttributes = set()
        self.groupedCatInfo: List[KITTY_Generator] = list()
        self.staticOrExcludedIDs = self.openOrAddStaticOrExcludedIDs()
        logging.info(f"Found {len(self.customAttributes)} Custom Attributes")

        # MAIN SEQUENCE
        self.findAllCATs(self.entity)
        self.findeDefaultCATs(self.entity)
        self.parse()
        self.generatePyFile()
        self.save()
        self.updateSuperClass()
        self.createCatSettings()

    def openOrAddStaticOrExcludedIDs(self):
        """opens the staticOrExcludedIDs.json file and returns the content as a dict, creates a new one if none exists"""
        if not os.path.exists(self.targetDirectory):
            os.mkdir(self.targetDirectory)

        if not os.path.exists(
            f"{self.targetDirectory}/{config.STATIC_IDS_JSON_FILE}.json"
        ):
            with open(
                f"{self.targetDirectory}/{config.STATIC_IDS_JSON_FILE}.json", "w+"
            ) as f:
                json.dump(config.STATIC_OR_EXCLUDED_IDS, f, indent=4)

        with open(
            f"{self.targetDirectory}/{config.STATIC_IDS_JSON_FILE}.json", "r"
        ) as f:
            return dict(json.load(f))

    def findeDefaultCATs(self, d):
        """finds the first layer of customAttributes and adds them to the defaultCustomAttributes set"""
        for cat in d.get("customAttributes", []):
            self.defaultCustomAttributes.add(cat["attributeDefinitionId"])

    def findAllCATs(self, d):
        """iterates recursively through a dict and finds all customAttributes regardless of the nesting"""
        if isinstance(d, dict):
            for key, value in d.items():
                if isinstance(value, list):
                    self.findAllCATs(value)
                elif key == "attributeDefinitionId":
                    self.customAttributes.add(value)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, (dict, list)):
                    self.findAllCATs(item)
        else:
            pass

    @property
    def name(self):
        """returns the name of the class"""
        return self.entityName[0].upper() + self.entityName[1:]

    def parse(self):
        """converts the customAttributes into KITTY_Generator objects and adds them to the groupedCatInfo list"""
        for el in self.customAttributes:
            prefix = ""
            catName = None
            if el in self.staticOrExcludedIDs:
                catName = self.staticOrExcludedIDs[el]
                prefix += str(config.PREFIX_GROUPNAME_STATIC_IDS)
                if not catName:
                    continue
            # sets Prefixes to better identify the group
            if not el in self.defaultCustomAttributes:
                prefix += str(config.PREFIX_GROUPNAME_ITEMS_ATTS)
            self.groupedCatInfo.append(
                KITTY_Generator.fromWeclapp(el, catName, groupNamePrefix=prefix)
            )

    def generatePyFile(self) -> Tuple[str, dict]:
        """Construcs the python file from the groupedCatInfo list and returns it as a string"""
        self.newJson = {}
        self.file = f"import json\n"
        self.file += f"from . import {config.FILENAME_CAT_SETTINGS}\n"
        self.file += f"from collections import namedtuple\n\n\n"
        self.file += (
            f"class CAT_{self.name}({config.FILENAME_CAT_SETTINGS}.CAT_Settings):\n\n"
        )
        self.file += f'\t@staticmethod\n\tdef is_namedtuple(obj):\n\t\ttry:\n\t\t\treturn isinstance(obj, tuple) and hasattr(obj, "_fields")\n\t\texcept:\n\t\t\treturn False\n\n'
        self.file += f'\tdef __init__(self, data:dict=None):\n\t\tsuper().__init__()\n\t\tif data is None:\n\t\t\twith open("{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}/{self.entityName}.json", "r") as f:\n\t\t\t\tdata = json.load(f)\n\n'

        lastGroupName = None
        for kitty in sorted(self.groupedCatInfo, key=lambda x: x.groupName):
            if not isinstance(kitty, KITTY_Generator):
                raise AssertionError(f"Expected KITTY_Generator got {type(kitty)}")

            if lastGroupName != kitty.groupName:
                lastGroupName = kitty.groupName
                self.file += f"\n"
                self.file += f"\t\t# {kitty.groupName}\n"

            self.newJson[kitty.catName] = kitty.to_dict()
            self.file += kitty.getPythonCode()

    def save(self, filetype=config.FILE_TYPE):

        # CHECK IF DIRECTORY EXISTS and create it if not
        if not os.path.exists(self.targetDirectory):
            os.mkdir(self.targetDirectory)

        if not os.path.exists(f"{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}"):
            os.mkdir(f"{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}")

        # SAVE ATTRIBUTES
        with open(
            f"{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}/{self.entityName}.json",
            "w+",
        ) as f:
            json.dump(self.newJson, f, indent=4)

        pathToAllCatData = f"{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}/{config.FILENAME_ALL_CAT_DATA}.json"
        if os.path.exists(pathToAllCatData):
            # read all other cat data
            with open(pathToAllCatData, "r") as f:
                data = dict(json.load(f))
                data.update(self.newJson)
                totalJson = data
        else:
            totalJson = self.newJson

        with open(pathToAllCatData, "w+") as f:
            json.dump(totalJson, f, indent=4)

        # WRITE PYTHON FILE
        with open(f"{self.targetDirectory}/cat_{self.name}.{filetype}", "w+") as f:
            f.write(self.file)

    def createCatSettings(self):
        """creates a cat_Settings.py file if none exists"""
        fileContent = f"from collections import namedtuple\n\n"
        fileContent += f"class CAT_Settings:\n"
        fileContent += f"\tdef __init__(self, data:dict=None):\n"
        fileContent += (
            f"\t\t# You can place global cat settings here. they will not be modified\n"
        )
        fileContent += f"\t\tpass\n"

        if not os.path.exists(
            f"{self.targetDirectory}/{config.FILENAME_CAT_SETTINGS}.py"
        ):
            with open(
                f"{self.targetDirectory}/{config.FILENAME_CAT_SETTINGS}.py", "w+"
            ) as file:
                file.write(fileContent)

    def estimateClassName(self, fileName: str):
        return fileName.replace("cat", "CAT")

    def updateSuperClass(self):

        # List all files in the directory
        all_files = os.listdir(self.targetDirectory)

        # Filter out files that are not Python files or are the __init__.py file
        python_files = [
            f
            for f in all_files
            if f.endswith(".py") and f not in ["__init__.py", "cat.py"]
        ]

        # Extract names without the .py extension
        module_names = [os.path.splitext(f)[0] for f in python_files]

        # Generate import statements
        import_statements = [f"from . import {module}" for module in module_names]
        import_statements.append("import json")
        # import_statements.append("import os")

        model = ", ".join(
            [f"{module}.{self.estimateClassName(module)}" for module in module_names]
        )

        fileContent = "\n".join(import_statements)
        fileContent += "\n# dynamic File please do not edit\n"
        fileContent += f"\n\nclass CAT({model}):\n"
        fileContent += f"\tdef __init__(self):\n"
        fileContent += f'\t\twith open("{self.targetDirectory}/{config.JSON_DATA_FOLDER_NAME}/{config.FILENAME_ALL_CAT_DATA}.json", "r") as f:\n'
        fileContent += f"\t\t\tself.data = json.load(f)\n"
        fileContent += f"\t\tsuper().__init__(self.data)\n"
        fileContent += f"\n\n"

        with open(f"{self.targetDirectory}/cat.py", "w+") as file:
            file.write(fileContent)

        # update Init.py dile
        module_names.append("cat")

        currentImports = [f"from .{fileName} import *" for fileName in module_names]

        with open(f"{self.targetDirectory}/__init__.py", "w+") as file:
            currentImports.insert(0, "# dynamic File please do not edit\n")
            file.write("\n".join(currentImports))
