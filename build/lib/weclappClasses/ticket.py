from pydantic import BaseModel
from .weclappClassBlueprint import *


class Ticket(BaseModel, Blueprint):
    id: str
    version: str
    assignedUserId: str = None
    billable: bool = False
    billableStatus: bool = False
    ccEmailAddresses: str = None
    contactId: str = None
    contractId: str = None
    createdDate: int
    customAttributes: List[WeclappMetaData] = []
    description: str = ""
    disableEmailTemplates: bool
    email: str
    entityReferences: list = []
    firstName: str
    followUpDate: int = None
    language: str = "de"
    lastModifiedDate: int
    lastName: str
    legacyTimeAndMaterialTicket: bool = False
    mail2TicketId: str = None
    note: str = None
    partyId: str = None
    performanceRecordedStatus: str = None
    phoneNumber: str = ""
    publicPageExpirationDate: int = None
    publicPageUuid: str = None
    resolvedYourIssue: bool = False
    responsibleUserId:str = None
    room: str = None
    solutionDueDate: int 
    subject: str
    tags: list = []
    ticketCategoryId: str
    ticketChannelId: str
    ticketNumber: str
    ticketPriorityId: str
    ticketRating: str = None
    ticketStatusId: str
    ticketTypeId: str = None

	# AutomationData
    ITEMS_NAME: str = "-"
    USED_ATTRIBUTES: dict = dict()
    __setattr__ = Blueprint.__setattr__
 
    def __init__(self, **kwargs):
        BaseModel.__init__(self, **kwargs)
        Blueprint.__init__(self, self.ITEMS_NAME, self.USED_ATTRIBUTES)