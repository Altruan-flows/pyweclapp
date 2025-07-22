"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class Addresses(Blueprint):
    """Subclass for addresses in Customer and Contact."""

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
    """Subclass for onlineAccounts in Contact."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    accountName: Union[str, None] = None
    accountType: Union[str, None] = None
    url: Union[str, None] = None


class Contacts(Blueprint):
    """Subclass for contact in Customer."""

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
    """Subclass for bankAccounts in Customer."""

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
    """Subclass for commissionSalesPartners in Customer."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    commissionFix: Union[str, None] = None
    commissionPercentage: Union[str, None] = None
    commissionType: Union[str, None] = None
    salesPartnerSupplierId: Union[str, None] = None
    salesPartnerSupplierNumber: Union[str, None] = None


class CustomerTopics(Blueprint):
    """Subclass for customerTopics in Customer."""

    id: Union[str, None] = None
    name: Union[str, None] = None


class Customer(Blueprint):
    """Class for customer endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    addresses: List[Addresses] = []
    amountInsured: Union[str, None] = None
    annualRevenue: Union[str, None] = None
    bankAccounts: List[BankAccounts] = []
    birthDate: Union[int, None] = None
    blockNotice: Union[str, None] = None
    blocked: Union[bool, None] = None
    commercialLanguageId: Union[str, None] = None
    commissionSalesPartners: List[CommissionSalesPartners] = []
    company: Union[str, None] = None
    company2: Union[str, None] = None
    companySizeId: Union[str, None] = None
    companySizeName: Union[str, None] = None
    contacts: List[Contacts] = []
    createdDate: Union[int, None]
    creditLimit: Union[str, None] = None
    currencyId: Union[str, None] = None
    currencyName: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerCategoryId: Union[str, None] = None
    customerCategoryName: Union[str, None] = None
    customerNumber: Union[str, None] = None
    customerRatingId: Union[str, None] = None
    customerRatingName: Union[str, None] = None
    customerSupplierNumber: Union[str, None] = None
    customerTopics: List[CustomerTopics] = []
    defaultHeaderDiscount: Union[str, None] = None
    defaultHeaderSurcharge: Union[str, None] = None
    deliveryAddressId: Union[str, None] = None
    deliveryBlock: Union[bool, None] = None
    description: Union[str, None] = None
    email: Union[str, None] = None
    fax: Union[str, None] = None
    firstName: Union[str, None] = None
    insolvent: Union[bool, None] = None
    insured: Union[bool, None] = None
    invoiceAddressId: Union[str, None] = None
    invoiceBlock: Union[bool, None] = None
    invoiceRecipientId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    leadSourceId: Union[str, None] = None
    leadSourceName: Union[str, None] = None
    lossDescription: Union[str, None] = None
    lossReasonId: Union[str, None] = None
    lossReasonName: Union[str, None] = None
    middleName: Union[str, None] = None
    mobilePhone1: Union[str, None] = None
    nonStandardTaxId: Union[str, None] = None
    oldCustomerNumber: Union[str, None] = None
    onlineAccounts: list = []
    optIn: Union[bool, None] = None
    optInLetter: Union[bool, None] = None
    optInPhone: Union[bool, None] = None
    optInSms: Union[bool, None] = None
    parentPartyId: Union[str, None] = None
    partyType: Union[str, None] = None
    paymentMethodId: Union[str, None] = None
    paymentMethodName: Union[str, None] = None
    personCompany: Union[str, None] = None
    personDepartmentId: Union[str, None] = None
    personRoleId: Union[str, None] = None
    phone: Union[str, None] = None
    primaryAddressId: Union[str, None] = None
    primaryContactId: Union[str, None] = None
    referenceNumber: Union[str, None] = None
    responsibleUserFixed: Union[bool, None] = None
    responsibleUserId: Union[str, None] = None
    responsibleUserUsername: Union[str, None] = None
    salesChannel: Union[str, None] = None
    salesStageId: Union[str, None] = None
    salesStageName: Union[str, None] = None
    salutation: Union[str, None] = None
    satisfaction: Union[str, None] = None
    sectorId: Union[str, None] = None
    sectorName: Union[str, None] = None
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    tags: list = []
    termOfPaymentId: Union[str, None] = None
    termOfPaymentName: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    useCustomsTariffNumber: Union[bool, None] = None
    vatRegistrationNumber: Union[str, None] = None
    website: Union[str, None] = None
