from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData
from pydantic import BaseModel
from typing import *



class Address(BaseModel, Blueprint):
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	firstName: str = None
	globalLocationNumber: str = None
	lastName: str = None
	middleName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class AdditionalAddresses(BaseModel, Blueprint):
	id: str
	version: str
	address: Address = Address.fromBlank()
	createdDate: int
	description: str = None
	lastModifiedDate: int



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class CommissionSalesPartners(BaseModel, Blueprint):
	id: str
	version: str
	commissionFix: str = None
	commissionPercentage: str = None
	commissionType: str = None
	createdDate: int
	lastModifiedDate: int
	salesPartnerSupplierId: str = None
	salesPartnerSupplierNumber: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ContractCostItems(BaseModel, Blueprint):
	id: str
	version: str
	articleId: str = None
	createdDate: int
	description: str = None
	descriptionFixed: bool
	discountPercentage: str = None
	interval: str = None
	intervalType: str = None
	lastModifiedDate: int
	manualUnitPrice: bool
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	note: str = None
	quantity: str = None
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	title: str = None
	unitId: str = None
	unitPrice: str = None
	unitPriceInCompanyCurrency: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class CommissionSalesPartners(BaseModel, Blueprint):
	id: str
	version: str
	commissionFix: str = None
	commissionPercentage: str = None
	commissionType: str = None
	createdDate: int
	lastModifiedDate: int
	salesPartnerSupplierId: str = None
	salesPartnerSupplierNumber: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ReductionAdditionItems(BaseModel, Blueprint):
	position: int = None
	source: str = None
	type: str = None
	value: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ContractItems(BaseModel, Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	articleId: str = None
	articleNumber: str = None
	billingGroupId: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	costTypeId: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	descriptionFixed: bool
	discountPercentage: str = None
	freeTextItem: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	groupName: str = None
	interval: str = None
	intervalType: str = None
	lastModifiedDate: int
	manualQuantity: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountForStatistics: str = None
	netAmountForStatisticsInCompanyCurrency: str = None
	netAmountInCompanyCurrency: str = None
	nextContractBillingDate: int = None
	note: str = None
	parentItemId: str = None
	positionNumber: int = None
	previousContractBillingDate: int = None
	quantity: str = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	servicePeriodFromDate: int = None
	servicePeriodToDate: int = None
	taxId: str = None
	taxName: str = None
	title: str = None
	type: str = None
	unitId: str = None
	unitName: str = None
	unitPrice: str = None
	unitPriceInCompanyCurrency: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class CorrespondenceAddress(BaseModel, Blueprint):
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	firstName: str = None
	globalLocationNumber: str = None
	lastName: str = None
	middleName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class DeliveryAddress(BaseModel, Blueprint):
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	firstName: str = None
	globalLocationNumber: str = None
	lastName: str = None
	middleName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class DeliveryEmailAddresses(BaseModel, Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class InvoiceAddress(BaseModel, Blueprint):
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	firstName: str = None
	globalLocationNumber: str = None
	lastName: str = None
	middleName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class PurchaseEmailAddresses(BaseModel, Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class RecordEmailAddresses(BaseModel, Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class SalesInvoiceEmailAddresses(BaseModel, Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class SalesOrderEmailAddresses(BaseModel, Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Types(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Contract(BaseModel, Blueprint):
	id: str
	version: str
	additionalAddresses: List[AdditionalAddresses] = []
	authorizationUnitId: str = None
	automaticExtension: bool
	billUntil: str = None
	billingDay: int = None
	billingTargetInvoiceStatus: str = None
	billingType: str = None
	cancellationDate: int = None
	cancellationPeriodQuantity: int = None
	cancellationPeriodSoftframe: str = None
	cancellationPeriodUnit: str = None
	commercialLanguage: str = None
	commission: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	contractCostItems: List[ContractCostItems] = []
	contractDate: int = None
	contractItems: List[ContractItems] = []
	contractNumber: str = None
	contractNumberAtParty: str = None
	contractStatus: str = None
	correspondenceAddress: CorrespondenceAddress = CorrespondenceAddress.fromBlank()
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
	deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.fromBlank()
	description: str = None
	differingCorrespondenceAddress: bool
	differingDeliveryAddress: bool
	differingInvoiceAddress: bool
	disableEmailTemplate: bool
	endDate: int = None
	extensionQuantity: int = None
	extensionUnit: str = None
	factoring: bool
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	invoiceRecipientId: str = None
	lastModifiedDate: int
	latestCancellationWarningQuantity: int = None
	latestCancellationWarningUnit: str = None
	latestPossibleTerminationDate: int = None
	name: str = None
	nextContractBillingDate: int = None
	nonStandardInputTaxId: str = None
	orderNumberAtCustomer: str = None
	partyId: str = None
	paymentMethodId: str = None
	pricingDate: int = None
	purchaseEmailAddresses: PurchaseEmailAddresses = PurchaseEmailAddresses.fromBlank()
	recordComment: str = None
	recordCurrencyId: str = None
	recordCurrencyName: str = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	reminderDate: int = None
	reminderSendType: str = None
	reminderType: str = None
	responsibleUserId: str = None
	salesChannel: str = None
	salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.fromBlank()
	salesOrderEmailAddresses: SalesOrderEmailAddresses = SalesOrderEmailAddresses.fromBlank()
	sentToRecipient: bool
	startDate: int = None
	tags: list = [] # could not be parsed
	template: bool
	termOfPaymentId: str = None
	terminationReasonId: str = None
	ticketServiceLevelAgreementId: str = None
	types: List[Types] = []
	unlimited: bool



	# AutomationData
	ITEMS_NAME: str = "contractItems"
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



