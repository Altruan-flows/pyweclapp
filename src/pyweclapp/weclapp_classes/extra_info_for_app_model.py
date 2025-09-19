"""Model for extraInfoForApp endpoint that provides stock and sales information
for articles."""

from pydantic import BaseModel
from ..weclapp import Weclapp


class ExtraInfoForApp(BaseModel):
    """Model for article/id/{articleId}/extraInfoForApp endpoint."""
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
    def from_weclapp(cls, article_id: str):
        """Fetch extra info for an article from Weclapp."""
        response = Weclapp(api_version="v1").get(f"article/id/{article_id}/extraInfoForApp")
        return cls(**response)
