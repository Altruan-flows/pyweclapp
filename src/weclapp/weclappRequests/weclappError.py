import requests
import json
import logging

   
class WeclappError(Exception):
    def __init__(self, errorResponse:requests.Response):
        self.response = errorResponse
        self.fullLog = False
        try:
            errorResponse = self.response.json()
            self.detail = errorResponse.get('detail', "No detail Found")
            self.error = errorResponse.get('error', "No error Found")
            self.status = errorResponse.get('status', 400)
            self.title = errorResponse.get('title', "No title Found")
            self.type = errorResponse.get('type', "No type Found")
            self.validationErrors = errorResponse.get('validationErrors', [])
            self.messages = errorResponse.get('messages', [])
            self.isJson = True
            self.url = str(self.response.url)[41:]
        except json.JSONDecodeError:
            self.detail = errorResponse.text
            self.isJson = False

        super().__init__(self.detail)
    
    @property
    def isOptimisticLoc(self) -> bool:
        if self.detail == "optimistic lock error":
            logging.error(f"Optimistic Loc error Found...")
            return True
        return False
    
    @property
    def hasWrongStatus(self) -> bool:
        if "Sales order confirmation created" in str(self.messages):
            logging.error(f"Wrong Status error...")
            return True
        return False
    
    def __str__(self) -> str:
        if self.isJson:
            if not self.fullLog:
                s = f"{self.title} at {self.url} with {self.response.status_code}: {self.error}:"
                for el in self.messages:
                    s += f"\n\t\t{el['severity']}={el['message']};"
                for el in self.validationErrors:
                    s += f"\n\t\t{el};"
                return s
            else:
                s = f"{self.title} with {self.response.status_code}: {self.error}: "
                
                s += f"\n\t{self.response.text};"

                return s
        return f"{self.response.status_code}: {self.detail}"