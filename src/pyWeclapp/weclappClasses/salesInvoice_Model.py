# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


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
    manualUnitCost: Optional[bool] = None
    unitCost: Optional[str] = None
    unitCostInCompanyCurrency: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Address(Blueprint):
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


class EmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ReductionAdditionItems(Blueprint):
    position: Optional[int] = None
    source: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class CommissionSalesPartners(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    commissionFix: Optional[str] = None
    commissionPercentage: Optional[str] = None
    commissionType: Optional[str] = None
    salesPartnerSupplierId: Optional[str] = None
    salesPartnerSupplierNumber: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class CostCenterItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    costCenterId: Optional[str] = None
    costCenterNumber: Optional[str] = None
    distributionPercentage: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesInvoiceItemRelationship(Blueprint):
    performanceRecordItemId: Optional[str] = None
    quantity: Optional[str] = None
    salesInvoiceItemId: Optional[str] = None
    salesOrderItemId: Optional[str] = None
    shipmentItemId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesInvoiceItems(Blueprint):
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
    commissionSalesPartners: List[CommissionSalesPartners] = []
    manualUnitCost: Optional[bool] = None
    servicePeriodFrom: Optional[int] = None
    servicePeriodTo: Optional[int] = None
    unitCost: Optional[str] = None
    unitCostInCompanyCurrency: Optional[str] = None
    accountId: Optional[str] = None
    accountNumber: Optional[str] = None
    costCenterItems: List[CostCenterItems] = []
    creditedInvoiceItemId: Optional[str] = None
    salesInvoiceItemRelationship: List[SalesInvoiceItemRelationship] = []
    serialNumbers: list = []
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesOrders(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
    status: Optional[str] = None
    statusDate: Optional[int] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesInvoice(Blueprint):
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
    commission: Optional[str] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    customerId: Optional[str] = None
    customerNumber: Optional[str] = None
    dispatchCountryCode: Optional[str] = None
    factoring: Optional[bool] = None
    pricingDate: Optional[int] = None
    responsibleUserId: Optional[str] = None
    responsibleUserUsername: Optional[str] = None
    salesChannel: Optional[str] = None
    servicePeriodFrom: Optional[int] = None
    servicePeriodTo: Optional[int] = None
    shipmentMethodId: Optional[str] = None
    shipmentMethodName: Optional[str] = None
    shippingCostItems: List[ShippingCostItems] = []
    bookingDate: Optional[int] = None
    cancellationDate: Optional[int] = None
    cancellationNumber: Optional[str] = None
    collectiveInvoicePositionPrintType: Optional[str] = None
    customerHabitualExporterLetterOfIntentId: Optional[str] = None
    deliveryAddress: Address = Address.fromBlank()
    deliveryDate: Optional[int] = None
    dueDate: Optional[int] = None
    invoiceDate: Optional[int] = None
    invoiceNumber: Optional[str] = None
    orderNumberAtCustomer: Optional[str] = None
    paid: Optional[bool] = None
    paymentStatus: Optional[str] = None
    precedingSalesInvoiceId: Optional[str] = None
    recordAddress: Address = Address.fromBlank()
    recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    salesInvoiceItems: List[SalesInvoiceItems] = []
    salesInvoiceType: Optional[str] = None
    salesOrderId: Optional[str] = None
    salesOrderNumber: Optional[str] = None
    salesOrders: List[SalesOrders] = []
    shippingDate: Optional[int] = None
    status: Optional[str] = None
    statusHistory: List[StatusHistory] = []
    vatRegistrationNumber: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "salesInvoiceItems"
