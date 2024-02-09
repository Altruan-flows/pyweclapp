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
	deliveryAddress: Union[bool, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	invoiceAddress: Union[bool, None] = None
	lastName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	primeAddress: Union[bool, None] = None
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


class Addresses(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	deliveryAddress: Union[bool, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	invoiceAddress: Union[bool, None] = None
	lastName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	primeAddress: Union[bool, None] = None
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


class Contacts(Blueprint):
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
	optIn: Union[bool, None] = None
	optInLetter: Union[bool, None] = None
	optInPhone: Union[bool, None] = None
	optInSms: Union[bool, None] = None
	phoneHome: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class BankAccounts(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	accountHolder: Union[str, None] = None
	accountNumber: Union[str, None] = None
	bankCode: Union[str, None] = None
	creditInstitute: Union[str, None] = None
	partyId: Union[str, None] = None
	primary: Union[bool, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class CommissionSalesPartners(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	commissionFix: Union[str, None] = None
	commissionPercentage: Union[str, None] = None
	commissionType: Union[Literal["FIX", "FIX_AND_MARGIN", "FIX_AND_REVENUE", "MARGIN", "NO_COMMISSION", "REVENUE"], None] = None
	salesPartnerSupplierId: Union[str, None] = None
	salesPartnerSupplierNumber: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class CustomerTopics(Blueprint):
	id: Union[str, None]
	name: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class Customer(Blueprint):
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
	commercialLanguageId: Union[str, None] = None
	contacts: List[Contacts] = []
	currencyId: Union[str, None] = None
	currencyName: Union[str, None] = None
	primaryContactId: Union[str, None] = None
	sectorId: Union[str, None] = None
	sectorName: Union[str, None] = None
	annualRevenue: Union[str, None] = None
	companySizeId: Union[str, None] = None
	companySizeName: Union[str, None] = None
	customerCategoryId: Union[str, None] = None
	customerCategoryName: Union[str, None] = None
	parentPartyId: Union[str, None] = None
	paymentMethodId: Union[str, None] = None
	paymentMethodName: Union[str, None] = None
	responsibleUserId: Union[str, None] = None
	responsibleUserUsername: Union[str, None] = None
	shipmentMethodId: Union[str, None] = None
	shipmentMethodName: Union[str, None] = None
	termOfPaymentId: Union[str, None] = None
	termOfPaymentName: Union[str, None] = None
	vatRegistrationNumber: Union[str, None] = None
	amountInsured: Union[str, None] = None
	bankAccounts: List[BankAccounts] = []
	blockNotice: Union[str, None] = None
	blocked: Union[bool, None] = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	creditLimit: Union[str, None] = None
	customerNumber: Union[str, None] = None
	customerRatingId: Union[str, None] = None
	customerRatingName: Union[str, None] = None
	customerSupplierNumber: Union[str, None] = None
	customerTopics: List[CustomerTopics] = []
	defaultHeaderDiscount: Union[str, None] = None
	defaultHeaderSurcharge: Union[str, None] = None
	deliveryBlock: Union[bool, None] = None
	description: Union[str, None] = None
	insolvent: Union[bool, None] = None
	insured: Union[bool, None] = None
	invoiceBlock: Union[bool, None] = None
	invoiceRecipientId: Union[str, None] = None
	leadSourceId: Union[str, None] = None
	leadSourceName: Union[str, None] = None
	lossDescription: Union[str, None] = None
	lossReasonId: Union[str, None] = None
	lossReasonName: Union[str, None] = None
	nonStandardTaxId: Union[str, None] = None
	oldCustomerNumber: Union[str, None] = None
	optIn: Union[bool, None] = None
	optInLetter: Union[bool, None] = None
	optInPhone: Union[bool, None] = None
	optInSms: Union[bool, None] = None
	referenceNumber: Union[str, None] = None
	responsibleUserFixed: Union[bool, None] = None
	salesChannel: Union[Literal["GROSS1", "GROSS10", "GROSS100", "GROSS101", "GROSS102", "GROSS103", "GROSS104", "GROSS105", "GROSS106", "GROSS107", "GROSS108", "GROSS109", "GROSS11", "GROSS110", "GROSS111", "GROSS112", "GROSS113", "GROSS114", "GROSS115", "GROSS116", "GROSS117", "GROSS118", "GROSS119", "GROSS12", "GROSS120", "GROSS121", "GROSS122", "GROSS123", "GROSS124", "GROSS125", "GROSS126", "GROSS127", "GROSS128", "GROSS129", "GROSS13", "GROSS130", "GROSS131", "GROSS132", "GROSS133", "GROSS134", "GROSS135", "GROSS136", "GROSS137", "GROSS138", "GROSS139", "GROSS14", "GROSS140", "GROSS141", "GROSS142", "GROSS143", "GROSS144", "GROSS145", "GROSS146", "GROSS147", "GROSS148", "GROSS149", "GROSS15", "GROSS150", "GROSS151", "GROSS152", "GROSS153", "GROSS154", "GROSS155", "GROSS156", "GROSS157", "GROSS158", "GROSS159", "GROSS16", "GROSS160", "GROSS161", "GROSS162", "GROSS163", "GROSS164", "GROSS165", "GROSS166", "GROSS167", "GROSS168", "GROSS169", "GROSS17", "GROSS170", "GROSS171", "GROSS172", "GROSS173", "GROSS174", "GROSS175", "GROSS176", "GROSS177", "GROSS178", "GROSS179", "GROSS18", "GROSS180", "GROSS181", "GROSS182", "GROSS183", "GROSS184", "GROSS185", "GROSS186", "GROSS187", "GROSS188", "GROSS189", "GROSS19", "GROSS190", "GROSS191", "GROSS192", "GROSS193", "GROSS194", "GROSS195", "GROSS196", "GROSS197", "GROSS198", "GROSS199", "GROSS2", "GROSS20", "GROSS200", "GROSS201", "GROSS202", "GROSS203", "GROSS204", "GROSS205", "GROSS206", "GROSS207", "GROSS208", "GROSS209", "GROSS21", "GROSS210", "GROSS211", "GROSS212", "GROSS213", "GROSS214", "GROSS215", "GROSS216", "GROSS217", "GROSS218", "GROSS219", "GROSS22", "GROSS220", "GROSS221", "GROSS222", "GROSS223", "GROSS224", "GROSS225", "GROSS226", "GROSS227", "GROSS228", "GROSS229", "GROSS23", "GROSS230", "GROSS231", "GROSS232", "GROSS233", "GROSS234", "GROSS235", "GROSS236", "GROSS237", "GROSS238", "GROSS239", "GROSS24", "GROSS240", "GROSS241", "GROSS242", "GROSS243", "GROSS244", "GROSS245", "GROSS246", "GROSS247", "GROSS248", "GROSS249", "GROSS25", "GROSS250", "GROSS251", "GROSS252", "GROSS253", "GROSS254", "GROSS255", "GROSS256", "GROSS257", "GROSS258", "GROSS259", "GROSS26", "GROSS260", "GROSS261", "GROSS262", "GROSS263", "GROSS264", "GROSS265", "GROSS266", "GROSS267", "GROSS268", "GROSS269", "GROSS27", "GROSS270", "GROSS271", "GROSS272", "GROSS273", "GROSS274", "GROSS275", "GROSS276", "GROSS277", "GROSS278", "GROSS279", "GROSS28", "GROSS280", "GROSS281", "GROSS282", "GROSS283", "GROSS284", "GROSS285", "GROSS286", "GROSS287", "GROSS288", "GROSS289", "GROSS29", "GROSS290", "GROSS291", "GROSS292", "GROSS293", "GROSS294", "GROSS295", "GROSS296", "GROSS297", "GROSS298", "GROSS299", "GROSS3", "GROSS30", "GROSS300", "GROSS31", "GROSS32", "GROSS33", "GROSS34", "GROSS35", "GROSS36", "GROSS37", "GROSS38", "GROSS39", "GROSS4", "GROSS40", "GROSS41", "GROSS42", "GROSS43", "GROSS44", "GROSS45", "GROSS46", "GROSS47", "GROSS48", "GROSS49", "GROSS5", "GROSS50", "GROSS51", "GROSS52", "GROSS53", "GROSS54", "GROSS55", "GROSS56", "GROSS57", "GROSS58", "GROSS59", "GROSS6", "GROSS60", "GROSS61", "GROSS62", "GROSS63", "GROSS64", "GROSS65", "GROSS66", "GROSS67", "GROSS68", "GROSS69", "GROSS7", "GROSS70", "GROSS71", "GROSS72", "GROSS73", "GROSS74", "GROSS75", "GROSS76", "GROSS77", "GROSS78", "GROSS79", "GROSS8", "GROSS80", "GROSS81", "GROSS82", "GROSS83", "GROSS84", "GROSS85", "GROSS86", "GROSS87", "GROSS88", "GROSS89", "GROSS9", "GROSS90", "GROSS91", "GROSS92", "GROSS93", "GROSS94", "GROSS95", "GROSS96", "GROSS97", "GROSS98", "GROSS99", "NET1", "NET10", "NET100", "NET101", "NET102", "NET103", "NET104", "NET105", "NET106", "NET107", "NET108", "NET109", "NET11", "NET110", "NET111", "NET112", "NET113", "NET114", "NET115", "NET116", "NET117", "NET118", "NET119", "NET12", "NET120", "NET121", "NET122", "NET123", "NET124", "NET125", "NET126", "NET127", "NET128", "NET129", "NET13", "NET130", "NET131", "NET132", "NET133", "NET134", "NET135", "NET136", "NET137", "NET138", "NET139", "NET14", "NET140", "NET141", "NET142", "NET143", "NET144", "NET145", "NET146", "NET147", "NET148", "NET149", "NET15", "NET150", "NET151", "NET152", "NET153", "NET154", "NET155", "NET156", "NET157", "NET158", "NET159", "NET16", "NET160", "NET161", "NET162", "NET163", "NET164", "NET165", "NET166", "NET167", "NET168", "NET169", "NET17", "NET170", "NET171", "NET172", "NET173", "NET174", "NET175", "NET176", "NET177", "NET178", "NET179", "NET18", "NET180", "NET181", "NET182", "NET183", "NET184", "NET185", "NET186", "NET187", "NET188", "NET189", "NET19", "NET190", "NET191", "NET192", "NET193", "NET194", "NET195", "NET196", "NET197", "NET198", "NET199", "NET2", "NET20", "NET200", "NET201", "NET202", "NET203", "NET204", "NET205", "NET206", "NET207", "NET208", "NET209", "NET21", "NET210", "NET211", "NET212", "NET213", "NET214", "NET215", "NET216", "NET217", "NET218", "NET219", "NET22", "NET220", "NET221", "NET222", "NET223", "NET224", "NET225", "NET226", "NET227", "NET228", "NET229", "NET23", "NET230", "NET231", "NET232", "NET233", "NET234", "NET235", "NET236", "NET237", "NET238", "NET239", "NET24", "NET240", "NET241", "NET242", "NET243", "NET244", "NET245", "NET246", "NET247", "NET248", "NET249", "NET25", "NET250", "NET251", "NET252", "NET253", "NET254", "NET255", "NET256", "NET257", "NET258", "NET259", "NET26", "NET260", "NET261", "NET262", "NET263", "NET264", "NET265", "NET266", "NET267", "NET268", "NET269", "NET27", "NET270", "NET271", "NET272", "NET273", "NET274", "NET275", "NET276", "NET277", "NET278", "NET279", "NET28", "NET280", "NET281", "NET282", "NET283", "NET284", "NET285", "NET286", "NET287", "NET288", "NET289", "NET29", "NET290", "NET291", "NET292", "NET293", "NET294", "NET295", "NET296", "NET297", "NET298", "NET299", "NET3", "NET30", "NET300", "NET31", "NET32", "NET33", "NET34", "NET35", "NET36", "NET37", "NET38", "NET39", "NET4", "NET40", "NET41", "NET42", "NET43", "NET44", "NET45", "NET46", "NET47", "NET48", "NET49", "NET5", "NET50", "NET51", "NET52", "NET53", "NET54", "NET55", "NET56", "NET57", "NET58", "NET59", "NET6", "NET60", "NET61", "NET62", "NET63", "NET64", "NET65", "NET66", "NET67", "NET68", "NET69", "NET7", "NET70", "NET71", "NET72", "NET73", "NET74", "NET75", "NET76", "NET77", "NET78", "NET79", "NET8", "NET80", "NET81", "NET82", "NET83", "NET84", "NET85", "NET86", "NET87", "NET88", "NET89", "NET9", "NET90", "NET91", "NET92", "NET93", "NET94", "NET95", "NET96", "NET97", "NET98", "NET99"], None] = None
	salesStageId: Union[str, None] = None
	salesStageName: Union[str, None] = None
	satisfaction: Union[Literal["NEUTRAL", "SATISFIED", "UNSATISFIED"], None] = None
	useCustomsTariffNumber: Union[bool, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


