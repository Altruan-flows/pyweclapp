"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class PurchaseOrders(Blueprint):
    """Subclass for purchaseOrders in Shipment."""

    id: Union[str, None] = None


class InvoiceAddress(Blueprint):
    """Subclass for invoiceAddress in Shipment."""

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
    """Subclass for recipientAddress in Shipment."""

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


class EmailAddresses(Blueprint):
    """Subclass for recordEmailAddresses and salesInvoiceEmailAddresses in Shipment."""

    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class SalesOrders(Blueprint):
    """Subclass for salesOrders in Shipment."""

    id: Union[str, None] = None


class ShipmentItems(Blueprint):
    """Subclass for shipmentItems in Shipment."""

    id: Union[str, None] = None
    version: Union[str, None] = None
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    articleNumber: Union[str, None] = None
    availability: Union[str, None] = None
    availabilityForAllWarehouses: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    groupName: Union[str, None] = None
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    note: Union[str, None] = None
    parentItemId: Union[str, None] = None
    picks: list = []
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


class ShippedFromAddress(Blueprint):
    """Subclass for shippedFromAddress in Shipment."""

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


class StatusHistory(Blueprint):
    """Subclass for statusHistory in Shipment."""

    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class Shipment(Blueprint):
    """Class for shipment endpoint."""

    id: Union[str, None]
    version: Union[str, None]
    additionalDeliveryInformation: Union[str, None] = None
    availability: Union[str, None] = None
    availabilityForAllWarehouses: Union[str, None] = None
    commercialLanguage: Union[str, None] = None
    consolidationStoragePlaceId: Union[str, None] = None
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerPurchaseOrderNumber: Union[str, None] = None
    declaredValueAmount: Union[str, None] = None
    declaredValueAmountCurrencyId: Union[str, None] = None
    declaredValueAmountCurrencyName: Union[str, None] = None
    deliveryDate: Union[int, None] = None
    description: Union[str, None] = None
    destinationStoragePlaceId: Union[str, None] = None
    destinationWarehouseId: Union[str, None] = None
    destinationWarehouseName: Union[str, None] = None
    dhlReceiverId: Union[str, None] = None
    disableEmailTemplate: Union[bool, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    packageHeight: Union[int, None] = None
    packageLength: Union[int, None] = None
    packageReferenceNumber: Union[str, None] = None
    packageReturnTrackingNumber: Union[str, None] = None
    packageReturnTrackingUrl: Union[str, None] = None
    packageTrackingNumber: Union[str, None] = None
    packageTrackingUrl: Union[str, None] = None
    packageWeight: Union[str, None] = None
    packageWidth: Union[int, None] = None
    pickingInstructions: Union[str, None] = None
    picksComplete: Union[bool, None] = None
    purchaseOrders: List[PurchaseOrders] = []
    recipientAddress: RecipientAddress = RecipientAddress.from_blank()
    recipientCustomerNumber: Union[str, None] = None
    recipientPartyId: Union[str, None] = None
    recipientSupplierNumber: Union[str, None] = None
    recordComment: Union[str, None] = None
    recordEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.from_blank()
    salesOrderId: Union[str, None] = None
    salesOrderNumber: Union[str, None] = None
    salesOrders: List[SalesOrders] = []
    sentToRecipient: Union[bool, None] = None
    shipmentItems: List[ShipmentItems] = []
    shipmentMethodId: Union[str, None] = None
    shipmentMethodName: Union[str, None] = None
    shipmentNumber: Union[str, None] = None
    shipmentType: Union[str, None] = None
    shippedFromAddress: ShippedFromAddress = ShippedFromAddress.from_blank()
    shippingCarrierId: Union[str, None] = None
    shippingCarrierName: Union[str, None] = None
    shippingDate: Union[int, None] = None
    shippingLabelsCount: Union[int, None] = None
    shippingReturnCarrierId: Union[str, None] = None
    shippingReturnCarrierName: Union[str, None] = None
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    warehouseId: Union[str, None] = None
    warehouseName: Union[str, None] = None
