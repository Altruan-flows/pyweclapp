from pydantic import BaseModel
from .weclappClassBlueprint import *





class QuotationItems(BaseModel, Blueprint):
	id: str
	version: str
	addPageBreakBefore: bool
	alternative: bool
	articleId: str
	articleNumber: str
	commissionSalesPartners: list
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = ""
	descriptionFixed: bool
	discountPercentage: str
	freeTextItem: bool
	grossAmount: str
	grossAmountInCompanyCurrency: str
	lastModifiedDate: int
	manualQuantity: bool
	manualUnitCost: bool
	manualUnitPrice: bool
	netAmount: str
	netAmountForStatistics: str
	netAmountForStatisticsInCompanyCurrency: str
	netAmountInCompanyCurrency: str
	optional: bool
	positionNumber: int
	quantity: str
	reductionAdditionItems: list
	serviceItem: bool
	taxId: str
	taxName: str
	title: str
	unitCost: str = ""
	unitCostInCompanyCurrency: str = ""
	unitId: str
	unitName: str
	unitPrice: str
	unitPriceInCompanyCurrency: str

	# AutomationData
	ITEMS_NAME: str = "-"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)


 
 
class Quotation(BaseModel, Blueprint):
	id: str
	version: str
	activeVersion: bool
	commercialLanguage: str = "de"
	commissionSalesPartners: list
	createdDate: int
	currencyConversionDate: int
	currencyConversionRate: str
	customAttributes: List[WeclappMetaData] = []
	customerId: str
	customerNumber: str
	defaultShippingCarrierId: str
	defaultShippingCarrierName: str
	deliveryAddress: dict
	deliveryEmailAddresses: dict = {}
	disableEmailTemplate: bool
	dispatchCountryCode: str
	factoring: bool
	grossAmount: str
	grossAmountInCompanyCurrency: str
	headerDiscount: str
	headerSurcharge: str
	invoiceAddress: dict
	lastModifiedDate: int
	netAmount: str
	netAmountInCompanyCurrency: str
	paymentMethodId: str = None
	paymentMethodName: str = None
	pricingDate: int
	publicLink: str
	quotationDate: int
	quotationItems: List[QuotationItems] = []
	quotationNumber: str
	quotationType: str
	quotationVersion: int
	recordAddress: dict
	recordCurrencyId: str
	recordCurrencyName: str
	recordEmailAddresses: dict = {}
	recordFreeText: str
	recordOpening: str
	requestDate: int
	responsibleUserId: str
	responsibleUserUsername: str
	salesChannel: str
	salesInvoiceEmailAddresses: dict = {}
	salesOrderEmailAddresses: dict = {}
	salesProbability: int
	salesStageHistory: list
	salesStageId: str
	salesStageName: str
	sentToRecipient: bool
	shipmentMethodId: str = None
	shipmentMethodName: str = None
	shippingCostItems: list
	status: str
	statusHistory: list
	tags: list
	template: bool
	termOfPaymentId: str
	termOfPaymentName: str
	validFrom: int
	validTo: int

	# AutomationData
	ITEMS_NAME: str = "quotationItems"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)

