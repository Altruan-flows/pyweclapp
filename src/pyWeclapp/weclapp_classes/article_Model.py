"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class AttributeOptions(Blueprint):
    """Subclass for attribute options in Variants."""

    id: Union[str, None] = None


class Variants(Blueprint):
    """Subclass for variants in VariantArticle."""

    id: Union[str, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    attributeOptions: List[AttributeOptions] = []
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    positionNumber: Union[int, None] = None


class VariantArticle(Blueprint):
    """Class for variantArticle endpoint."""

    id: Union[str, None] = None
    version: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    primaryArticleId: Union[str, None] = None
    primaryArticleNumber: Union[str, None] = None
    variantArticleName: Union[str, None] = None
    variantArticleNumber: Union[str, None] = None
    variants: List[Variants] = []


class ArticleAlternativeQuantities(Blueprint):
    """Subclass for articleAlternativeQuantities in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    minimumOrderQuantity: Union[str, None] = None
    minimumStockQuantity: Union[str, None] = None
    targetStockQuantity: Union[str, None] = None
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None


class ArticleCalculationPrices(Blueprint):
    """Subclass for articleCalculationPrices in Article."""

    id: Union[str, None]
    version: Union[str, None] = None
    articleCalculationPriceType: Union[str, None] = None
    createdDate: Union[int, None]
    endDate: Union[int, None] = None
    lastModifiedDate: Union[int, None]
    price: Union[str, None] = None
    salesChannel: Union[str, None] = None
    startDate: Union[int, None] = None


class ArticleImages(Blueprint):
    """Subclass for articleImages in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    fileName: Union[str, None] = None
    mainImage: Union[bool, None] = None


class ReductionAdditions(Blueprint):
    """Subclass for reductionAdditions of ArticlePrices."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    name: Union[str, None] = None
    type: Union[str, None] = None
    value: Union[str, None] = None


class ArticlePrices(Blueprint):
    """Subclass for articlePrices in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    currencyId: Union[str, None] = None
    currencyName: Union[str, None] = None
    customerId: Union[str, None] = None
    description: Union[str, None] = None
    endDate: Union[int, None] = None
    lastModifiedByUserId: Union[str, None] = None
    positionNumber: Union[int, None] = None
    price: Union[str, None] = None
    priceScaleType: Union[str, None] = None
    priceScaleValue: Union[str, None] = None
    reductionAdditions: List[ReductionAdditions] = []
    startDate: Union[int, None] = None
    salesChannel: Union[str, None] = None


class CustomerArticleNumbers(Blueprint):
    """Subclass for customerArticleNumbers in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customerArticleNumber: Union[str, None] = None
    customerId: Union[str, None] = None


class DefaultStoragePlaces(Blueprint):
    """Subclass for defaultStoragePlaces in Article."""

    id: Union[str, None] = None


class PriceCalculationParameters(Blueprint):
    """Subclass for priceCalculationParameters in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    fixSurcharge: Union[str, None] = None
    fromScale: Union[str, None] = None
    lowerPurchasePriceBound: Union[str, None] = None
    margin: Union[str, None] = None
    percentSurcharge: Union[str, None] = None
    profit: Union[str, None] = None
    salesChannel: Union[str, None] = None


class ProductionBillOfMaterialItems(Blueprint):
    """Subclass for productionBillOfMaterialItems in Article."""

    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    positionNumber: Union[int, None] = None
    quantity: Union[str, None] = None


class QuantityConversions(Blueprint):
    """Subclass for quantityConversions in Article."""

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
    """Subclass for salesBillOfMaterialItems in Article."""

    id: Union[str, None] = None
    version: Union[str, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    createdDate: Union[int, None]
    lastModifiedDate: Union[int, None]
    positionNumber: Union[int, None]
    quantity: Union[str, None] = None


class Article(Blueprint):
    """Class for article endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    accountId: Union[str, None] = None
    accountNumber: Union[str, None] = None
    accountingCodeId: Union[str, None] = None
    active: Union[bool, None]
    applyCashDiscount: Union[bool, None] = None
    articleAlternativeQuantities: List[ArticleAlternativeQuantities] = []
    articleCalculationPrices: List[ArticleCalculationPrices] = []
    articleCategoryId: Union[str, None] = None
    articleGrossWeight: Union[str, None] = None
    articleHeight: Union[str, None] = None
    articleImages: List[ArticleImages] = []
    articleLength: Union[str, None] = None
    articleNetWeight: Union[str, None] = None
    articleNumber: Union[str, None] = None
    articlePrices: List[ArticlePrices] = []
    articleType: Union[str, None]
    articleWidth: Union[str, None] = None
    availableForSalesChannels: List[str] = []
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
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    customerArticleNumbers: List[CustomerArticleNumbers] = []
    customsDescription: Union[str, None] = None
    customsTariffNumber: Union[str, None] = None
    customsTariffNumberId: Union[str, None] = None
    defaultLoadingEquipmentIdentifierId: Union[str, None] = None
    defaultPriceCalculationType: Union[str, None] = None
    defaultStoragePlaces: List[DefaultStoragePlaces] = []
    defineIndividualTaskTemplates: Union[bool, None] = None
    description: Union[str, None] = None
    ean: Union[str, None] = None
    expenseAccountId: Union[str, None] = None
    expenseAccountNumber: Union[str, None] = None
    expirationDays: Union[int, None] = None
    fixedPurchaseQuantity: Union[str, None] = None
    internalNote: Union[str, None] = None
    invoicingType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    launchDate: Union[int, None] = None
    loadingEquipmentArticleId: Union[str, None] = None
    longText: Union[str, None] = None
    lowLevelCode: Union[int, None] = None
    manufacturerId: Union[str, None] = None
    manufacturerName: Union[str, None] = None
    manufacturerPartNumber: Union[str, None] = None
    marginCalculationPriceType: Union[str, None] = None
    matchCode: Union[str, None] = None
    minimumPurchaseQuantity: Union[str, None] = None
    minimumStockQuantity: Union[str, None] = None
    name: Union[str, None] = None
    packagingQuantity: Union[int, None] = None
    packagingUnitBaseArticleId: Union[str, None] = None
    packagingUnitParentArticleId: Union[str, None] = None
    plannedWorkingTimePerUnit: Union[int, None] = None
    priceCalculationParameters: List[PriceCalculationParameters] = []
    primarySupplySourceId: Union[str, None] = None
    procurementLeadDays: Union[int, None] = None
    producerType: Union[str, None] = None
    productionArticle: Union[bool, None] = None
    productionBillOfMaterialItems: List[ProductionBillOfMaterialItems] = []
    productionConfigurationRule: Union[str, None] = None
    purchaseCostCenterId: Union[str, None] = None
    purchaseCostCenterNumber: Union[str, None] = None
    quantityConversions: List[QuantityConversions] = []
    ratingId: Union[str, None] = None
    ratingName: Union[str, None] = None
    recordItemGroupName: Union[str, None] = None
    safetyStockDays: Union[int, None] = None
    salesBillOfMaterialItems: List[SalesBillOfMaterialItems] = []
    salesCostCenterId: Union[str, None] = None
    salesCostCenterNumber: Union[str, None] = None
    sellByDate: Union[int, None] = None
    sellFromDate: Union[int, None] = None
    serialNumberRequired: Union[bool, None] = None
    serviceArticleForServiceQuotaBookingId: Union[str, None] = None
    serviceQuotaQuantity: Union[str, None] = None
    shortDescription1: Union[str, None] = None
    shortDescription2: Union[str, None] = None
    showOnDeliveryNote: Union[bool, None] = None
    statusId: Union[str, None] = None
    supplySources: list = []
    supportUntilDate: Union[int, None] = None
    systemCode: Union[str, None] = None
    tags: list = []
    targetStockQuantity: Union[str, None] = None
    taxRateType: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None
    useAvailableForSalesChannels: Union[bool, None] = None
    useSalesBillOfMaterialItemPrices: Union[bool, None] = None
    useSalesBillOfMaterialItemPricesForPurchase: Union[bool, None] = None
    useSalesBillOfMaterialSubitemCosts: Union[bool, None] = None
