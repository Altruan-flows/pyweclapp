from util import weclapp, weclappClasses
from util.weclappClasses.weclappClassBlueprint import *
import logging
from typing import *
import json






class Blueprint_Templates(Blueprint):
    
    def __init__(self, itemsName: str, usedAtts: dict):
        super().__init__(itemsName, usedAtts)
        
        
    def incrementVersion(self):
        raise Exception("This method does not work in this class")
            
    def refreshVersion(self):
        raise Exception("This method does not work in this class")
    

    def updateWeclapp(self, updateType:Literal['full', 'used', "used+"]='full', setLoopVersion:bool=False, entityName:str=None) -> dict:
        raise Exception("This method does not work in this class")


    def updateWeclapp2(self, updateType:Literal['full', 'used', "used+"]='full', setLoopVersion:bool=False, entityName:str=None) -> dict:
        raise Exception("This method does not work in this class")
    
    
    def updateEntity(self, updateType:Literal['full', 'used', "used+"]='full', log:bool=False):
        raise Exception("This method does not work in this class")
        
        
    def refershEntity(self):
        raise Exception("This method does not work in this class")
            

    @classmethod
    def fromWeclapp(cls, entityName:str, entityId:str):
        raise Exception("This method does not work in this class")
    
    @classmethod
    def fromWeclapp2(cls, entityId:str):
        raise Exception("This method does not work in this class")
    
    @property
    def __entityName__(self) -> str:
        classType = type(self)
        entityName = str(classType.__name__)
        entityName = entityName[:1].lower() + entityName[1:]
        mark = entityName.find("_Template")
        entityName = entityName[:mark]
        return entityName
    
    def create_entity(self, entityName:str=None):
        if entityName is None:
            entityName = self.__entityName__
        body = self.getUpdateDict("full")
        new = weclapp.POST(entityName, body)
        return new