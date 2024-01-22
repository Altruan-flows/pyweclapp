# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



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


class ShippingCostItems(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	articleId: Union[str, None] = None
	articleNumber: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	manualUnitPrice: Union[bool, None]
	netAmount: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	taxId: Union[str, None] = None
	taxName: Union[str, None] = None
	unitPrice: Union[str, None] = None
	unitPriceInCompanyCurrency: Union[str, None] = None
	manualUnitCost: Union[bool, None]
	unitCost: Union[str, None] = None
	unitCostInCompanyCurrency: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class DeliveryAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class DeliveryEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class InvoiceAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class RecordAddress(Blueprint):
	city: Union[str, None] = None
	company: Union[str, None] = None
	company2: Union[str, None] = None
	countryCode: Union[str, None] = None
	firstName: Union[str, None] = None
	globalLocationNumber: Union[str, None] = None
	lastName: Union[str, None] = None
	middleName: Union[str, None] = None
	phoneNumber: Union[str, None] = None
	postOfficeBoxCity: Union[str, None] = None
	postOfficeBoxNumber: Union[str, None] = None
	postOfficeBoxZipCode: Union[str, None] = None
	salutation: Union[Literal["COMPANY", "FAMILY", "MR", "MRS", "NO_SALUTATION"], None] = None
	state: Union[str, None] = None
	street1: Union[str, None] = None
	street2: Union[str, None] = None
	title: Union[str, None] = None
	titleId: Union[str, None] = None
	zipcode: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class SalesInvoiceEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class ReductionAdditionItems(Blueprint):
	position: Union[int, None] = None
	source: Union[Literal["ARTICLE", "ARTICLE_AND_CUSTOMER", "ARTICLE_CATEGORY", "ARTICLE_CATEGORY_AND_CUSTOMER", "MANUAL"], None] = None
	type: Union[Literal["ADDITION_ABSOLUTE", "ADDITION_PERCENT", "REDUCTION_ABSOLUTE", "REDUCTION_PERCENT"], None] = None
	value: Union[str, None] = None
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


class QuotationItems(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	articleId: Union[str, None] = None
	articleNumber: Union[str, None] = None
	note: Union[str, None] = None
	positionNumber: Union[int, None]
	quantity: Union[str, None] = None
	description: Union[str, None] = None
	descriptionFixed: Union[bool, None]
	manualQuantity: Union[bool, None]
	parentItemId: Union[str, None] = None
	title: Union[str, None] = None
	unitId: Union[str, None] = None
	unitName: Union[str, None] = None
	discountPercentage: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	manualUnitPrice: Union[bool, None]
	netAmount: Union[str, None] = None
	netAmountForStatistics: Union[str, None] = None
	netAmountForStatisticsInCompanyCurrency: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	taxId: Union[str, None] = None
	taxName: Union[str, None] = None
	unitPrice: Union[str, None] = None
	unitPriceInCompanyCurrency: Union[str, None] = None
	addPageBreakBefore: Union[bool, None]
	customAttributes: List[WeclappMetaData] = []
	freeTextItem: Union[bool, None]
	groupName: Union[str, None] = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	manualUnitCost: Union[bool, None]
	servicePeriodFrom: Union[int, None] = None
	servicePeriodTo: Union[int, None] = None
	unitCost: Union[str, None] = None
	unitCostInCompanyCurrency: Union[str, None] = None
	invoicingType: Union[Literal["EFFORT", "FIXED_PRICE"], None] = None
	manualPlannedWorkingTimePerUnit: Union[bool, None]
	plannedWorkingTimePerUnit: Union[str, None] = None
	serviceItem: Union[bool, None]
	alternative: Union[bool, None]
	optional: Union[bool, None]
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class RecordEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class SalesOrderEmailAddresses(Blueprint):
	bccAddresses: Union[str, None] = None
	ccAddresses: Union[str, None] = None
	toAddresses: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class SalesStageHistory(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	salesStageId: Union[str, None] = None
	salesStageName: Union[str, None] = None
	userId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
	status: Union[Literal["ACCEPTED", "INQUIRED", "OPEN", "REJECTED"], None] = None
	statusDate: Union[int, None] = None
	userId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class Quotation(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	customAttributes: List[WeclappMetaData] = []
	commercialLanguage: Union[str, None] = None
	creatorId: Union[str, None] = None
	description: Union[str, None] = None
	disableEmailTemplate: Union[bool, None]
	recordComment: Union[str, None] = None
	recordFreeText: Union[str, None] = None
	recordOpening: Union[str, None] = None
	sentToRecipient: Union[bool, None]
	tags: list = []
	currencyConversionDate: Union[int, None] = None
	currencyConversionRate: Union[str, None] = None
	grossAmount: Union[str, None] = None
	grossAmountInCompanyCurrency: Union[str, None] = None
	headerDiscount: Union[str, None] = None
	headerSurcharge: Union[str, None] = None
	netAmount: Union[str, None] = None
	netAmountInCompanyCurrency: Union[str, None] = None
	nonStandardTaxId: Union[str, None] = None
	nonStandardTaxName: Union[str, None] = None
	paymentMethodId: Union[str, None] = None
	paymentMethodName: Union[str, None] = None
	recordCurrencyId: Union[str, None] = None
	recordCurrencyName: Union[str, None] = None
	termOfPaymentId: Union[str, None] = None
	termOfPaymentName: Union[str, None] = None
	commission: Union[str, None] = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	customerId: Union[str, None] = None
	customerNumber: Union[str, None] = None
	dispatchCountryCode: Union[str, None] = None
	factoring: Union[bool, None]
	pricingDate: Union[int, None] = None
	responsibleUserId: Union[str, None] = None
	responsibleUserUsername: Union[str, None] = None
	salesChannel: Union[Literal["GROSS1", "GROSS10", "GROSS100", "GROSS101", "GROSS102", "GROSS103", "GROSS104", "GROSS105", "GROSS106", "GROSS107", "GROSS108", "GROSS109", "GROSS11", "GROSS110", "GROSS111", "GROSS112", "GROSS113", "GROSS114", "GROSS115", "GROSS116", "GROSS117", "GROSS118", "GROSS119", "GROSS12", "GROSS120", "GROSS121", "GROSS122", "GROSS123", "GROSS124", "GROSS125", "GROSS126", "GROSS127", "GROSS128", "GROSS129", "GROSS13", "GROSS130", "GROSS131", "GROSS132", "GROSS133", "GROSS134", "GROSS135", "GROSS136", "GROSS137", "GROSS138", "GROSS139", "GROSS14", "GROSS140", "GROSS141", "GROSS142", "GROSS143", "GROSS144", "GROSS145", "GROSS146", "GROSS147", "GROSS148", "GROSS149", "GROSS15", "GROSS150", "GROSS151", "GROSS152", "GROSS153", "GROSS154", "GROSS155", "GROSS156", "GROSS157", "GROSS158", "GROSS159", "GROSS16", "GROSS160", "GROSS161", "GROSS162", "GROSS163", "GROSS164", "GROSS165", "GROSS166", "GROSS167", "GROSS168", "GROSS169", "GROSS17", "GROSS170", "GROSS171", "GROSS172", "GROSS173", "GROSS174", "GROSS175", "GROSS176", "GROSS177", "GROSS178", "GROSS179", "GROSS18", "GROSS180", "GROSS181", "GROSS182", "GROSS183", "GROSS184", "GROSS185", "GROSS186", "GROSS187", "GROSS188", "GROSS189", "GROSS19", "GROSS190", "GROSS191", "GROSS192", "GROSS193", "GROSS194", "GROSS195", "GROSS196", "GROSS197", "GROSS198", "GROSS199", "GROSS2", "GROSS20", "GROSS200", "GROSS201", "GROSS202", "GROSS203", "GROSS204", "GROSS205", "GROSS206", "GROSS207", "GROSS208", "GROSS209", "GROSS21", "GROSS210", "GROSS211", "GROSS212", "GROSS213", "GROSS214", "GROSS215", "GROSS216", "GROSS217", "GROSS218", "GROSS219", "GROSS22", "GROSS220", "GROSS221", "GROSS222", "GROSS223", "GROSS224", "GROSS225", "GROSS226", "GROSS227", "GROSS228", "GROSS229", "GROSS23", "GROSS230", "GROSS231", "GROSS232", "GROSS233", "GROSS234", "GROSS235", "GROSS236", "GROSS237", "GROSS238", "GROSS239", "GROSS24", "GROSS240", "GROSS241", "GROSS242", "GROSS243", "GROSS244", "GROSS245", "GROSS246", "GROSS247", "GROSS248", "GROSS249", "GROSS25", "GROSS250", "GROSS251", "GROSS252", "GROSS253", "GROSS254", "GROSS255", "GROSS256", "GROSS257", "GROSS258", "GROSS259", "GROSS26", "GROSS260", "GROSS261", "GROSS262", "GROSS263", "GROSS264", "GROSS265", "GROSS266", "GROSS267", "GROSS268", "GROSS269", "GROSS27", "GROSS270", "GROSS271", "GROSS272", "GROSS273", "GROSS274", "GROSS275", "GROSS276", "GROSS277", "GROSS278", "GROSS279", "GROSS28", "GROSS280", "GROSS281", "GROSS282", "GROSS283", "GROSS284", "GROSS285", "GROSS286", "GROSS287", "GROSS288", "GROSS289", "GROSS29", "GROSS290", "GROSS291", "GROSS292", "GROSS293", "GROSS294", "GROSS295", "GROSS296", "GROSS297", "GROSS298", "GROSS299", "GROSS3", "GROSS30", "GROSS300", "GROSS31", "GROSS32", "GROSS33", "GROSS34", "GROSS35", "GROSS36", "GROSS37", "GROSS38", "GROSS39", "GROSS4", "GROSS40", "GROSS41", "GROSS42", "GROSS43", "GROSS44", "GROSS45", "GROSS46", "GROSS47", "GROSS48", "GROSS49", "GROSS5", "GROSS50", "GROSS51", "GROSS52", "GROSS53", "GROSS54", "GROSS55", "GROSS56", "GROSS57", "GROSS58", "GROSS59", "GROSS6", "GROSS60", "GROSS61", "GROSS62", "GROSS63", "GROSS64", "GROSS65", "GROSS66", "GROSS67", "GROSS68", "GROSS69", "GROSS7", "GROSS70", "GROSS71", "GROSS72", "GROSS73", "GROSS74", "GROSS75", "GROSS76", "GROSS77", "GROSS78", "GROSS79", "GROSS8", "GROSS80", "GROSS81", "GROSS82", "GROSS83", "GROSS84", "GROSS85", "GROSS86", "GROSS87", "GROSS88", "GROSS89", "GROSS9", "GROSS90", "GROSS91", "GROSS92", "GROSS93", "GROSS94", "GROSS95", "GROSS96", "GROSS97", "GROSS98", "GROSS99", "NET1", "NET10", "NET100", "NET101", "NET102", "NET103", "NET104", "NET105", "NET106", "NET107", "NET108", "NET109", "NET11", "NET110", "NET111", "NET112", "NET113", "NET114", "NET115", "NET116", "NET117", "NET118", "NET119", "NET12", "NET120", "NET121", "NET122", "NET123", "NET124", "NET125", "NET126", "NET127", "NET128", "NET129", "NET13", "NET130", "NET131", "NET132", "NET133", "NET134", "NET135", "NET136", "NET137", "NET138", "NET139", "NET14", "NET140", "NET141", "NET142", "NET143", "NET144", "NET145", "NET146", "NET147", "NET148", "NET149", "NET15", "NET150", "NET151", "NET152", "NET153", "NET154", "NET155", "NET156", "NET157", "NET158", "NET159", "NET16", "NET160", "NET161", "NET162", "NET163", "NET164", "NET165", "NET166", "NET167", "NET168", "NET169", "NET17", "NET170", "NET171", "NET172", "NET173", "NET174", "NET175", "NET176", "NET177", "NET178", "NET179", "NET18", "NET180", "NET181", "NET182", "NET183", "NET184", "NET185", "NET186", "NET187", "NET188", "NET189", "NET19", "NET190", "NET191", "NET192", "NET193", "NET194", "NET195", "NET196", "NET197", "NET198", "NET199", "NET2", "NET20", "NET200", "NET201", "NET202", "NET203", "NET204", "NET205", "NET206", "NET207", "NET208", "NET209", "NET21", "NET210", "NET211", "NET212", "NET213", "NET214", "NET215", "NET216", "NET217", "NET218", "NET219", "NET22", "NET220", "NET221", "NET222", "NET223", "NET224", "NET225", "NET226", "NET227", "NET228", "NET229", "NET23", "NET230", "NET231", "NET232", "NET233", "NET234", "NET235", "NET236", "NET237", "NET238", "NET239", "NET24", "NET240", "NET241", "NET242", "NET243", "NET244", "NET245", "NET246", "NET247", "NET248", "NET249", "NET25", "NET250", "NET251", "NET252", "NET253", "NET254", "NET255", "NET256", "NET257", "NET258", "NET259", "NET26", "NET260", "NET261", "NET262", "NET263", "NET264", "NET265", "NET266", "NET267", "NET268", "NET269", "NET27", "NET270", "NET271", "NET272", "NET273", "NET274", "NET275", "NET276", "NET277", "NET278", "NET279", "NET28", "NET280", "NET281", "NET282", "NET283", "NET284", "NET285", "NET286", "NET287", "NET288", "NET289", "NET29", "NET290", "NET291", "NET292", "NET293", "NET294", "NET295", "NET296", "NET297", "NET298", "NET299", "NET3", "NET30", "NET300", "NET31", "NET32", "NET33", "NET34", "NET35", "NET36", "NET37", "NET38", "NET39", "NET4", "NET40", "NET41", "NET42", "NET43", "NET44", "NET45", "NET46", "NET47", "NET48", "NET49", "NET5", "NET50", "NET51", "NET52", "NET53", "NET54", "NET55", "NET56", "NET57", "NET58", "NET59", "NET6", "NET60", "NET61", "NET62", "NET63", "NET64", "NET65", "NET66", "NET67", "NET68", "NET69", "NET7", "NET70", "NET71", "NET72", "NET73", "NET74", "NET75", "NET76", "NET77", "NET78", "NET79", "NET8", "NET80", "NET81", "NET82", "NET83", "NET84", "NET85", "NET86", "NET87", "NET88", "NET89", "NET9", "NET90", "NET91", "NET92", "NET93", "NET94", "NET95", "NET96", "NET97", "NET98", "NET99"], None] = None
	servicePeriodFrom: Union[int, None] = None
	servicePeriodTo: Union[int, None] = None
	shipmentMethodId: Union[str, None] = None
	shipmentMethodName: Union[str, None] = None
	shippingCostItems: List[ShippingCostItems] = []
	defaultShippingCarrierId: Union[str, None] = None
	defaultShippingCarrierName: Union[str, None] = None
	deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
	deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.fromBlank()
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	plannedDeliveryDate: Union[int, None] = None
	plannedShippingDate: Union[int, None] = None
	recordAddress: RecordAddress = RecordAddress.fromBlank()
	salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.fromBlank()
	activeVersion: Union[bool, None]
	invoiceRecipientId: Union[str, None] = None
	opportunityId: Union[str, None] = None
	opportunityNumber: Union[str, None] = None
	publicLink: Union[str, None] = None
	quotationDate: Union[int, None] = None
	quotationItems: List[QuotationItems] = []
	quotationNumber: Union[str, None] = None
	quotationType: Union[Literal["CONTRACT", "NONE", "PROJECT", "SALES_INVOICE", "SALES_ORDER"], None] = None
	quotationVersion: Union[int, None] = None
	recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.fromBlank()
	rejectionReason: Union[str, None] = None
	requestDate: Union[int, None] = None
	salesOrderEmailAddresses: SalesOrderEmailAddresses = SalesOrderEmailAddresses.fromBlank()
	salesProbability: Union[int, None] = None
	salesStageHistory: List[SalesStageHistory] = []
	salesStageId: Union[str, None] = None
	salesStageName: Union[str, None] = None
	status: Union[Literal["ACCEPTED", "INQUIRED", "OPEN", "REJECTED"], None] = None
	statusHistory: List[StatusHistory] = []
	template: Union[bool, None]
	validFrom: Union[int, None] = None
	validTo: Union[int, None] = None
	warehouseId: Union[str, None] = None
	warehouseName: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


