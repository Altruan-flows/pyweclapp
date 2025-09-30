"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List, Set
from .blueprints import Blueprint, WeclappMetaData


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


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class ReductionAdditionItems(Blueprint):
    position: Union[int, None] = None
    source: Union[str, None] = None
    specialPriceReduction: Union[bool, None] = None
    title: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class CommissionSalesPartners(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None


class CostCenterItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    costCenterId: Union[str, None] = None
    distributionPercentage: Union[str, None] = None


class SalesInvoiceItemRelationships(Blueprint):
    performanceRecordItemId: Union[str, None] = None
    quantity: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None
    shipmentItemId: Union[str, None] = None


class SalesInvoiceItems(Blueprint):
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
    accountId: Union[str, None] = None
    contractItemId: Union[str, None] = None
    cost2CostCenterId: Union[str, None] = None
    costCenterItems: List[CostCenterItems] = []
    costTypeId: Union[str, None] = None
    creditedInvoiceItemId: Union[str, None] = None
    deliveryDate: Union[int, None] = None
    salesInvoiceItemRelationships: List[SalesInvoiceItemRelationships] = []
    serialNumbers: list = []
    shippingDate: Union[int, None] = None

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
        "salesInvoiceItemRelationships",
    }


class SalesOrders(Blueprint):
    id: Union[str, None] = None


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


class SalesInvoice(Blueprint):
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
    bookingDate: Union[int, None] = None
    bookingText: Union[str, None] = None
    cancellationDate: Union[int, None] = None
    cancellationNumber: Union[str, None] = None
    cancellationSlipCommissionBlock: Union[bool, None] = None
    cancellationSlipCommissionSettlementDone: Union[bool, None] = None
    collectiveInvoicePositionPrintType: Union[str, None] = None
    commissionBlock: Union[bool, None] = None
    commissionSettlementDone: Union[bool, None] = None
    costCenterId: Union[str, None] = None
    costTypeId: Union[str, None] = None
    creditResetsOrderState: Union[bool, None] = None
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None
    deliveryAddress: DeliveryAddress = None
    deliveryDate: Union[int, None] = None
    directDebitFileCreated: Union[bool, None] = None
    directDebitFileLatestDate: Union[int, None] = None
    dueDate: Union[int, None] = None
    dunningBlockDateUntilDate: Union[int, None] = None
    dunningBlockNote: Union[str, None] = None
    dunningBlockState: Union[str, None] = None
    invoiceDate: Union[int, None] = None
    invoiceNumber: Union[str, None] = None
    orderNumberAtCustomer: Union[str, None] = None
    paid: Union[bool, None] = None
    paymentStatus: Union[str, None] = None
    precedingSalesInvoiceId: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress()
    recordCommentInheritance: Union[bool, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses()
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    salesInvoiceItems: List[SalesInvoiceItems] = []
    salesInvoiceType: Union[str, None] = None
    salesOrderId: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    sepaDirectDebitMandateId: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingDate: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    vatRegistrationNumber: Union[str, None] = None

    excluded_keys: Set[str] = {
        "paid",
        "unitCostInCompanyCurrency",
        "unitPriceInCompanyCurrency",
        "netAmount",
        "netAmountInCompanyCurrency",
        "grossAmount",
        "grossAmountInCompanyCurrency",
        "salesInvoiceItemRelationships"
    }
