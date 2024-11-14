import requests
import json
import logging
from . import config


class WeclappError(Exception):
    def __init__(self, errorResponse: requests.Response):
        self.response = errorResponse
        self.fullLog = False
        try:
            errorResponse = self.response.json()
            self.detail = errorResponse.get("detail", "No detail found")
            self.error = errorResponse.get("error", "No error found")
            self.status = errorResponse.get("status", 400)
            self.title = errorResponse.get("title", "No title found")
            self.errorType = errorResponse.get("type", "No type found")
            self.validationErrors = errorResponse.get("validationErrors", [])
            self.messages = errorResponse.get("messages", [])
            self.isJson = True
            self.url = str(self.response.url).split(f"/api/{config.API_VERSION}")[-1]
        except json.JSONDecodeError:
            self.detail = errorResponse.text
            self.isJson = False

        super().__init__(self.detail)

    @property
    def isOptimisticLock(self) -> bool:
        if self.detail == config.OPTIMISTIC_LOCK_IDENTIFIER:
            logging.error("Optimistic Loc error Found...")
            return True
        return False

    @property
    def hasWrongStatus(self) -> bool:
        if config.HAS_WRONG_STATUS_IDENTIFIER in str(self.messages):
            logging.error("Wrong Status error...")
            return True
        return False

    def __str__(self) -> str:
        if self.isJson:
            if not self.fullLog:
                errorMessage = f"{self.title} at {self.url} with {self.response.status_code}: {self.error}:"
                for message in self.messages:
                    if isinstance(message, dict):
                        errorMessage += (
                            f"\n\t\t{message.get('severity')}={message.get('message')};"
                        )
                for message in self.validationErrors:
                    errorMessage += f"\n\t\t{message};"
                return errorMessage
            else:
                errorMessage = (
                    f"{self.title} with {self.response.status_code}: {self.error}: "
                )

                errorMessage += f"\n\t{self.response.text};"

                return errorMessage
        return f"{self.response.status_code}: {self.detail}"
