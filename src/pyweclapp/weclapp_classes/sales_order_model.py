"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List, Set
from .blueprints import Blueprint, WeclappMetaData


class CommissionSalesPartners(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None


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


class DeliveryEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


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


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class EcommerceOrder(Blueprint):
    ecommerceId: Union[str, None] = None
    externalConnectionId: Union[str, None] = None


class ReductionAdditionItems(Blueprint):
    position: Union[int, None] = None
    source: Union[str, None] = None
    specialPriceReduction: Union[bool, None] = None
    title: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class Picks(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    batchNumber: Union[str, None] = None
    confirmedByUserId: Union[str, None] = None
    confirmedDate: Union[int, None] = None
    internalTransportReferenceId: Union[str, None] = None
    quantity: Union[str, None] = None
    serialNumbers: list = []
    storagePlaceId: Union[str, None] = None
    bookedDate: Union[int, None] = None
    orderItemId: Union[str, None] = None
    sourceInternalTransportReferenceId: Union[str, None] = None
    sourceStoragePlaceId: Union[str, None] = None
    transportationOrderId: Union[str, None] = None


class Tasks(Blueprint):
    id: Union[str, None] = None


class OrderItems(Blueprint):
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
    commissionSalesPartners: List[CommissionSalesPartners] = []
    manualUnitCost: Union[bool, None] = None
    recommendedRetailPrice: Union[str, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    invoicingType: Union[str, None] = None
    manualPlannedWorkingTimePerUnit: Union[bool, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    plannedWorkingTimePerUnit: Union[int, None] = None
    contractChargeId: Union[str, None] = None
    ecommerceOrderItemIds: list = []
    invoicedQuantity: Union[str, None] = None
    picks: List[Picks] = []
    returnedQuantity: Union[str, None] = None
    serviceQuotaId: Union[str, None] = None
    shipped: Union[bool, None] = None
    shippedQuantity: Union[str, None] = None
    tasks: List[Tasks] = []

    excluded_keys: Set[str] = {
        "version",
        "grossAmount",
        "grossAmountInCompanyCurrency",
        "netAmount",
        "netAmountForStatistics",
        "netAmountForStatisticsInCompanyCurrency",
        "netAmountInCompanyCurrency",
        "unitPriceInCompanyCurrency",
        "unitCostInCompanyCurrency",
        "invoicedQuantity",
        "shippedQuantity",
        "returnedQuantity",
        "shipped",
    }


class SalesInvoices(Blueprint):
    id: Union[str, None] = None


class Payments(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    amount: Union[str, None] = None
    condition: Union[str, None] = None
    conditionMet: Union[bool, None] = None
    dueDate: Union[int, None] = None
    positionNumber: Union[int, None] = None
    salesInvoiceId: Union[str, None] = None
    salesInvoices: List[SalesInvoices] = []


class ProjectMembers(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    hourlyCost: Union[str, None] = None
    teamRole: Union[str, None] = None
    userId: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


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
    manualUnitCost: Union[bool, None] = None
    taxId: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    ecommerceOrderItemIds: list = []

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
    creditLimitExceeded: Union[bool, None] = None
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class SalesOrder(Blueprint):
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
    commission: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    customerId: Union[str, None] = None
    dispatchCountryCode: Union[str, None] = None
    factoring: Union[bool, None] = None
    pricingDate: Union[int, None] = None
    responsibleUserId: Union[str, None] = None
    salesChannel: Union[str, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    shipmentMethodId: Union[str, None] = None
    defaultShippingCarrierId: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress()
    deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses()
    invoiceAddress: InvoiceAddress = InvoiceAddress()
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    recordAddress: RecordAddress = RecordAddress()
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses()
    advancePaymentAmount: Union[str, None] = None
    advancePaymentStatus: Union[str, None] = None
    applyShippingCostsOnlyOnce: Union[bool, None] = None
    cashAccountId: Union[str, None] = None
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None
    defaultShippingReturnCarrierId: Union[str, None] = None
    ecommerceOrder: EcommerceOrder = EcommerceOrder()
    fulfillmentProviderId: Union[str, None] = None
    invoiceRecipientId: Union[str, None] = None
    invoiced: Union[bool, None] = None
    note: Union[str, None] = None
    onlyServices: Union[bool, None] = None
    orderDate: Union[int, None] = None
    orderItems: List[OrderItems] = []
    orderNumber: Union[str, None] = None
    orderNumberAtCustomer: Union[str, None] = None
    paid: Union[bool, None] = None
    payments: List[Payments] = []
    plannedProjectEndDate: Union[int, None] = None
    plannedProjectStartDate: Union[int, None] = None
    projectGoals: Union[str, None] = None
    projectMembers: List[ProjectMembers] = []
    projectModeActive: Union[bool, None] = None
    quotationId: Union[str, None] = None
    recordAsn: Union[str, None] = None
    recordCommentInheritance: Union[bool, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses()
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    salesOrderPaymentType: Union[str, None] = None
    sepaDirectDebitMandateId: Union[str, None] = None
    servicesFinished: Union[bool, None] = None
    shipped: Union[bool, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingLabelsCount: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    template: Union[bool, None] = None
    warehouseId: Union[str, None] = None

    excluded_keys: Set[str] = {
        "paid",
        "unitCostInCompanyCurrency",
        "unitPriceInCompanyCurrency",
        "shippedQuantity",
        "invoicedQuantity",
        "returnedQuantity",
        "shipped",
        "invoiced",
    }
