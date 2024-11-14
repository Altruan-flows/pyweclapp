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


class EcommerceOrder(Blueprint):
    ecommerceId: Optional[str] = None
    externalConnectionId: Optional[str] = None
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


class Tasks(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class OrderItems(Blueprint):
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
    invoicingType: Optional[str] = None
    manualPlannedWorkingTimePerUnit: Optional[bool] = None
    plannedWorkingTimePerUnit: Optional[str] = None
    serviceItem: Optional[bool] = None
    availability: Optional[str] = None
    availabilityForAllWarehouses: Optional[str] = None
    ecommerceOrderItemId: Optional[str] = None
    invoicedQuantity: Optional[str] = None
    pickBatchNumber: Optional[str] = None
    pickSerialNumbers: list = []
    pickStoragePlaceId: Optional[str] = None
    plannedShippingDate: Optional[int] = None
    returnedQuantity: Optional[str] = None
    shipped: Optional[bool] = None
    shippedQuantity: Optional[str] = None
    tasks: List[Tasks] = []
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ProjectMembers(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    hourlyCost: Optional[str] = None
    teamRole: Optional[str] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class EmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
    status: Optional[str] = None
    statusDate: Optional[int] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesOrder(Blueprint):
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
    defaultShippingCarrierId: Optional[str] = None
    defaultShippingCarrierName: Optional[str] = None
    deliveryAddress: Address = Address.fromBlank()
    deliveryEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    invoiceAddress: Address = Address.fromBlank()
    plannedDeliveryDate: Optional[int] = None
    plannedShippingDate: Optional[int] = None
    recordAddress: Address = Address.fromBlank()
    salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    advancePaymentStatus: Optional[str] = None
    availability: Optional[str] = None
    availabilityForAllWarehouses: Optional[str] = None
    cashAccountId: Optional[str] = None
    customerHabitualExporterLetterOfIntentId: Optional[str] = None
    defaultShippingReturnCarrierId: Optional[str] = None
    defaultShippingReturnCarrierName: Optional[str] = None
    ecommerceOrder: EcommerceOrder = EcommerceOrder.fromBlank()
    fulfillmentProviderId: Optional[str] = None
    invoiceRecipientId: Optional[str] = None
    invoiced: Optional[bool] = None
    onlyServices: Optional[bool] = None
    orderDate: Optional[int] = None
    orderItems: List[OrderItems] = []
    orderNumber: Optional[str] = None
    orderNumberAtCustomer: Optional[str] = None
    paid: Optional[bool] = None
    plannedProjectEndDate: Optional[int] = None
    plannedProjectStartDate: Optional[int] = None
    projectGoals: Optional[str] = None
    projectMembers: List[ProjectMembers] = []
    projectModeActive: Optional[bool] = None
    quotationId: Optional[str] = None
    quotationNumber: Optional[str] = None
    recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    salesOrderPaymentType: Optional[str] = None
    servicesFinished: Optional[bool] = None
    shipped: Optional[bool] = None
    shippingLabelsCount: Optional[int] = None
    status: Optional[str] = None
    statusHistory: List[StatusHistory] = []
    warehouseId: Optional[str] = None
    warehouseName: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "orderItems"
