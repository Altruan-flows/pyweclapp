# This code was dynamically created using WeclappClassCreator from pyWeclapp

from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class EntityReferences(Blueprint):
	entityId: Union[str, None] = None
	entityName: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = None


class Ticket(Blueprint):
	id: Union[str, None]
	createdDate: Union[int, None]
	lastModifiedDate: Union[int, None]
	version: Union[str, None]
	customAttributes: List[WeclappMetaData] = []
	assignedPoolingGroupId: Union[str, None] = None
	assignedUserId: Union[str, None] = None
	billable: Union[bool, None] = None
	billableStatus: Union[bool, None] = None
	ccEmailAddresses: Union[str, None] = None
	contactId: Union[str, None] = None
	contractId: Union[str, None] = None
	description: Union[str, None] = None
	disableEmailTemplates: Union[bool, None] = None
	email: Union[str, None] = None
	entityReferences: List[EntityReferences] = []
	finishedDate: Union[int, None] = None
	firstName: Union[str, None] = None
	followUpDate: Union[int, None] = None
	invoicingStatus: Union[Literal["INVOICED", "NOT_INVOICED", "PARTLY_INVOICED"], None] = None
	language: Union[str, None] = None
	lastName: Union[str, None] = None
	legacyArticleId: Union[str, None] = None
	legacyTimeAndMaterialTicket: Union[bool, None] = None
	mail2TicketId: Union[str, None] = None
	mobilePhoneNumber: Union[str, None] = None
	note: Union[str, None] = None
	partyId: Union[str, None] = None
	performanceRecordedStatus: Union[Literal["NOT_PERFORMANCE_RECORDED", "PERFORMANCE_RECORDED", "UNDEFINED"], None] = None
	phoneNumber: Union[str, None] = None
	publicPageExpirationDate: Union[int, None] = None
	publicPageUuid: Union[str, None] = None
	resolvedYourIssue: Union[bool, None] = None
	responsibleUserId: Union[str, None] = None
	room: Union[str, None] = None
	salesOrderId: Union[str, None] = None
	solutionDueDate: Union[int, None] = None
	subject: Union[str, None] = None
	tags: list = []
	ticketCategoryId: Union[str, None] = None
	ticketChannelId: Union[str, None] = None
	ticketNumber: Union[str, None] = None
	ticketPriorityId: Union[str, None] = None
	ticketRating: Union[Literal["STARS_1", "STARS_2", "STARS_3", "STARS_4", "STARS_5"], None] = None
	ticketRatingComment: Union[str, None] = None
	ticketRatingDate: Union[int, None] = None
	ticketServiceLevelAgreementId: Union[str, None] = None
	ticketStatusId: Union[str, None] = None
	ticketTypeId: Union[str, None] = None
	# AutomationData
	ITEMS_NAME: ClassVar[str] = "entityReferences"


