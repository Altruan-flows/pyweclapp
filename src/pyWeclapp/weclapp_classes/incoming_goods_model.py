"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class PurchaseOrders(Blueprint):
    """Subclass for purchaseOrders in IncomingGoods."""

    id: Union[str, None] = None


class CustomerDeliveryAddress(Blueprint):
    """Subclass for customerDeliveryAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class CustomerInvoiceAddress(Blueprint):
    """Subclass for customerInvoiceAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
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
    dropshippingShipmentItemId: Union[str, None] = None  # Type estimated
    itemGroup: Union[str, None] = None  # Type estimated
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    note: Union[str, None] = None  # Type estimated
    parentItemId: Union[str, None] = None  # Type estimated
    positionNumber: Union[int, None]
    purchaseOrderItemId: Union[str, None] = None  # Type estimated
    quantity: Union[str, None] = None
    returnAssessmentId: Union[str, None] = None  # Type estimated
    returnAssessmentName: Union[str, None] = None  # Type estimated
    returnDescription: Union[str, None] = None  # Type estimated
    returnErrorId: Union[str, None] = None  # Type estimated
    returnErrorName: Union[str, None] = None  # Type estimated
    returnReasonId: Union[str, None] = None  # Type estimated
    returnReasonName: Union[str, None] = None  # Type estimated
    returnRectificationId: Union[str, None] = None  # Type estimated
    returnRectificationName: Union[str, None] = None  # Type estimated
    salesOrderItemId: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None
    unitId: Union[str, None] = None
    unitName: Union[str, None] = None


class InvoiceAddress(Blueprint):
    """Subclass for invoiceAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None  # Type estimated
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class RecipientAddress(Blueprint):
    """Subclass for recipientAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None  # Type estimated
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class ReturnAddress(Blueprint):
    """Subclass for returnAddress in IncomingGoods."""

    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    lastName: Union[str, None] = None
    middleName: Union[str, None] = None  # Type estimated
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    title: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
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
    deliveryNoteNumber: Union[str, None] = None  # Type estimated
    description: Union[str, None] = None
    dhlReceiverId: Union[str, None] = None  # Type estimated
    disableEmailTemplate: Union[bool, None] = None
    dropshippingShipmentId: Union[str, None] = None  # Type estimated
    incomingGoodsItems: List[IncomingGoodsItems] = []
    incomingGoodsNumber: Union[str, None] = None
    incomingGoodsType: Union[str, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    purchaseOrderId: Union[str, None] = None  # Type estimated
    purchaseOrderNumber: Union[str, None] = None  # Type estimated
    purchaseOrders: List[PurchaseOrders] = []
    recipientAddress: RecipientAddress = RecipientAddress.from_blank()
    recordComment: Union[str, None] = None  # Type estimated
    recordFreeText: Union[str, None] = None  # Type estimated
    recordOpening: Union[str, None] = None  # Type estimated
    relatedShipmentId: Union[str, None] = None  # Type estimated
    responsibleUserId: Union[str, None] = None  # Type estimated
    returnAddress: ReturnAddress = ReturnAddress.from_blank()
    salesOrderId: Union[str, None] = None
    salesOrderNumber: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    senderCustomerNumber: Union[str, None] = None
    senderPartyId: Union[str, None] = None
    senderSupplierNumber: Union[str, None] = None  # Type estimated
    sentToRecipient: Union[bool, None] = None
    shippingReturnCarrierId: Union[str, None] = None  # Type estimated
    sourceWarehouseId: Union[str, None] = None  # Type estimated
    sourceWarehouseName: Union[str, None] = None  # Type estimated
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
