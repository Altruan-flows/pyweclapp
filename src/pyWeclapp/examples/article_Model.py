# This code was dynamically created using WeclappClassCreator from pyWeclapp

from weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


class ArticleAlternativeQuantities(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    minimumOrderQuantity: Optional[str] = None
    minimumStockQuantity: Optional[str] = None
    targetStockQuantity: Optional[str] = None
    warehouseId: Optional[str] = None
    warehouseName: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ArticleCalculationPrices(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleCalculationPriceType: Optional[str] = None
    endDate: Optional[int] = None
    positionNumber: Optional[int] = None
    price: Optional[str] = None
    salesChannel: Optional[str] = None
    startDate: Optional[int] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ArticleImages(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    fileName: Optional[str] = None
    mainImage: Optional[bool] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ReductionAdditions(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ArticlePrices(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    currencyId: Optional[str] = None
    currencyName: Optional[str] = None
    customerId: Optional[str] = None
    description: Optional[str] = None
    endDate: Optional[int] = None
    lastModifiedByUserId: Optional[str] = None
    positionNumber: Optional[int] = None
    price: Optional[str] = None
    priceScaleType: Optional[str] = None
    priceScaleValue: Optional[str] = None
    reductionAdditions: List[ReductionAdditions] = []
    startDate: Optional[int] = None
    salesChannel: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class CustomerArticleNumbers(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customerArticleNumber: Optional[str] = None
    customerId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class DefaultStoragePlaces(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PriceCalculationParameters(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    fixSurcharge: Optional[str] = None
    fromScale: Optional[str] = None
    lowerPurchasePriceBound: Optional[str] = None
    margin: Optional[str] = None
    percentSurcharge: Optional[str] = None
    profit: Optional[str] = None
    salesChannel: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ProductionBillOfMaterialItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    articleNumber: Optional[str] = None
    positionNumber: Optional[int] = None
    quantity: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class QuantityConversions(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    conversionQuantity: Optional[str] = None
    createdUserId: Optional[str] = None
    lastEditedUserId: Optional[str] = None
    oppositeDirection: Optional[bool] = None
    unitId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SalesBillOfMaterialItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    articleNumber: Optional[str] = None
    positionNumber: Optional[int] = None
    quantity: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class SupplySources(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleSupplySourceId: Optional[str] = None
    positionNumber: Optional[int] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Article(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    articleNumber: Optional[str] = None
    description: Optional[str] = None
    ean: Optional[str] = None
    fixedPurchaseQuantity: Optional[str] = None
    internalNote: Optional[str] = None
    manufacturerPartNumber: Optional[str] = None
    matchCode: Optional[str] = None
    minimumPurchaseQuantity: Optional[str] = None
    name: Optional[str] = None
    shortDescription1: Optional[str] = None
    shortDescription2: Optional[str] = None
    taxRateType: Optional[str] = None
    unitId: Optional[str] = None
    unitName: Optional[str] = None
    accountId: Optional[str] = None
    accountNumber: Optional[str] = None
    accountingCodeId: Optional[str] = None
    active: Optional[bool] = None
    applyCashDiscount: Optional[bool] = None
    articleAlternativeQuantities: List[ArticleAlternativeQuantities] = []
    articleCalculationPrices: List[ArticleCalculationPrices] = []
    articleCategoryId: Optional[str] = None
    articleGrossWeight: Optional[str] = None
    articleHeight: Optional[str] = None
    articleImages: List[ArticleImages] = []
    articleLength: Optional[str] = None
    articleNetWeight: Optional[str] = None
    articlePrices: List[ArticlePrices] = []
    articleType: Optional[str] = None
    articleWidth: Optional[str] = None
    availableForSalesChannels: list = []  # could not be parsed
    availableInSale: Optional[bool] = None
    averageDeliveryTime: Optional[int] = None
    barcode: Optional[str] = None
    batchNumberRequired: Optional[bool] = None
    billOfMaterialPartDeliveryPossible: Optional[bool] = None
    catalogCode: Optional[str] = None
    commissionRate: Optional[str] = None
    contractBillingCycle: Optional[str] = None
    contractBillingMode: Optional[str] = None
    countryOfOriginCode: Optional[str] = None
    customerArticleNumbers: List[CustomerArticleNumbers] = []
    customsDescription: Optional[str] = None
    customsTariffNumber: Optional[str] = None
    customsTariffNumberId: Optional[str] = None
    defaultLoadingEquipmentIdentifierId: Optional[str] = None
    defaultPriceCalculationType: Optional[str] = None
    defaultStoragePlaces: List[DefaultStoragePlaces] = []
    defineIndividualTaskTemplates: Optional[bool] = None
    expenseAccountId: Optional[str] = None
    expenseAccountNumber: Optional[str] = None
    expirationDays: Optional[int] = None
    invoicingType: Optional[str] = None
    launchDate: Optional[int] = None
    loadingEquipmentArticleId: Optional[str] = None
    longText: Optional[str] = None
    lowLevelCode: Optional[int] = None
    manufacturerId: Optional[str] = None
    manufacturerName: Optional[str] = None
    marginCalculationPriceType: Optional[str] = None
    minimumStockQuantity: Optional[str] = None
    packagingQuantity: Optional[int] = None
    packagingUnitBaseArticleId: Optional[str] = None
    packagingUnitParentArticleId: Optional[str] = None
    plannedWorkingTimePerUnit: Optional[str] = None
    priceCalculationParameters: List[PriceCalculationParameters] = []
    primarySupplySourceId: Optional[str] = None
    procurementLeadDays: Optional[int] = None
    producerType: Optional[str] = None
    productionArticle: Optional[bool] = None
    productionBillOfMaterialItems: List[ProductionBillOfMaterialItems] = []
    purchaseCostCenterId: Optional[str] = None
    purchaseCostCenterNumber: Optional[str] = None
    quantityConversions: List[QuantityConversions] = []
    ratingId: Optional[str] = None
    ratingName: Optional[str] = None
    recordItemGroupName: Optional[str] = None
    safetyStockDays: Optional[int] = None
    salesBillOfMaterialItems: List[SalesBillOfMaterialItems] = []
    salesCostCenterId: Optional[str] = None
    salesCostCenterNumber: Optional[str] = None
    sellByDate: Optional[int] = None
    sellFromDate: Optional[int] = None
    serialNumberRequired: Optional[bool] = None
    showOnDeliveryNote: Optional[bool] = None
    statusId: Optional[str] = None
    supplySources: List[SupplySources] = []
    supportUntilDate: Optional[int] = None
    systemCode: Optional[str] = None
    tags: list = []
    targetStockQuantity: Optional[str] = None
    useAvailableForSalesChannels: Optional[bool] = None
    useSalesBillOfMaterialItemPrices: Optional[bool] = None
    useSalesBillOfMaterialItemPricesForPurchase: Optional[bool] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "articlePrices"
