"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class InvoiceAddress(Blueprint):
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
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class Parcels(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    createdDate: Union[int, None]
    declaredValueAmount: Union[str, None] = None
    declaredValueCurrencyId: Union[str, None] = None
    dhlPremiumInternationalService: Union[bool, None] = None
    height: Union[int, None] = None
    lastModifiedDate: Union[int, None]
    length: Union[int, None] = None
    positionNumber: Union[int, None]
    reference: Union[str, None] = None
    saturdayDelivery: Union[bool, None] = None
    shippingCarrierAddition: Union[str, None] = None  # Type estimated
    shippingCarrierId: Union[str, None] = None
    shippingLabelsCount: Union[int, None] = None
    trackingId: Union[str, None] = None  # Type estimated
    trackingUrl: Union[str, None] = None
    useDeliveryDateAsPreferredDeliveryDate: Union[bool, None] = None
    weight: Union[str, None] = None
    width: Union[int, None] = None


class RecipientAddress(Blueprint):
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
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class RecordEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesInvoiceEmailAddresses(Blueprint):
    bccAddresses: Union[str, None] = None  # Type estimated
    ccAddresses: Union[str, None] = None  # Type estimated
    toAddresses: Union[str, None] = None


class SalesOrders(Blueprint):
    id: Union[str, None]


class ShipmentItems(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    addPageBreakBefore: Union[bool, None] = None
    articleId: Union[str, None] = None
    createdDate: Union[int, None]
    customAttributes: List[WeclappMetaData] = []
    description: Union[str, None] = None
    descriptionFixed: Union[bool, None] = None
    groupName: Union[str, None] = None  # Type estimated
    itemType: Union[str, None] = None
    lastModifiedDate: Union[int, None]
    manualQuantity: Union[bool, None] = None
    note: Union[str, None] = None  # Type estimated
    parentItemId: Union[str, None] = None  # Type estimated
    picks: list = []
    positionNumber: Union[int, None]
    purchaseOrderItemId: Union[str, None] = None  # Type estimated
    quantity: Union[str, None] = None
    returnAssessmentId: Union[str, None] = None  # Type estimated
    returnDescription: Union[str, None] = None  # Type estimated
    returnErrorId: Union[str, None] = None  # Type estimated
    returnReasonId: Union[str, None] = None  # Type estimated
    returnRectificationId: Union[str, None] = None  # Type estimated
    salesOrderItemId: Union[str, None] = None
    title: Union[str, None] = None
    unitId: Union[str, None] = None


class ShippedFromAddress(Blueprint):
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
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class StatusHistory(Blueprint):
    status: Union[str, None] = None
    statusDate: Union[int, None] = None
    userId: Union[str, None] = None


class Shipment(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    additionalDeliveryInformation: Union[str, None] = None  # Type estimated
    commercialLanguage: Union[str, None] = None  # Type estimated
    consolidationStoragePlaceId: Union[str, None] = None  # Type estimated
    createdDate: Union[int, None]
    creatorId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customerPurchaseOrderNumber: Union[str, None] = None  # Type estimated
    declaredValueAmount: Union[str, None] = None
    declaredValueAmountCurrencyId: Union[str, None] = None
    deliveryDate: Union[int, None] = None  # Type estimated
    description: Union[str, None] = None  # Type estimated
    destinationStoragePlaceId: Union[str, None] = None  # Type estimated
    destinationWarehouseId: Union[str, None] = None  # Type estimated
    dhlReceiverId: Union[str, None] = None  # Type estimated
    disableRecordEmailingRule: Union[bool, None] = None
    invoiceAddress: InvoiceAddress = InvoiceAddress.from_blank()
    invoiceRecipientId: Union[str, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    mainSalesOrderId: Union[str, None] = None
    packageHeight: Union[int, None] = None
    packageLength: Union[int, None] = None
    packageReferenceNumber: Union[str, None] = None
    packageReturnTrackingNumber: Union[str, None] = None  # Type estimated
    packageReturnTrackingUrl: Union[str, None] = None  # Type estimated
    packageTrackingNumber: Union[str, None] = None  # Type estimated
    packageTrackingUrl: Union[str, None] = None
    packageWeight: Union[str, None] = None
    packageWidth: Union[int, None] = None
    parcels: List[Parcels] = []
    pickingInstructions: Union[str, None] = None  # Type estimated
    picksComplete: Union[bool, None] = None
    purchaseOrders: list = []
    recipientAddress: RecipientAddress = RecipientAddress.from_blank()
    recipientCustomerNumber: Union[str, None] = None
    recipientPartyId: Union[str, None] = None
    recipientSupplierNumber: Union[str, None] = None  # Type estimated
    recordComment: Union[str, None] = None
    recordEmailAddresses: RecordEmailAddresses = RecordEmailAddresses.from_blank()
    recordFreeText: Union[str, None] = None
    recordOpening: Union[str, None] = None
    responsibleUserId: Union[str, None] = None  # Type estimated
    salesInvoiceEmailAddresses: SalesInvoiceEmailAddresses = SalesInvoiceEmailAddresses.from_blank()
    salesOrders: List[SalesOrders] = []
    sentToRecipient: Union[bool, None] = None
    shipmentItems: List[ShipmentItems] = []
    shipmentMethodId: Union[str, None] = None
    shipmentNumber: Union[str, None] = None
    shipmentType: Union[str, None] = None
    shippedFromAddress: ShippedFromAddress = ShippedFromAddress.from_blank()
    shippingCarrierId: Union[str, None] = None
    shippingDate: Union[int, None] = None
    shippingLabelsCount: Union[int, None] = None
    shippingReturnCarrierId: Union[str, None] = None  # Type estimated
    status: Union[str, None] = None
    statusHistory: List[StatusHistory] = []
    tags: list = []
    totalWeight: Union[str, None] = None
    warehouseId: Union[str, None] = None
