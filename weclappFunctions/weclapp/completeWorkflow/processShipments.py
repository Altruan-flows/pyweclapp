from util import weclappClasses, weclapp, attDefManager
from typing import *
from collections import defaultdict
import logging, time



class ShipementProcessing:
    def __init__(self, salesOrder:weclappClasses.SalesOrder,
                 apiKey:Literal["Johannes", "Jakob"]= "Jakob", 
                 ad:attDefManager.attDef=attDefManager.attDef(),
                 maxRetries:int=0,
                 retriesStatus:List[int] = [500, 502, 503, 504, 409]):
        self.salesOrder = salesOrder
        self.ad = ad
        self.maxRetries = maxRetries
        self.retriesStatus = retriesStatus
        self.apiKey = apiKey
        
        
    def createShipment(self) -> Union[weclappClasses.Shipment, None]:
        assert self.salesOrder.status == "ORDER_CONFIRMATION_PRINTED", f"please confirm order before trying to create a Shipment"
        self.shipments:List[weclappClasses.Shipment] = []

        items = defaultdict(lambda:0)
        for shipment in weclapp.GET(entityName='shipment', query={"salesOrderId-eq": self.salesOrder.id}, apiKey=self.apiKey, asType=list):  
            shipmentClass = weclappClasses.Shipment(**shipment)
            if shipmentClass.status != "CANCELLED":
                for item in shipmentClass.shipmentItems:
                    items[item.salesOrderItemId] += int(item.quantity)
                self.shipments.append(shipmentClass)
        
        if not all([int(oItem.quantity) == items[oItem.id] for oItem in self.salesOrder.orderItems]) and not "NEW" in [ship.status for ship in self.shipments]:
            shipment = weclapp.POST(entityName="salesOrder", 
                                            entityId=f"{self.salesOrder.id}/createShipment", 
                                            body={}, 
                                            apiKey=self.apiKey, 
                                            maxRetries=self.maxRetries,
                                            retriesStatus=self.retriesStatus)
            shipmentClass = weclappClasses.Shipment(**shipment)
            self.shipments.append(shipmentClass)
            self.salesOrder.incrementVersion()
            logging.info(f"   Compleetworkflow: Shipment {shipmentClass.id} created.")
            time.sleep(0.4)
            return shipmentClass
        logging.info("   Compleetworkflow: No new shipments created")
        return None

            
            
    def confirmShipment(self):
        assert hasattr(self, "shipments"), f"Please Create Shipments before confirming"
        assert isinstance(self.shipments, list), f"Please Create Shipments before confirming"
        assert all([isinstance(shipment, weclappClasses.Shipment) for shipment in self.shipments]), f"All items must be weclappClasses.Shipment"
        for shipment in self.shipments:
            if shipment.status == "NEW":
                body ={
                    "status": "DELIVERY_NOTE_PRINTED"
                }
                if self.apiKey == 'Johannes':
                    body["customAttributes"] = [{
                        "attributeDefinitionId": self.ad.rueckstellungsDatum,
                        "dateValue": self.salesOrder.orderDate
                    }]
                ship = weclapp.PUT(entityName='shipment', 
                                   entityId=shipment.id, 
                                   apiKey=self.apiKey, 
                                   body=body, 
                                   ignore=True, 
                                    maxRetries=self.maxRetries,
                                    retriesStatus=self.retriesStatus)
                # shipments_New.append(weclappClasses.Shipment(**ship))
                shipment.updateEntityFromNewEntity(newEntity=ship)
        logging.info(f"   Compleetworkflow: All New Shipments confirmed")

