from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import Addresses


class Contact(BaseModel, Blueprint):
	id: str
	version: str
	addresses: List[Addresses] = []
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	company:str=None
	email: str = None
	firstName: str = None
	lastModifiedDate: int
	lastName: str = None
	onlineAccounts: list = []
	optIn: bool = None
	optInLetter: bool = None
	optInPhone: bool = None
	optInSms: bool = None
	partyType: str
	primaryAddressId: str
	salutation: str = None
	tags: list = []
	title: str = None
	titleId: str = None
 

	# AutomationData
	ITEMS_NAME: str = "addresses"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
 
 
class Party(BaseModel, Blueprint):
	id: str
	version: str
	addresses: List[Addresses] = []
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	email: str
	firstName: str
	lastModifiedDate: int
	lastName: str
	onlineAccounts: list
	optIn: bool
	optInLetter: bool
	optInPhone: bool
	optInSms: bool
	partyType: str
	primaryAddressId: str
	salutation: str = None
	tags: list
	title: str = None
	titleId: str = None

	# AutomationData
	ITEMS_NAME: str = "addresses"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)