# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class Addresses(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	deliveryAddress: Union[bool, None]
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	invoiceAddress: Union[bool, None]
	lastName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	primeAddress: Union[bool, None]
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class OnlineAccounts(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	accountName: Union[str, None] = None
	accountType: Union[Literal["AMAZON", "BLOG", "EBAY", "FACEBOOK", "GOOGLE_DRIVE", "INSTAGRAM", "LINKEDIN", "OTHER", "PINTEREST", "SKYPE", "SLIDESHARE", "TWITTER", "WIKIPEDIA", "XING", "YELP", "YOUTUBE"], None] = None
	url: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class Contact(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
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
	partyType: Union[Literal["ORGANIZATION", "PERSON"], None] = None
	personCompany: Union[str, None] = None
	personDepartmentId: Union[str, None] = None
	personRoleId: Union[str, None] = None
	phone: Union[str, None] = None
	primaryAddressId: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	tags: list = []
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	website: Union[str, None] = None
	customerCategoryId: Union[str, None] = None
	customerCategoryName: Union[str, None] = None
	description: Union[str, None] = None
	fixPhone2: Union[str, None] = None
	mobilePhone2: Union[str, None] = None
	optIn: Union[bool, None]
	optInLetter: Union[bool, None]
	optInPhone: Union[bool, None]
	optInSms: Union[bool, None]
	phoneHome: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


