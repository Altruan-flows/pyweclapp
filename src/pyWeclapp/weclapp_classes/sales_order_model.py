"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class ReductionAdditionItems(Blueprint):
    """Subclass for reductionAdditionItems in OrderItems."""

    position: Union[int, None] = None
    source: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class CommissionSalesPartners(Blueprint):
    """Subclass for commissionSalesPartners in SalesOrder."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None
    salesPartnerSupplierNumber: Union[str, None] = None


class Tasks(Blueprint):
    """Subclass for tasks in OrderItems."""

    id: Union[str, None] = None


class ProjectMembers(Blueprint):
    """Subclass for projectMembers in SalesOrder."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    hourlyCost: Union[str, None] = None
    teamRole: Union[str, None] = None
    userId: Union[str, None] = None


class EcommerceOrder(Blueprint):
    """Subclass for ecommerceOrder in SalesOrder."""

    ecommerceId: Union[str, None] = None
    externalConnectionId: Union[str, None] = None


class EmailAddress(Blueprint):
    """Subclass for deliveryEmailAddresses, recordEmailAddresses,
    salesInvoiceEmailAddresses in SalesOrder."""

    toAddresses: Union[str, None] = None


class DeliveryAddress(Blueprint):
    """Subclass for deliveryAddress in SalesOrder."""

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
    """Subclass for invoiceAddress in SalesOrder."""

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


class OrderItems(Blueprint):
    """Subclass for orderItems in SalesOrder."""

    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    availability: Union[str, None] = None
    availabilityForAllWarehouses: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    contractChargeId: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    discountPercentage: Union[str, None] = None
    ecommerceOrderItemIds: list = []
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    groupName: Union[str, None] = None
    invoicedQuantity: Union[str, None] = None
    invoicingType: Union[str, None] = None
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
    picks: list = []
    plannedDeliveryDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    plannedWorkingTimePerUnit: Union[int, None] = None
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None
    recommendedRetailPrice: Union[str, None] = None
    reductionAdditionItems: List[ReductionAdditionItems] = []
    returnedQuantity: Union[str, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    serviceQuotaId: Union[str, None] = None
    shipped: Union[bool, None] = None
    shippedQuantity: Union[str, None] = None
    tasks: List[Tasks] = []
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
    """Subclass for recordAddress in SalesOrder."""

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


class ShippingCostItems(Blueprint):
    """Subclass for shippingCostItems in SalesOrder."""

    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
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
    taxName: Union[str, None] = None
    unitCost: Union[str, None] = None
    unitCostInCompanyCurrency: Union[str, None] = None
    unitPrice: Union[str, None] = None
    unitPriceInCompanyCurrency: Union[str, None] = None


class StatusHistory(Blueprint):
    """Subclass for statusHistory in SalesOrder."""

    creditLimitExceeded: Union[bool, None] = None
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class SalesOrder(Blueprint):
    """Class for salesOrder endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    advancePaymentAmount: Union[float, None] = None
    advancePaymentStatus: Union[str, None] = None
    applyShippingCostsOnlyOnce: Union[bool, None] = None
    availability: Union[str, None] = None
    availabilityForAllWarehouses: Union[str, None] = None
    cashAccountId: Union[str, None] = None
    commercialLanguage: Union[str, None] = None
    commission: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    currencyConversionDate: Union[int, None] = None
    currencyConversionRate: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerHabitualExporterLetterOfIntentId: Union[str, None] = None
    customerId: Union[str, None] = None
    customerNumber: Union[str, None] = None
    defaultShippingCarrierId: Union[str, None] = None
    defaultShippingCarrierName: Union[str, None] = None
    defaultShippingReturnCarrierId: Union[str, None] = None
    defaultShippingReturnCarrierName: Union[str, None] = None
    deliveryAddress: DeliveryAddress = DeliveryAddress.from_blank()
    deliveryEmailAddresses: EmailAddress = EmailAddress.from_blank()
    description: Union[str, None] = None
    disableEmailTemplate: Union[bool, None] = None
    dispatchCountryCode: Union[str, None] = None
    ecommerceOrder: EcommerceOrder = EcommerceOrder.from_blank()
    factoring: Union[bool, None] = None
    fulfillmentProviderId: Union[str, None] = None
    grossAmount: Union[str, None] = None
    grossAmountInCompanyCurrency: Union[str, None] = None
    headerDiscount: Union[str, None] = None
    headerSurcharge: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None
    invoiced: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    netAmount: Union[str, None] = None
    netAmountInCompanyCurrency: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None
    nonStandardTaxName: Union[str, None] = None
    note: Union[str, None] = None
    onlyServices: Union[bool, None] = None
    orderDate: Union[int, None] = None
    orderItems: List[OrderItems] = []
    orderNumber: Union[str, None] = None
    orderNumberAtCustomer: Union[str, None] = None
    paid: Union[bool, None] = None
    paymentMethodId: Union[str, None] = None
    paymentMethodName: Union[str, None] = None
    payments: list = []
    plannedDeliveryDate: Union[int, None] = None
    plannedProjectEndDate: Union[int, None] = None
    plannedProjectStartDate: Union[int, None] = None
    plannedShippingDate: Union[int, None] = None
    pricingDate: Union[int, None] = None
    projectGoals: Union[str, None] = None
    projectMembers: List[ProjectMembers] = []
    projectModeActive: Union[bool, None] = None
    quotationId: Union[str, None] = None
    quotationNumber: Union[str, None] = None
    recordAddress: RecordAddress = RecordAddress.from_blank()
    recordAsn: Union[str, None] = None
    recordComment: Union[str, None] = None
    recordCommentInheritance: Union[bool, None] = None
    recordCurrencyId: Union[str, None] = None
    recordCurrencyName: Union[str, None] = None
    recordEmailAddresses: EmailAddress = EmailAddress.from_blank()
    recordFreeText: Union[str, None] = None
    recordFreeTextInheritance: Union[bool, None] = None
    recordOpening: Union[str, None] = None
    recordOpeningInheritance: Union[bool, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesInvoiceEmailAddresses: EmailAddress = EmailAddress.from_blank()
    salesOrderPaymentType: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    sepaDirectDebitMandateId: Union[int, None] = None
    servicePeriodFrom: Union[int, None] = None
    servicePeriodTo: Union[int, None] = None
    servicesFinished: Union[bool, None] = None
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    shipped: Union[bool, None] = None
    shippingCostItems: List[ShippingCostItems] = []
    shippingLabelsCount: Union[int, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    template: Union[bool, None] = None
    termOfPaymentId: Union[str, None] = None
    termOfPaymentName: Union[str, None] = None
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
