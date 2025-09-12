"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class DeliveryAddress(Blueprint):
    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class RecordAddress(Blueprint):
    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class SalesInvoiceItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    accountId: Union[str, None] = None
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    commissionSalesPartners: list = []
    contractItemId: Union[str, None] = None  # Type estimated
    cost2CostCenterId: Union[str, None] = None  # Type estimated
    costCenterItems: list = []
    costTypeId: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    creditedInvoiceItemId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    deliveryDate: Union[int, None] = None  # Type estimated
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None  # Type estimated
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    manualUnitCost: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountForStatistics: Union[str, None] = None
    netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    note: Union[str, None] = None  # Type estimated
    parentItemId: Union[str, None] = None  # Type estimated
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None  # Type estimated
    reductionAdditionItems: list = []
    salesInvoiceItemRelationships: list = []
    serialNumbers: list = []
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    shippingDate: Union[int, None] = None
    taxId: Union[str, None] = None
    title: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitId: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class SalesOrders(Blueprint):
    id: Union[str, None]


class ShippingCostItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    createdDate: Union[int, None]
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
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class SalesInvoice(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    bookingDate: Union[int, None] = None  # Type estimated
    bookingText: Union[str, None] = None  # Type estimated
    cancellationDate: Union[int, None] = None  # Type estimated
    cancellationNumber: Union[str, None] = None  # Type estimated
    cancellationSlipCommissionBlock: Union[bool, None] = None
    cancellationSlipCommissionSettlementDone: Union[bool, None] = None
    collectiveInvoicePositionPrintType: Union[str, None] = None  # Type estimated
    commercialLanguage: Union[str, None] = None  # Type estimated
    commission: Union[str, None] = None  # Type estimated
    commissionBlock: Union[bool, None] = None
    commissionSalesPartners: list = []
    commissionSettlementDone: Union[bool, None] = None
    costCenterId: Union[str, None] = None  # Type estimated
    costTypeId: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    creditResetsOrderState: Union[bool, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionLocked: Union[bool, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None  # Type estimated
    customerId: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryDate: Union[int, None] = None  # Type estimated
    description: Union[str, None] = None
    directDebitFileCreated: Union[bool, None] = None
    directDebitFileLatestDate: Union[int, None] = None  # Type estimated
    disableRecordEmailingRule: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    dueDate: Union[int, None] = None
    dunningBlockDateUntilDate: Union[int, None] = None  # Type estimated
    dunningBlockNote: Union[str, None] = None  # Type estimated
    dunningBlockState: Union[str, None] = None
    factoring: Union[bool, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceDate: Union[int, None] = None
    invoiceNumber: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None  # Type estimated
    orderNumberAtCustomer: Union[str, None] = None  # Type estimated
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    paymentStatus: Union[str, None] = None
    precedingSalesInvoiceId: Union[str, None] = None
    pricingDate: Union[int, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None  # Type estimated
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordEmailAddresses: Union[str, None] = None  # Type estimated
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    responsibleUserId: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceItems: List[SalesInvoiceItems] = []
    salesInvoiceType: Union[str, None] = None
    salesOrderId: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    sentToRecipient: Union[bool, None] = None
    sepaDirectDebitMandateId: Union[int, None] = None  # Type estimated
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    shipmentMethodId: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingDate: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    termOfPaymentId: Union[str, None] = None
    vatRegistrationNumber: Union[str, None] = None  # Type estimated
