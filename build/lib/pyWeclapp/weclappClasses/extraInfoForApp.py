from pydantic import BaseModel
from .. import weclapp

class ExtraInfoForApp(BaseModel):
    confirmedOrderedQuantity: str = None
    consignmentStockQuantity: str = None
    currentYearRevenue: str = None
    currentYearSalesOrderVolume: str = None
    inventoryValuationAtAvgArticlePrice: str = None
    lastYearRevenue: str = None
    lastYearSalesOrderVolume: str = None
    openQuantityInShipments: str = None
    openShipmentQuantity: str = None
    orderedQuantity: str = None
    plannedSalesQuantity: str = None
    purchasePrice: str = None
    purchasePriceCurrencyId: str = None
    reservedStockQuantity: str = None
    salesPrice: str = None
    salesPriceCurrencyId: str = None
    stockQuantity: str = None
    stockQuantityWithoutOrder: str = None
    stockQuantityWithoutOrderToDate: str = None
    stockValuationPrice: str = None
    supplierStockQuantity: str = None
    unconfirmedOrderedQuantity: str = None
    unreservedStockQuantity: str = None
    

    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)

    @classmethod
    def fromWeclapp(cls, articleId):
        response = weclapp.GET(f"article/id/{articleId}/extraInfoForApp")
        return cls(**response)