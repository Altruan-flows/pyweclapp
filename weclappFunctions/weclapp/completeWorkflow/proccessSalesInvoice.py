from util import weclappClasses, weclapp, attDefManager
from typing import *
import time
import logging
from .processShipments import ShipementProcessing


class SalesInvoiceProcessing(ShipementProcessing):
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
        self.shipmentId = None
        ShipementProcessing.__init__(self, salesOrder=self.salesOrder ,apiKey=self.apiKey, ad=self.ad, retriesStatus=self.retriesStatus, maxRetries=self.maxRetries)
        
        
        
    def createInvoice(self):
        self.invoices:List[weclappClasses.SalesInvoice] = []
        items = 0
        for inv in weclapp.GET(entityName="salesInvoice", query={"salesOrders.id-eq": self.salesOrder.id}, apiKey=self.apiKey, asType=list):  
            invoice = weclappClasses.SalesInvoice(**inv)
            if invoice.status not in ["VOID", "CANCELLED"]:
                for item in invoice.salesInvoiceItems:
                    items += int(item.quantity)
            self.invoices.append(invoice)
        
        if sum([int(oItem.quantity) for oItem in self.salesOrder.orderItems]) != items and not "NEW" in [inv.status for inv in self.invoices]:
            assert all([shipment.status in ["DELIVERY_NOTE_PRINTED", "SHIPPED"] for shipment in self.shipments]), f"Please confirm shipments before creating invoices"
            invoice = weclapp.POST(entityName="salesOrder", 
                                           entityId=f"{self.salesOrder.id}/createSalesInvoice", 
                                           apiKey=self.apiKey, 
                                           maxRetries=self.maxRetries,
                                           retriesStatus=self.retriesStatus)
            invoiceClass = weclappClasses.SalesInvoice(**invoice)
            self.invoices.append(invoiceClass)
            logging.info(f"   Compleetworkflow: Invoice {invoiceClass.id} created.")
            time.sleep(0.4)
            return invoiceClass
        logging.info(f"   Compleetworkflow: Invoice already exists")
        return None

    def createInvoiceFromShipment(self):
        assert self.shipmentId is not None, f"Please set ShipmentId before creating invoices"
        self.invoices:List[weclappClasses.SalesInvoice] = []
        items = 0
        for inv in weclapp.GET(entityName="salesInvoice", query={"salesOrders.id-eq": self.salesOrder.id}, apiKey=self.apiKey, asType=list):  
            invoice = weclappClasses.SalesInvoice(**inv)
            if invoice.status != "VOID":
                for item in invoice.salesInvoiceItems:
                    items += int(item.quantity)
            self.invoices.append(invoice)
        
        if sum([int(oItem.quantity) for oItem in self.salesOrder.orderItems]) != items and not "NEW" in [inv.status for inv in self.invoices]:
            # assert all([shipment.status in ["DELIVERY_NOTE_PRINTED", "SHIPPED"] for shipment in self.shipments]), f"Please confirm shipments before creating invoices"
            invoice = weclapp.POST(entityName="shipment", 
                                           entityId=f"{self.shipmentId}/createSalesInvoice", 
                                           apiKey=self.apiKey, 
                                           maxRetries=self.maxRetries,
                                           retriesStatus=self.retriesStatus)
            invoiceClass = weclappClasses.SalesInvoice(**invoice)
            self.invoices.append(invoiceClass)
            logging.info(f"   Compleetworkflow: Invoice {invoiceClass.id} created from shipment.")
            time.sleep(0.4)
            return invoiceClass
        logging.info(f"   Compleetworkflow: Invoice already exists")
        return None

        
    def confirmInvoice(self):
        assert hasattr(self, 'invoices'), f"Please Create Invoices before confirming"
        assert isinstance(self.invoices, list), f"Please Create Invoices before confirming"
        assert all([isinstance(invoice, weclappClasses.SalesInvoice) for invoice in self.invoices]), f"All items must be SalesInvoices"
        
        for invoice in self.invoices:
            if invoice.status == "NEW":
                inv = weclapp.PUT(entityName='salesInvoice', entityId=invoice.id, apiKey=self.apiKey,
                        body = {
                                "status": "DOCUMENT_CREATED"
                                }, ignore=True, 
                        maxRetries=self.maxRetries,
                        retriesStatus=self.retriesStatus)
                invoice.updateEntityFromNewEntity(newEntity=inv)
        logging.info(f"   Compleetworkflow: All new Invoices confirmed.")

    
    
    
    def createOpenItems(self):
        time.sleep(0.5)   # Should target: - ERROR=Invoice document could not be created because the invoice items have not yet been delivered/recorded. A delivery with minimum status "Delivery note created" or a performance record with minimum status "Performance record document created" 
        assert hasattr(self, 'invoices'), f"Please Create Invoices before confirming"
        assert isinstance(self.invoices, list), f"Please Create Invoices before confirming"
        assert all([isinstance(invoice, weclappClasses.SalesInvoice) for invoice in self.invoices]), f"All items must be SalesInvoices"
        logging.info("Compleetworkflow: Creating open Items...")
        for invoice in self.invoices:
            if invoice.status == "DOCUMENT_CREATED":
                inv = weclapp.PUT(entityName='salesInvoice', entityId=invoice.id, apiKey=self.apiKey,
                        body = {
                                "status": "OPEN_ITEM_CREATED"
                                }, ignore=True, 
                        maxRetries=self.maxRetries,
                        retriesStatus=self.retriesStatus)
                invoice.updateEntityFromNewEntity(newEntity=inv)
        logging.info(f"   Compleetworkflow: Created for All DOCUMENT_CREATED open Items")

