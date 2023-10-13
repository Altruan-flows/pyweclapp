from pyWeclapp.weclappClasses import Blueprint, WeclappMetaData
from pydantic import BaseModel
from typing import *



class ArticleAlternativeQuantities(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	lastModifiedDate: int
	minimumOrderQuantity: str = None
	minimumStockQuantity: str = None
	targetStockQuantity: str = None
	warehouseId: str = None
	warehouseName: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ArticleCalculationPrices(BaseModel, Blueprint):
	id: str
	version: str
	articleCalculationPriceType: str = None
	createdDate: int
	endDate: int = None
	lastModifiedDate: int
	positionNumber: int = None
	price: str = None
	salesChannel: str = None
	startDate: int = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ArticleImages(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	fileName: str = None
	lastModifiedDate: int
	mainImage: bool



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ReductionAdditions(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	lastModifiedDate: int
	name: str = None
	type: str = None
	value: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ArticlePrices(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	currencyId: str = None
	currencyName: str = None
	customerId: str = None
	description: str = None
	endDate: int = None
	lastModifiedByUserId: str = None
	lastModifiedDate: int
	positionNumber: int = None
	price: str = None
	priceScaleType: str
	priceScaleValue: str = None
	reductionAdditions: List[ReductionAdditions] = []
	salesChannel: str = None
	startDate: int = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class CustomerArticleNumbers(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	customerArticleNumber: str = None
	customerId: str = None
	lastModifiedDate: int



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class DefaultStoragePlaces(BaseModel, Blueprint):
	id: str



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class PriceCalculationParameters(BaseModel, Blueprint):
	id: str
	version: str
	createdDate: int
	fixSurcharge: str = None
	fromScale: str = None
	lastModifiedDate: int
	lowerPurchasePriceBound: str = None
	margin: str = None
	percentSurcharge: str = None
	profit: str = None
	salesChannel: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class ProductionBillOfMaterialItems(BaseModel, Blueprint):
	id: str
	version: str
	articleId: str = None
	articleNumber: str = None
	createdDate: int
	lastModifiedDate: int
	positionNumber: int = None
	quantity: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class QuantityConversions(BaseModel, Blueprint):
	id: str
	version: str
	conversionQuantity: str = None
	createdDate: int
	createdUserId: str = None
	lastEditedUserId: str = None
	lastModifiedDate: int
	oppositeDirection: bool
	unitId: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class SalesBillOfMaterialItems(BaseModel, Blueprint):
	id: str
	version: str
	articleId: str = None
	articleNumber: str = None
	createdDate: int
	lastModifiedDate: int
	positionNumber: int = None
	quantity: str = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class SupplySources(BaseModel, Blueprint):
	id: str
	version: str
	articleSupplySourceId: str = None
	createdDate: int
	lastModifiedDate: int
	positionNumber: int = None



	# AutomationData
	ITEMS_NAME: str = None
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



class Article(BaseModel, Blueprint):
	id: str
	version: str
	accountId: str = None
	accountNumber: str = None
	accountingCodeId: str = None
	active: bool
	applyCashDiscount: bool
	articleAlternativeQuantities: List[ArticleAlternativeQuantities] = []
	articleCalculationPrices: List[ArticleCalculationPrices] = []
	articleCategoryId: str = None
	articleGrossWeight: str = None
	articleHeight: str = None
	articleImages: List[ArticleImages] = []
	articleLength: str = None
	articleNetWeight: str = None
	articleNumber: str = None
	articlePrices: List[ArticlePrices] = []
	articleType: str
	articleWidth: str = None
	availableForSalesChannels: list = [] # could not be parsed
	availableInSale: bool
	averageDeliveryTime: int = None
	barcode: str = None
	batchNumberRequired: bool
	billOfMaterialPartDeliveryPossible: bool
	catalogCode: str = None
	contractBillingCycle: str = None
	contractBillingMode: str = None
	countryOfOriginCode: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	customerArticleNumbers: List[CustomerArticleNumbers] = []
	customsDescription: str = None
	customsTariffNumber: str = None
	customsTariffNumberId: str = None
	defaultLoadingEquipmentIdentifierId: str = None
	defaultPriceCalculationType: str = None
	defaultStoragePlaces: List[DefaultStoragePlaces] = []
	defineIndividualTaskTemplates: bool
	description: str = None
	ean: str = None
	expenseAccountId: str = None
	expenseAccountNumber: str = None
	expirationDays: int = None
	fixedPurchaseQuantity: str = None
	internalNote: str = None
	invoicingType: str = None
	lastModifiedDate: int
	launchDate: int = None
	loadingEquipmentArticleId: str = None
	longText: str = None
	lowLevelCode: int = None
	manufacturerId: str = None
	manufacturerName: str = None
	manufacturerPartNumber: str = None
	marginCalculationPriceType: str = None
	matchCode: str = None
	minimumPurchaseQuantity: str = None
	minimumStockQuantity: str = None
	name: str = None
	packagingQuantity: int = None
	packagingUnitBaseArticleId: str = None
	packagingUnitParentArticleId: str = None
	plannedWorkingTimePerUnit: str = None
	priceCalculationParameters: List[PriceCalculationParameters] = []
	primarySupplySourceId: str = None
	procurementLeadDays: int = None
	producerType: str = None
	productionArticle: bool
	productionBillOfMaterialItems: List[ProductionBillOfMaterialItems] = []
	purchaseCostCenterId: str = None
	purchaseCostCenterNumber: str = None
	quantityConversions: List[QuantityConversions] = []
	ratingId: str = None
	ratingName: str = None
	recordItemGroupName: str = None
	safetyStockDays: int = None
	salesBillOfMaterialItems: List[SalesBillOfMaterialItems] = []
	salesCostCenterId: str = None
	salesCostCenterNumber: str = None
	sellByDate: int = None
	sellFromDate: int = None
	serialNumberRequired: bool
	shortDescription1: str = None
	shortDescription2: str = None
	showOnDeliveryNote: bool
	statusId: str = None
	supplySources: List[SupplySources] = []
	supportUntilDate: int = None
	systemCode: str = None
	tags: list = []
	targetStockQuantity: str = None
	taxRateType: str = None
	unitId: str = None
	unitName: str = None
	useAvailableForSalesChannels: bool
	useSalesBillOfMaterialItemPrices: bool
	useSalesBillOfMaterialItemPricesForPurchase: bool



	# AutomationData
	ITEMS_NAME: str = "articlePrices"
	USED_ATTRIBUTES: dict = dict()
	__setattr__ = Blueprint.__setattr__


	def __init__(self, **kwargs):
		BaseModel.__init__(self, **kwargs)
		Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)



