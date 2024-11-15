from .docDescription import DocDescription
from .document import Document
from typing import *
import logging
import io
from pyWeclapp import weclapp
from pyWeclapp.weclapp.weclappError import WeclappError
import time
import base64
from . import config


class DocManager:
    

    @staticmethod
    def convertPdfToTiff(docs:List[io.BytesIO], names:List[str]) -> Tuple[List[io.BytesIO], List[str]]:
        try:
            import fitz
        except ImportError:
            logging.error('Special Functionality requires fitz module to manually install (pip install PyMuPDF)')
            raise AssertionError('Special Functionality requires fitz module to manually install (pip install PyMuPDF)')
        logging.info('converting pdf to tiff')
        img_list = []
        name_list = []
        for doc, name in zip(docs, names):
            doc = fitz.open(stream=doc.read(), filetype="pdf")
            for i, page in enumerate(doc):
                pix = page.get_pixmap(alpha=False)
                img_bytes = io.BytesIO(pix.tobytes('tiff'))
                img_list.append(img_bytes)
                nameRaw = str(name).split('.')[0]
                name_list.append(f"{nameRaw}-{i}.tiff")
            doc.close()
        return img_list, name_list
    
    
    @staticmethod
    def downloadDocById(docId) -> io.BytesIO:
        content = weclapp.GET(entityName="document",
                            entityId=f"{docId}/download", 
                            asType=bytes)
        file = io.BytesIO()
        file.write(content)
        file.seek(0)
        return file
        
        
    
    
    def __init__(self, entityName, entityId) -> None:
        self.entityName = entityName
        self.entityId = entityId
        self.documents: List[Document] = []

        
        
    def getDocuments(self) -> List[Document]:
        """Gets a list of weclapp Documents as Document class for the given entity"""
        response = weclapp.GET(entityName="document",
                                query={
                                    "entityName": self.entityName, 
                                    "entityId": self.entityId})
        for doc in response:
            self.documents.append(Document(**doc))
        
        return self.documents
    
    def setDescriptionOfLatestDocument(self, docType:config.ALLOWED_DOC_TYPES_LITERAL):
        
        docsWithoutDescription = [doc for doc in self.getDocuments() if not doc.description]
        if docsWithoutDescription:
            latestDoc = max(docsWithoutDescription, key=lambda x: x.createdDate)
            logging.info(f"found document without description {latestDoc.id}")
            latestDoc.setDescription(docType=docType)
            latestDoc.updateDescription()
        else:
            logging.error('No Document found!!!')
            
            
    def queryDoc(self, value:str, key:str="docType", raiseError:bool=True) -> Document:
        """Searches the entity for a document with a specified doctype and returns it"""
        if not self.documents:
            self.getDocuments()
        for doc in self.documents:
            if key in ["id", "version", "createdDate", "description", "lastModifiedDate", "mediaType", "name", "userId", "versions"]:
                if hasattr(doc, key) and getattr(doc, key) == value:
                    return doc
            elif doc.description:
                if hasattr(doc.description, key) and getattr(doc.description, key) == value:
                    return doc
        if raiseError:
            raise AssertionError('Document not found')
        return None


    def queryDocDescription(self, value:str, key:str="docType", raiseError:bool=True) -> DocDescription:
        if not self.documents:
            self.getDocuments()
        for doc in self.documents:
            if doc.description:
                if hasattr(doc.description, key) and getattr(doc.description, key) == value:
                    return doc.description
        if raiseError:
            raise AssertionError('Description not found')
        
        
    def uploadFile(self, name:str, 
                   docType:config.ALLOWED_DOC_TYPES_LITERAL, 
                   file:bytes= None, 
                   base64Content:str = None, 
                   buffer:io.BytesIO = None, 
                   docFormat:config.ALLOWED_DOC_FORMATS_LITERAL = 'pdf',  
                   demo:bool = False,
                   tryToUpdateFirst:bool=False) -> Document:
        """Uploads a file to the entity and returns the document class"""
        logging.info('---weclapp.uploadFile()---')
        if file:
            file = file
        if base64Content:
            file = base64.b64decode(base64Content.encode())
        
        elif buffer:
            file = buffer.read()

        name, docType = Document.documentNamingConvention(docType=docType, docFormat=docFormat, fullName=name)
        
        if tryToUpdateFirst:
            existingDoc = self.queryDoc(value=docType, raiseError=False)
            if isinstance(existingDoc, Document):
                existingDoc.updateFile(file)
                logging.info(f"UPDATED EXISTING DOCUMENT {existingDoc.id}")
                try:
                    weclapp.PUT(entityName="document", entityId=existingDoc.id, body={"name": name})
                except Exception as e:
                    logging.warning(f"Document Name could not be updated {e}")
                return existingDoc
            
        try:
            response = weclapp.POST(entityName="document/upload",
                                    query={
                                        "entityName": self.entityName, 
                                        "entityId": self.entityId, 
                                        "name": name},
                                    body=file)
        except WeclappError as e:
            if e.isOptimisticLock:
                logging.error(f"Optimistic Locking Error while uploading File {name}... retrying")
                time.sleep(1)
                response = weclapp.POST(entityName="document/upload",
                        query={
                            "entityName": self.entityName, 
                            "entityId": self.entityId, 
                            "name": name},
                        body=file)
            else:
                raise e

        # update Description
        doc = Document(**response)
        doc.setDescription(docType=docType)
        doc.updateDescription()
        return doc
    
    
    def getDocumentFiles(self,
                   docType: config.ALLOWED_DOC_TYPES_LITERAL,
                   docFormat: config.ALLOWED_DOC_FORMATS,
                   by:Literal['all', 'latest']) -> Tuple[List[io.BytesIO], List[str]]:
        """downloads all documents of a given type and format and returns them as a list of BytesIO objects"""
        # ensure Nameing Convention
        _, docType = Document.documentNamingConvention(docType=docType, docFormat=docFormat, fullName='')
        logging.info(f"Getting Document files {docType=} {docFormat=} {by=}")
        # get All documents
        if not self.documents:
            self.getDocuments()
        
        relevantDocs:List[Document] = []
        latestDoc = None
        for doc in self.documents:
            # check if format specified
            if docFormat in doc.name and doc.description and doc.description.docType == docType:
                logging.info(f"doument found Document name={doc.name}")
                if by == 'all':
                    relevantDocs.append(doc)
                    
                elif by == 'latest':
                    if latestDoc is None or latestDoc.createdDate < doc.createdDate:
                        logging.info(f"doument found Document name={doc.name}")
                        latestDoc = doc

            # else:
            #     logging.warning(f"doument found with invalid docType {docFormat=} =! name={doc.name}")

        if by == 'latest' and latestDoc:
            relevantDocs.append(latestDoc)
            
        documents = []
        names = []
        logging.info('downloading Documents')
        for doc in relevantDocs:
            documents.append(doc.downloadDoc())
            names.append(doc.name)
            
        return documents, names

    
        
        
