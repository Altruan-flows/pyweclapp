"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List, Set
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


class PurchaseOrders(Blueprint):
    id: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None
    ccAddresses: Union[str, None] = None
    toAddresses: Union[str, None] = None


class Picks(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    batchNumber: Union[str, None] = None
    confirmedByUserId: Union[str, None] = None
    confirmedDate: Union[int, None] = None
    internalTransportReferenceId: Union[str, None] = None
    quantity: Union[str, None] = None
    serialNumbers: list = []
    storagePlaceId: Union[str, None] = None
    bookedDate: Union[int, None] = None
    orderItemId: Union[str, None] = None
    sourceInternalTransportReferenceId: Union[str, None] = None
    sourceStoragePlaceId: Union[str, None] = None
    transportationOrderId: Union[str, None] = None


class ShipmentItems(Blueprint):
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
    addPageBreakBefore: Union[bool, None] = None
    groupName: Union[str, None] = None
    picks: List[Picks] = []
    purchaseOrderItemId: Union[str, None] = None
    returnAssessmentId: Union[str, None] = None
    returnDescription: Union[str, None] = None
    returnErrorId: Union[str, None] = None
    returnReasonId: Union[str, None] = None
    returnRectificationId: Union[str, None] = None
    salesOrderItemId: Union[str, None] = None

    excluded_keys: Set[str] = {
        "version"
    }


class ShippedFromAddress(Blueprint):
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


class Shipment(Blueprint):
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
    additionalDeliveryInformation: Union[str, None] = None
    consolidationStoragePlaceId: Union[str, None] = None
    customerPurchaseOrderNumber: Union[str, None] = None
    declaredValueAmount: Union[str, None] = None
    declaredValueAmountCurrencyId: Union[str, None] = None
    deliveryDate: Union[int, None] = None
    destinationStoragePlaceId: Union[str, None] = None
    destinationWarehouseId: Union[str, None] = None
    dhlReceiverId: Union[str, None] = None
    invoiceRecipientId: Union[str, None] = None
    mainSalesOrderId: Union[str, None] = None
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
    recipientCustomerNumber: Union[str, None] = None
    recipientPartyId: Union[str, None] = None
    recipientSupplierNumber: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = None
    responsibleUserId: Union[str, None] = None
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses()
    shipmentItems: List[ShipmentItems] = []
    shipmentMethodId: Union[str, None] = None
    shipmentNumber: Union[str, None] = None
    shipmentType: Union[str, None] = None
    shippedFromAddress: ShippedFromAddress = ShippedFromAddress()
    shippingCarrierId: Union[str, None] = None
    shippingDate: Union[int, None] = None
    shippingLabelsCount: Union[int, None] = None
    shippingReturnCarrierId: Union[str, None] = None
    warehouseId: Union[str, None] = None

    excluded_keys: Set[str] = {
        "picksComplete"
    }
