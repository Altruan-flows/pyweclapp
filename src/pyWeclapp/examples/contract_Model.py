# This code was dynamically created using WeclappClassCreator from pyWeclapp

from weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


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


class AdditionalAddresses(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    address: Address = Address.fromBlank()
    description: Optional[str] = None
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


class ContractCostItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    description: Optional[str] = None
    descriptionFixed: Optional[bool] = None
    discountPercentage: Optional[str] = None
    interval: Optional[str] = None
    intervalType: Optional[str] = None
    manualUnitPrice: Optional[bool] = None
    netAmount: Optional[str] = None
    netAmountInCompanyCurrency: Optional[str] = None
    note: Optional[str] = None
    quantity: Optional[str] = None
    servicePeriodFrom: Optional[int] = None
    servicePeriodTo: Optional[int] = None
    title: Optional[str] = None
    unitId: Optional[str] = None
    unitPrice: Optional[str] = None
    unitPriceInCompanyCurrency: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ReductionAdditionItems(Blueprint):
    position: Optional[int] = None
    source: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ContractItems(Blueprint):
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
    billingGroupId: Optional[str] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    costTypeId: Optional[str] = None
    interval: Optional[str] = None
    intervalType: Optional[str] = None
    nextContractBillingDate: Optional[int] = None
    previousContractBillingDate: Optional[int] = None
    servicePeriodFromDate: Optional[int] = None
    servicePeriodToDate: Optional[int] = None
    type: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class CorrespondenceAddress(Blueprint):
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


class DeliveryAddress(Blueprint):
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


class DeliveryEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class InvoiceAddress(Blueprint):
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


class PurchaseEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesOrderEmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Types(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Contract(Blueprint):
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
    additionalAddresses: List[AdditionalAddresses] = []
    authorizationUnitId: Optional[str] = None
    automaticExtension: Optional[bool] = None
    billUntil: Optional[str] = None
    billingDay: Optional[int] = None
    billingTargetInvoiceStatus: Optional[str] = None
    billingType: Optional[str] = None
    cancellationDate: Optional[int] = None
    cancellationPeriodQuantity: Optional[int] = None
    cancellationPeriodSoftframe: Optional[str] = None
    cancellationPeriodUnit: Optional[str] = None
    commission: Optional[str] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    contractCostItems: List[ContractCostItems] = []
    contractDate: Optional[int] = None
    contractItems: List[ContractItems] = []
    contractNumber: Optional[str] = None
    contractNumberAtParty: Optional[str] = None
    contractStatus: Optional[str] = None
    correspondenceAddress: CorrespondenceAddress = CorrespondenceAddress.fromBlank()
    deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
    deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.fromBlank()
    differingCorrespondenceAddress: Optional[bool] = None
    differingDeliveryAddress: Optional[bool] = None
    differingInvoiceAddress: Optional[bool] = None
    endDate: Optional[int] = None
    extensionQuantity: Optional[int] = None
    extensionUnit: Optional[str] = None
    factoring: Optional[bool] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
    invoiceRecipientId: Optional[str] = None
    latestCancellationWarningQuantity: Optional[int] = None
    latestCancellationWarningUnit: Optional[str] = None
    latestPossibleTerminationDate: Optional[int] = None
    name: Optional[str] = None
    nextContractBillingDate: Optional[int] = None
    nonStandardInputTaxId: Optional[str] = None
    orderNumberAtCustomer: Optional[str] = None
    partyId: Optional[str] = None
    paymentMethodId: Optional[str] = None
    pricingDate: Optional[int] = None
    purchaseEmailAddresses: PurchaseEmailAddresses = PurchaseEmailAddresses.fromBlank()
    recordCurrencyId: Optional[str] = None
    recordCurrencyName: Optional[str] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
    reminderDate: Optional[int] = None
    reminderSendType: Optional[str] = None
    reminderType: Optional[str] = None
    responsibleUserId: Optional[str] = None
    salesChannel: Optional[str] = None
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = (
        SalesInvoiceEmailAddresses.fromBlank()
    )
    salesOrderEmailAddresses: SalesOrderEmailAddresses = (
        SalesOrderEmailAddresses.fromBlank()
    )
    startDate: Optional[int] = None
    template: Optional[bool] = None
    termOfPaymentId: Optional[str] = None
    terminationReasonId: Optional[str] = None
    ticketServiceLevelAgreementId: Optional[str] = None
    types: List[Types] = []
    unlimited: Optional[bool] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "contractItems"
