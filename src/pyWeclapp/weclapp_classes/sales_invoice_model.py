"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class ReductionAdditionItems(Blueprint):
    """Subclass for reductionAdditionItems in SalesInvoiceItems."""

    position: Union[int, None] = None
    source: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class CommissionSalesPartners(Blueprint):
    """Subclass for commissionSalesPartners in SalesInvoice and SalesInvoiceItems."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None
    salesPartnerSupplierNumber: Union[str, None] = None


class CostCenterItems(Blueprint):
    """Subclass for costCenterItems in SalesInvoiceItems."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    costCenterId: Union[str, None] = None
    costCenterNumber: Union[str, None] = None
    distributionPercentage: Union[str, None] = None


class DeliveryAddress(Blueprint):
    """Subclass for deliveryAddress in SalesInvoice."""

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


class RecordAddress(Blueprint):
    """Subclass for recordAddress in SalesInvoice."""

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
    """Subclass for recordEmailAddresses in SalesInvoice."""

    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class SalesInvoiceItemRelationship(Blueprint):
    """Subclass for salesInvoiceItemRelationship in SalesInvoiceItems."""

    performanceRecordItemId: Union[str, None] = None
    quantity: Union[str, None] = None
    salesInvoiceItemId: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None
    shipmentItemId: Union[str, None] = None


class SalesInvoiceItems(Blueprint):
    """Subclass for salesInvoiceItems in SalesInvoice."""

    id: Union[str, None]
    version: Union[str, None]
    accountId: Union[str, None] = None
    accountNumber: Union[str, None] = None
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    contractItemId: Union[str, None] = None
    cost2CostCenterId: Union[str, None] = None
    costCenterItems: List[CostCenterItems] = []
    costTypeId: Union[str, None] = None
    createdDate: Union[int, None]
    creditedInvoiceItemId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    deliveryDate: Union[int, None] = None
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    manualUnitCost: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountForStatistics: Union[str, None] = None
    netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    note: Union[str, None] = None
    parentItemId: Union[str, None] = None
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None
    reductionAdditionItems: List[ReductionAdditionItems] = []
    salesInvoiceItemRelationship: List[SalesInvoiceItemRelationship] = []
    serialNumbers: list = []
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    shippingDate: Union[int, None] = None
    taxId: Union[str, None] = None
    taxName: Union[str, None] = None
    title: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class SalesOrders(Blueprint):
    """Subclass for salesOrders in SalesInvoice."""

    id: Union[str, None]


class ShippingCostItems(Blueprint):
    """Subclass for shippingCostItems in SalesInvoice."""

    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    createdDate: Union[int, None]
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualUnitCost: Union[bool, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    taxId: Union[str, None] = None
    taxName: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class StatusHistory(Blueprint):
    """Subclass for statusHistory in SalesInvoice."""

    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class SalesInvoice(Blueprint):
    """Class for salesInvoice endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    bookingDate: Union[int, None] = None
    bookingText: Union[str, None] = None
    cancellationDate: Union[int, None] = None
    cancellationNumber: Union[str, None] = None
    cancellationSlipCommissionBlock: Union[bool, None] = None
    cancellationSlipCommissionSettlementDone: Union[bool, None] = None
    collectiveInvoicePositionPrintType: Union[str, None] = None
    commercialLanguage: Union[str, None] = None
    commission: Union[str, None] = None
    commissionBlock: Union[bool, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    commissionSettlementDone: Union[bool, None] = None
    costCenterId: Union[str, None] = None
    costTypeId: Union[str, None] = None
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    creditResetsOrderState: Union[bool, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None
    customerId: Union[str, None] = None
    customerNumber: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryDate: Union[int, None] = None
    description: Union[str, None] = None
    directDebitFileCreated: Union[bool, None] = None
    directDebitFileLatestDate: Union[int, None] = None
    disableEmailTemplate: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    dueDate: Union[int, None] = None
    dunningBlockDateUntilDate: Union[int, None] = None
    dunningBlockNote: Union[str, None] = None
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
    nonStandardTaxId: Union[str, None] = None
    nonStandardTaxName: Union[str, None] = None
    orderNumberAtCustomer: Union[str, None] = None
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    paymentMethodName: Union[str, None] = None
    paymentStatus: Union[str, None] = None
    precedingSalesInvoiceId: Union[str, None] = None
    pricingDate: Union[int, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordCurrencyName: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceItems: List[SalesInvoiceItems] = []
    salesInvoiceType: Union[str, None] = None
    salesOrderId: Union[str, None] = None
    salesOrderNumber: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    sentToRecipient: Union[bool, None] = None
    sepaDirectDebitMandateId: Union[str, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingDate: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    termOfPaymentId: Union[str, None] = None
    termOfPaymentName: Union[str, None] = None
    vatRegistrationNumber: Union[str, None] = None
