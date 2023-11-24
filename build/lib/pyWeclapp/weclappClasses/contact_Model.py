from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class Addresses(Blueprint):
	id: str
	version: str
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	createdDate: int
	deliveryAddress: bool
	firstName: str = None
	globalLocationNumber: str = None
	invoiceAddress: bool
	lastModifiedDate: int
	lastName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	primeAddress: bool
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None




class OnlineAccounts(Blueprint):
	id: str
	version: str
	accountName: str = None
	accountType: str = None
	createdDate: int
	lastModifiedDate: int
	url: str = None





class Contact(Blueprint):
	id: str
	version: str
	addresses: List[Addresses] = []
	birthDate: int = None
	company: str = None
	company2: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	customerCategoryId: str = None
	customerCategoryName: str = None
	deliveryAddressId: str = None
	description: str = None
	email: str = None
	fax: str = None
	firstName: str = None
	fixPhone2: str = None
	invoiceAddressId: str = None
	lastModifiedDate: int
	lastName: str = None
	middleName: str = None
	mobilePhone1: str = None
	mobilePhone2: str = None
	onlineAccounts: List[OnlineAccounts] = []
	optIn: bool
	optInLetter: bool
	optInPhone: bool
	optInSms: bool
	partyType: str
	personCompany: str = None
	personDepartmentId: str = None
	personRoleId: str = None
	phone: str = None
	phoneHome: str = None
	primaryAddressId: str = None
	salutation: str = None
	tags: list = [] # could not be parsed
	title: str = None
	titleId: str = None
	website: str = None



	# AutomationData
	ITEMS_NAME: str = 'addresses'



