from pyWeclapp import weclapp, timeFunctions
import logging
import io
import base64
from typing import Any, Optional
from pydantic import BaseModel
from .docDescription import DocDescription
from . import config


class Document(BaseModel):
    id: str
    version: str
    createdDate: int
    description: Optional[str] = None
    lastModifiedDate: int = None
    mediaType: str
    name: str
    userId: str
    versions: list = []

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.description is not None and isinstance(self.description, str):
            if "{" in self.description:
                self.description = DocDescription.fromString(self.description)
                assert (
                    self.description.docId == self.id
                ), "document id in description is not equal to actual Id"
            # handl old format
            elif str(self.description) in config.ALLOWED_DOC_TYPES:
                self.description = DocDescription(
                    docType=self.description.strip(), docId=self.id
                )
                self.updateDescription()
                logging.warning("old document description found and updated")

    @classmethod
    def fromWeclapp(cls, docId: str = None, docJson: dict = None):
        assert docId or docJson, " Please provide ether docId or docJson"
        if docJson is None:
            assert (
                "." in docId
            ), f"DokumentenId falsch. Das Format sollte >entity.11111.11111< sein, not {docId}"
            docJson = weclapp.GET(entity_name="document", entity_id=docId)
        return cls(**docJson)

    @classmethod
    def documentNamingConvention(
        cls,
        docType: config.ALLOWED_DOC_TYPES_LITERAL,
        docFormat: config.ALLOWED_DOC_FORMATS_LITERAL,
        fullName: str,
    ):
        if docType not in config.ALLOWED_DOC_TYPES:
            logging.warning(f"documentNamingConvention: No convention for {docType}")
            # assert docType in ALLOWED_DOC_TYPES, f"documentNamingConvention: No convention for {docType}"
        if docFormat not in config.ALLOWED_DOC_FORMATS:
            logging.warning(f"documentNamingConvention: No Doctype for {docType}")
            # assert docFormat in ALLOWED_DOC_FORMATS, f"documentNamingConvention: No Doctype for {docType}"

        description = docType
        fullName = str(fullName).split(".")[0].replace(" ", "-")
        name = f"{docType}-{fullName}.{docFormat}"
        return name, description

    def remotePrintJob(
        self,
        hardwareId: str = "9bbb119cf1ca8151aee3269930f5148af03c46d57610",
        printer="HP_LaserJet_Pro_M404_M405_2",
        quantity=1,
    ) -> bool:
        weclapp.POST(
            entityName="remotePrintJob",
            body={
                "documentId": self.id,
                "printerName": printer,
                "printStatus": "DOCUMENT_NOT_FOUND",
                "quantity": quantity,
                "weclappOsHardwareId": hardwareId,
                # "weclappOsId": "string"
            },
        )

    def updateDescription(self):
        if self.description and isinstance(self.description, DocDescription):
            entityName, entityId, docId = self.id.split(".")
            desc = self.description.getDescriptionAsString()
            try:
                weclapp.PUT(
                    entityName="document",
                    entityId=f"{self.id}",
                    query={"entityId": entityId, "entityName": entityName},
                    body={"description": desc},
                )
                logging.info("updated description of documet")
            except Exception as e:
                logging.error(f"failed to update description of documet: {self.id}")
                logging.info(f"description = {desc}")
                raise AssertionError(
                    f"Beschreibung konnte nicht aktualisiert werden: {e}"
                )
        else:
            logging.warning("no Document description found to update")

    def setDescription(
        self,
        docType: config.ALLOWED_DOC_TYPES_LITERAL,
        startdate: str = None,
        enddate: str = None,
    ):
        if not self.description:
            self.description = DocDescription(docType=docType, docId=self.id)
        else:
            self.description.docType = docType

        if startdate:
            self.description.startdate = timeFunctions.localeDatetimeToStr(
                timestemp=startdate, to="utcDate"
            )
        if enddate:
            self.description.enddate = timeFunctions.localeDatetimeToStr(
                timestemp=enddate, to="utcDate"
            )
        logging.info(f"set description of documet to {self.description}")

    def updateFile(
        self, file: bytes = None, base64Content: str = None, buffer: io.BytesIO = None
    ):
        """Updates the file content"""
        logging.info("---weclapp.uploadFile()---")
        if file:
            file = file
        if base64Content:
            file = base64.b64decode(base64Content.encode())

        elif buffer:
            file = buffer.read()

        weclapp.POST(entityName="document", entityId=f"{self.id}/upload", body=file)

    def downloadDoc(self) -> io.BytesIO:
        content = weclapp.GET(
            entity_name="document", entity_id=f"{self.id}/download", as_type=bytes
        )
        """Downloads the file content as BytesIO"""
        file = io.BytesIO()
        file.write(content)
        file.seek(0)
        return file
