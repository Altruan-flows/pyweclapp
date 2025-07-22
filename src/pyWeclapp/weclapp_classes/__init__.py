"""Module for weclapp classes package imports. Add more classes if necessary."""

from .blueprints.custom_attributes_model import WeclappMetaData
from .sales_order_model import SalesOrder, OrderItems
from .shipment_model import Shipment, ShipmentItems
from .customer_model import Customer
from .party_model import Party
from .article_model import Article, ArticlePrices
from .contact_model import Contact
from .incoming_goods_model import IncomingGoods, IncomingGoodsItems
from .purchase_order_model import PurchaseOrder, PurchaseOrderItems
from .quotation_model import Quotation, QuotationItems
from .sales_invoice_model import SalesInvoice, SalesInvoiceItems
