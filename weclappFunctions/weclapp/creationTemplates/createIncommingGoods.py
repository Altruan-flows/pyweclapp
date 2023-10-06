import logging
from util import weclapp
from .bluePrints import CreationBluePrint

class IncommingGoodsCreator(CreationBluePrint):
    
    def __init__(self, senderPartyId, deliveryNoteNumber:str=None, recipientAddress:dict=None, salesOrderId:str=None, shipmentId:str=None) -> None:
        self.senderPartyId = senderPartyId
        self.deliveryNoteNumber = deliveryNoteNumber
        self.recipientAddress = recipientAddress
        self.incomingGoodsItems = []
        self.customAttributes = []
        if salesOrderId is not None:
            self.addCAtt("21200651", str(salesOrderId), "entityId")
        if shipmentId is not None:
            self.addCAtt("21200378", str(salesOrderId), "entityId")
    
    def addItem(self, articleId:str, quantity:str):
        incomingGoodsItem = {"manualQuantity": True}
        incomingGoodsItem["quantity"] = str(int(float(quantity)))
        incomingGoodsItem["articleId"] = str(articleId)
        self.incomingGoodsItems.append(incomingGoodsItem)
        
        
    def createIncommingGoods(self):

            # create Body
            try:
                # incommingGoodsTemplate = {
                #     "incomingGoodsItems": [],
                #     "incomingGoodsType": "STANDARD",
                #     "senderPartyId": "15687422",
                #     # "status": "INCOMING_MOVED_INTO_STORE",
                #     "deliveryNoteNumber": self.toProcess.shipmentNumber,
                #     "customAttributes": [
                #         {
                #             "attributeDefinitionId": "21200378",    # ad.incomingGoodsShipmentReference
                #             "entityId": self.toProcess.id
                #         },
                #         {
                #             "attributeDefinitionId": "21200651",    # ad.incomingGoodsSalesOrderReference
                #             "entityId": self.toProcess.salesOrderId
                #         }
                #     ],
                #     "recipientAddress": self.toProcess.recipientAddress
                # }
                # Append Positions
                # for item in self.toProcess.shipmentItems:
                #     # Keine Unterpositionen und nicht kassenleistung
                #     if not item.parentItemId and item.articleId != self.ad.kassenleistungsArtikelId:
                #         incomingGoodsItem = {"manualQuantity": True}
                #         incomingGoodsItem["quantity"] = str(int(float(item.quantity)))
                #         incomingGoodsItem["articleId"] = str(item.articleId)
                #         incommingGoodsTemplate["incomingGoodsItems"].append(incomingGoodsItem)
                
                incommingGoodsTemplate = self.to_dict()
                logging.info(f"Posting new Incomming Goods: -> {incommingGoodsTemplate}")
                incommingGood = weclapp.POST(entityName="incomingGoods", body=incommingGoodsTemplate)
                incommingID = incommingGood.get('id')
                try:
                    incommingGood = weclapp.PUT(entityName="incomingGoods", entityId=incommingID, body={"status": "INCOMING_MOVED_INTO_STORE"})
                except weclapp.WeclappError as we:
                    for message in we.messages:
                        if "Batch number is missing for booking records of item" in message.get("message", ""):
                            position = int(str(message.get("message", ""))[-3:].replace(" ", ""))
                            item = incommingGood.get("incomingGoodsItems", [])[position -1]
                            articlePrice = weclapp.GET('article', f'{item["articleId"]}/extraInfoForApp').get("stockValuationPrice", "1.0")
                            body = {
                                "incomingBookings": [
                                    {
                                        "incomingGoodsItemId": item["id"],
                                        "batchNumber": "alreadySent",
                                        "articleValuationPrice": articlePrice,
                                        "quantity": item.get("quantity", "1"),
                                        "levelId": 3702     # Hauptlager
                                    }
                                ]
                            }
                            weclapp.POST(entityName="incomingGoods", entityId=f"{incommingID}/updateIncomingBookings", body=body )
                    incommingGood = weclapp.PUT(entityName="incomingGoods", entityId=incommingID, body={"status": "INCOMING_MOVED_INTO_STORE"})
            except Exception as e:
                raise e
