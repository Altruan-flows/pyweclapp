# This code was dynamically created using WeclappClassCreator from pyWeclapp

from pyWeclapp.weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


class RecordEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ShippingCostItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    articleNumber: Optional[str] = None
    grossAmount: Optional[str] = None
    grossAmountInCompanyCurrency: Optional[str] = None
    manualUnitPrice: Optional[bool] = None
    netAmount: Optional[str] = None
    netAmountInCompanyCurrency: Optional[str] = None
    taxId: Optional[str] = None
    taxName: Optional[str] = None
    unitPrice: Optional[str] = None
    unitPriceInCompanyCurrency: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class DeliveryAddress(Blueprint):
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class InvoiceAddress(Blueprint):
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ReductionAdditionItems(Blueprint):
    position: Optional[int] = None
    source: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class BatchSerialNumbers(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    batchNumber: Optional[str] = None
    expirationDate: Optional[int] = None
    quantity: Optional[str] = None
    serialNumbers: list = []
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PurchaseOrderItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    articleNumber: Optional[str] = None
    note: Optional[str] = None
    positionNumber: Optional[int] = None
    quantity: Optional[str] = None
    description: Optional[str] = None
    descriptionFixed: Optional[bool] = None
    manualQuantity: Optional[bool] = None
    parentItemId: Optional[str] = None
    title: Optional[str] = None
    unitId: Optional[str] = None
    unitName: Optional[str] = None
    discountPercentage: Optional[str] = None
    grossAmount: Optional[str] = None
    grossAmountInCompanyCurrency: Optional[str] = None
    manualUnitPrice: Optional[bool] = None
    netAmount: Optional[str] = None
    netAmountForStatistics: Optional[str] = None
    netAmountForStatisticsInCompanyCurrency: Optional[str] = None
    netAmountInCompanyCurrency: Optional[str] = None
    reductionAdditionItems: List[ReductionAdditionItems] = []
    taxId: Optional[str] = None
    taxName: Optional[str] = None
    unitPrice: Optional[str] = None
    unitPriceInCompanyCurrency: Optional[str] = None
    addPageBreakBefore: Optional[bool] = None
    customAttributes: List[WeclappMetaData] = []
    freeTextItem: Optional[bool] = None
    groupName: Optional[str] = None
    batchSerialNumbers: List[BatchSerialNumbers] = []
    blanketPurchaseOrderId: Optional[str] = None
    blanketPurchaseOrderReleaseId: Optional[str] = None
    invoicedQuantity: Optional[str] = None
    plannedDeliveryDate: Optional[int] = None
    plannedShippingDate: Optional[int] = None
    receivedQuantity: Optional[str] = None
    salesOrderItemId: Optional[int] = None
    supplierArticleId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class RecordAddress(Blueprint):
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
    status: Optional[str] = None
    statusDate: Optional[int] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PurchaseOrder(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    commercialLanguage: Optional[str] = None
    creatorId: Optional[str] = None
    description: Optional[str] = None
    disableEmailTemplate: Optional[bool] = None
    recordComment: Optional[str] = None
    recordFreeText: Optional[str] = None
    recordOpening: Optional[str] = None
    sentToRecipient: Optional[bool] = None
    tags: list = []
    currencyConversionDate: Optional[int] = None
    currencyConversionRate: Optional[str] = None
    grossAmount: Optional[str] = None
    grossAmountInCompanyCurrency: Optional[str] = None
    headerDiscount: Optional[str] = None
    headerSurcharge: Optional[str] = None
    netAmount: Optional[str] = None
    netAmountInCompanyCurrency: Optional[str] = None
    nonStandardTaxId: Optional[str] = None
    nonStandardTaxName: Optional[str] = None
    paymentMethodId: Optional[str] = None
    paymentMethodName: Optional[str] = None
    recordCurrencyId: Optional[str] = None
    recordCurrencyName: Optional[str] = None
    termOfPaymentId: Optional[str] = None
    termOfPaymentName: Optional[str] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
    responsibleUserId: Optional[str] = None
    responsibleUserUsername: Optional[str] = None
    servicePeriodFrom: Optional[int] = None
    servicePeriodTo: Optional[int] = None
    shippingCostItems: List[ShippingCostItems] = []
    supplierId: Optional[str] = None
    supplierNumber: Optional[str] = None
    advancePaymentStatus: Optional[str] = None
    commission: Optional[str] = None
    confirmationNumber: Optional[str] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
    externalPurchaseOrderNumber: Optional[str] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
    orderDate: Optional[int] = None
    packageTrackingNumber: Optional[str] = None
    packageTrackingUrl: Optional[str] = None
    plannedDeliveryDate: Optional[int] = None
    plannedShippingDate: Optional[int] = None
    purchaseOrderItems: List[PurchaseOrderItems] = []
    purchaseOrderNumber: Optional[str] = None
    purchaseOrderRequestId: Optional[str] = None
    purchaseOrderType: Optional[str] = None
    received: Optional[bool] = None
    recordAddress: RecordAddress = RecordAddress.fromBlank()
    salesOrderId: Optional[str] = None
    salesOrderNumber: Optional[str] = None
    shipmentMethodId: Optional[str] = None
    shipmentMethodName: Optional[str] = None
    shippingCarrierId: Optional[str] = None
    status: Optional[str] = None
    statusHistory: List[StatusHistory] = []
    supplierHabitualExporterLetterOfIntentId: Optional[str] = None
    supplierQuotationNumber: Optional[str] = None
    warehouseId: Optional[str] = None
    warehouseName: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None
