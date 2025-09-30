"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List, Set
from .blueprints import Blueprint, WeclappMetaData


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class DropshippingDeliveryNoteFormTexts(Blueprint):
    recordComment: Union[str, None] = None
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None


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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class ReductionAdditionItems(Blueprint):
    position: Union[int, None] = None
    source: Union[str, None] = None
    specialPriceReduction: Union[bool, None] = None
    title: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class BatchSerialNumbers(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    batchNumber: Union[str, None] = None
    expirationDate: Union[int, None] = None
    quantity: Union[str, None] = None
    serialNumbers: list = []


class PurchaseOrderItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    articleId: Union[str, None] = None
    note: Union[str, None] = None
    positionNumber: Union[int, None] = None
    quantity: Union[str, None] = None
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    itemType: Union[str, None] = None
    manualQuantity: Union[bool, None] = None
    parentItemId: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None
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
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None
    addPageBreakBefore: Union[bool, None] = None
    groupName: Union[str, None] = None
    articleSupplySourceId: Union[str, None] = None
    batchSerialNumbers: List[BatchSerialNumbers] = []
    blanketPurchaseOrderId: Union[str, None] = None
    blanketPurchaseOrderReleaseId: Union[str, None] = None
    invoicedQuantity: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    purchaseOrderRequestOfferItemId: Union[str, None] = None
    receivedQuantity: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None
    servicePeriodFromDate: Union[int, None] = None
    servicePeriodToDate: Union[int, None] = None


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
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class ShippingCostItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None
    taxId: Union[str, None] = None

    excluded_keys: Set[str] = {
        "version",
        "grossAmount",
        "grossAmountInCompanyCurrency",
        "netAmount",
        "netAmountInCompanyCurrency",
        "unitPriceInCompanyCurrency",
        "unitCostInCompanyCurrency",
    }


class StatusHistory(Blueprint):
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class PurchaseOrder(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    commercialLanguage: Union[str, None] = None
    creatorId: Union[str, None] = None
    description: Union[str, None] = None
    disableRecordEmailingRule: Union[bool, None] = None
    recordComment: Union[str, None] = None
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    tags: list = []
    currencyConversionDate: Union[int, None] = None
    currencyConversionLocked: Union[bool, None] = None
    currencyConversionRate: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None
    paymentMethodId: Union[str, None] = None
    recordCurrencyId: Union[str, None] = None
    termOfPaymentId: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses()
    responsibleUserId: Union[str, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    supplierId: Union[str, None] = None
    advancePaymentStatus: Union[str, None] = None
    commercialLanguageCustomer: Union[str, None] = None
    commission: Union[str, None] = None
    confirmationNumber: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress()
    dropshippingDeliveryNoteFormTexts: DropshippingDeliveryNoteFormTexts = DropshippingDeliveryNoteFormTexts()
    externalPurchaseOrderNumber: Union[str, None] = None
    formSettingsFromSalesChannel: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress()
    invoiced: Union[bool, None] = None
    mergedToPurchaseOrderId: Union[str, None] = None
    note: Union[str, None] = None
    orderDate: Union[int, None] = None
    packageTrackingNumber: Union[str, None] = None
    packageTrackingUrl: Union[str, None] = None
    paid: Union[bool, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    purchaseOrderItems: List[PurchaseOrderItems] = []
    purchaseOrderNumber: Union[str, None] = None
    purchaseOrderRequestId: Union[str, None] = None
    purchaseOrderType: Union[str, None] = None
    received: Union[bool, None] = None
    recipientCountryCode: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress()
    salesOrderId: Union[str, None] = None
    senderCountryCode: Union[str, None] = None
    shipmentMethodId: Union[str, None] = None
    shippingCarrierId: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingNotificationDate: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    supplierHabitualExporterLetterOfIntentId: Union[str, None] = None
    supplierQuotationNumber: Union[str, None] = None
    warehouseId: Union[str, None] = None
