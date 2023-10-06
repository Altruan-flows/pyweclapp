from pydantic import BaseModel
from .weclappClassBlueprint import *




class ReductionAdditions(BaseModel, Blueprint):
    id: str
    version: str
    createdDate: int
    lastModifiedDate: int
    type: str
    value: str

    # AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES:dict=dict()
    __setattr__ = Blueprint.__setattr__
    
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)


##################################################################


class ArticlePrices(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	currencyId: str
	currencyName: str
	lastModifiedByUserId: str
	lastModifiedDate: int
	positionNumber: int
	price: str
	priceScaleType: str
	priceScaleValue: str
	reductionAdditions: List[ReductionAdditions] = []
	salesChannel: str
	startDate: int = 0
	endDate: int = 0

	# AutomationData
	ITEMS_NAME: str = "reductionAdditions"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__
    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)
  
	def queryItems(self, key:str, value:str, justParentItems:bool=False, raiseError:bool=True) -> ReductionAdditions:
		return Blueprint.queryItems(self, key=key, value=value, justParentItems=justParentItems, raiseError=raiseError)
 

##################################################################


class Article(BaseModel, Blueprint):
	id: str
	version: str
	active: bool
	applyCashDiscount: bool
	articleAlternativeQuantities: list = []
	articleCalculationPrices: list = []
	articleCategoryId: str = None
	articleImages: list = []
	articleNumber: str
	articlePrices: List[ArticlePrices] = []
	articleType: str
	articleGrossWeight: str = None
	articleHeight: str = None
	articleLength: str = None
	articleNetWeight: str = None
	articleWidth: str = None
	availableForSalesChannels: list = []
	availableInSale: bool
	averageDeliveryTime: int = None
	batchNumberRequired: bool
	billOfMaterialPartDeliveryPossible: bool
	createdDate: int
	customerArticleNumbers: list = []
	customsTariffNumber: str = None
	customsTariffNumberId: str = None
	customAttributes: List[WeclappMetaData] = []
	defaultPriceCalculationType: str
	defaultWarehouseLevels: list = []
	defineIndividualTaskTemplates: bool
	description: str = None
	ean: str = None
	fixedPurchaseQuantity: str = None
	lastModifiedDate: int
	lowLevelCode: int
	manufacturerId: str = None
	manufacturerName: str = None
	manufacturerPartNumber: str = None
	marginCalculationPriceType: str
	minimumStockQuantity: str = None
	name: str
	priceCalculationParameters: list = []
	procurementLeadDays: int = None
	productionArticle: bool
	productionBillOfMaterialItems: list = []
	quantityConversions: list = []
	safetyStockDays: int = None
	salesBillOfMaterialItems: list = []
	serialNumberRequired: bool
	shortDescription1: str = None
	showOnDeliveryNote: bool
	supplySources: list = []
	tags: list = []
	targetStockQuantity: str = None
	taxRateType: str
	unitId: str
	unitName: str
	useAvailableForSalesChannels: bool
	useSalesBillOfMaterialItemPrices: bool
	useSalesBillOfMaterialItemPricesForPurchase: bool

    # # AutomationData
	ITEMS_NAME: str = "articlePrices"
	USED_ATTRIBUTES:dict=dict()
	__setattr__ = Blueprint.__setattr__

    
	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)

	def queryItems(self, key:str, value:str, justParentItems:bool=False, raiseError:bool=True) -> ArticlePrices:
		return Blueprint.queryItems(self, key=key, value=value, justParentItems=justParentItems, raiseError=raiseError)


 
