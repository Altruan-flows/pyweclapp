from typing import *
from util import weclappClasses, weclapp
import logging

from .bluePrints import CreationBluePrint

class ArticlePriceCreator(CreationBluePrint):
    def __init__(self, price,  salesChannel, priceScaleType:Literal["SCALE_FROM", "SCALE_TO"], priceScaleValue:Union[str, int, float], startDate=None, endDate=None, description=None, currencyId:str=255):
        self.currencyId = currencyId
        self.price = price
        self.priceScaleType = priceScaleType
        self.priceScaleValue = str(int(float(priceScaleValue)))
        self.reductionAdditions = []
        self.salesChannel = salesChannel
        self.description = description
        self.startDate = startDate
        self.endDate = endDate

    def add_reduction(self, reduction_type:Literal["REDUCTION_ABS", "REDUCTION_PERCENT", "ADDITION_PERCENT", "ADDITIONAL_ABS"], reduction_value, name:str=None):
        assert reduction_type in ["REDUCTION_ABS", "REDUCTION_PERCENT", "ADDITION_PERCENT", "ADDITIONAL_ABS"], f"{reduction_type=} is invalid"
        reduction = {
            "type": reduction_type,
            "value": reduction_value
        }
        if name:
            reduction["name"] = str(name)
        self.reductionAdditions.append(reduction)

    
    
    

    
class ArticleCreator(CreationBluePrint):
    @classmethod
    def fromExistingArticle(cls, article:weclappClasses.Article, articleType:Literal["SALES_BILL_OF_MATERIAL", "STORABLE", "BASIC"], name:str):
        """Creates a updateDict based on a existing article -> all list items are excluded!!!

        Args:
            article (weclappClasses.Article): Template Article
            articleType: Target Article Type
            name (str): neue Name

        Returns:
            _type_: ArticleCreator class
        """
        assert isinstance(article, weclappClasses.Article), f"Provided article must be weclappclass to ensure correctness"
        articleDict = article.getUpdateDict(updateType="full")
        creator = cls(articleType=articleType, name=name)
        blackList = ["id", "version", "createdDate", "lastModifiedDate", "positionNumber", "articleType", "name", 
                     "articlePrices", "customAttributes", "salesBillOfMaterialItems", "articleCalculationPrices",
                     "articleAlternativeQuantities", "supplySources", "tags", "articleImages", "availableForSalesChannels",
                     "customerArticleNumbers",
                     "ean", "manufacturerPartNumber", "priceCalculationParameters"]
        # logging.warning(articleDict)
        for key, value in articleDict.items():
            if key not in blackList:
                setattr(creator, key, value)
                logging.info(f"Adding {key} x {value} from motherarticle")
        
        return creator
                
            
        
    def __init__(self, articleType:Literal["SALES_BILL_OF_MATERIAL", "STORABLE", "BASIC"], name:str, 
                 ean:str=None, articleNumber:str=None, articleCategoryId:str="1971350", unitId:str="3001", 
                 description:str=None, shortDescription1:str=None, mpn:str=None):
        self.name:str = str(name)
        self.articleType:str = str(articleType)
        self.articleNumber = articleNumber
        self.articleCategoryId = articleCategoryId  # A-Hygiene
        self.unitId:str = str(unitId)       # Stück
        self.ean = ean
        self.manufacturerPartNumber = mpn
        self.description:str= description
        self.shortDescription1 = shortDescription1
        self.articlePrices = []
        self.customAttributes = []
        self.salesBillOfMaterialItems = []
        self.articleCalculationPrices = []
        self.articleAlternativeQuantities = []
        self.defaults()
        
    def defaults(self):
        self.active = True
        self.productionArticle = False
        self.batchNumberRequired = None
        self.marginCalculationPriceType = None

    def addSalesBillOfMaterialItems(self, quantity, articleId):
        self.salesBillOfMaterialItems.append(
            {
                "articleId": str(articleId),
                "quantity": str(int(float(quantity)))
            }
        )
        
    def addArticleCalculationPrice(self, price, priceType:Literal["CALCULATION_PRICE", "RECOMMENDED_RETAIL_PRICE"]= "CALCULATION_PRICE"):
        self.articleCalculationPrices.append(
            {
                "articleCalculationPriceType": priceType,
                "price": str(float(price))
            }
        )
    
    def addArticlePriceClass(self, articlePriceCreator:ArticlePriceCreator):
        assert isinstance(articlePriceCreator, ArticlePriceCreator), f"articlePriceCreator is not ArticlePriceCreator class "
        self.articlePrices.append(articlePriceCreator.to_dict())
    
    def addArticlePrice(self, price,  salesChannel, 
                         priceScaleType:Literal["SCALE_FROM", "SCALE_TO"], priceScaleValue:Union[str, int, float], 
                         startDate=None, endDate=None, description=None, currencyId:str=255, reductions:List[dict]=[]):
        aPrice = ArticlePriceCreator(price=price, salesChannel=salesChannel, priceScaleType=priceScaleType, priceScaleValue=priceScaleValue,
                                     startDate=startDate, endDate=endDate, description=description, currencyId=currencyId)
        if reductions:
            for reduction in reductions:
                assert isinstance(reduction, dict), f"reduction needs to be dict"
                aPrice.add_reduction(reduction.get("reduction_type"), reduction.get("reduction_value"))
        self.articlePrices.append(aPrice.to_dict())
    

    def createArticle(self) -> weclappClasses.Article:
        logging.info(f"try to create new Article")
        # Validattions
        if self.articleType == "STORABLE":
            logging.info(f"Validating ArticleType {self.articleType}: ...")
            for critticlalKey in ["useSalesBillOfMaterialItemPricesForPurchase", "billOfMaterialPartDeliveryPossible"]:
                if hasattr(self, critticlalKey):
                    logging.warning(f"{critticlalKey} is not allowed for {self.articleType} -> excluding")
                    setattr(self, critticlalKey, None)
                    
            if len(self.salesBillOfMaterialItems) > 0:
                logging.warning(f"salesBillOfMaterialItems is not alllowed for {self.articleType} -> resetting")
                self.salesBillOfMaterialItems = []
                
        elif self.articleType == "SALES_BILL_OF_MATERIAL":
            logging.info(f"Validating ArticleType {self.articleType}: ...")
            # Not allowed for storable SalesBill articles:
            for critticlalKey in ["safetyStockDays", "procurementLeadDays", "minimumStockQuantity", "targetStockQuantity", 
                                   "averageDeliveryTime", "minimumPurchaseQuantity", "fixedPurchaseQuantity", 
                                   "ratingId", "ratingName"]:
                if hasattr(self, critticlalKey):
                    logging.warning(f"{critticlalKey} is not allowed for {self.articleType} -> excluding")
                    setattr(self, critticlalKey, None)
                
            if len(self.articleAlternativeQuantities) > 0:
                logging.warning(f"articleAlternativeQuantities is not alllowed for {self.articleType} -> resetting")
                self.articleAlternativeQuantities = []
            
            # set defauts
            self.marginCalculationPriceType = "ARTICLE_CALCULATION_PRICE"

            if not self.articleCalculationPrices:
                self.addArticleCalculationPrice(price=0, priceType="CALCULATION_PRICE")
            
        body = self.to_dict()
        print(body)
        # return body
        newArticle = weclapp.POST(entityName="article", body=body)
        return weclappClasses.Article(**newArticle)
