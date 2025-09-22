"""This module provides the DocManager class to manage documents for a specific
entity in Weclapp."""

from typing import List
from ..weclapp import Weclapp
from .document import Document


class DocManager:
    """A class to manage documents for a specific entity in Weclapp."""

    def __init__(self, entity_name: str, entity_id: str) -> None:
        self.entity_name = entity_name
        self.entity_id = entity_id
        self.weclapp = Weclapp()
        self.documents: List[Document] = []

    def get_documents(self) -> List[Document]:
        """Queries all documents of the entity and returns them as a list of
        Document objects"""
        response = self.weclapp.get(
            entity_name="document",
            query={"entityName": self.entity_name, "entityId": self.entity_id},
            as_type=list
        )
        for doc in response:
            self.documents.append(Document(**doc))

        return self.documents
