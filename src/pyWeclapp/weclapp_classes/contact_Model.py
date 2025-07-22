"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class Addresses(Blueprint):
    """Subclass for addresses in Contact."""

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


class Contact(Blueprint):
    """Subclass for contact endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    addresses: List[Addresses] = []
    birthDate: Union[int, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    customerCategoryId: Union[str, None] = None
    customerCategoryName: Union[str, None] = None
    deliveryAddressId: Union[str, None] = None
    description: Union[str, None] = None
    email: Union[str, None] = None
    fax: Union[str, None] = None
    firstName: Union[str, None] = None
    fixPhone2: Union[str, None] = None
    invoiceAddressId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    mobilePhone1: Union[str, None] = None
    mobilePhone2: Union[str, None] = None
    onlineAccounts: list = []
    optIn: Union[bool, None] = None
    optInLetter: Union[bool, None] = None
    optInPhone: Union[bool, None] = None
    optInSms: Union[bool, None] = None
    partyType: Union[str, None] = None
    personCompany: Union[str, None] = None
    personDepartmentId: Union[str, None] = None
    personRoleId: Union[str, None] = None
    phone: Union[str, None] = None
    phoneHome: Union[str, None] = None
    primaryAddressId: Union[str, None] = None
    salutation: Union[str, None] = None
    tags: list = []
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    website: Union[str, None] = None
