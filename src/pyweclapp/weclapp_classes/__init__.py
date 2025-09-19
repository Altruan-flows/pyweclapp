"""Module for weclapp classes package imports. Add more classes if necessary."""

from .blueprints.custom_attributes_model import WeclappMetaData
from .sales_order_model import SalesOrder, OrderItems
from .incoming_goods_model import IncomingGoods, IncomingGoodsItems
from .purchase_order_model import PurchaseOrder, PurchaseOrderItems
from .sales_invoice_model import SalesInvoice, SalesInvoiceItems
from .shipment_model import Shipment, ShipmentItems
from .quotation_model import Quotation
from .party_model import Party
from .extra_info_for_app_model import ExtraInfoForApp
from .article_model import Article, ArticlePrices
from .currency_model import Currency
