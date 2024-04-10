# This code was dynamically created using WeclappClassCreator from pyWeclapp

from pyWeclapp.weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class RecordEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class ShippingCostItems(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	articleId: Union[str, None] = None
	articleNumber: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	manualUnitPrice: Union[bool, None] = None
	netAmount: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	taxId: Union[str, None] = None
	taxName: Union[str, None] = None
	unitPrice: Union[str, None] = None
	unitPriceInCompanyCurrency: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class DeliveryAddress(Blueprint):
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


class ReductionAdditionItems(Blueprint):
	position: Union[int, None] = None
	source: Union[Literal["ARTICLE", "ARTICLE_AND_CUSTOMER", "ARTICLE_CATEGORY", "ARTICLE_CATEGORY_AND_CUSTOMER", "MANUAL"], None] = None
	type: Union[Literal["ADDITION_ABSOLUTE", "ADDITION_PERCENT", "REDUCTION_ABSOLUTE", "REDUCTION_PERCENT"], None] = None
	value: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class BatchSerialNumbers(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	batchNumber: Union[str, None] = None
	expirationDate: Union[int, None] = None
	quantity: Union[str, None] = None
	serialNumbers: list = []
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class PurchaseOrderItems(Blueprint):
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
	discountPercentage: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	manualUnitPrice: Union[bool, None] = None
	netAmount: Union[str, None] = None
	netAmountForStatistics: Union[str, None] = None
	netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	taxId: Union[str, None] = None
	taxName: Union[str, None] = None
	unitPrice: Union[str, None] = None
	unitPriceInCompanyCurrency: Union[str, None] = None
	addPageBreakBefore: Union[bool, None] = None
	customAttributes: List[WeclappMetaData] = []
	freeTextItem: Union[bool, None] = None
	groupName: Union[str, None] = None
	batchSerialNumbers: List[BatchSerialNumbers] = []
	blanketPurchaseOrderId: Union[str, None] = None
	blanketPurchaseOrderReleaseId: Union[str, None] = None
	invoicedQuantity: Union[str, None] = None
	plannedDeliveryDate: Union[int, None] = None
	plannedShippingDate: Union[int, None] = None
	receivedQuantity: Union[str, None] = None
	salesOrderItemId: Union[int, None] = None
	supplierArticleId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class RecordAddress(Blueprint):
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
	status: Union[Literal["CANCELLED", "CLOSED", "CONFIRMED", "ORDER_DOCUMENTS_PRINTED", "ORDER_ENTRY_COMPLETED", "ORDER_ENTRY_IN_PROGRESS"], None] = None
	statusDate: Union[int, None] = None
	userId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class PurchaseOrder(Blueprint):
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
	currencyConversionDate: Union[int, None] = None
	currencyConversionRate: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	headerDiscount: Union[str, None] = None
	headerSurcharge: Union[str, None] = None
	netAmount: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	nonStandardTaxId: Union[str, None] = None
	nonStandardTaxName: Union[str, None] = None
	paymentMethodId: Union[str, None] = None
	paymentMethodName: Union[str, None] = None
	recordCurrencyId: Union[str, None] = None
	recordCurrencyName: Union[str, None] = None
	termOfPaymentId: Union[str, None] = None
	termOfPaymentName: Union[str, None] = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	responsibleUserId: Union[str, None] = None
	responsibleUserUsername: Union[str, None] = None
	servicePeriodFrom: Union[int, None] = None
	servicePeriodTo: Union[int, None] = None
	shippingCostItems: List[ShippingCostItems] = []
	supplierId: Union[str, None] = None
	supplierNumber: Union[str, None] = None
	advancePaymentStatus: Union[Literal["OPEN", "PAID"], None] = None
	commission: Union[str, None] = None
	confirmationNumber: Union[str, None] = None
	deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
	externalPurchaseOrderNumber: Union[str, None] = None
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	orderDate: Union[int, None] = None
	packageTrackingNumber: Union[str, None] = None
	packageTrackingUrl: Union[str, None] = None
	plannedDeliveryDate: Union[int, None] = None
	plannedShippingDate: Union[int, None] = None
	purchaseOrderItems: List[PurchaseOrderItems] = []
	purchaseOrderNumber: Union[str, None] = None
	purchaseOrderRequestId: Union[str, None] = None
	purchaseOrderType: Union[Literal["BLANKET_PURCHASE_ORDER", "NORMAL", "SALES_ORDER", "TRIANGULAR"], None] = None
	received: Union[bool, None] = None
	recordAddress: RecordAddress = RecordAddress.fromBlank()
	salesOrderId: Union[str, None] = None
	salesOrderNumber: Union[str, None] = None
	shipmentMethodId: Union[str, None] = None
	shipmentMethodName: Union[str, None] = None
	shippingCarrierId: Union[str, None] = None
	status: Union[Literal["CANCELLED", "CLOSED", "CONFIRMED", "ORDER_DOCUMENTS_PRINTED", "ORDER_ENTRY_COMPLETED", "ORDER_ENTRY_IN_PROGRESS"], None] = None
	statusHistory: List[StatusHistory] = []
	supplierHabitualExporterLetterOfIntentId: Union[str, None] = None
	supplierQuotationNumber: Union[str, None] = None
	warehouseId: Union[str, None] = None
	warehouseName: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


