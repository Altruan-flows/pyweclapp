from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData
from pydantic import BaseModel
from typing import *



class Addresses(BaseModel, Blueprint):
	id: str
	version: str
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	createdDate: int
	deliveryAddress: bool
	firstName: str = None
	globalLocationNumber: str = None
	invoiceAddress: bool
	lastModifiedDate: int
	lastName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	primeAddress: bool
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



class BankAccounts(BaseModel, Blueprint):
	id: str
	version: str
	accountHolder: str = None
	accountNumber: str = None
	bankCode: str = None
	createdDate: int
	creditInstitute: str = None
	lastModifiedDate: int
	partyId: str = None
	primary: bool



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



class Contacts(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class CustomerSalesStageHistory(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	lastModifiedDate: int
	salesStageId: str = None
	salesStageName: str = None
	userId: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class OnlineAccounts(BaseModel, Blueprint):
	id: str
	version: str
	accountName: str = None
	accountType: str = None
	createdDate: int
	lastModifiedDate: int
	url: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class PartyEmailAddresses(BaseModel, Blueprint):
	id: str
	version: str
	bccAddresses: str = None
	ccAddresses: str = None
	createdDate: int
	lastModifiedDate: int
	toAddresses: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Invoices(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class PartyHabitualExporterLettersOfIntent(BaseModel, Blueprint):
	id: str
	version: str
	automaticallySuggestInInvoice: bool
	createdDate: int
	date: int = None
	fromSupplier: bool
	invoices: List[Invoices] = []
	lastModifiedDate: int
	numberDeclarer: str = None
	numberSupplier: str = None
	totalAmount: str = None
	type: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Topics(BaseModel, Blueprint):
	id: str
	name: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Party(BaseModel, Blueprint):
	id: str
	version: str
	addresses: List[Addresses] = []
	bankAccounts: List[BankAccounts] = []
	birthDate: int = None
	commercialLanguageId: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	company: str = None
	company2: str = None
	companySizeId: str = None
	companySizeName: str = None
	competitor: bool
	contacts: List[Contacts] = []
	createdDate: int
	currencyId: str = None
	currencyName: str = None
	customAttributes: List[WeclappMetaData] = []
	customer: bool
	customerAmountInsured: str = None
	customerAnnualRevenue: str = None
	customerBlockNotice: str = None
	customerBlocked: bool
	customerBusinessType: str = None
	customerCategoryId: str = None
	customerCategoryName: str = None
	customerCreditLimit: str = None
	customerCurrentSalesStageId: str = None
	customerCurrentSalesStageName: str = None
	customerDebtorAccountId: str = None
	customerDebtorAccountNumber: str = None
	customerDebtorAccountingCodeId: str = None
	customerDefaultHeaderDiscount: str = None
	customerDefaultHeaderSurcharge: str = None
	customerDefaultShippingCarrierId: str = None
	customerDeliveryBlock: bool
	customerInsolvent: bool
	customerInsured: bool
	customerInternalNote: str = None
	customerLossDescription: str = None
	customerLossReasonId: str = None
	customerLossReasonName: str = None
	customerNonStandardTaxId: str = None
	customerNumber: str = None
	customerNumberOld: str = None
	customerPaymentMethodId: str = None
	customerPaymentMethodName: str = None
	customerSalesChannel: str = None
	customerSalesOrderPaymentType: str = None
	customerSalesProbability: int = None
	customerSalesStageHistory: List[CustomerSalesStageHistory] = []
	customerSatisfaction: str = None
	customerShipmentMethodId: str = None
	customerShipmentMethodName: str = None
	customerSupplierNumber: str = None
	customerTermOfPaymentId: str = None
	customerTermOfPaymentName: str = None
	customerUseCustomsTariffNumber: bool
	deliveryAddressId: str = None
	deliveryEmailAddressesId: str = None
	description: str = None
	dunningAddressId: str = None
	dunningEmailAddressesId: str = None
	email: str = None
	enableDropshippingInNewSupplySources: bool
	eoriNumber: str = None
	factoring: bool
	fax: str = None
	firstName: str = None
	fixPhone2: str = None
	fixedResponsibleUser: bool
	formerSalesPartner: bool
	habitualExporter: bool
	imageId: str = None
	invoiceAddressId: str = None
	invoiceBlock: bool
	invoiceRecipientId: str = None
	lastModifiedDate: int
	lastName: str = None
	leadRatingId: str = None
	leadRatingName: str = None
	leadSourceId: str = None
	leadSourceName: str = None
	leadStatus: str = None
	legalFormId: str = None
	legalFormName: str = None
	middleName: str = None
	mobilePhone1: str = None
	mobilePhone2: str = None
	onlineAccounts: List[OnlineAccounts] = []
	optInEmail: bool
	optInLetter: bool
	optInPhone: bool
	optInSms: bool
	parentPartyId: str = None
	partyEmailAddresses: List[PartyEmailAddresses] = []
	partyHabitualExporterLettersOfIntent: List[PartyHabitualExporterLettersOfIntent] = []
	partyType: str = None
	personCompany: str = None
	personDepartmentId: str = None
	personRoleId: str = None
	phone: str = None
	phoneHome: str = None
	primaryAddressId: str = None
	primaryContactId: str = None
	purchaseEmailAddressesId: str = None
	purchaseViaPlafond: bool
	quotationEmailAddressesId: str = None
	ratingId: str = None
	ratingName: str = None
	referenceNumber: str = None
	responsibleUserId: str = None
	responsibleUserUsername: str = None
	salesInvoiceEmailAddressesId: str = None
	salesOrderEmailAddressesId: str = None
	salesPartner: bool
	salesPartnerDefaultCommissionFix: str = None
	salesPartnerDefaultCommissionPercentage: str = None
	salesPartnerDefaultCommissionType: str = None
	salutation: str = None
	sectorId: str = None
	sectorName: str = None
	supplier: bool
	supplierCreditorAccountId: str = None
	supplierCreditorAccountNumber: str = None
	supplierCreditorAccountingCodeId: str = None
	supplierCustomerNumberAtSupplier: str = None
	supplierDefaultShippingCarrierId: str = None
	supplierInternalNote: str = None
	supplierMinimumPurchaseOrderAmount: str = None
	supplierNonStandardTaxId: str = None
	supplierNumber: str = None
	supplierNumberOld: str = None
	supplierOrderBlock: bool
	supplierPaymentMethodId: str = None
	supplierPaymentMethodName: str = None
	supplierShipmentMethodId: str = None
	supplierShipmentMethodName: str = None
	supplierTermOfPaymentId: str = None
	supplierTermOfPaymentName: str = None
	tags: list = [] # could not be parsed
	taxId: str = None
	title: str = None
	titleId: str = None
	topics: List[Topics] = []
	vatIdentificationNumber: str = None
	website: str = None
	xRechnungLeitwegId: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



