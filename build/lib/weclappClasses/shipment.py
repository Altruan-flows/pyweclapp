from pydantic import BaseModel
from .weclappClassBlueprint import *
from .addresses import InvoiceAddress





class ShipmentItems(BaseModel, Blueprint):
    id: str
    version: str
    addPageBreakBefore: bool
    articleId: str = "31528346"
    articleNumber: str = "AL-Gutschrift"
    availability: str
    availabilityForAllWarehouses: str
    createdDate: int
    customAttributes: List[WeclappMetaData] = []
    descriptionFixed: bool
    freeTextItem: bool
    lastModifiedDate: int
    manualQuantity: bool
    parentItemId:str = None
    positionNumber: int
    quantity: str
    salesOrderItemId: str = None        # does not exist, when Status is cancelled
    title: str = None
    unitId: str
    unitName: str
    
    
    ITEMS_NAME:str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
        


##################################################################



class Shipment(Blueprint, BaseModel):
    id: str
    version: str
    allWithdrawalsConfirmed: bool = None # Be carefull  is not always included
    availability: str
    availabilityForAllWarehouses: str
    commercialLanguage: str = "de"
    createdDate: int
    customAttributes: List[WeclappMetaData] = []
    customerPurchaseOrderNumber: str = ""
    disableEmailTemplate: bool
    description:str = ""
    invoiceAddress: InvoiceAddress = {}
    lastModifiedDate: int
    packageHeight: int
    packageTrackingNumber:str = ""
    packageLength: int
    packageReferenceNumber: str = None
    packageTrackingUrl: str = ""
    packageWeight: str
    packageWidth: int
    purchaseOrders: list = []
    recipientAddress: dict
    recipientCustomerNumber: str
    recipientPartyId: str
    recordEmailAddresses: dict = {}
    recordFreeText: str
    recordOpening: str
    salesInvoiceEmailAddresses: dict = {}
    salesOrderId: str
    salesOrderNumber: str
    sentToRecipient: bool
    shipmentItems: List[ShipmentItems] = []
    shipmentMethodId: str = None
    shipmentMethodName: str = None
    shipmentNumber: str
    shipmentType: str
    shippedFromAddress: dict
    shippingCarrierId: str = None
    shippingCarrierName: str = None
    shippingDate: int = None
    shippingLabelsCount: int
    status: str
    statusHistory: list = []
    tags: list = []
    warehouseId: str
    warehouseName: str
    withdrawalsComplete: bool = None # Be carefull is not always included
    
    # # AutomationData
    ITEMS_NAME: str = "shipmentItems"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__

    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
        
    def queryItems(self, key:str, value:str, justParentItems:bool=False, raiseError:bool=True) -> ShipmentItems:
        return Blueprint.queryItems(self, key=key, value=value, justParentItems=justParentItems, raiseError=raiseError)

