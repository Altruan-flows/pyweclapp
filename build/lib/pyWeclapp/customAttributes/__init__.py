from .. import weclapp
import logging
import json
from .citty import CITTY_Generator
import os


class CAT_Generator:
    def __init__(self, entityName:str, entityId:str, targetDirectory:str, blackDict:dict={}):
        """Creates or updated a CAT Class for a givern weclapp entity in a predefined directory
        it will use the 
        blackDict: dict = {catId: catName}; if catName is None the cat will be ignored"""
        self.entityName = entityName
        self.entityId = entityId
        self.targetDirectory = targetDirectory
        self.entity = weclapp.GET(entityName=entityName, entityId=entityId)
        self.customAttributes = set()
        self.groupedCatInfo = list()
        self.blackDict = blackDict
        logging.info(f"Found {len(self.customAttributes)} Custom Attributes")
        self.main()
        
        
    def main(self):
        self.findAllCATs(self.entity)
        self.parse()
        self.save()
        self.updateSuperClass()
        self.createCatSettings()
    
    def findAllCATs(self, d):
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
        return self.entityName[0].upper() + self.entityName[1:]

    
    def parse(self):
        for el in self.customAttributes:
            catName = None
            if el in self.blackDict:
                catName = self.blackDict[el]
                if not catName:
                    continue
            self.groupedCatInfo.append(CITTY_Generator.fromWeclapp(el, catName))
            
            
    def save(self, filetype="py"):
        self.newJson = {}
        self.file = f'import json\n'
        self.file += f'from . import cat_Settings\n'
        self.file += f'from collections import namedtuple\n\n'
        self.file += f'class CAT_{self.name}(cat_Settings.CAT_Settings):\n\n'
        self.file += f'\t@staticmethod\n\tdef is_namedtuple(obj):\n\t\ttry:\n\t\t\treturn isinstance(obj, tuple) and hasattr(obj, "_fields")\n\t\texcept:\n\t\t\treturn False\n\n'
        self.file += f'\tdef __init__(self, data:dict=None):\n\t\tsuper().__init__()\n\t\tif data is None:\n\t\t\twith open("{self.targetDirectory}/catData_{self.name}.json", "r") as f:\n\t\t\t\tdata = json.load(f)\n\n'

        lastGroupName = None
        for citty in sorted(self.groupedCatInfo, key=lambda x: x.groupName):
            assert isinstance(citty, CITTY_Generator), f"Expected CITTY_Generator got {type(citty)}"
            if lastGroupName != citty.groupName:
                lastGroupName = citty.groupName
                self.file += f"\n"
                self.file += f"\t\t# {self.name} - {citty.groupName}\n"

            self.newJson[citty.catName] = citty.getDict()
            self.file += citty.getPythonCode()
        
        # Save Json to singleFile
        with open(f"{self.targetDirectory}/catData_{self.name}.json", 'w+') as f:
            json.dump(self.newJson, f, indent=4)
            
        try:
            with open(f"{self.targetDirectory}/allCatData.json", 'r') as f:
                data = dict(json.load(f))
                data.update(self.newJson)
                totalJson = data
        except:
            totalJson = self.newJson
            
        with open(f"{self.targetDirectory}/allCatData.json", "w+") as f:
            json.dump(totalJson, f, indent=4)
            
            
        with open(f"{self.targetDirectory}/cat_{self.name}.{filetype}", 'w+') as f:
            f.write(self.file)
            
    def createCatSettings(self):
        fileContent = f"class CAT_Settings:\n"
        fileContent += f"\tdef __init__(self, data:dict=None):\n"
        fileContent += f"\t\t# You can place global cat settings here. they will not be modified\n"
        fileContent += f"\t\tpass\n"
        
        if not os.path.exists(f"{self.targetDirectory}/cat_Settings.py"):
            with open(f"{self.targetDirectory}/cat_Settings.py", "w+") as file:
                file.write(fileContent)

    
    def estimateClassName(self, fileName:str):
        return fileName.replace("cat", "CAT")
        
        
    def updateSuperClass(self):

        # List all files in the directory
        all_files = os.listdir(self.targetDirectory)

        # Filter out files that are not Python files or are the __init__.py file
        python_files = [f for f in all_files if f.endswith('.py') and f not in ['__init__.py', "cat.py"]]

        # Extract names without the .py extension
        module_names = [os.path.splitext(f)[0] for f in python_files]

        # Generate import statements
        import_statements = [f"from . import {module}" for module in module_names]
        import_statements.append("import json")
        # import_statements.append("import os")
        
        model = ", ".join([f"{module}.{self.estimateClassName(module)}" for module in module_names])

        fileContent = "\n".join(import_statements)
        fileContent += "\n# dynamic File please do not edit\n"
        fileContent += f"\n\n\n\nclass CAT({model}):\n"
        fileContent += f"\tdef __init__(self):\n"
        # fileContent += f"\t\tcurrent_directory = os.path.dirname(os.path.abspath(__file__))\n"
        # fileContent += f'\t\tfile_path = os.path.join(current_directory, "allCatData.json")\n'
        fileContent += f"\t\twith open(\"{self.targetDirectory}/allCatData.json\", \"r\") as f:\n"
        fileContent += f"\t\t\tself.data = json.load(f)\n"
        fileContent += f"\t\tsuper().__init__(self.data)\n"
        fileContent += f"\n\n\n\n"
        
        with open(f"{self.targetDirectory}/cat.py", "w+") as file:
            file.write(fileContent)
            
        # update Init.py dile
        module_names.append("cat")
        
        currentImports = [f"from .{fileName} import *" for fileName in module_names]
            
        with open(f"{self.targetDirectory}/__init__.py", "w+") as file:
            currentImports.insert(0, "# dynamic File please do not edit\n")
            file.write("\n".join(currentImports))

