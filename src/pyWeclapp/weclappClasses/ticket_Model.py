# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import Optional, List, ClassVar


class EntityReferences(Blueprint):
    entityId: Optional[str] = None
    entityName: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = None


class TicketWeclapp(Blueprint):
    id: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    version: Optional[str] = None
    customAttributes: List[WeclappMetaData] = []
    assignedPoolingGroupId: Optional[str] = None
    assignedUserId: Optional[str] = None
    billable: Optional[bool] = None
    billableStatus: Optional[bool] = None
    ccEmailAddresses: Optional[str] = None
    contactId: Optional[str] = None
    contractId: Optional[str] = None
    description: Optional[str] = None
    disableEmailTemplates: Optional[bool] = None
    email: Optional[str] = None
    entityReferences: List[EntityReferences] = []
    finishedDate: Optional[int] = None
    firstName: Optional[str] = None
    followUpDate: Optional[int] = None
    invoicingStatus: Optional[str] = None
    language: Optional[str] = None
    lastName: Optional[str] = None
    legacyArticleId: Optional[str] = None
    legacyTimeAndMaterialTicket: Optional[bool] = None
    mail2TicketId: Optional[str] = None
    mobilePhoneNumber: Optional[str] = None
    note: Optional[str] = None
    partyId: Optional[str] = None
    performanceRecordedStatus: Optional[str] = None
    phoneNumber: Optional[str] = None
    publicPageExpirationDate: Optional[int] = None
    publicPageUuid: Optional[str] = None
    resolvedYourIssue: Optional[bool] = None
    responsibleUserId: Optional[str] = None
    room: Optional[str] = None
    salesOrderId: Optional[str] = None
    solutionDueDate: Optional[int] = None
    subject: Optional[str] = None
    tags: list = []
    ticketCategoryId: Optional[str] = None
    ticketChannelId: Optional[str] = None
    ticketNumber: Optional[str] = None
    ticketPriorityId: Optional[str] = None
    ticketRating: Optional[str] = None
    ticketRatingComment: Optional[str] = None
    ticketRatingDate: Optional[int] = None
    ticketServiceLevelAgreementId: Optional[str] = None
    ticketStatusId: Optional[str] = None
    ticketTypeId: Optional[str] = None
    # AutomationData
    ITEMS_NAME: ClassVar[str] = "entityReferences"
