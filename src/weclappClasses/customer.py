from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import Addresses






class Customer(BaseModel, Blueprint):
	id: str
	version: str
	addresses: List[Addresses] = []
	bankAccounts: list = []
	blocked: bool
	commissionSalesPartners: list
	contacts: list = []
	createdDate: int
	currencyId: str
	currencyName: str
	customAttributes: List[WeclappMetaData] = []
	customerNumber: str
	customerTopics: list = []
	deliveryAddressId: str = ""
	deliveryBlock: bool
	email: str = ""
	firstName: str = ""
	insolvent: bool
	insured: bool
	invoiceAddressId: str = ""
	invoiceBlock: bool
	lastModifiedDate: int
	lastName: str = ""
	leadSourceId: str = ""
	leadSourceName: str = ""
	onlineAccounts: list = []
	optIn: bool
	optInLetter: bool
	optInPhone: bool
	optInSms: bool
	partyType: str
	paymentMethodId: str = ""
	paymentMethodName: str = ""
	phone: str = ""
	primaryAddressId: str
	responsibleUserFixed: bool
	responsibleUserId: str
	responsibleUserUsername: str
	salesChannel: str
	salesPartner: bool = False	# -------
	salutation: str = ""
	shipmentMethodId: str = ""
	shipmentMethodName: str = ""
	tags: list = []
	termOfPaymentId: str
	termOfPaymentName: str
	useCustomsTariffNumber: bool

	# AutomationData
	ITEMS_NAME: str = "addresses"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
