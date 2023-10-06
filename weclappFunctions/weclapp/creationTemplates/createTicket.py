import logging
from typing import *
import util
from util import weclappClasses, weclapp

from .bluePrints import CreationBluePrint



class TicketCreator(CreationBluePrint):
    def __init__(self, subject:str, description:str, email:str, firstName:str=None, lastName:str=None, phone:str=None,
                 daysTillCompleetion:int=1, ticketStatus:Literal["3350"]="3350", ticketCategoryId:Literal["39929340", "3261666"]="3261666", 
                 ticketTypeId:Literal["3347"]=None, ticketPriorityId:Literal["3331"]="3331", 
                 ticketChannelId:Literal["3332"]=None) -> None:
        self.assignedUserId = None
        self.billable = False
        self.description = description
        self.disableEmailTemplates = True
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phone
        self.solutionDueDate = util.convertDateTimeTo(timestemp=util.addWorkdaysToDate(add_days=daysTillCompleetion), to="unix")
        self.subject = subject
        self.ticketCategoryId = ticketCategoryId    # "3261666"=Shop Auftrags Check, ""
        self.ticketChannelId = ticketChannelId
        self.ticketPriorityId = ticketPriorityId    # "3330" =  Normal
        self.ticketTypeId = ticketTypeId            # "3348" =  Problem
        self.ticketStatusId = ticketStatus          # "3350" = "Noch nicht zugewiesen"
        
        self.entityReferences = []
        self.customAttributes = []
        
            
    def addReferences(self, entityName:Literal["salesOrder", "party"], entityId:str ):
        self.entityReferences.append({
            "entityId": str(entityId),
            "entityName": str(entityName)
        })
        

    def createTicket(self) -> weclappClasses.Article:
        logging.info(f"try to create new Ticket")
        # Validattions
            
        body = self.to_dict()
        # return body
        newArticle = weclapp.POST(entityName="ticket", body=body)
        return weclappClasses.Ticket(**newArticle)
