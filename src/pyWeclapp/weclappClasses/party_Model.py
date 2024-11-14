# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


class Addresses(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    deliveryAddress: Optional[bool] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    invoiceAddress: Optional[bool] = None
    lastName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    primeAddress: Optional[bool] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class OnlineAccounts(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    accountName: Optional[str] = None
    accountType: Optional[str] = None
    url: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class BankAccounts(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    accountHolder: Optional[str] = None
    accountNumber: Optional[str] = None
    bankCode: Optional[str] = None
    creditInstitute: Optional[str] = None
    partyId: Optional[str] = None
    primary: Optional[bool] = None
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


class Contacts(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class CustomerSalesStageHistory(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    salesStageId: Optional[str] = None
    salesStageName: Optional[str] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PartyEmailAddresses(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Invoices(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PartyHabitualExporterLettersOfIntent(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    automaticallySuggestInInvoice: Optional[bool] = None
    date: Optional[int] = None
    fromSupplier: Optional[bool] = None
    invoices: List[Invoices] = []
    numberDeclarer: Optional[str] = None
    numberSupplier: Optional[str] = None
    totalAmount: Optional[str] = None
    type: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Topics(Blueprint):
    id: Optional[str] = None
    name: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Party(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    addresses: List[Addresses] = []
    birthDate: Optional[int] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    deliveryAddressId: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    firstName: Optional[str] = None
    invoiceAddressId: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    mobilePhone1: Optional[str] = None
    onlineAccounts: List[OnlineAccounts] = []
    partyType: Optional[str] = None
    personCompany: Optional[str] = None
    personDepartmentId: Optional[str] = None
    personRoleId: Optional[str] = None
    phone: Optional[str] = None
    primaryAddressId: Optional[str] = None
    salutation: Optional[str] = None
    tags: list = []
    title: Optional[str] = None
    titleId: Optional[str] = None
    website: Optional[str] = None
    bankAccounts: List[BankAccounts] = []
    commercialLanguageId: Optional[str] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    companySizeId: Optional[str] = None
    companySizeName: Optional[str] = None
    competitor: Optional[bool] = None
    contacts: List[Contacts] = []
    currencyId: Optional[str] = None
    currencyName: Optional[str] = None
    customer: Optional[bool] = None
    customerAmountInsured: Optional[str] = None
    customerAnnualRevenue: Optional[str] = None
    customerBlockNotice: Optional[str] = None
    customerBlocked: Optional[bool] = None
    customerBusinessType: Optional[str] = None
    customerCategoryId: Optional[str] = None
    customerCategoryName: Optional[str] = None
    customerCreditLimit: Optional[str] = None
    customerCurrentSalesStageId: Optional[str] = None
    customerCurrentSalesStageName: Optional[str] = None
    customerDebtorAccountId: Optional[str] = None
    customerDebtorAccountNumber: Optional[str] = None
    customerDebtorAccountingCodeId: Optional[str] = None
    customerDefaultHeaderDiscount: Optional[str] = None
    customerDefaultHeaderSurcharge: Optional[str] = None
    customerDefaultShippingCarrierId: Optional[str] = None
    customerDeliveryBlock: Optional[bool] = None
    customerInsolvent: Optional[bool] = None
    customerInsured: Optional[bool] = None
    customerInternalNote: Optional[str] = None
    customerLossDescription: Optional[str] = None
    customerLossReasonId: Optional[str] = None
    customerLossReasonName: Optional[str] = None
    customerNonStandardTaxId: Optional[str] = None
    customerNumber: Optional[str] = None
    customerNumberOld: Optional[str] = None
    customerPaymentMethodId: Optional[str] = None
    customerPaymentMethodName: Optional[str] = None
    customerSalesChannel: Optional[str] = None
    customerSalesOrderPaymentType: Optional[str] = None
    customerSalesProbability: Optional[int] = None
    customerSalesStageHistory: List[CustomerSalesStageHistory] = []
    customerSatisfaction: Optional[str] = None
    customerShipmentMethodId: Optional[str] = None
    customerShipmentMethodName: Optional[str] = None
    customerSupplierNumber: Optional[str] = None
    customerTermOfPaymentId: Optional[str] = None
    customerTermOfPaymentName: Optional[str] = None
    customerUseCustomsTariffNumber: Optional[bool] = None
    deliveryEmailAddressesId: Optional[str] = None
    description: Optional[str] = None
    dunningAddressId: Optional[str] = None
    dunningEmailAddressesId: Optional[str] = None
    enableDropshippingInNewSupplySources: Optional[bool] = None
    eoriNumber: Optional[str] = None
    factoring: Optional[bool] = None
    fixPhone2: Optional[str] = None
    fixedResponsibleUser: Optional[bool] = None
    formerSalesPartner: Optional[bool] = None
    habitualExporter: Optional[bool] = None
    imageId: Optional[str] = None
    invoiceBlock: Optional[bool] = None
    invoiceRecipientId: Optional[str] = None
    leadRatingId: Optional[str] = None
    leadRatingName: Optional[str] = None
    leadSourceId: Optional[str] = None
    leadSourceName: Optional[str] = None
    leadStatus: Optional[str] = None
    legalFormId: Optional[str] = None
    legalFormName: Optional[str] = None
    mobilePhone2: Optional[str] = None
    optInEmail: Optional[bool] = None
    optInLetter: Optional[bool] = None
    optInPhone: Optional[bool] = None
    optInSms: Optional[bool] = None
    parentPartyId: Optional[str] = None
    partyEmailAddresses: List[PartyEmailAddresses] = []
    partyHabitualExporterLettersOfIntent: List[PartyHabitualExporterLettersOfIntent] = (
        []
    )
    phoneHome: Optional[str] = None
    primaryContactId: Optional[str] = None
    purchaseEmailAddressesId: Optional[str] = None
    purchaseViaPlafond: Optional[bool] = None
    quotationEmailAddressesId: Optional[str] = None
    ratingId: Optional[str] = None
    ratingName: Optional[str] = None
    referenceNumber: Optional[str] = None
    responsibleUserId: Optional[str] = None
    responsibleUserUsername: Optional[str] = None
    salesInvoiceEmailAddressesId: Optional[str] = None
    salesOrderEmailAddressesId: Optional[str] = None
    salesPartner: Optional[bool] = None
    salesPartnerDefaultCommissionFix: Optional[str] = None
    salesPartnerDefaultCommissionPercentage: Optional[str] = None
    salesPartnerDefaultCommissionType: Optional[str] = None
    sectorId: Optional[str] = None
    sectorName: Optional[str] = None
    supplier: Optional[bool] = None
    supplierCreditorAccountId: Optional[str] = None
    supplierCreditorAccountNumber: Optional[str] = None
    supplierCreditorAccountingCodeId: Optional[str] = None
    supplierCustomerNumberAtSupplier: Optional[str] = None
    supplierDefaultShippingCarrierId: Optional[str] = None
    supplierInternalNote: Optional[str] = None
    supplierMinimumPurchaseOrderAmount: Optional[str] = None
    supplierNonStandardTaxId: Optional[str] = None
    supplierNumber: Optional[str] = None
    supplierNumberOld: Optional[str] = None
    supplierOrderBlock: Optional[bool] = None
    supplierPaymentMethodId: Optional[str] = None
    supplierPaymentMethodName: Optional[str] = None
    supplierShipmentMethodId: Optional[str] = None
    supplierShipmentMethodName: Optional[str] = None
    supplierTermOfPaymentId: Optional[str] = None
    supplierTermOfPaymentName: Optional[str] = None
    taxId: Optional[str] = None
    topics: List[Topics] = []
    vatIdentificationNumber: Optional[str] = None
    xRechnungLeitwegId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None
