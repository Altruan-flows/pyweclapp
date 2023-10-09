from pydantic import BaseModel
from util.weclappClasses.weclappClassBlueprint import *
from .addresses import InvoiceAddress_Template, DeliveryAddress_Template
from .blueprintTemplate import Blueprint_Templates




    
class OrderItems_Template(BaseModel, Blueprint_Templates):
    id: str = None
    version: str = None
    addPageBreakBefore: bool  = None
    articleId: str = None
    articleNumber: str = None
    availability: str = None
    availabilityForAllWarehouses: str = None
    commissionSalesPartners: list= []
    createdDate: int = None
    customAttributes: list = []
    description: str = None 
    descriptionFixed: bool = None
    discountPercentage: str = None
    freeTextItem: bool = None
    grossAmount: str = None
    grossAmountInCompanyCurrency: str = None
    invoicedQuantity: str = None
    lastModifiedDate: int = None
    manualQuantity: bool = None
    manualUnitCost: bool = None
    manualUnitPrice: bool = None
    netAmount: str = None
    netAmountForStatistics: str = None
    netAmountForStatisticsInCompanyCurrency: str = None
    netAmountInCompanyCurrency: str = None
    plannedShippingDate: int = None
    parentItemId: str = None
    positionNumber: int = None
    quantity: str = None
    reductionAdditionItems: list = []
    serviceItem: bool  = None
    servicePeriodFrom: int = None
    servicePeriodTo: int = None
    shipped: bool = None
    shippedQuantity: str = None
    tasks: list = []
    taxId: str = None
    taxName: str = None
    title: str = None
    unitCost: str = None
    unitCostInCompanyCurrency: str = None
    unitId: str = None
    unitName: str = None
    unitPrice: str = None
    unitPriceInCompanyCurrency: str = None
    withdrawalSerialNumbers: list = []
    withdrawalWarehouseLevelId: str = None
    
    # AutomationData
    ITEMS_NAME: str = "orderItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint_Templates.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
    
    
    
    
##################################################################


class SalesOrder_Template(BaseModel, Blueprint_Templates):
    id: str = None
    version: str = None
    availability: str = None
    availabilityForAllWarehouses: str = None
    commercialLanguage: str = None
    commissionSalesPartners: list = []
    createdDate: int = None
    currencyConversionDate: int = None
    currencyConversionRate: str = None
    customAttributes: list = []
    customerId: str = "1234" # this field is required
    customerNumber: str = None
    deliveryAddress: DeliveryAddress_Template = {}
    deliveryEmailAddresses: dict = {}
    disableEmailTemplate: bool = None
    dispatchCountryCode: str = None
    factoring: bool = None
    fulfillmentProviderId: str = None
    grossAmount: str = None
    grossAmountInCompanyCurrency: str = None
    invoiceAddress: InvoiceAddress_Template = {}
    invoiced: bool = None
    lastModifiedDate: int = None
    netAmount: str = None
    netAmountInCompanyCurrency: str = None
    onlyServices: bool = None
    orderDate: int = None
    orderItems: list = []
    orderNumber: str = None
    paid: bool = None
    paymentMethodId: str = None
    paymentMethodName: str = None
    plannedShippingDate: int = None
    pricingDate: int = None
    projectMembers: list = []
    projectModeActive: bool = None
    recordAddress: dict = {}
    recordCurrencyId: str = None
    recordCurrencyName: str = None
    recordEmailAddresses: dict = {}
    recordFreeText: str = None
    recordOpening: str = None
    responsibleUserId: str = None
    responsibleUserUsername: str = None
    salesChannel: str = None
    salesInvoiceEmailAddresses: dict = {}
    salesOrderPaymentType: str = None
    sentToRecipient: bool = None
    servicesFinished: bool = None
    servicePeriodFrom: int = None
    servicePeriodTo: int = None
    shipmentMethodId: str = None
    shipmentMethodName: str = None
    shipped: bool = None
    shippingCostItems: list = []
    shippingLabelsCount: int = None
    status: str = None
    statusHistory: list = []
    tags: list = []
    termOfPaymentId: str = None
    termOfPaymentName: str = None
    warehouseId: str = None
    warehouseName: str = None
    
    # SystemVariables 
    ITEMS_NAME: str = "orderItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint_Templates.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint_Templates.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)