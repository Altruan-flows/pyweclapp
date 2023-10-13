from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData
from pydantic import BaseModel
from typing import *



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



class EcommerceOrder(BaseModel, Blueprint):
	ecommerceId: str = None
	externalConnectionId: str = None



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



class Tasks(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class OrderItems(BaseModel, Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	articleId: str = None
	articleNumber: str = None
	availability: str = None
	availabilityForAllWarehouses: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	descriptionFixed: bool
	discountPercentage: str = None
	ecommerceOrderItemId: str = None
	freeTextItem: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	groupName: str = None
	invoicedQuantity: str = None
	invoicingType: str = None
	lastModifiedDate: int
	manualPlannedWorkingTimePerUnit: bool
	manualQuantity: bool
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountForStatistics: str = None
	netAmountForStatisticsInCompanyCurrency: str = None
	netAmountInCompanyCurrency: str = None
	note: str = None
	parentItemId: str = None
	pickBatchNumber: str = None
	pickSerialNumbers: list = [] # could not be parsed
	pickStoragePlaceId: str = None
	plannedShippingDate: int = None
	plannedWorkingTimePerUnit: str = None
	positionNumber: int = None
	quantity: str = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	returnedQuantity: str = None
	serviceItem: bool
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	shipped: bool
	shippedQuantity: str = None
	tasks: List[Tasks] = []
	taxId: str = None
	taxName: str = None
	title: str = None
	unitCost: str = None
	unitCostInCompanyCurrency: str = None
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



class ProjectMembers(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	hourlyCost: str = None
	lastModifiedDate: int
	teamRole: str = None
	userId: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class RecordAddress(BaseModel, Blueprint):
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



class ShippingCostItems(BaseModel, Blueprint):
	id: str
	version: str
	articleId: str = None
	articleNumber: str = None
	createdDate: int
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	lastModifiedDate: int
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	taxId: str = None
	taxName: str = None
	unitCost: str = None
	unitCostInCompanyCurrency: str = None
	unitPrice: str = None
	unitPriceInCompanyCurrency: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class StatusHistory(BaseModel, Blueprint):
	status: str = None
	statusDate: int = None
	userId: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class SalesOrder(BaseModel, Blueprint):
	id: str
	version: str
	advancePaymentStatus: str = None
	availability: str = None
	availabilityForAllWarehouses: str = None
	cashAccountId: str = None
	commercialLanguage: str = None
	commission: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	createdDate: int
	currencyConversionDate: int = None
	currencyConversionRate: str = None
	customAttributes: List[WeclappMetaData] = []
	customerHabitualExporterLetterOfIntentId: str = None
	customerId: str = None
	customerNumber: str = None
	defaultShippingCarrierId: str = None
	defaultShippingCarrierName: str = None
	defaultShippingReturnCarrierId: str = None
	defaultShippingReturnCarrierName: str = None
	deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
	deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.fromBlank()
	description: str = None
	disableEmailTemplate: bool
	dispatchCountryCode: str = None
	ecommerceOrder: EcommerceOrder = EcommerceOrder.fromBlank()
	factoring: bool
	fulfillmentProviderId: str = None
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	headerDiscount: str = None
	headerSurcharge: str = None
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	invoiceRecipientId: str = None
	invoiced: bool
	lastModifiedDate: int
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	nonStandardTaxId: str = None
	nonStandardTaxName: str = None
	onlyServices: bool
	orderDate: int = None
	orderItems: List[OrderItems] = []
	orderNumber: str = None
	orderNumberAtCustomer: str = None
	paid: bool
	paymentMethodId: str = None
	paymentMethodName: str = None
	plannedDeliveryDate: int = None
	plannedProjectEndDate: int = None
	plannedProjectStartDate: int = None
	plannedShippingDate: int = None
	pricingDate: int = None
	projectGoals: str = None
	projectMembers: List[ProjectMembers] = []
	projectModeActive: bool
	quotationId: str = None
	quotationNumber: str = None
	recordAddress: RecordAddress = RecordAddress.fromBlank()
	recordComment: str = None
	recordCurrencyId: str = None
	recordCurrencyName: str = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	responsibleUserId: str = None
	responsibleUserUsername: str = None
	salesChannel: str = None
	salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.fromBlank()
	salesOrderPaymentType: str = None
	sentToRecipient: bool
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	servicesFinished: bool
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shipped: bool
	shippingCostItems: List[ShippingCostItems] = []
	shippingLabelsCount: int = None
	status: str = None
	statusHistory: List[StatusHistory] = []
	tags: list = [] # could not be parsed
	termOfPaymentId: str = None
	termOfPaymentName: str = None
	warehouseId: str = None
	warehouseName: str = None



	# AutomationData
	ITEMS_NAME: str = "orderItems"
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



