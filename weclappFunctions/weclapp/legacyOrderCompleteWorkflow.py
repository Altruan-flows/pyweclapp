from .legacyWeclappRequests import askWeclapp, updateWeclapp
from typing import Literal
import logging
# from util.error import ReportError






def orderCompleteWorkflow(orderId:str, raiseError:bool= True, useSecondaryAuth:Literal["Johannes", "Jakob"]= "Jakob") -> bool:
    
    try:
        # Confirm Order
        updateWeclapp(entityName='salesOrder', entityId=orderId, useSecondaryAuth= useSecondaryAuth,
                    body = {
                            "status": "ORDER_CONFIRMATION_PRINTED"
                            })
        
        # create Shipment
        shipment = askWeclapp(method="POST", endpoint=f"salesOrder/id/{orderId}/createShipment")['result']
        shipmentId = shipment.get('id')
        
        # Shipement documents
        updateWeclapp(entityName='shipment', entityId=shipmentId, useSecondaryAuth= useSecondaryAuth,
                    body = {
                            "status": "DELIVERY_NOTE_PRINTED"
                            })
        
        # create Invoice
        invoice = askWeclapp(method="POST", endpoint=f"shipment/id/{shipmentId}/createSalesInvoice")['result']
        
        invoiceId = invoice.get('id')
        
        # Invoice documents
        updateWeclapp(entityName='salesInvoice', entityId=invoiceId, useSecondaryAuth= useSecondaryAuth,
                    body = {
                            "status": "DOCUMENT_CREATED"
                            })
        
        # Create Open Itemns
        updateWeclapp(entityName='salesInvoice', entityId=invoiceId, useSecondaryAuth= useSecondaryAuth,
                    body = {
                            "status": "OPEN_ITEM_CREATED"
                            })
        
        return True
    except Exception as e:
        # r = ReportError(error= e, message="order Complette Workflow failed")
        logging.error(f"legacyOrderCompleteWorkflow.py\n{type(e).__name__}: {e}")
        if raiseError:
            raise e
        return False
    
    