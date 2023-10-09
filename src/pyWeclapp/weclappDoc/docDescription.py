from .. import timeFunctions
import logging,  json, datetime
from typing import *


ALLOWED_DOC_TYPES = ['anlage2', 'anlage4', 'signature', 'pod', 'reciept', 'tzmo_LS', 'reciept2', '-', "kkDoc", "abrechnung"]
ALLOWED_DOC_TYPES_LITERAL = Literal['anlage2', 'anlage4', 'signature', 'pod', 'reciept', 'tzmo_LS', 'reciept2', '-', "kkDoc", "abrechnung"]
ALLOWED_DOC_FORMATS = ['pdf', 'png', 'tiff', "txt"]
ALLOWED_DOC_FORMATS_LITERAL = Literal['pdf', 'png', 'tiff', "txt"]



class DocDescription:
    @classmethod
    def fromString(cls, description:str, raiseError:bool=True):
        try:
            content = json.loads(description.replace("'", '"'))
            dd = cls(docType = content['docType'], docId = content['docId'], version=content.get('version', '0'))
            for key, value in content.items():
                setattr(dd, key, value)
        except json.JSONDecodeError as js:
            if raiseError:
                raise AssertionError(f">{description}< is not a vaild json")
            return None
        except KeyError as k:
            if raiseError:
                raise AssertionError(f"Key {k} not found in doc description")
            return None
        return dd
    
    @classmethod
    def fromDict(cls, docDict:dict, raiseError:bool=True):
        dd = cls.fromString(description=docDict['description'], raiseError=raiseError)
        assert dd.docId == docDict['id'], f"document id in description is not equal to actual Id"
        return dd
    
    
    
    def __init__(self, docType:ALLOWED_DOC_TYPES_LITERAL, docId:str, version:str='0') -> None:
        self.docType = docType
        self.docId = docId
        self.descVersion=version
        self.validateInput()
    
        
    def validateInput(self):
        # Validate docType
        if not isinstance(self.docType, str):
            raise AssertionError("docType must be a string")
        if not self.docType in ALLOWED_DOC_TYPES:
            raise AssertionError("docType is not in specified options")

        # Validate docId
        if not isinstance(self.docId, str):
            raise AssertionError("docId must be a string")
        if len(self.docId.split('.')) != 3:
            raise AssertionError("docId must contain exactly two dots")
        if not all(s.isdigit() for s in self.docId.split('.')[1:] if not s == ''):
            raise AssertionError("docId must contain only digits between dots")

    def getValue(self, key) -> str:
        if hasattr(self, key):
            return getattr(self, key)
        return None
    
    def __repr__(self):
        rep = []
        for attr in dir(self):
            if not callable(getattr(self, attr)) and not attr.startswith("__"):
                rep.append(f"{attr}={getattr(self, attr)}")
        return f"DocDescription({', '.join(rep)})"
                
    def setValue(self, key, value, to:Type[datetime.datetime]=str):
        if to == datetime.datetime:
            value = timeFunctions.localeDatetimeToStr(value, to="utcDate")
        setattr(self, key, str(value))
    
    def getDescriptionAsString(self) -> str:
        json_dict = {}
        for attr in dir(self):
            if not callable(getattr(self, attr)) and not attr.startswith("__"):
                json_dict[attr] = getattr(self, attr)
        return json.dumps(json_dict, indent=4).replace('"', "'")