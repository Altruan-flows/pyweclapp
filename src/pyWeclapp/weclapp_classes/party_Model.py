"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class Addresses(Blueprint):
    """Subclass for addresses in Party and Contacts."""

    id: Union[str, None]
    version: Union[str, None]
    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    createdDate: Union[int, None]
    deliveryAddress: Union[bool, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    invoiceAddress: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    primeAddress: Union[bool, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class OnlineAccounts(Blueprint):
    """Subclass for onlineAccounts in Party and Contacts."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    accountName: Union[str, None] = None
    accountType: Union[str, None] = None
    url: Union[str, None] = None


class Contacts(Blueprint):
    """Subclass for contacts in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    addresses: List[Addresses] = []
    birthDate: Union[int, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    deliveryAddressId: Union[str, None] = None
    email: Union[str, None] = None
    fax: Union[str, None] = None
    firstName: Union[str, None] = None
    invoiceAddressId: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    mobilePhone1: Union[str, None] = None
    onlineAccounts: List[OnlineAccounts] = []
    partyType: Union[str, None] = None
    personCompany: Union[str, None] = None
    personDepartmentId: Union[str, None] = None
    personRoleId: Union[str, None] = None
    phone: Union[str, None] = None
    primaryAddressId: Union[str, None] = None
    salutation: Union[str, None] = None
    tags: List[str] = []
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    website: Union[str, None] = None
    customerCategoryId: Union[str, None] = None
    customerCategoryName: Union[str, None] = None
    description: Union[str, None] = None
    fixPhone2: Union[str, None] = None
    mobilePhone2: Union[str, None] = None
    optIn: Union[bool, None] = None
    optInLetter: Union[bool, None] = None
    optInPhone: Union[bool, None] = None
    optInSms: Union[bool, None] = None
    phoneHome: Union[str, None] = None


class BankAccounts(Blueprint):
    """Subclass for bankAccounts in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    accountHolder: Union[str, None] = None
    accountNumber: Union[str, None] = None
    bankCode: Union[str, None] = None
    creditInstitute: Union[str, None] = None
    partyId: Union[str, None] = None
    primary: Union[bool, None] = None


class CommissionSalesPartners(Blueprint):
    """Subclass for commissionSalesPartners in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None
    salesPartnerSupplierNumber: Union[str, None] = None


class CustomerSalesStageHistory(Blueprint):
    """Subclass for customerSalesStageHistory in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    salesStageId: Union[str, None] = None
    salesStageName: Union[str, None] = None
    userId: Union[str, None] = None


class PartyEmailAddresses(Blueprint):
    """Subclass for partyEmailAddresses in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class Invoices(Blueprint):
    """Subclass for invoices in PartyHabitualExporterLettersOfIntent."""

    id: Union[str, None] = None


class PartyHabitualExporterLettersOfIntent(Blueprint):
    """Subclass for partyHabitualExporterLettersOfIntent in Party."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    automaticallySuggestInInvoice: Union[bool, None] = None
    date: Union[int, None] = None
    fromSupplier: Union[bool, None] = None
    invoices: List[Invoices] = []
    numberDeclarer: Union[str, None] = None
    numberSupplier: Union[str, None] = None
    totalAmount: Union[str, None] = None
    type: Union[str, None] = None


class Topics(Blueprint):
    """Subclass for topics in Party."""

    id: Union[str, None] = None
    name: Union[str, None] = None


class Party(Blueprint):
    """Class for party endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    addresses: List[Addresses] = []
    allowPurchaseOrderCreation: Union[bool, None] = None
    bankAccounts: List[BankAccounts] = []
    birthDate: Union[int, None] = None
    commercialLanguageId: Union[str, None] = None
    commissionBlock: Union[bool, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    company: Union[str, None] = None
    company2: Union[str, None] = None
    companySizeId: Union[str, None] = None
    companySizeName: Union[str, None] = None
    competitor: Union[bool, None] = None
    contacts: List[Contacts] = []
    convertedOnDate: Union[int, None] = None
    createdDate: Union[int, None]
    currencyId: Union[str, None] = None
    currencyName: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customer: Union[bool, None] = None
    customerAllowDropshippingOrderCreation: Union[bool, None] = None
    customerAmountInsured: Union[str, None] = None
    customerAnnualRevenue: Union[str, None] = None
    customerBlockNotice: Union[str, None] = None
    customerBlocked: Union[bool, None] = None
    customerBusinessType: Union[str, None] = None
    customerCategoryId: Union[str, None] = None
    customerCategoryName: Union[str, None] = None
    customerCreditLimit: Union[str, None] = None
    customerCurrentSalesStageId: Union[str, None] = None
    customerCurrentSalesStageName: Union[str, None] = None
    customerDebtorAccountId: Union[str, None] = None
    customerDebtorAccountNumber: Union[str, None] = None
    customerDebtorAccountingCodeId: Union[str, None] = None
    customerDefaultHeaderDiscount: Union[str, None] = None
    customerDefaultHeaderSurcharge: Union[str, None] = None
    customerDefaultShippingCarrierId: Union[str, None] = None
    customerDeliveryBlock: Union[bool, None] = None
    customerInsolvent: Union[bool, None] = None
    customerInsured: Union[bool, None] = None
    customerInternalNote: Union[str, None] = None
    customerLossDescription: Union[str, None] = None
    customerLossReasonId: Union[str, None] = None
    customerLossReasonName: Union[str, None] = None
    customerNonStandardTaxId: Union[str, None] = None
    customerNumber: Union[str, None] = None
    customerNumberOld: Union[str, None] = None
    customerPaymentMethodId: Union[str, None] = None
    customerPaymentMethodName: Union[str, None] = None
    customerSalesChannel: Union[str, None] = None
    customerSalesOrderPaymentType: Union[str, None] = None
    customerSalesProbability: Union[int, None] = None
    customerSalesStageHistory: List[CustomerSalesStageHistory] = []
    customerSatisfaction: Union[str, None] = None
    customerShipmentMethodId: Union[str, None] = None
    customerShipmentMethodName: Union[str, None] = None
    customerSupplierNumber: Union[str, None] = None
    customerTermOfPaymentId: Union[str, None] = None
    customerTermOfPaymentName: Union[str, None] = None
    customerUseCustomsTariffNumber: Union[bool, None] = None
    deliveryAddressId: Union[str, None] = None
    deliveryEmailAddressesId: Union[str, None] = None
    description: Union[str, None] = None
    dunningAddressId: Union[str, None] = None
    dunningEmailAddressesId: Union[str, None] = None
    email: Union[str, None] = None
    enableDropshippingInNewSupplySources: Union[bool, None] = None
    eoriNumber: Union[str, None] = None
    factoring: Union[bool, None] = None
    fax: Union[str, None] = None
    firstName: Union[str, None] = None
    fixPhone2: Union[str, None] = None
    fixedResponsibleUser: Union[bool, None] = None
    formerSalesPartner: Union[bool, None] = None
    habitualExporter: Union[bool, None] = None
    imageId: Union[str, None] = None
    invoiceAddressId: Union[str, None] = None
    invoiceBlock: Union[bool, None] = None
    invoiceRecipientId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    leadRatingId: Union[str, None] = None
    leadRatingName: Union[str, None] = None
    leadSourceId: Union[str, None] = None
    leadSourceName: Union[str, None] = None
    leadStatus: Union[str, None] = None
    legalFormId: Union[str, None] = None
    legalFormName: Union[str, None] = None
    middleName: Union[str, None] = None
    mobilePhone1: Union[str, None] = None
    mobilePhone2: Union[str, None] = None
    onlineAccounts: List[OnlineAccounts] = []
    optInEmail: Union[bool, None] = None
    optInLetter: Union[bool, None] = None
    optInPhone: Union[bool, None] = None
    optInSms: Union[bool, None] = None
    parentPartyId: Union[str, None] = None
    partyEmailAddresses: List[PartyEmailAddresses] = []
    partyHabitualExporterLettersOfIntent: List[PartyHabitualExporterLettersOfIntent] = (
        []
    )
    partyType: Union[str, None] = None
    personCompany: Union[str, None] = None
    personDepartmentId: Union[str, None] = None
    personRoleId: Union[str, None] = None
    phone: Union[str, None] = None
    phoneHome: Union[str, None] = None
    primaryAddressId: Union[str, None] = None
    primaryContactId: Union[str, None] = None
    publicPageExpirationDate: Union[int, None] = None
    publicPageUuid: Union[str, None] = None
    purchaseEmailAddressesId: Union[str, None] = None
    purchaseViaPlafond: Union[bool, None] = None
    quotationEmailAddressesId: Union[str, None] = None
    ratingId: Union[str, None] = None
    ratingName: Union[str, None] = None
    referenceNumber: Union[str, None] = None
    regionId: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesInvoiceEmailAddressesId: Union[str, None] = None
    salesOrderEmailAddressesId: Union[str, None] = None
    salesPartner: Union[bool, None] = None
    salesPartnerDefaultCommissionFix: Union[str, None] = None
    salesPartnerDefaultCommissionPercentage: Union[str, None] = None
    salesPartnerDefaultCommissionType: Union[str, None] = None
    salutation: Union[str, None] = None
    sectorId: Union[str, None] = None
    sectorName: Union[str, None] = None
    supplier: Union[bool, None] = None
    supplierCreditorAccountId: Union[str, None] = None
    supplierCreditorAccountNumber: Union[str, None] = None
    supplierCreditorAccountingCodeId: Union[str, None] = None
    supplierCustomerNumberAtSupplier: Union[str, None] = None
    supplierDefaultShippingCarrierId: Union[str, None] = None
    supplierInternalNote: Union[str, None] = None
    supplierMergeItemsForOcrInvoiceUpload: Union[bool, None] = None
    supplierMinimumPurchaseOrderAmount: Union[str, None] = None
    supplierNonStandardTaxId: Union[str, None] = None
    supplierNumber: Union[str, None] = None
    supplierNumberOld: Union[str, None] = None
    supplierOrderBlock: Union[bool, None] = None
    supplierPaymentMethodId: Union[str, None] = None
    supplierPaymentMethodName: Union[str, None] = None
    supplierShipmentMethodId: Union[str, None] = None
    supplierShipmentMethodName: Union[str, None] = None
    supplierTermOfPaymentId: Union[str, None] = None
    supplierTermOfPaymentName: Union[str, None] = None
    tags: list = []
    taxId: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    topics: List[Topics] = []
    vatIdentificationNumber: Union[str, None] = None
    website: Union[str, None] = None
    xRechnungLeitwegId: Union[str, None] = None
