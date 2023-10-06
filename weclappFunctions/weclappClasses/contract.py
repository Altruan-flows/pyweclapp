from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import InvoiceAddress, DeliveryAddress





        
class ContractItems(BaseModel, Blueprint):
    id:str
    version:str
    addPageBreakBefore:bool = None
    articleId:str = None
    articleNumber:str = None
    billingGroupId:str=None
    commissionSalesPartners:list = []
    createdDate:int
    customAttributes:List[WeclappMetaData] = []
    description:str = None
    descriptionFixed:bool = None
    discountPercentage:str = None
    freeTextItem:bool = None
    grossAmount:str = None
    grossAmountInCompanyCurrency:str = None
    groupName:str = None    
    parentItemId:str = None
    interval:str
    intervalType:str
    lastModifiedDate:int
    manualQuantity:bool
    manualUnitPrice:bool
    netAmount:str
    netAmountForStatistics:str = None
    netAmountForStatisticsInCompanyCurrency:str = None
    netAmountInCompanyCurrency:str = None
    nextContractBillingDate:int = None
    note:str = None
    positionNumber:int
    previousContractBillingDate:int = None
    quantity:str
    reductionAdditionItems:list = None
    servicePeriodFromDate:int = None
    servicePeriodToDate:int = None
    taxId:str
    taxName:str = None
    title:str = None
    type:str
    unitId:str
    unitName:str = None
    unitPrice:str = None
    unitPriceInCompanyCurrency:str = None
    
    
    # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
    


##################################################################


    
class Contract(BaseModel, Blueprint):
    id:str  
    version:str
    additionalAddresses:list
    automaticExtension:bool
    billingDay: int = 1
    billingType:str
    commercialLanguage:str = "de"                      
    commissionSalesPartners:list
    contractDate:int = None                      # Date Signed -> Tag an den der Vertrag unterschreiebn wurder
    contractCostItems:list = []
    contractItems:List[ContractItems] = []
    contractNumber:str
    contractStatus:str
    correspondenceAddress:dict = {}
    createdDate:int
    customAttributes:List[WeclappMetaData] = []
    deliveryAddress:DeliveryAddress = {}
    deliveryEmailAddresses:dict = {}
    description:str = "<p></p>"
    differingCorrespondenceAddress:bool
    differingDeliveryAddress:bool
    differingInvoiceAddress:bool 
    disableEmailTemplate:bool
    endDate:int = None
    factoring:bool
    invoiceAddress:InvoiceAddress = {}
    lastModifiedDate:int
    latestPossibleTerminationDate:int = None
    latestCancellationWarningQuantity:int
    latestCancellationWarningUnit:str
    name:str
    orderNumberAtCustomer:str = None
    partyId:str
    paymentMethodId:str
    pricingDate:int
    recordCurrencyId:str
    recordCurrencyName:str
    recordEmailAddresses:dict = {}
    recordFreeText:str = None
    recordOpening:str = None
    reminderSendType:str
    reminderType:str
    responsibleUserId:str
    salesChannel:str
    salesInvoiceEmailAddresses:dict = {}
    salesOrderEmailAddresses:dict = {}
    sentToRecipient:bool
    startDate:int = None
    tags:list
    template:bool
    termOfPaymentId:str
    types:list
    unlimited:bool = False
    
    # AutomationData
    ITEMS_NAME: str = "contractItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
    