"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class DeliveryAddress(Blueprint):
    """Subclass for deliveryAddress in PurchaseOrder."""

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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class ShippingCostItems(Blueprint):
    """Subclass for shippingCostItems in PurchaseOrder."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
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


class ReductionAdditionItems(Blueprint):
    """Subclass for reductionAdditionItems in PurchaseOrderItems."""

    position: Union[int, None] = None
    source: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class BatchSerialNumbers(Blueprint):
    """Subclass for batchSerialNumbers in PurchaseOrderItems."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    batchNumber: Union[str, None] = None
    expirationDate: Union[int, None] = None
    quantity: Union[str, None] = None
    serialNumbers: list = []


class DropshippingDeliveryNoteFormTexts(Blueprint):
    """Subclass for dropshippingDeliveryNoteFormTexts in PurchaseOrder."""

    recordComment: Union[str, None] = None
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None


class InvoiceAddress(Blueprint):
    """Subclass for invoiceAddress in PurchaseOrder."""

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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class PurchaseOrderItems(Blueprint):
    """Subclass for purchaseOrderItems in PurchaseOrder."""

    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    batchSerialNumbers: List[BatchSerialNumbers] = []
    blanketPurchaseOrderId: Union[str, None] = None
    blanketPurchaseOrderReleaseId: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None
    invoicedQuantity: Union[str, None] = None
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountForStatistics: Union[str, None] = None
    netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    note: Union[str, None] = None
    parentItemId: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    positionNumber: Union[int, None]
    purchaseOrderRequestOfferItemId: Union[str, None] = None
    quantity: Union[str, None] = None
    receivedQuantity: Union[str, None] = None
    reductionAdditionItems: List[ReductionAdditionItems] = []
    salesOrderItemId: Union[int, None] = None
    servicePeriodFromDate: Union[int, None] = None
    servicePeriodToDate: Union[int, None] = None
    supplierArticleId: Union[str, None] = None
    taxId: Union[str, None] = None
    taxName: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class RecordAddress(Blueprint):
    """Subclass for recordAddress in PurchaseOrder."""

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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    """Subclass for recordEmailAddresses in PurchaseOrder."""

    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class StatusHistory(Blueprint):
    """Subclass for statusHistory in PurchaseOrder."""

    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class PurchaseOrder(Blueprint):
    """Class for purchaseOrder endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    advancePaymentStatus: Union[str, None] = None
    commercialLanguage: Union[str, None] = None
    commercialLanguageCustomer: Union[str, None] = None
    commission: Union[str, None] = None
    confirmationNumber: Union[str, None] = None
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    description: Union[str, None] = None
    disableEmailTemplate: Union[bool, None] = None
    dropshippingDeliveryNoteFormTexts: DropshippingDeliveryNoteFormTexts = (
        DropshippingDeliveryNoteFormTexts.from_blank()
    )
    externalPurchaseOrderNumber: Union[str, None] = None
    formSettingsFromSalesChannel: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiced: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    mergedToPurchaseOrderId: Union[str, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None
    nonStandardTaxName: Union[str, None] = None
    note: Union[str, None] = None
    orderDate: Union[int, None] = None
    packageTrackingNumber: Union[str, None] = None
    packageTrackingUrl: Union[str, None] = None
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    paymentMethodName: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    purchaseOrderItems: List[PurchaseOrderItems] = []
    purchaseOrderNumber: Union[str, None] = None
    purchaseOrderRequestId: Union[str, None] = None
    purchaseOrderType: Union[str, None] = None
    received: Union[bool, None] = None
    recipientCountryCode: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None
    recordCurrencyId: Union[str, None] = None
    recordCurrencyName: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesOrderId: Union[str, None] = None
    salesOrderNumber: Union[str, None] = None
    senderCountryCode: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    shippingCarrierId: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingNotificationDate: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    supplierHabitualExporterLetterOfIntentId: Union[str, None] = None
    supplierId: Union[str, None] = None
    supplierNumber: Union[str, None] = None
    supplierQuotationNumber: Union[str, None] = None
    tags: list = []
    termOfPaymentId: Union[str, None] = None
    termOfPaymentName: Union[str, None] = None
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
