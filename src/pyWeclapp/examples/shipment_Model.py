# This code was dynamically created using WeclappClassCreator from pyWeclapp

from pyWeclapp.weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class InvoiceAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class RecipientAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
	status: Union[Literal["CANCELLED", "DELIVERED", "DELIVERY_NOTE_PRINTED", "INCOMING_CANCELLED", "INCOMING_GOODS_MOVEMENT_PRINTED", "INCOMING_MOVED_INTO_STORE", "INCOMING_SHIPPED", "IN_ROUTE", "NEW", "SHIPPED"], None] = None
	statusDate: Union[int, None] = None
	userId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class PurchaseOrders(Blueprint):
	id: Union[str, None]
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class RecordEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class SalesInvoiceEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class ShipmentItems(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	articleId: Union[str, None] = None
	articleNumber: Union[str, None] = None
	note: Union[str, None] = None
	positionNumber: Union[int, None]
	quantity: Union[str, None] = None
	description: Union[str, None] = None
	descriptionFixed: Union[bool, None]
	manualQuantity: Union[bool, None]
	parentItemId: Union[str, None] = None
	title: Union[str, None] = None
	unitId: Union[str, None] = None
	unitName: Union[str, None] = None
	addPageBreakBefore: Union[bool, None]
	availability: Union[Literal["COMPLETELY_AVAILABLE", "NOTHING_AVAILABLE", "NOT_CHECKED", "PARTIALLY_AVAILABLE", "TRANSFER_REQUIRED"], None] = None
	availabilityForAllWarehouses: Union[Literal["COMPLETELY_AVAILABLE", "NOTHING_AVAILABLE", "NOT_CHECKED", "PARTIALLY_AVAILABLE", "TRANSFER_REQUIRED"], None] = None
	customAttributes: List[WeclappMetaData] = []
	freeTextItem: Union[bool, None]
	groupName: Union[str, None] = None
	purchaseOrderItemId: Union[str, None] = None
	returnAssessmentId: Union[str, None] = None
	returnAssessmentName: Union[str, None] = None
	returnDescription: Union[str, None] = None
	returnErrorId: Union[str, None] = None
	returnErrorName: Union[str, None] = None
	returnReasonId: Union[str, None] = None
	returnReasonName: Union[str, None] = None
	returnRectificationId: Union[str, None] = None
	returnRectificationName: Union[str, None] = None
	salesOrderItemId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class ShippedFromAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class Shipment(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	customAttributes: List[WeclappMetaData] = []
	commercialLanguage: Union[str, None] = None
	creatorId: Union[str, None] = None
	description: Union[str, None] = None
	disableEmailTemplate: Union[bool, None]
	recordComment: Union[str, None] = None
	recordFreeText: Union[str, None] = None
	recordOpening: Union[str, None] = None
	sentToRecipient: Union[bool, None]
	tags: list = []
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	recipientAddress: RecipientAddress = RecipientAddress.fromBlank()
	salesOrderId: Union[str, None] = None
	salesOrderNumber: Union[str, None] = None
	status: Union[Literal["CANCELLED", "DELIVERED", "DELIVERY_NOTE_PRINTED", "INCOMING_CANCELLED", "INCOMING_GOODS_MOVEMENT_PRINTED", "INCOMING_MOVED_INTO_STORE", "INCOMING_SHIPPED", "IN_ROUTE", "NEW", "SHIPPED"], None] = None
	statusHistory: List[StatusHistory] = []
	additionalDeliveryInformation: Union[str, None] = None
	availability: Union[Literal["COMPLETELY_AVAILABLE", "NOTHING_AVAILABLE", "NOT_CHECKED", "PARTIALLY_AVAILABLE", "TRANSFER_REQUIRED"], None] = None
	availabilityForAllWarehouses: Union[Literal["COMPLETELY_AVAILABLE", "NOTHING_AVAILABLE", "NOT_CHECKED", "PARTIALLY_AVAILABLE", "TRANSFER_REQUIRED"], None] = None
	consolidationStoragePlaceId: Union[str, None] = None
	customerPurchaseOrderNumber: Union[str, None] = None
	declaredValueAmount: Union[str, None] = None
	declaredValueAmountCurrencyId: Union[str, None] = None
	declaredValueAmountCurrencyName: Union[str, None] = None
	deliveryDate: Union[int, None] = None
	destinationStoragePlaceId: Union[str, None] = None
	destinationWarehouseId: Union[str, None] = None
	destinationWarehouseName: Union[str, None] = None
	invoiceRecipientId: Union[str, None] = None
	packageHeight: Union[int, None] = None
	packageLength: Union[int, None] = None
	packageReferenceNumber: Union[str, None] = None
	packageReturnTrackingNumber: Union[str, None] = None
	packageReturnTrackingUrl: Union[str, None] = None
	packageTrackingNumber: Union[str, None] = None
	packageTrackingUrl: Union[str, None] = None
	packageWeight: Union[str, None] = None
	packageWidth: Union[int, None] = None
	pickingInstructions: Union[str, None] = None
	picksComplete: Union[bool, None]
	purchaseOrders: List[PurchaseOrders] = []
	recipientCustomerNumber: Union[str, None] = None
	recipientPartyId: Union[str, None] = None
	recipientSupplierNumber: Union[str, None] = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	responsibleUserId: Union[str, None] = None
	salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.fromBlank()
	shipmentItems: List[ShipmentItems] = []
	shipmentMethodId: Union[str, None] = None
	shipmentMethodName: Union[str, None] = None
	shipmentNumber: Union[str, None] = None
	shipmentType: Union[Literal["CONSIGNMENT", "CONSIGNMENT_RETURN", "CUSTOMER_COMPENSATION", "INTERNAL", "STANDARD", "SUPPLIER_RETURN"], None] = None
	shippedFromAddress: ShippedFromAddress = ShippedFromAddress.fromBlank()
	shippingCarrierId: Union[str, None] = None
	shippingCarrierName: Union[str, None] = None
	shippingDate: Union[int, None] = None
	shippingLabelsCount: Union[int, None] = None
	shippingReturnCarrierId: Union[str, None] = None
	shippingReturnCarrierName: Union[str, None] = None
	warehouseId: Union[str, None] = None
	warehouseName: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = "shipmentItems"


