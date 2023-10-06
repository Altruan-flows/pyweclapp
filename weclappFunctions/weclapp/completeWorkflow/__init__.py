from util import weclappClasses, weclapp, attDefManager
from typing import *
from collections import defaultdict
import logging, time
from .proccessSalesInvoice import SalesInvoiceProcessing


class SalesOrderCompleteWorkflow(SalesInvoiceProcessing):
    def __init__(self, 
                 sales_order_id,
                 salesOrder:weclappClasses.SalesOrder = None,
                 apiKey:Literal["Johannes", "Jakob"]= "Jakob", 
                 ad:attDefManager.attDef=attDefManager.attDef(),
                 maxRetries:int=0,
                 retriesStatus:List[int] = [500, 502, 503, 504, 409]):
        if  salesOrder is not None:
            self.salesOrder = salesOrder
        else:
            self.salesOrder = weclappClasses.SalesOrder.fromWeclapp2(entityId=sales_order_id)
        self.ad = ad
        self.maxRetries = maxRetries
        self.retriesStatus = retriesStatus
        self.apiKey = apiKey
        SalesInvoiceProcessing.__init__(self, salesOrder=self.salesOrder ,apiKey=self.apiKey, ad=self.ad, retriesStatus=self.retriesStatus, maxRetries=self.maxRetries)


    def retryPolicy(self, func:Callable, errorFunc:Callable=None, retries:int=2) -> Any:
        assert callable(func), f"Retry policy function must be callable, but is {type(func)}"
        savedError = None
        for i in range(retries):
            try:
                return func()

            except weclapp.WeclappError as e:
                savedError = e
                # not for last execution!!!
                if i != retries-1:
                    logging.error(e)
                    logging.warning(logging.info(f"   Compleetworkflow: Error -> restart {func.__name__} {i+1}"))
                    # do custom Error Handling
                    if errorFunc is not None:
                        assert  callable(errorFunc), f"ErrorFunc must be callable, but is {type(errorFunc)}"
                        errorFunc(e)
                    time.sleep(0.6)
        # get full response displayed
        logging.warning(f"   Compleetworkflow: {retries-1} Retrys of {func.__name__} were useless :(")
        savedError.fullLog = True
        raise savedError
        

    def confirmOrder(self):
        if self.salesOrder.status in ["NEW", "ORDER_ENTRY_IN_PROGRESS"]:
            new = weclapp.PUT(entityName='salesOrder', entityId=self.salesOrder.id, apiKey=self.apiKey,
                        body = {
                                "status": "ORDER_CONFIRMATION_PRINTED"
                                }, 
                        maxRetries=self.maxRetries,
                        retriesStatus=self.retriesStatus)
            self.salesOrder.updateEntityFromNewEntity(newEntity=new)
        assert self.salesOrder.status == "ORDER_CONFIRMATION_PRINTED", f"Status must be ORDER_CONFIRMATION_PRINTED, but is {self.salesOrder.status}"
        logging.info("   Compleetworkflow: SalesOrder is confirmed")
        
        
    def autoworkflow(self):
        logging.warning("   Compleetworkflow: Starting auto workflow...")
        # SalesOrder
        self.retryPolicy(func=self.confirmOrder)
        
        # Shipement
        self.retryPolicy(func=self.createShipment)
        self.retryPolicy(func=self.confirmShipment)
        
        # SalesInvoices
        self.retryPolicy(func=self.createInvoice)
        self.retryPolicy(func=self.confirmInvoice)
        self.retryPolicy(func=self.createOpenItems)
