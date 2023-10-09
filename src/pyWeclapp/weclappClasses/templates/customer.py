from pydantic import BaseModel
from util.weclappClasses.weclappClassBlueprint import *
from .blueprintTemplate import Blueprint_Templates






class Customer_Template(BaseModel, Blueprint_Templates):
	id: str = None
	version: str = None
	addresses: list = []
	bankAccounts: list = []
	blocked: bool = None
	commissionSalesPartners: list = []
	company: str = None
	contacts: list = []
	createdDate: int = None
	currencyId: str = None
	currencyName: str = None
	customAttributes: list = []
	customerNumber: str = None
	customerTopics: list = []
	deliveryAddressId: str = None
	deliveryBlock: bool = None
	email: str = None
	firstName: str = None
	insolvent: bool = None
	insured: bool = None
	invoiceAddressId: str = None
	invoiceBlock: bool = None
	lastModifiedDate: int = None
	lastName: str = "No Lastname" # this field is required
	leadSourceId: str = None
	leadSourceName: str = None
	onlineAccounts: list = []
	optIn: bool = None
	optInLetter: bool = None
	optInPhone: bool = None
	optInSms: bool = None
	partyType: str = "PERSON" # this field is required
	paymentMethodId: str = None
	paymentMethodName: str = None
	phone: str = None
	primaryAddressId: str = None
	responsibleUserFixed: bool = None
	responsibleUserId: str =None
	responsibleUserUsername: str = None
	salesChannel: str = None
	salesPartner: bool = None
	salutation: str = None
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	tags: list = []
	termOfPaymentId: str = None
	termOfPaymentName: str = None
	useCustomsTariffNumber: bool = None

	# AutomationData
	ITEMS_NAME: str = "addresses"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint_Templates.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)