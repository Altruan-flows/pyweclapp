"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class DeliveryAddress(Blueprint):
    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None  # Type estimated
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class DropshippingDeliveryNoteFormTexts(Blueprint):
    recordComment: Union[str, None] = None  # Type estimated
    recordFreeText: Union[str, None] = None  # Type estimated
    recordOpening: Union[str, None] = None  # Type estimated


class InvoiceAddress(Blueprint):
    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None  # Type estimated
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class PurchaseOrderItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleSupplySourceId: Union[str, None] = None
    batchSerialNumbers: list = []
    blanketPurchaseOrderId: Union[str, None] = None  # Type estimated
    blanketPurchaseOrderReleaseId: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None  # Type estimated
    invoicedQuantity: Union[str, None] = None
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountForStatistics: Union[str, None] = None
    netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    note: Union[str, None] = None  # Type estimated
    parentItemId: Union[str, None] = None  # Type estimated
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None  # Type estimated
    positionNumber: Union[int, None]
    purchaseOrderRequestOfferItemId: Union[str, None] = None  # Type estimated
    quantity: Union[str, None] = None
    receivedQuantity: Union[str, None] = None
    reductionAdditionItems: list = []
    salesOrderItemId: Union[str, None] = None  # Type estimated
    servicePeriodFromDate: Union[int, None] = None  # Type estimated
    servicePeriodToDate: Union[int, None] = None  # Type estimated
    taxId: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class RecordAddress(Blueprint):
    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None  # Type estimated
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class StatusHistory(Blueprint):
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class PurchaseOrder(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    advancePaymentStatus: Union[str, None] = None  # Type estimated
    commercialLanguage: Union[str, None] = None
    commercialLanguageCustomer: Union[str, None] = None  # Type estimated
    commission: Union[str, None] = None  # Type estimated
    confirmationNumber: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionLocked: Union[bool, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    description: Union[str, None] = None  # Type estimated
    disableRecordEmailingRule: Union[bool, None] = None
    dropshippingDeliveryNoteFormTexts: DropshippingDeliveryNoteFormTexts = DropshippingDeliveryNoteFormTexts.from_blank()
    externalPurchaseOrderNumber: Union[str, None] = None  # Type estimated
    formSettingsFromSalesChannel: Union[str, None] = None  # Type estimated
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiced: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    mergedToPurchaseOrderId: Union[str, None] = None  # Type estimated
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None  # Type estimated
    note: Union[str, None] = None  # Type estimated
    orderDate: Union[int, None] = None
    packageTrackingNumber: Union[str, None] = None  # Type estimated
    packageTrackingUrl: Union[str, None] = None  # Type estimated
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None  # Type estimated
    purchaseOrderItems: List[PurchaseOrderItems] = []
    purchaseOrderNumber: Union[str, None] = None
    purchaseOrderRequestId: Union[str, None] = None  # Type estimated
    purchaseOrderType: Union[str, None] = None
    received: Union[bool, None] = None
    recipientCountryCode: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None  # Type estimated
    recordCurrencyId: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None  # Type estimated
    recordOpening: Union[str, None] = None  # Type estimated
    responsibleUserId: Union[str, None] = None
    salesOrderId: Union[str, None] = None  # Type estimated
    senderCountryCode: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    shipmentMethodId: Union[str, None] = None  # Type estimated
    shippingCarrierId: Union[str, None] = None  # Type estimated
    shippingCostItems: list = []
    shippingNotificationDate: Union[int, None] = None  # Type estimated
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    supplierHabitualExporterLetterOfIntentId: Union[str, None] = None  # Type estimated
    supplierId: Union[str, None] = None
    supplierQuotationNumber: Union[str, None] = None  # Type estimated
    tags: list = []
    termOfPaymentId: Union[str, None] = None
    warehouseId: Union[str, None] = None
