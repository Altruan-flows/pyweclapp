from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import InvoiceAddress, DeliveryAddress





    
class OrderItems(BaseModel, Blueprint):
    id: str
    version: str
    addPageBreakBefore: bool  = None
    articleId: str = "31528346"
    articleNumber: str = "AL-Gutschrift"
    availability: str = None
    availabilityForAllWarehouses: str
    commissionSalesPartners: list= []
    createdDate: int
    customAttributes: List[WeclappMetaData] = []
    description: str = None
    descriptionFixed: bool
    discountPercentage: str
    freeTextItem: bool
    grossAmount: str
    grossAmountInCompanyCurrency: str
    invoicedQuantity: str
    lastModifiedDate: int
    manualQuantity: bool
    manualUnitCost: bool
    manualUnitPrice: bool
    netAmount: str
    netAmountForStatistics: str
    netAmountForStatisticsInCompanyCurrency: str
    netAmountInCompanyCurrency: str
    plannedShippingDate: int = None
    parentItemId: str = None
    positionNumber: int
    quantity: str
    reductionAdditionItems: list = []
    serviceItem: bool  = None
    servicePeriodFrom: int = None
    servicePeriodTo: int = None
    shipped: bool
    shippedQuantity: str
    tasks: list = []
    taxId: str
    taxName: str = None
    title: str = None
    unitCost: str = None
    unitCostInCompanyCurrency: str = None
    unitId: str
    unitName: str = None
    unitPrice: str
    unitPriceInCompanyCurrency: str = None
    withdrawalSerialNumbers: list = []
    withdrawalWarehouseLevelId: str = None
    
    # AutomationData
    ITEMS_NAME: str = "orderItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
    
    
    
    
##################################################################



    
class SalesOrder(BaseModel, Blueprint):
    id: str
    version: str
    availability: str
    availabilityForAllWarehouses: str
    commercialLanguage: str = "de"
    commissionSalesPartners: list
    createdDate: int
    currencyConversionDate: int
    currencyConversionRate: str
    customAttributes: List[WeclappMetaData] = []
    customerId: str
    customerNumber: str
    deliveryAddress: DeliveryAddress = {}
    deliveryEmailAddresses: dict = {}
    disableEmailTemplate: bool
    dispatchCountryCode: str
    factoring: bool
    fulfillmentProviderId: str
    grossAmount: str
    grossAmountInCompanyCurrency: str
    invoiceAddress: InvoiceAddress = {}
    invoiced: bool
    lastModifiedDate: int
    netAmount: str
    netAmountInCompanyCurrency: str
    onlyServices: bool
    orderDate: int
    orderItems: List[OrderItems] = []
    orderNumber: str
    paid: bool
    paymentMethodId: str = None
    paymentMethodName: str = None
    plannedShippingDate: int = None
    pricingDate: int
    projectMembers: list
    projectModeActive: bool
    recordAddress: dict
    recordCurrencyId: str
    recordCurrencyName: str
    recordEmailAddresses: dict = {}
    recordFreeText: str = None
    recordOpening: str = None
    responsibleUserId: str
    responsibleUserUsername: str
    salesChannel: str
    salesInvoiceEmailAddresses: dict = {}
    salesOrderPaymentType: str
    sentToRecipient: bool
    servicesFinished: bool
    servicePeriodFrom: int = None
    servicePeriodTo: int = None
    shipmentMethodId: str = ""
    shipmentMethodName: str = ""
    shipped: bool
    shippingCostItems: list = []
    shippingLabelsCount: int
    status: str
    statusHistory: list
    tags: list
    termOfPaymentId: str = None
    termOfPaymentName: str = None
    warehouseId: str
    warehouseName: str
    
    # SystemVariables 
    ITEMS_NAME: str = "orderItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
