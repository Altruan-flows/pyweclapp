from pydantic import BaseModel
from util.weclappClasses.weclappClassBlueprint import *
from .blueprintTemplate import Blueprint_Templates



class DeliveryAddress_Template(BaseModel, Blueprint_Templates):
    city:str = None
    company:str = None
    countryCode:str = "DE"
    firstName:str = None
    lastName:str = None
    street1:str = None
    street2:str = None
    zipcode:str = None
    phoneNumber: str = None
    
    # # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint_Templates.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)

    
    
    
class InvoiceAddress_Template(BaseModel, Blueprint_Templates):
    city:str = None
    company: str = None
    countryCode:str = "DE"
    firstName:str = None
    lastName:str = None
    street1:str = None
    street2:str = None
    zipcode:str = None
    phoneNumber: str = None
    
    
    # # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint_Templates.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
        

    
    
class Addresses_Template(BaseModel, Blueprint_Templates):
    id: str = ""
    version: str = ""
    city: str = None
    countryCode: str = None
    createdDate: int = None
    deliveryAddress: bool = None
    invoiceAddress: bool = None
    lastModifiedDate: int = None
    primeAddress: bool = None
    state: str = ""
    street1: str = None
    zipcode: str = None
    
    
    # # AutomationData
    ITEMS_NAME: str = "#"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint_Templates.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



 
    


        