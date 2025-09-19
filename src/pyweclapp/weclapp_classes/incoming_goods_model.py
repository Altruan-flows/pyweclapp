"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class InvoiceAddress(Blueprint):
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
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class RecipientAddress(Blueprint):
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
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class SalesOrders(Blueprint):
    id: Union[str, None] = None


class StatusHistory(Blueprint):
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class CustomerDeliveryAddress(Blueprint):
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
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class CustomerInvoiceAddress(Blueprint):
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
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class IncomingGoodsItems(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    articleId: Union[str, None] = None
    note: Union[str, None] = None
    positionNumber: Union[int, None] = None
    quantity: Union[str, None] = None
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    itemType: Union[str, None] = None
    manualQuantity: Union[bool, None] = None
    parentItemId: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None
    dropshippingShipmentItemId: Union[str, None] = None
    itemGroup: Union[str, None] = None
    purchaseOrderItemId: Union[str, None] = None
    returnAssessmentId: Union[str, None] = None
    returnDescription: Union[str, None] = None
    returnErrorId: Union[str, None] = None
    returnReasonId: Union[str, None] = None
    returnRectificationId: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None


class PurchaseOrders(Blueprint):
    id: Union[str, None] = None


class ReturnAddress(Blueprint):
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
    titleId: Union[str, None] = None
    zipcode: Union[str, None] = None


class IncomingGoods(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    commercialLanguage: Union[str, None] = None
    creatorId: Union[str, None] = None
    description: Union[str, None] = None
    disableRecordEmailingRule: Union[bool, None] = None
    recordComment: Union[str, None] = None
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    sentToRecipient: Union[bool, None] = None
    tags: list = []
    invoiceAddress: InvoiceAddress = InvoiceAddress()
    recipientAddress: RecipientAddress = RecipientAddress()
    salesOrders: List[SalesOrders] = []
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    customerDeliveryAddress: CustomerDeliveryAddress = CustomerDeliveryAddress()
    customerInvoiceAddress: CustomerInvoiceAddress = CustomerInvoiceAddress()
    deliveryNoteNumber: Union[str, None] = None
    dhlReceiverId: Union[str, None] = None
    dropshippingShipmentId: Union[str, None] = None
    incomingGoodsItems: List[IncomingGoodsItems] = []
    incomingGoodsNumber: Union[str, None] = None
    incomingGoodsType: Union[str, None] = None
    invoiceRecipientId: Union[str, None] = None
    purchaseOrders: List[PurchaseOrders] = []
    relatedShipmentId: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    returnAddress: ReturnAddress = ReturnAddress()
    senderCustomerNumber: Union[str, None] = None
    senderPartyId: Union[str, None] = None
    senderSupplierNumber: Union[str, None] = None
    shippingReturnCarrierId: Union[str, None] = None
    sourceWarehouseId: Union[str, None] = None
    warehouseId: Union[str, None] = None
