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


class DeliveryEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


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


class OrderItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    commissionSalesPartners: list = []
    contractChargeId: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    ecommerceOrderItemIds: list = []
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None  # Type estimated
    invoicedQuantity: Union[str, None] = None
    invoicingType: Union[str, None] = None  # Type estimated
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualPlannedWorkingTimePerUnit: Union[bool, None] = None
    manualQuantity: Union[bool, None] = None
    manualUnitCost: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountForStatistics: Union[str, None] = None
    netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    note: Union[str, None] = None  # Type estimated
    parentItemId: Union[str, None] = None  # Type estimated
    picks: list = []
    plannedDeliveryDate: Union[int, None] = None  # Type estimated
    plannedShippingDate: Union[int, None] = None
    plannedWorkingTimePerUnit: Union[str, None] = None  # Type estimated
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None  # Type estimated
    reductionAdditionItems: list = []
    returnedQuantity: Union[str, None] = None
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    serviceQuotaId: Union[str, None] = None  # Type estimated
    shipped: Union[bool, None] = None
    shippedQuantity: Union[str, None] = None
    tasks: list = []
    taxId: Union[str, None] = None
    title: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
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
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class ShippingCostItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    createdDate: Union[int, None]
    ecommerceOrderItemIds: list = []
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualUnitCost: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    taxId: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class StatusHistory(Blueprint):
    creditLimitExceeded: Union[bool, None] = None
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class SalesOrder(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    advancePaymentAmount: Union[str, None] = None  # Type estimated
    advancePaymentStatus: Union[str, None] = None  # Type estimated
    applyShippingCostsOnlyOnce: Union[bool, None] = None
    cashAccountId: Union[str, None] = None  # Type estimated
    commercialLanguage: Union[str, None] = None  # Type estimated
    commission: Union[str, None] = None  # Type estimated
    commissionSalesPartners: list = []
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionLocked: Union[bool, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None  # Type estimated
    customerId: Union[str, None] = None
    defaultShippingCarrierId: Union[str, None] = None
    defaultShippingReturnCarrierId: Union[str, None] = None  # Type estimated
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.from_blank()
    description: Union[str, None] = None  # Type estimated
    disableRecordEmailingRule: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    ecommerceOrder: Union[str, None] = None  # Type estimated
    factoring: Union[bool, None] = None
    fulfillmentProviderId: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None  # Type estimated
    invoiced: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None  # Type estimated
    note: Union[str, None] = None  # Type estimated
    onlyServices: Union[bool, None] = None
    orderDate: Union[int, None] = None
    orderItems: List[OrderItems] = []
    orderNumber: Union[str, None] = None
    orderNumberAtCustomer: Union[str, None] = None  # Type estimated
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    payments: Union[str, None] = None  # Type estimated
    plannedDeliveryDate: Union[int, None] = None  # Type estimated
    plannedProjectEndDate: Union[int, None] = None  # Type estimated
    plannedProjectStartDate: Union[int, None] = None  # Type estimated
    plannedShippingDate: Union[int, None] = None
    pricingDate: Union[int, None] = None
    projectGoals: Union[str, None] = None  # Type estimated
    projectMembers: list = []
    projectModeActive: Union[bool, None] = None
    quotationId: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordAsn: Union[str, None] = None  # Type estimated
    recordComment: Union[str, None] = None  # Type estimated
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    responsibleUserId: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.from_blank()
    salesOrderPaymentType: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    sepaDirectDebitMandateId: Union[int, None] = None  # Type estimated
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    servicesFinished: Union[bool, None] = None
    shipmentMethodId: Union[str, None] = None
    shipped: Union[bool, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingLabelsCount: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    template: Union[bool, None] = None
    termOfPaymentId: Union[str, None] = None
    warehouseId: Union[str, None] = None
