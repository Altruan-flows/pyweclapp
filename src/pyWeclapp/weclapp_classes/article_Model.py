"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class ArticleCalculationPrices(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    articleCalculationPriceType: Union[str, None] = None
    createdDate: Union[int, None]
    endDate: Union[int, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    price: Union[str, None] = None
    salesChannel: Union[str, None] = None  # Type estimated
    startDate: Union[int, None] = None


class SalesBillOfMaterialItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    createdDate: Union[int, None]
    lastModifiedDate: Union[int, None]
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None


class Article(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    accountId: Union[str, None] = None  # Type estimated
    accountingCodeId: Union[str, None] = None  # Type estimated
    active: Union[bool, None]
    applyCashDiscount: Union[bool, None] = None
    articleAlternativeQuantities: list = []
    articleCalculationPrices: List[ArticleCalculationPrices] = []
    articleCategoryId: Union[str, None] = None
    articleGrossWeight: Union[str, None] = None  # Type estimated
    articleHeight: Union[str, None] = None  # Type estimated
    articleImages: list = []
    articleLength: Union[str, None] = None  # Type estimated
    articleNetWeight: Union[str, None] = None  # Type estimated
    articleNumber: Union[str, None] = None
    articlePrices: list = []
    articleType: Union[str, None]
    articleWidth: Union[str, None] = None  # Type estimated
    availableForSalesChannels: list = []
    availableInSale: Union[bool, None] = None
    averageDeliveryTime: Union[str, None] = None  # Type estimated
    barcode: Union[str, None] = None  # Type estimated
    batchNumberRequired: Union[bool, None] = None
    billOfMaterialPartDeliveryPossible: Union[bool, None] = None
    catalogCode: Union[str, None] = None  # Type estimated
    commissionRate: Union[str, None] = None
    contractBillingCycle: Union[str, None] = None  # Type estimated
    contractBillingMode: Union[str, None] = None  # Type estimated
    countryOfOriginCode: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    customerArticleNumbers: list = []
    customsDescription: Union[str, None] = None  # Type estimated
    customsTariffNumberId: Union[str, None] = None  # Type estimated
    defaultLoadingEquipmentIdentifierId: Union[str, None] = None  # Type estimated
    defaultPriceCalculationType: Union[str, None] = None
    defaultStoragePlaces: list = []
    defineIndividualTaskTemplates: Union[bool, None] = None
    description: Union[str, None] = None
    ean: Union[str, None] = None  # Type estimated
    expenseAccountId: Union[str, None] = None  # Type estimated
    expirationDays: Union[str, None] = None  # Type estimated
    fixedPurchaseQuantity: Union[str, None] = None  # Type estimated
    internalNote: Union[str, None] = None  # Type estimated
    invoicingType: Union[str, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    launchDate: Union[int, None] = None  # Type estimated
    loadingEquipmentArticleId: Union[str, None] = None  # Type estimated
    longText: Union[str, None] = None  # Type estimated
    lowLevelCode: Union[int, None] = None
    manufacturerId: Union[str, None] = None
    manufacturerPartNumber: Union[str, None] = None  # Type estimated
    marginCalculationPriceType: Union[str, None] = None
    matchCode: Union[str, None] = None  # Type estimated
    minimumPurchaseQuantity: Union[str, None] = None  # Type estimated
    minimumStockQuantity: Union[str, None] = None  # Type estimated
    name: Union[str, None] = None
    packagingQuantity: Union[str, None] = None  # Type estimated
    packagingUnitBaseArticleId: Union[str, None] = None
    packagingUnitParentArticleId: Union[str, None] = None  # Type estimated
    plannedWorkingTimePerUnit: Union[str, None] = None  # Type estimated
    primarySupplySourceId: Union[str, None] = None  # Type estimated
    procurementLeadDays: Union[str, None] = None  # Type estimated
    producerType: Union[str, None] = None  # Type estimated
    productionArticle: Union[bool, None] = None
    productionBillOfMaterialItems: list = []
    productionConfigurationRule: Union[str, None] = None
    purchaseCostCenterId: Union[str, None] = None  # Type estimated
    quantityConversions: list = []
    ratingId: Union[str, None] = None  # Type estimated
    recordItemGroupName: Union[str, None] = None  # Type estimated
    safetyStockDays: Union[str, None] = None  # Type estimated
    salesBillOfMaterialItems: List[SalesBillOfMaterialItems] = []
    salesCostCenterId: Union[str, None] = None  # Type estimated
    sellByDate: Union[int, None] = None  # Type estimated
    sellFromDate: Union[int, None] = None  # Type estimated
    serialNumberRequired: Union[bool, None] = None
    serviceArticleForServiceQuotaBookingId: Union[str, None] = None  # Type estimated
    serviceQuotaQuantity: Union[str, None] = None  # Type estimated
    shortDescription1: Union[str, None] = None
    shortDescription2: Union[str, None] = None  # Type estimated
    showOnDeliveryNote: Union[bool, None] = None
    statusId: Union[str, None] = None  # Type estimated
    supplySources: list = []
    supportUntilDate: Union[int, None] = None  # Type estimated
    systemCode: Union[str, None] = None  # Type estimated
    tags: list = []
    targetStockQuantity: Union[str, None] = None  # Type estimated
    taxRateType: Union[str, None] = None
    unitId: Union[str, None] = None
    useAvailableForSalesChannels: Union[bool, None] = None
    useSalesBillOfMaterialItemPrices: Union[bool, None] = None
    useSalesBillOfMaterialItemPricesForPurchase: Union[bool, None] = None
    useSalesBillOfMaterialSubitemCosts: Union[bool, None] = None
