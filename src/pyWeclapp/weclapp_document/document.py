"""This mopdule contains the Document class, which represents a document in
Weclapp and provides methods to interact with it."""

import io
from typing import Any, Union
from pydantic import BaseModel
from ..weclapp import Weclapp


class Document(BaseModel):
    """A class representing a document in Weclapp."""

    id: Union[str, None] = None
    version: Union[str, None] = None
    createdDate: Union[int, None] = None
    description: Union[str, None] = None
    lastModifiedDate: Union[int, None] = None
    mediaType: Union[str, None] = None
    name: Union[str, None] = None
    userId: Union[str, None] = None
    versions: list = []

    def __init__(self, **data: Any):
        super().__init__(**data)

    @classmethod
    def from_weclapp(cls, document_id: str = None, json_document: dict = None):
        """Creates a Document instance using either data from Weclapp entity or
        a provided JSON document."""
        if document_id is None and json_document is None:
            raise ValueError("Either document_id or json_document must be provided.")
        if json_document is None:
            if not isinstance(document_id, str):
                raise TypeError("document_id must be a string.")
            if not document_id.isdigit():
                raise ValueError("document_id must be a numeric string.")
            json_document = Weclapp().get(entity_name="document", entity_id=document_id)
        return cls(**json_document)

    def download_doc(self) -> io.BytesIO:
        """Downloads the document content as a BytesIO object."""
        content = Weclapp().get(
            entity_name="document", entity_id=f"{self.id}/download", as_type=bytes
        )
        file = io.BytesIO()
        file.write(content)
        file.seek(0)
        return file
