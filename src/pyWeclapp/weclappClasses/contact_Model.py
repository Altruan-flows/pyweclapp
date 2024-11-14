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


class Contact(Blueprint):
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
