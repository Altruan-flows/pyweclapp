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
	status: Union[Literal["CANCELLED", "DELIVERED", "DELIVERY_NOTE_PRINTED", "INCOMING_CANCELLED", "INCOMING_MOVED_INTO_STORE", "INCOMING_SHIPPED", "IN_ROUTE", "NEW", "SHIPPED"], None] = None
	statusDate: Union[int, None] = None
	userId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class CustomerDeliveryAddress(Blueprint):
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


class CustomerInvoiceAddress(Blueprint):
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


class IncomingGoodsItems(Blueprint):
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
	descriptionFixed: Union[bool, None] = None
	manualQuantity: Union[bool, None] = None
	parentItemId: Union[str, None] = None
	title: Union[str, None] = None
	unitId: Union[str, None] = None
	unitName: Union[str, None] = None
	customAttributes: List[WeclappMetaData] = []
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


class PurchaseOrders(Blueprint):
	id: Union[str, None]
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class ReturnAddress(Blueprint):
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


class IncomingGoods(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	customAttributes: List[WeclappMetaData] = []
	commercialLanguage: Union[str, None] = None
	creatorId: Union[str, None] = None
	description: Union[str, None] = None
	disableEmailTemplate: Union[bool, None] = None
	recordComment: Union[str, None] = None
	recordFreeText: Union[str, None] = None
	recordOpening: Union[str, None] = None
	sentToRecipient: Union[bool, None] = None
	tags: list = []
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	recipientAddress: RecipientAddress = RecipientAddress.fromBlank()
	salesOrderId: Union[str, None] = None
	salesOrderNumber: Union[str, None] = None
	status: Union[Literal["CANCELLED", "DELIVERED", "DELIVERY_NOTE_PRINTED", "INCOMING_CANCELLED", "INCOMING_MOVED_INTO_STORE", "INCOMING_SHIPPED", "IN_ROUTE", "NEW", "SHIPPED"], None] = None
	statusHistory: List[StatusHistory] = []
	customerDeliveryAddress: CustomerDeliveryAddress = CustomerDeliveryAddress.fromBlank()
	customerInvoiceAddress: CustomerInvoiceAddress = CustomerInvoiceAddress.fromBlank()
	deliveryNoteNumber: Union[str, None] = None
	incomingGoodsItems: List[IncomingGoodsItems] = []
	incomingGoodsNumber: Union[str, None] = None
	incomingGoodsType: Union[Literal["CUSTOMER_RETURN", "INTERNAL", "STANDARD", "SUPPLIER_COMPENSATION"], None] = None
	invoiceRecipientId: Union[str, None] = None
	purchaseOrderId: Union[str, None] = None
	purchaseOrderNumber: Union[str, None] = None
	purchaseOrders: List[PurchaseOrders] = []
	relatedShipmentId: Union[str, None] = None
	responsibleUserId: Union[str, None] = None
	returnAddress: ReturnAddress = ReturnAddress.fromBlank()
	senderCustomerNumber: Union[str, None] = None
	senderPartyId: Union[str, None] = None
	senderSupplierNumber: Union[str, None] = None
	sourceWarehouseId: Union[str, None] = None
	sourceWarehouseName: Union[str, None] = None
	warehouseId: Union[str, None] = None
	warehouseName: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


