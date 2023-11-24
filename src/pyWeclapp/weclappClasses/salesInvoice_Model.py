from .weclappClassBlueprint import Blueprint, WeclappMetaData

from typing import *



class CommissionSalesPartners(Blueprint):
	id: str
	version: str
	commissionFix: str = None
	commissionPercentage: str = None
	commissionType: str = None
	createdDate: int
	lastModifiedDate: int
	salesPartnerSupplierId: str = None
	salesPartnerSupplierNumber: str = None



class Address(Blueprint):
	city: str = None
	company: str = None
	company2: str = None
	countryCode: str = None
	firstName: str = None
	globalLocationNumber: str = None
	lastName: str = None
	middleName: str = None
	phoneNumber: str = None
	postOfficeBoxCity: str = None
	postOfficeBoxNumber: str = None
	postOfficeBoxZipCode: str = None
	salutation: str = None
	state: str = None
	street1: str = None
	street2: str = None
	title: str = None
	titleId: str = None
	zipcode: str = None







class EmailAddresses( Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None






class CommissionSalesPartners(Blueprint):
	id: str
	version: str
	commissionFix: str = None
	commissionPercentage: str = None
	commissionType: str = None
	createdDate: int
	lastModifiedDate: int
	salesPartnerSupplierId: str = None
	salesPartnerSupplierNumber: str = None




class CostCenterItems(Blueprint):
	id: str
	version: str
	costCenterId: str = None
	costCenterNumber: str = None
	createdDate: int
	distributionPercentage: str = None
	lastModifiedDate: int




class ReductionAdditionItems(Blueprint):
	position: int = None
	source: str = None
	type: str = None
	value: str = None





class SalesInvoiceItemRelationship(Blueprint):
	performanceRecordItemId: str = None
	quantity: str = None
	salesInvoiceItemId: str = None
	salesOrderItemId: str = None
	shipmentItemId: str = None





class SalesInvoiceItems(Blueprint):
	id: str
	version: str
	accountId: str = None
	accountNumber: str = None
	addPageBreakBefore: bool
	articleId: str = None
	articleNumber: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	costCenterItems: List[CostCenterItems] = []
	createdDate: int
	creditedInvoiceItemId: str = None
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	descriptionFixed: bool
	discountPercentage: str = None
	freeTextItem: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	groupName: str = None
	lastModifiedDate: int
	manualQuantity: bool
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountForStatistics: str = None
	netAmountForStatisticsInCompanyCurrency: str = None
	netAmountInCompanyCurrency: str = None
	note: str = None
	parentItemId: str = None
	positionNumber: int
	quantity: str = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	salesInvoiceItemRelationship: List[SalesInvoiceItemRelationship] = []
	serialNumbers: list = [] # could not be parsed
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	taxId: str = None
	taxName: str = None
	title: str = None
	unitCost: str = None
	unitCostInCompanyCurrency: str = None
	unitId: str = None
	unitName: str = None
	unitPrice: str = None
	unitPriceInCompanyCurrency: str = None



	# AutomationData
	ITEMS_NAME: str = 'reductionAdditionItems'




class SalesOrders(Blueprint):
	id: str




class ShippingCostItems(Blueprint):
	id: str
	version: str
	articleId: str = None
	articleNumber: str = None
	createdDate: int
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	lastModifiedDate: int
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	taxId: str = None
	taxName: str = None
	unitCost: str = None
	unitCostInCompanyCurrency: str = None
	unitPrice: str = None
	unitPriceInCompanyCurrency: str = None





class StatusHistory(Blueprint):
	status: str = None
	statusDate: int = None
	userId: str = None




class SalesInvoice( Blueprint):
	id: str
	version: str
	cancellationDate: int = None
	cancellationNumber: str = None
	collectiveInvoicePositionPrintType: str = None
	commercialLanguage: str = None
	commission: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	createdDate: int
	currencyConversionDate: int = None
	currencyConversionRate: str = None
	customAttributes: List[WeclappMetaData] = []
	customerHabitualExporterLetterOfIntentId: str = None
	customerId: str = None
	customerNumber: str = None
	deliveryAddress: Address = Address.fromBlank()
	deliveryDate: int = None
	description: str = None
	disableEmailTemplate: bool
	dispatchCountryCode: str = None
	dueDate: int = None
	factoring: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	headerDiscount: str = None
	headerSurcharge: str = None
	invoiceDate: int = None
	invoiceNumber: str = None
	lastModifiedDate: int
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	nonStandardTaxId: str = None
	nonStandardTaxName: str = None
	orderNumberAtCustomer: str = None
	paid: bool
	paymentMethodId: str = None
	paymentMethodName: str = None
	paymentStatus: str = None
	precedingSalesInvoiceId: str = None
	pricingDate: int = None
	recordAddress: Address = Address.fromBlank()
	recordComment: str = None
	recordCurrencyId: str = None
	recordCurrencyName: str = None
	recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	responsibleUserId: str = None
	responsibleUserUsername: str = None
	salesChannel: str = None
	salesInvoiceItems: List[SalesInvoiceItems] = []
	salesInvoiceType: str = None
	salesOrderId: str = None
	salesOrderNumber: str = None
	salesOrders: List[SalesOrders] = []
	sentToRecipient: bool
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shippingCostItems: List[ShippingCostItems] = []
	shippingDate: int = None
	status: str = None
	statusHistory: List[StatusHistory] = []
	tags: list = [] # could not be parsed
	termOfPaymentId: str = None
	termOfPaymentName: str = None
	vatRegistrationNumber: str = None



	# AutomationData
	ITEMS_NAME: str = "salesInvoiceItems"




