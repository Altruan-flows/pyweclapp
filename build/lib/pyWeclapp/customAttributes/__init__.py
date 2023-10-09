from .. import weclapp
import logging
import json
from .citty import CITTY_Generator


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
        self.findAllCATs(self.entity)
        self.blackDict = blackDict
        logging.info(f"Found {len(self.customAttributes)} Custom Attributes")
    
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
        self.file = f'import json\nfrom collections import namedtuple\n\nclass CAT_{self.name}:\n\n\t@staticmethod\n\tdef is_namedtuple(obj):\n\t\ttry:\n\t\t\treturn isinstance(obj, tuple) and hasattr(obj, "_fields")\n\t\texcept:\n\t\t\treturn False\n\n\tdef __init__(self, data:dict=None):\n\t\tif data is None:\n\t\t\twith open("{self.targetDirectory}/customAttributes/catData_{self.name}.json", "r") as f:\n\t\t\t\tdata = json.load(f)\n\n'

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
            
    def updateInitFile(self):
        pass
