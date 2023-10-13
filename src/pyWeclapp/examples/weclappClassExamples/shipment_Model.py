from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData
from pydantic import BaseModel
from typing import *



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



class PurchaseOrders(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class RecipientAddress(BaseModel, Blueprint):
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



class ShipmentItems(BaseModel, Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	articleId: str = None
	articleNumber: str = None
	availability: str = None
	availabilityForAllWarehouses: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	descriptionFixed: bool
	freeTextItem: bool
	groupName: str = None
	lastModifiedDate: int
	manualQuantity: bool
	note: str = None
	parentItemId: str = None
	positionNumber: int = None
	purchaseOrderItemId: str = None
	quantity: str = None
	returnAssessmentId: str = None
	returnAssessmentName: str = None
	returnDescription: str = None
	returnErrorId: str = None
	returnErrorName: str = None
	returnReasonId: str = None
	returnReasonName: str = None
	returnRectificationId: str = None
	returnRectificationName: str = None
	salesOrderItemId: str = None
	title: str = None
	unitId: str = None
	unitName: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ShippedFromAddress(BaseModel, Blueprint):
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



class Shipment(BaseModel, Blueprint):
	id: str
	version: str
	additionalDeliveryInformation: str = None
	availability: str = None
	availabilityForAllWarehouses: str = None
	commercialLanguage: str = None
	consolidationStoragePlaceId: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	customerPurchaseOrderNumber: str = None
	declaredValueAmount: str = None
	declaredValueAmountCurrencyId: str = None
	declaredValueAmountCurrencyName: str = None
	deliveryDate: int = None
	description: str = None
	destinationStoragePlaceId: str = None
	destinationWarehouseId: str = None
	destinationWarehouseName: str = None
	disableEmailTemplate: bool
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	invoiceRecipientId: str = None
	lastModifiedDate: int
	packageHeight: int = None
	packageLength: int = None
	packageReferenceNumber: str = None
	packageReturnTrackingNumber: str = None
	packageReturnTrackingUrl: str = None
	packageTrackingNumber: str = None
	packageTrackingUrl: str = None
	packageWeight: str = None
	packageWidth: int = None
	pickingInstructions: str = None
	picksComplete: bool
	purchaseOrders: List[PurchaseOrders] = []
	recipientAddress: RecipientAddress = RecipientAddress.fromBlank()
	recipientCustomerNumber: str = None
	recipientPartyId: str = None
	recipientSupplierNumber: str = None
	recordComment: str = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	responsibleUserId: str = None
	salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.fromBlank()
	salesOrderId: str = None
	salesOrderNumber: str = None
	sentToRecipient: bool
	shipmentItems: List[ShipmentItems] = []
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shipmentNumber: str = None
	shipmentType: str = None
	shippedFromAddress: ShippedFromAddress = ShippedFromAddress.fromBlank()
	shippingCarrierId: str = None
	shippingCarrierName: str = None
	shippingDate: int = None
	shippingLabelsCount: int = None
	shippingReturnCarrierId: str = None
	shippingReturnCarrierName: str = None
	status: str = None
	statusHistory: List[StatusHistory] = []
	tags: list = [] # could not be parsed
	warehouseId: str = None
	warehouseName: str = None



	# AutomationData
	ITEMS_NAME: str = "shipmentItems"
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



