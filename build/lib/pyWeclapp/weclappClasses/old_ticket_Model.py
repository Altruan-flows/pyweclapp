from .weclappClassBlueprint import Blueprint, WeclappMetaData
from typing import *



class EntityReferences( Blueprint):
	entityId: str = None
	entityName: str = None



class Ticket(Blueprint):
	id: str
	version: str
	assignedUserId: str = None
	billable: bool
	billableStatus: bool
	ccEmailAddresses: str = None
	contactId: str = None
	contractId: str = None
	createdDate: int
	customAttributes: List[WeclappMetaData] = []
	description: str = None
	disableEmailTemplates: bool
	email: str = None
	entityReferences: List[EntityReferences] = []
	finishedDate: int = None
	firstName: str = None
	followUpDate: int = None
	invoicingStatus: str = None
	language: str = None
	lastModifiedDate: int
	lastName: str = None
	legacyArticleId: str = None
	legacyTimeAndMaterialTicket: bool
	mail2TicketId: str = None
	mobilePhoneNumber: str = None
	note: str = None
	partyId: str = None
	performanceRecordedStatus: str = None
	phoneNumber: str = None
	publicPageExpirationDate: int = None
	publicPageUuid: str = None
	resolvedYourIssue: bool
	responsibleUserId: str = None
	room: str = None
	salesOrderId: str = None
	solutionDueDate: int = None
	subject: str = None
	tags: list = [] # could not be parsed
	ticketCategoryId: str = None
	ticketChannelId: str = None
	ticketNumber: str = None
	ticketPriorityId: str = None
	ticketRating: str = None
	ticketRatingComment: str = None
	ticketRatingDate: int = None
	ticketServiceLevelAgreementId: str = None
	ticketStatusId: str = None
	ticketTypeId: str = None



	# AutomationData
	ITEMS_NAME: str = 'entityReferences'
