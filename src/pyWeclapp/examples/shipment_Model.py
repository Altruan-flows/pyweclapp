# This code was dynamically created using WeclappClassCreator from pyWeclapp

from weclappClasses.weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


class Address(Blueprint):
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class StatusHistory(Blueprint):
    status: Optional[str] = None
    statusDate: Optional[int] = None
    userId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class PurchaseOrders(Blueprint):
    id: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class EmailAddresses(Blueprint):
    bccAddresses: Optional[str] = None
    ccAddresses: Optional[str] = None
    toAddresses: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ShipmentItems(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    articleId: Optional[str] = None
    articleNumber: Optional[str] = None
    note: Optional[str] = None
    positionNumber: Optional[int] = None
    quantity: Optional[str] = None
    description: Optional[str] = None
    descriptionFixed: Optional[bool] = None
    manualQuantity: Optional[bool] = None
    parentItemId: Optional[str] = None
    title: Optional[str] = None
    unitId: Optional[str] = None
    unitName: Optional[str] = None
    addPageBreakBefore: Optional[bool] = None
    availability: Optional[str] = None
    availabilityForAllWarehouses: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    freeTextItem: Optional[bool] = None
    groupName: Optional[str] = None
    purchaseOrderItemId: Optional[str] = None
    returnAssessmentId: Optional[str] = None
    returnAssessmentName: Optional[str] = None
    returnDescription: Optional[str] = None
    returnErrorId: Optional[str] = None
    returnErrorName: Optional[str] = None
    returnReasonId: Optional[str] = None
    returnReasonName: Optional[str] = None
    returnRectificationId: Optional[str] = None
    returnRectificationName: Optional[str] = None
    salesOrderItemId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class ShippedFromAddress(Blueprint):
    city: Optional[str] = None
    company: Optional[str] = None
    company2: Optional[str] = None
    countryCode: Optional[str] = None
    firstName: Optional[str] = None
    globalLocationNumber: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    phoneNumber: Optional[str] = None
    postOfficeBoxCity: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postOfficeBoxZipCode: Optional[str] = None
    salutation: Optional[str] = None
    state: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    title: Optional[str] = None
    titleId: Optional[str] = None
    zipcode: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class Shipment(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    commercialLanguage: Optional[str] = None
    creatorId: Optional[str] = None
    description: Optional[str] = None
    disableEmailTemplate: Optional[bool] = None
    recordComment: Optional[str] = None
    recordFreeText: Optional[str] = None
    recordOpening: Optional[str] = None
    sentToRecipient: Optional[bool] = None
    tags: list = []
    invoiceAddress: Address = Address.fromBlank()
    recipientAddress: Address = Address.fromBlank()
    salesOrderId: Optional[str] = None
    salesOrderNumber: Optional[str] = None
    status: Optional[str] = None
    statusHistory: List[StatusHistory] = []
    additionalDeliveryInformation: Optional[str] = None
    availability: Optional[str] = None
    availabilityForAllWarehouses: Optional[str] = None
    consolidationStoragePlaceId: Optional[str] = None
    customerPurchaseOrderNumber: Optional[str] = None
    declaredValueAmount: Optional[str] = None
    declaredValueAmountCurrencyId: Optional[str] = None
    declaredValueAmountCurrencyName: Optional[str] = None
    deliveryDate: Optional[int] = None
    destinationStoragePlaceId: Optional[str] = None
    destinationWarehouseId: Optional[str] = None
    destinationWarehouseName: Optional[str] = None
    invoiceRecipientId: Optional[str] = None
    packageHeight: Optional[int] = None
    packageLength: Optional[int] = None
    packageReferenceNumber: Optional[str] = None
    packageReturnTrackingNumber: Optional[str] = None
    packageReturnTrackingUrl: Optional[str] = None
    packageTrackingNumber: Optional[str] = None
    packageTrackingUrl: Optional[str] = None
    packageWeight: Optional[str] = None
    packageWidth: Optional[int] = None
    pickingInstructions: Optional[str] = None
    picksComplete: Optional[bool] = None
    purchaseOrders: List[PurchaseOrders] = []
    recipientCustomerNumber: Optional[str] = None
    recipientPartyId: Optional[str] = None
    recipientSupplierNumber: Optional[str] = None
    recordEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    responsibleUserId: Optional[str] = None
    salesInvoiceEmailAddresses: EmailAddresses = EmailAddresses.fromBlank()
    shipmentItems: List[ShipmentItems] = []
    shipmentMethodId: Optional[str] = None
    shipmentMethodName: Optional[str] = None
    shipmentNumber: Optional[str] = None
    shipmentType: Optional[str] = None
    shippedFromAddress: ShippedFromAddress = ShippedFromAddress.fromBlank()
    shippingCarrierId: Optional[str] = None
    shippingCarrierName: Optional[str] = None
    shippingDate: Optional[int] = None
    shippingLabelsCount: Optional[int] = None
    shippingReturnCarrierId: Optional[str] = None
    shippingReturnCarrierName: Optional[str] = None
    warehouseId: Optional[str] = None
    warehouseName: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "shipmentItems"
