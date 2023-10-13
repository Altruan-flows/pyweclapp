from pydantic import BaseModel
from pyWeclapp import weclapp
from ..import Article

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
    
    
    @classmethod
    def fromArticle(cls, article:Article):
        if len(article.salesBillOfMaterialItems) > 0:
            mapper = {}
            extraInfos = []
            for item in article.salesBillOfMaterialItems:
                mapper[item.articleId] = item.quantity
                extraInfos.append(cls.fromWeclapp(item.articleId))
            
            if len(extraInfos) > 0:
                data = cls()
                for extraInfo in extraInfos:
                    for key, value in extraInfo.dict().items():
                        if value is not None:
                            if getattr(data, key) is None:
                                setattr(data, key, float(value) * float(mapper[extraInfo.id]))
                            else:
                                setattr(data, key, float(getattr(data, key)) + float(value) * float(mapper[extraInfo.id]))
                return data
            else:
                return cls.fromWeclapp(article.id)
        else:
            return cls.fromWeclapp(article.id)