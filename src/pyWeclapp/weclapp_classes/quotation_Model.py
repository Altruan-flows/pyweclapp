"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class ShippingCostItems(Blueprint):
    """Subclass for shippingCostItems in Quotation."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    manualUnitPrice: Union[bool, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    taxId: Union[str, None] = None
    taxName: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None
    manualUnitCost: Union[bool, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None


class ReductionAdditionItems(Blueprint):
    """Subclass for reductionAdditionItems in QuotationItems."""

    position: Union[int, None] = None
    source: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class CommissionSalesPartners(Blueprint):
    """Subclass for commissionSalesPartners in QuotationItems and Quotation."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None
    salesPartnerSupplierNumber: Union[str, None] = None


class DeliveryAddress(Blueprint):
    """Subclass for deliveryAddress in Quotation."""

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


class InvoiceAddress(Blueprint):
    """Subclass for invoiceAddress in Quotation."""

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


class QuotationItems(Blueprint):
    """Subclass for quotationItems in Quotation."""

    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    alternative: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None
    invoicingType: Union[str, None] = None
    itScopeId: Union[str, None] = None
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
    note: Union[str, None] = None
    parentItemId: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    plannedWorkingTimePerUnit: Union[str, None] = None
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None
    reductionAdditionItems: List[ReductionAdditionItems] = []
    scaleValues: list = []
    servicePeriodFrom: Union[str, None] = None
    servicePeriodTo: Union[str, None] = None
    taxId: Union[str, None] = None
    taxName: Union[str, None] = None
    title: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class RecordAddress(Blueprint):
    """Subclass for recordAddress in Quotation."""

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


class EmailAddresses(Blueprint):
    """Subclass for salesInvoiceEmailAddresses, deliveryEmailAddresses,
    salesOrderEmailAddresses, recordEmailAddresses in Quotation."""

    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class SalesStageHistory(Blueprint):
    """Subclass for salesStageHistory in Quotation."""

    id: Union[str, None]
    version: Union[str, None]
    createdDate: Union[int, None]
    lastModifiedDate: Union[int, None]
    salesStageId: Union[str, None] = None
    salesStageName: Union[str, None] = None
    userId: Union[str, None] = None


class StatusHistory(Blueprint):
    """Subclass for statusHistory in Quotation."""

    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class Quotation(Blueprint):
    """Class for quotation endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    activeVersion: Union[bool, None] = None
    commercialLanguage: Union[str, None] = None
    commission: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerId: Union[str, None] = None
    customerNumber: Union[str, None] = None
    defaultShippingCarrierId: Union[str, None] = None
    defaultShippingCarrierName: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    description: Union[str, None] = None
    disableEmailTemplate: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    expectedSignatureDate: Union[int, None] = None
    factoring: Union[bool, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    mergedToQuotationId: Union[str, None] = None
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None
    nonStandardTaxName: Union[str, None] = None
    opportunityId: Union[str, None] = None
    opportunityNumber: Union[str, None] = None
    paymentMethodId: Union[str, None] = None
    paymentMethodName: Union[str, None] = None
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    pricingDate: Union[int, None] = None
    publicLink: Union[str, None] = None
    quotationDate: Union[int, None] = None
    quotationItems: List[QuotationItems] = []
    quotationNumber: Union[str, None] = None
    quotationType: Union[str, None] = None
    quotationVersion: Union[int, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordComment: Union[str, None] = None
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordCurrencyName: Union[str, None] = None
    recordEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    rejectionReason: Union[str, None] = None
    requestDate: Union[int, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    salesOrderEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    salesProbability: Union[int, None] = None
    salesStageHistory: List[SalesStageHistory] = []
    salesStageId: Union[str, None] = None
    salesStageName: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    template: Union[bool, None] = None
    termOfPaymentId: Union[str, None] = None
    termOfPaymentName: Union[str, None] = None
    validFrom: Union[int, None] = None
    validTo: Union[int, None] = None
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
