from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import DeliveryAddress






class SalesInvoiceItems(BaseModel, Blueprint):
	id: str
	version: str
	accountId: str = None
	accountNumber: str = None
	addPageBreakBefore: bool
	articleId: str = None
	articleNumber: str = None
	commissionSalesPartners: list
	costCenterItems: list
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
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
	netAmountForStatisticsInCompanyCurrency: str = None
	netAmountInCompanyCurrency: str
	note: str = None
	positionNumber: int
	quantity: str
	reductionAdditionItems: list
	salesInvoiceItemRelationship: list
	serialNumbers: list
	servicePeriodFrom: int = None
	servicePeriodTo: int = None
	taxId: str
	taxName: str
	title: str = None
	unitCost: str = None
	unitCostInCompanyCurrency: str = None
	unitId: str
	unitName: str
	unitPrice: str
	unitPriceInCompanyCurrency: str = None

	# AutomationData
	ITEMS_NAME: str = "-"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)


############################################################################################################################################################################


class SalesInvoice(BaseModel, Blueprint):
    id: str
    version: str
    commercialLanguage: str = "de"
    commissionSalesPartners: list
    createdDate: int
    currencyConversionDate: int
    currencyConversionRate: str
    customAttributes: List[WeclappMetaData] = []
    customerId: str
    customerNumber: str
    deliveryAddress: DeliveryAddress = []
    disableEmailTemplate: bool
    dispatchCountryCode: str
    dueDate: int
    factoring: bool
    grossAmount: str
    grossAmountInCompanyCurrency: str
    headerDiscount: str = None
    headerSurcharge: str = None
    invoiceDate: int
    invoiceNumber: str
    lastModifiedDate: int
    netAmount: str
    netAmountInCompanyCurrency: str
    paid: bool
    paymentMethodId: str
    paymentMethodName: str
    paymentStatus: str
    pricingDate: int
    recordAddress: dict = {}
    recordCurrencyId: str
    recordCurrencyName: str
    recordEmailAddresses: dict = {}
    recordFreeText: str
    recordOpening: str
    responsibleUserId: str
    responsibleUserUsername: str
    salesChannel: str
    salesInvoiceItems: List[SalesInvoiceItems] = []
    salesInvoiceType: str
    salesOrderId: str
    salesOrderNumber: str
    salesOrders: list = []
    sentToRecipient: bool
    servicePeriodFrom: int = None
    servicePeriodTo: int = None
    shipmentMethodId: str = None
    shipmentMethodName: str = None
    shippingCostItems: list = []
    shippingDate: int = None
    status: str
    statusHistory: list = []
    tags: list = []
    termOfPaymentId: str
    termOfPaymentName: str

    # AutomationData
    ITEMS_NAME: str = "salesInvoiceItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)