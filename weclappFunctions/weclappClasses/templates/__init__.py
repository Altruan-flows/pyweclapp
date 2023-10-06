from util import weclapp
from .salesOrder import *
from .customer import *
from .addresses import *
from .blueprintTemplate import Blueprint_Templates


def createDataClassTemplate(newClassName:str, entity:dict, itemsName):
    # helps to generate Neu classes
    print(f"class {newClassName}(BaseModel, Blueprint):")
    for key, value in entity.items():
        if key == itemsName:
            classNameItemName = f"{itemsName[:1].upper()}{itemsName[1:]}"
            print(f"\t{key}: List[{classNameItemName}] = []")
        elif key == "customAttributes":
            print(f"\t{key}: List[WeclappMetaData] = []")
        else:
            print(f"\t{key}: {type(value).__name__}")
    print()
    print( f"\t# AutomationData")
    print( f'\tITEMS_NAME: str = "{itemsName}"')
    print( f"\tUSED_ATTRIBUTES: dict = dict()")
    print( f"\t__setattr__ = Blueprint.__setattr__")

    
    print( f"\tdef __init__(self, **kwargs):")
    print( f"\t\tBaseModel.__init__(self, **kwargs)")
    print( f"\t\tBlueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)")
    
    
    
