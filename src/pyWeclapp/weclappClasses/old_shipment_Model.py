from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class Address(Blueprint):
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





class PurchaseOrders( Blueprint):
	id: str








class EmailAddresses(Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None







class ShipmentItems(Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	articleId: str = "31528346"
	articleNumber: str = "AL-Gutschrift"
	availability: str
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
	positionNumber: int
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








class StatusHistory(Blueprint):
	status: str = None
	statusDate: int = None
	userId: str = None





class Shipment( Blueprint):
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
	invoiceAddress: Address = Address.fromBlank()
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
	recipientAddress: Address = Address.fromBlank()
	recipientCustomerNumber: str = None
	recipientPartyId: str = None
	recipientSupplierNumber: str = None
	recordComment: str = None
	recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	responsibleUserId: str = None
	salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	salesOrderId: str = None
	salesOrderNumber: str = None
	sentToRecipient: bool
	shipmentItems: List[ShipmentItems] = []
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shipmentNumber: str = None
	shipmentType: str = None
	shippedFromAddress: Address = Address.fromBlank()
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



