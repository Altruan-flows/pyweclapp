"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union, List
from .blueprints import Blueprint, WeclappMetaData


class Addresses(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    city: Union[str, None] = None
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    countryCode: Union[str, None] = None
    createdDate: Union[int, None]
    deliveryAddress: Union[bool, None] = None
    firstName: Union[str, None] = None
    globalLocationNumber: Union[str, None] = None  # Type estimated
    invoiceAddress: Union[bool, None] = None
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    phoneNumber: Union[str, None] = None
    postOfficeBoxCity: Union[str, None] = None  # Type estimated
    postOfficeBoxNumber: Union[str, None] = None  # Type estimated
    postOfficeBoxZipCode: Union[str, None] = None  # Type estimated
    primaryAddress: Union[bool, None] = None
    salutation: Union[str, None] = None  # Type estimated
    state: Union[str, None] = None  # Type estimated
    street1: Union[str, None] = None
    street2: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    zipcode: Union[str, None] = None


class Party(Blueprint):
    id: Union[str, None]
    version: Union[str, None]
    addresses: List[Addresses] = []
    bankAccounts: list = []
    birthDate: Union[int, None] = None  # Type estimated
    commercialLanguageId: Union[str, None] = None  # Type estimated
    commissionBlock: Union[bool, None] = None
    commissionSalesPartners: list = []
    company: Union[str, None] = None  # Type estimated
    company2: Union[str, None] = None  # Type estimated
    companySizeId: Union[str, None] = None  # Type estimated
    competitor: Union[bool, None] = None
    contacts: list = []
    convertedOnDate: Union[int, None] = None  # Type estimated
    createdDate: Union[int, None]
    currencyId: Union[str, None] = None
    customAttributes: List[WeclappMetaData] = []
    customer: Union[bool, None] = None
    customerAllowDropshippingOrderCreation: Union[bool, None] = None
    customerAmountInsured: Union[str, None] = None  # Type estimated
    customerAnnualRevenue: Union[str, None] = None  # Type estimated
    customerBlockNotice: Union[str, None] = None  # Type estimated
    customerBlocked: Union[bool, None] = None
    customerBusinessType: Union[str, None] = None
    customerCategoryId: Union[str, None] = None  # Type estimated
    customerCreditLimit: Union[str, None] = None  # Type estimated
    customerCurrentSalesStageId: Union[str, None] = None  # Type estimated
    customerDebtorAccountId: Union[str, None] = None
    customerDebtorAccountingCodeId: Union[str, None] = None  # Type estimated
    customerDefaultHeaderDiscount: Union[str, None] = None  # Type estimated
    customerDefaultHeaderSurcharge: Union[str, None] = None  # Type estimated
    customerDefaultShippingCarrierId: Union[str, None] = None
    customerDeliveryBlock: Union[bool, None] = None
    customerInsolvent: Union[bool, None] = None
    customerInsured: Union[bool, None] = None
    customerInternalNote: Union[str, None] = None  # Type estimated
    customerLossDescription: Union[str, None] = None  # Type estimated
    customerLossReasonId: Union[str, None] = None  # Type estimated
    customerNonStandardTaxId: Union[str, None] = None  # Type estimated
    customerNumber: Union[str, None] = None
    customerNumberOld: Union[str, None] = None  # Type estimated
    customerPaymentMethodId: Union[str, None] = None
    customerSalesChannel: Union[str, None] = None
    customerSalesOrderPaymentType: Union[str, None] = None  # Type estimated
    customerSalesProbability: Union[str, None] = None  # Type estimated
    customerSalesStageHistory: list = []
    customerSatisfaction: Union[str, None] = None  # Type estimated
    customerShipmentMethodId: Union[str, None] = None
    customerSupplierNumber: Union[str, None] = None  # Type estimated
    customerTermOfPaymentId: Union[str, None] = None
    customerUseCustomsTariffNumber: Union[bool, None] = None
    deliveryAddressId: Union[str, None] = None  # Type estimated
    deliveryEmailAddressesId: Union[str, None] = None  # Type estimated
    description: Union[str, None] = None  # Type estimated
    dunningAddressId: Union[str, None] = None  # Type estimated
    dunningEmailAddressesId: Union[str, None] = None  # Type estimated
    email: Union[str, None] = None
    enableDropshippingInNewSupplySources: Union[bool, None] = None
    eoriNumber: Union[str, None] = None  # Type estimated
    factoring: Union[bool, None] = None
    fax: Union[str, None] = None  # Type estimated
    firstName: Union[str, None] = None
    fixPhone2: Union[str, None] = None  # Type estimated
    fixedResponsibleUser: Union[bool, None] = None
    formerSalesPartner: Union[bool, None] = None
    habitualExporter: Union[bool, None] = None
    imageId: Union[str, None] = None  # Type estimated
    invoiceAddressId: Union[str, None] = None  # Type estimated
    invoiceBlock: Union[bool, None] = None
    invoiceRecipientId: Union[str, None] = None  # Type estimated
    lastModifiedDate: Union[int, None]
    lastName: Union[str, None] = None
    leadRatingId: Union[str, None] = None  # Type estimated
    leadSourceId: Union[str, None] = None
    leadStatus: Union[str, None] = None  # Type estimated
    legalFormId: Union[str, None] = None  # Type estimated
    middleName: Union[str, None] = None  # Type estimated
    mobilePhone1: Union[str, None] = None  # Type estimated
    mobilePhone2: Union[str, None] = None  # Type estimated
    onlineAccounts: list = []
    optInEmail: Union[bool, None] = None
    optInLetter: Union[bool, None] = None
    optInPhone: Union[bool, None] = None
    optInSms: Union[bool, None] = None
    parentPartyId: Union[str, None] = None  # Type estimated
    partyEmailAddresses: list = []
    partyHabitualExporterLettersOfIntent: list = []
    partyType: Union[str, None] = None
    personCompany: Union[str, None] = None  # Type estimated
    personDepartmentId: Union[str, None] = None  # Type estimated
    personRoleId: Union[str, None] = None  # Type estimated
    phone: Union[str, None] = None
    phoneHome: Union[str, None] = None  # Type estimated
    primaryAddressId: Union[str, None] = None
    primaryContactId: Union[str, None] = None  # Type estimated
    publicPageExpirationDate: Union[int, None] = None  # Type estimated
    publicPageUuid: Union[str, None] = None  # Type estimated
    purchaseEmailAddressesId: Union[str, None] = None  # Type estimated
    purchaseViaPlafond: Union[bool, None] = None
    quotationEmailAddressesId: Union[str, None] = None  # Type estimated
    ratingId: Union[str, None] = None  # Type estimated
    referenceNumber: Union[str, None] = None  # Type estimated
    regionId: Union[str, None] = None
    responsibleUserId: Union[str, None] = None
    salesInvoiceEmailAddressesId: Union[str, None] = None  # Type estimated
    salesOrderEmailAddressesId: Union[str, None] = None  # Type estimated
    salesPartner: Union[bool, None] = None
    salesPartnerDefaultCommissionFix: Union[str, None] = None  # Type estimated
    salesPartnerDefaultCommissionPercentage: Union[str, None] = None  # Type estimated
    salesPartnerDefaultCommissionType: Union[str, None] = None  # Type estimated
    salutation: Union[str, None] = None  # Type estimated
    sectorId: Union[str, None] = None  # Type estimated
    supplier: Union[bool, None] = None
    supplierActive: Union[bool, None] = None
    supplierCreditorAccountId: Union[str, None] = None  # Type estimated
    supplierCreditorAccountingCodeId: Union[str, None] = None  # Type estimated
    supplierCustomerNumberAtSupplier: Union[str, None] = None  # Type estimated
    supplierDefaultShippingCarrierId: Union[str, None] = None  # Type estimated
    supplierInternalNote: Union[str, None] = None  # Type estimated
    supplierMergeItemsForOcrInvoiceUpload: Union[bool, None] = None
    supplierMinimumPurchaseOrderAmount: Union[str, None] = None  # Type estimated
    supplierNonStandardTaxId: Union[str, None] = None  # Type estimated
    supplierNumber: Union[str, None] = None  # Type estimated
    supplierNumberOld: Union[str, None] = None  # Type estimated
    supplierOrderBlock: Union[bool, None] = None
    supplierPaymentMethodId: Union[str, None] = None  # Type estimated
    supplierShipmentMethodId: Union[str, None] = None  # Type estimated
    supplierTermOfPaymentId: Union[str, None] = None  # Type estimated
    tags: list = []
    taxId: Union[str, None] = None  # Type estimated
    titleId: Union[str, None] = None  # Type estimated
    topics: list = []
    vatIdentificationNumber: Union[str, None] = None  # Type estimated
    website: Union[str, None] = None  # Type estimated
    xRechnungLeitwegId: Union[str, None] = None  # Type estimated
