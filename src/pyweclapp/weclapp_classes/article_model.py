"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List, Set
from .blueprints import Blueprint, WeclappMetaData


class ArticleAlternativeQuantities(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    minimumOrderQuantity: Union[str, None] = None
    minimumStockQuantity: Union[str, None] = None
    targetStockQuantity: Union[str, None] = None
    warehouseId: Union[str, None] = None


class ArticleCalculationPrices(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleCalculationPriceType: Union[str, None] = None
    endDate: Union[int, None] = None
    price: Union[str, None] = None
    salesChannel: Union[str, None] = None
    startDate: Union[int, None] = None


class ArticleImages(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    fileName: Union[str, None] = None
    mainImage: Union[bool, None] = None


class ReductionAdditions(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    name: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class ArticlePrices(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    currencyId: Union[str, None] = None
    customerId: Union[str, None] = None
    description: Union[str, None] = None
    endDate: Union[int, None] = None
    lastModifiedByUserId: Union[str, None] = None
    price: Union[str, None] = None
    priceScaleType: Union[str, None] = None
    priceScaleValue: Union[str, None] = None
    reductionAdditions: List[ReductionAdditions] = []
    startDate: Union[int, None] = None
    salesChannel: Union[str, None] = None


class CustomerArticleNumbers(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customerArticleNumber: Union[str, None] = None
    customerId: Union[str, None] = None


class DefaultStoragePlaces(Blueprint):
    id: Union[str, None] = None


class ProductionBillOfMaterialItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    positionNumber: Union[int, None] = None
    quantity: Union[str, None] = None


class QuantityConversions(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    conversionQuantity: Union[str, None] = None
    createdUserId: Union[str, None] = None
    lastEditedUserId: Union[str, None] = None
    oppositeDirection: Union[bool, None] = None
    unitId: Union[str, None] = None


class SalesBillOfMaterialItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    positionNumber: Union[int, None] = None
    quantity: Union[str, None] = None


class SupplySources(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleSupplySourceId: Union[str, None] = None
    positionNumber: Union[int, None] = None


class Article(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    articleNumber: Union[str, None] = None
    description: Union[str, None] = None
    ean: Union[str, None] = None
    fixedPurchaseQuantity: Union[str, None] = None
    internalNote: Union[str, None] = None
    manufacturerPartNumber: Union[str, None] = None
    matchCode: Union[str, None] = None
    minimumPurchaseQuantity: Union[str, None] = None
    name: Union[str, None] = None
    shortDescription1: Union[str, None] = None
    shortDescription2: Union[str, None] = None
    taxRateType: Union[str, None] = None
    unitId: Union[str, None] = None
    accountId: Union[str, None] = None
    accountingCodeId: Union[str, None] = None
    active: Union[bool, None] = None
    applyCashDiscount: Union[bool, None] = None
    articleAlternativeQuantities: List[ArticleAlternativeQuantities] = []
    articleCalculationPrices: List[ArticleCalculationPrices] = []
    articleCategoryId: Union[str, None] = None
    articleGrossWeight: Union[str, None] = None
    articleHeight: Union[str, None] = None
    articleImages: List[ArticleImages] = []
    articleLength: Union[str, None] = None
    articleNetWeight: Union[str, None] = None
    articlePrices: List[ArticlePrices] = []
    articleType: Union[str, None] = None
    articleWidth: Union[str, None] = None
    availableForSalesChannels: list = []
    availableInSale: Union[bool, None] = None
    averageDeliveryTime: Union[int, None] = None
    barcode: Union[str, None] = None
    batchNumberRequired: Union[bool, None] = None
    billOfMaterialPartDeliveryPossible: Union[bool, None] = None
    catalogCode: Union[str, None] = None
    commissionRate: Union[str, None] = None
    contractBillingCycle: Union[str, None] = None
    contractBillingMode: Union[str, None] = None
    countryOfOriginCode: Union[str, None] = None
    customerArticleNumbers: List[CustomerArticleNumbers] = []
    customsDescription: Union[str, None] = None
    customsTariffNumberId: Union[str, None] = None
    defaultLoadingEquipmentIdentifierId: Union[str, None] = None
    defaultPriceCalculationType: Union[str, None] = None
    defaultStoragePlaces: List[DefaultStoragePlaces] = []
    defineIndividualTaskTemplates: Union[bool, None] = None
    expenseAccountId: Union[str, None] = None
    expirationDays: Union[int, None] = None
    invoicingType: Union[str, None] = None
    launchDate: Union[int, None] = None
    loadingEquipmentArticleId: Union[str, None] = None
    longText: Union[str, None] = None
    lowLevelCode: Union[int, None] = None
    manufacturerId: Union[str, None] = None
    marginCalculationPriceType: Union[str, None] = None
    minimumStockQuantity: Union[str, None] = None
    packagingQuantity: Union[int, None] = None
    packagingUnitBaseArticleId: Union[str, None] = None
    packagingUnitParentArticleId: Union[str, None] = None
    plannedWorkingTimePerUnit: Union[int, None] = None
    primarySupplySourceId: Union[str, None] = None
    procurementLeadDays: Union[int, None] = None
    producerType: Union[str, None] = None
    productionArticle: Union[bool, None] = None
    productionBillOfMaterialItems: List[ProductionBillOfMaterialItems] = []
    productionConfigurationRule: Union[str, None] = None
    purchaseCostCenterId: Union[str, None] = None
    quantityConversions: List[QuantityConversions] = []
    ratingId: Union[str, None] = None
    recordItemGroupName: Union[str, None] = None
    safetyStockDays: Union[int, None] = None
    salesBillOfMaterialItems: List[SalesBillOfMaterialItems] = []
    salesCostCenterId: Union[str, None] = None
    sellByDate: Union[int, None] = None
    sellFromDate: Union[int, None] = None
    serialNumberRequired: Union[bool, None] = None
    serviceArticleForServiceQuotaBookingId: Union[str, None] = None
    serviceQuotaQuantity: Union[str, None] = None
    showOnDeliveryNote: Union[bool, None] = None
    statusId: Union[str, None] = None
    supplySources: List[SupplySources] = []
    supportUntilDate: Union[int, None] = None
    systemCode: Union[str, None] = None
    tags: list = []
    targetStockQuantity: Union[str, None] = None
    useAvailableForSalesChannels: Union[bool, None] = None
    useSalesBillOfMaterialItemPrices: Union[bool, None] = None
    useSalesBillOfMaterialItemPricesForPurchase: Union[bool, None] = None
    useSalesBillOfMaterialSubitemCosts: Union[bool, None] = None

    excluded_keys: Set[str] = {
        "lowLevelCode"
    }
