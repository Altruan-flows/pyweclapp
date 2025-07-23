"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class PurchaseOrders(Blueprint):
    """Subclass for purchaseOrders in IncomingGoods."""

    id: Union[str, None] = None


class CustomerDeliveryAddress(Blueprint):
    """Subclass for customerDeliveryAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class CustomerInvoiceAddress(Blueprint):
    """Subclass for customerInvoiceAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class IncomingGoodsItems(Blueprint):
    """Subclass for incomingGoodsItems in IncomingGoods."""

    id: Union[str, None]
    version: Union[str, None]
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    dropshippingShipmentItemId: Union[str, None] = None
    itemGroup: Union[str, None] = None
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    note: Union[str, None] = None
    parentItemId: Union[str, None] = None
    positionNumber: Union[int, None]
    purchaseOrderItemId: Union[str, None] = None
    quantity: Union[str, None] = None
    returnAssessmentId: Union[str, None] = None
    returnAssessmentName: Union[str, None] = None
    returnDescription: Union[str, None] = None
    returnErrorId: Union[str, None] = None
    returnErrorName: Union[str, None] = None
    returnReasonId: Union[str, None] = None
    returnReasonName: Union[str, None] = None
    returnRectificationId: Union[str, None] = None
    returnRectificationName: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None


class InvoiceAddress(Blueprint):
    """Subclass for invoiceAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class RecipientAddress(Blueprint):
    """Subclass for recipientAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class ReturnAddress(Blueprint):
    """Subclass for returnAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None
    postOfficeBoxNumber: Union[str, None] = None
    postOfficeBoxZipCode: Union[str, None] = None
    salutation: Union[str, None] = None
    state: Union[str, None] = None
    street1: Union[str, None] = None
    street2: Union[str, None] = None
    title: Union[str, None] = None
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class SalesOrders(Blueprint):
    """Subclass for salesOrders in IncomingGoods."""

    id: Union[str, None]


class StatusHistory(Blueprint):
    """Subclass for statusHistory in IncomingGoods."""

    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class IncomingGoods(Blueprint):
    """Class for incomingGoods endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    commercialLanguage: Union[str, None] = None
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerDeliveryAddress: CustomerDeliveryAddress = (
        CustomerDeliveryAddress.from_blank()
    )
    customerInvoiceAddress: CustomerInvoiceAddress = CustomerInvoiceAddress.from_blank()
    deliveryNoteNumber: Union[str, None] = None
    description: Union[str, None] = None
    dhlReceiverId: Union[str, None] = None
    disableEmailTemplate: Union[bool, None] = None
    dropshippingShipmentId: Union[str, None] = None
    incomingGoodsItems: List[IncomingGoodsItems] = []
    incomingGoodsNumber: Union[str, None] = None
    incomingGoodsType: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    purchaseOrderId: Union[str, None] = None
    purchaseOrderNumber: Union[str, None] = None
    purchaseOrders: List[PurchaseOrders] = []
    recipientAddress: RecipientAddress = RecipientAddress.from_blank()
    recordComment: Union[str, None] = None
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    relatedShipmentId: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    returnAddress: ReturnAddress = ReturnAddress.from_blank()
    salesOrderId: Union[str, None] = None
    salesOrderNumber: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    senderCustomerNumber: Union[str, None] = None
    senderPartyId: Union[str, None] = None
    senderSupplierNumber: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    shippingReturnCarrierId: Union[str, None] = None
    sourceWarehouseId: Union[str, None] = None
    sourceWarehouseName: Union[str, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
