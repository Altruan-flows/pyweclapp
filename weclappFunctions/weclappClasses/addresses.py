from pydantic import BaseModel
from .weclappClassBlueprint import *



class DeliveryAddress(BaseModel, Blueprint):
    city:str = None
    company:str = None
    countryCode:str = "DE"
    firstName:str = None
    lastName:str = None
    street1:str = None
    zipcode:str = None
    phoneNumber: str = None
    
    # # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)

    
    
    
class InvoiceAddress(BaseModel, Blueprint):
    city:str = None
    company: str = None
    countryCode:str = "DE"
    firstName:str = None
    lastName:str = None
    street1:str = None
    zipcode:str = None
    phoneNumber: str = None
    
    
    # # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
        

    
    
class Addresses(BaseModel, Blueprint):
    id: str
    version: str
    city: str = None
    countryCode: str = None
    createdDate: int
    deliveryAddress: bool
    invoiceAddress: bool
    lastModifiedDate: int
    primeAddress: bool
    state: str = ""
    street1: str = None
    zipcode: str = None
    
    
    # # AutomationData
    ITEMS_NAME: str = "#"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



 
    


        