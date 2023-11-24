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





class DeliveryAddress(Blueprint):
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





class DeliveryEmailAddresses(Blueprint):
	bccAddresses: str = None
	ccAddresses: str = None
	toAddresses: str = None




class InvoiceAddress( Blueprint):
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





class ReductionAdditionItems(Blueprint):
	position: int = None
	source: str = None
	type: str = None
	value: str = None





class QuotationItems(Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	alternative: bool
	articleId: str = None
	articleNumber: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	descriptionFixed: bool
	discountPercentage: str = None
	freeTextItem: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	groupName: str = None
	invoicingType: str = None
	lastModifiedDate: int
	manualPlannedWorkingTimePerUnit: bool
	manualQuantity: bool
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str = None
	netAmountForStatistics: str = None
	netAmountForStatisticsInCompanyCurrency: str = None
	netAmountInCompanyCurrency: str = None
	note: str = None
	optional: bool
	parentItemId: str = None
	plannedWorkingTimePerUnit: str = None
	positionNumber: int = None
	quantity: str = None
	reductionAdditionItems: List[ReductionAdditionItems] = []
	serviceItem: bool
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




class RecordAddress(Blueprint):
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








class SalesStageHistory(Blueprint):
	id: str
	version: str
	createdDate: int
	lastModifiedDate: int
	salesStageId: str = None
	salesStageName: str = None
	userId: str = None





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




class StatusHistory( Blueprint):
	status: str = None
	statusDate: int = None
	userId: str = None



class Quotation(Blueprint):
	id: str
	version: str
	activeVersion: bool
	commercialLanguage: str = None
	commission: str = None
	commissionSalesPartners: List[CommissionSalesPartners] = []
	createdDate: int
	currencyConversionDate: int = None
	currencyConversionRate: str = None
	customAttributes: List[WeclappMetaData] = []
	customerId: str = None
	customerNumber: str = None
	defaultShippingCarrierId: str = None
	defaultShippingCarrierName: str = None
	deliveryAddress: DeliveryAddress = DeliveryAddress.fromBlank()
	deliveryEmailAddresses: DeliveryEmailAddresses = DeliveryEmailAddresses.fromBlank()
	description: str = None
	disableEmailTemplate: bool
	dispatchCountryCode: str = None
	factoring: bool
	grossAmount: str = None
	grossAmountInCompanyCurrency: str = None
	headerDiscount: str = None
	headerSurcharge: str = None
	invoiceAddress: InvoiceAddress = InvoiceAddress.fromBlank()
	invoiceRecipientId: str = None
	lastModifiedDate: int
	netAmount: str = None
	netAmountInCompanyCurrency: str = None
	nonStandardTaxId: str = None
	nonStandardTaxName: str = None
	opportunityId: str = None
	opportunityNumber: str = None
	paymentMethodId: str = None
	paymentMethodName: str = None
	plannedDeliveryDate: int = None
	plannedShippingDate: int = None
	pricingDate: int = None
	publicLink: str = None
	quotationDate: int = None
	quotationItems: List[QuotationItems] = []
	quotationNumber: str = None
	quotationType: str = None
	quotationVersion: int = None
	recordAddress: RecordAddress = RecordAddress.fromBlank()
	recordComment: str = None
	recordCurrencyId: str = None
	recordCurrencyName: str = None
	recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	recordFreeText: str = None
	recordOpening: str = None
	rejectionReason: str = None
	requestDate: int = None
	responsibleUserId: str = None
	responsibleUserUsername: str = None
	salesChannel: str = None
	salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	salesOrderEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
	salesProbability: int = None
	salesStageHistory: List[SalesStageHistory] = []
	salesStageId: str = None
	salesStageName: str = None
	sentToRecipient: bool
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shippingCostItems: List[ShippingCostItems] = []
	status: str = None
	statusHistory: List[StatusHistory] = []
	tags: list = [] # could not be parsed
	template: bool
	termOfPaymentId: str = None
	termOfPaymentName: str = None
	validFrom: int = None
	validTo: int = None
	warehouseId: str = None
	warehouseName: str = None



	# AutomationData
	ITEMS_NAME: str = 'quotationItems'



