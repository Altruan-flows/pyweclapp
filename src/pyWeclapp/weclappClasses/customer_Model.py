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


class Contacts(Blueprint):
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
    customerCategoryId: Optional[str] = None
    customerCategoryName: Optional[str] = None
    description: Optional[str] = None
    fixPhone2: Optional[str] = None
    mobilePhone2: Optional[str] = None
    optIn: Optional[bool] = None
    optInLetter: Optional[bool] = None
    optInPhone: Optional[bool] = None
    optInSms: Optional[bool] = None
    phoneHome: Optional[str] = None
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


class CustomerTopics(Blueprint):
    id: Optional[str] = None
    name: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Customer(Blueprint):
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
    commercialLanguageId: Optional[str] = None
    contacts: List[Contacts] = []
    currencyId: Optional[str] = None
    currencyName: Optional[str] = None
    primaryContactId: Optional[str] = None
    sectorId: Optional[str] = None
    sectorName: Optional[str] = None
    annualRevenue: Optional[str] = None
    companySizeId: Optional[str] = None
    companySizeName: Optional[str] = None
    customerCategoryId: Optional[str] = None
    customerCategoryName: Optional[str] = None
    parentPartyId: Optional[str] = None
    paymentMethodId: Optional[str] = None
    paymentMethodName: Optional[str] = None
    responsibleUserId: Optional[str] = None
    responsibleUserUsername: Optional[str] = None
    shipmentMethodId: Optional[str] = None
    shipmentMethodName: Optional[str] = None
    termOfPaymentId: Optional[str] = None
    termOfPaymentName: Optional[str] = None
    vatRegistrationNumber: Optional[str] = None
    amountInsured: Optional[str] = None
    bankAccounts: List[BankAccounts] = []
    blockNotice: Optional[str] = None
    blocked: Optional[bool] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    creditLimit: Optional[str] = None
    customerNumber: Optional[str] = None
    customerRatingId: Optional[str] = None
    customerRatingName: Optional[str] = None
    customerSupplierNumber: Optional[str] = None
    customerTopics: List[CustomerTopics] = []
    defaultHeaderDiscount: Optional[str] = None
    defaultHeaderSurcharge: Optional[str] = None
    deliveryBlock: Optional[bool] = None
    description: Optional[str] = None
    insolvent: Optional[bool] = None
    insured: Optional[bool] = None
    invoiceBlock: Optional[bool] = None
    invoiceRecipientId: Optional[str] = None
    leadSourceId: Optional[str] = None
    leadSourceName: Optional[str] = None
    lossDescription: Optional[str] = None
    lossReasonId: Optional[str] = None
    lossReasonName: Optional[str] = None
    nonStandardTaxId: Optional[str] = None
    oldCustomerNumber: Optional[str] = None
    optIn: Optional[bool] = None
    optInLetter: Optional[bool] = None
    optInPhone: Optional[bool] = None
    optInSms: Optional[bool] = None
    referenceNumber: Optional[str] = None
    responsibleUserFixed: Optional[bool] = None
    salesChannel: Optional[str] = None
    salesStageId: Optional[str] = None
    salesStageName: Optional[str] = None
    satisfaction: Optional[str] = None
    useCustomsTariffNumber: Optional[bool] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None
