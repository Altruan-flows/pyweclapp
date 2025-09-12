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


class ReductionAdditionItems(Blueprint):
    position: Union[int, None] = None
    source: Union[str, None] = None
    specialPriceReduction: Union[bool, None] = None
    title: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class QuotationItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    alternative: Union[bool, None] = None
    articleId: Union[str, None] = None
    commissionSalesPartners: list = []
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None  # Type estimated
    invoicingType: Union[str, None] = None  # Type estimated
    itScopeId: Union[str, None] = None  # Type estimated
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
    optional: Union[bool, None] = None
    parentItemId: Union[str, None] = None  # Type estimated
    plannedDeliveryDate: Union[int, None] = None  # Type estimated
    plannedShippingDate: Union[int, None] = None  # Type estimated
    plannedWorkingTimePerUnit: Union[str, None] = None  # Type estimated
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None  # Type estimated
    reductionAdditionItems: List[ReductionAdditionItems] = []
    scaleValues: list = []
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
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


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesOrderEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesStageHistory(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    createdDate: Union[int, None]
    lastModifiedDate: Union[int, None]
    salesStageId: Union[str, None] = None
    userId: Union[str, None] = None


class StatusHistory(Blueprint):
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class Quotation(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    activeVersion: Union[bool, None] = None
    commercialLanguage: Union[str, None] = None  # Type estimated
    commission: Union[str, None] = None  # Type estimated
    commissionSalesPartners: list = []
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionLocked: Union[bool, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerId: Union[str, None] = None
    defaultShippingCarrierId: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.from_blank()
    description: Union[str, None] = None  # Type estimated
    disableRecordEmailingRule: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    expectedSignatureDate: Union[int, None] = None  # Type estimated
    factoring: Union[bool, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    mergedToQuotationId: Union[str, None] = None  # Type estimated
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None  # Type estimated
    opportunityId: Union[str, None] = None  # Type estimated
    paymentMethodId: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None  # Type estimated
    plannedShippingDate: Union[int, None] = None  # Type estimated
    pricingDate: Union[int, None] = None
    publicLink: Union[str, None] = None
    quotationDate: Union[int, None] = None
    quotationItems: List[QuotationItems] = []
    quotationNumber: Union[str, None] = None
    quotationType: Union[str, None] = None
    quotationVersion: Union[int, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None  # Type estimated
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    rejectionReason: Union[str, None] = None  # Type estimated
    requestDate: Union[int, None] = None
    responsibleUserId: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.from_blank()
    salesOrderEmailAddresses: SalesOrderEmailAddresses = SalesOrderEmailAddresses.from_blank()
    salesProbability: Union[int, None] = None
    salesStageHistory: List[SalesStageHistory] = []
    salesStageId: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    servicePeriodFrom: Union[str, None] = None  # Type estimated
    servicePeriodTo: Union[str, None] = None  # Type estimated
    shipmentMethodId: Union[str, None] = None  # Type estimated
    shippingCostItems: list = []
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    template: Union[bool, None] = None
    termOfPaymentId: Union[str, None] = None
    validFrom: Union[int, None] = None
    validTo: Union[int, None] = None
    warehouseId: Union[str, None] = None  # Type estimated
