"""This code was dynamically created using WeclappClassCreator from pyweclapp"""

from typing import Union
from .blueprints import Blueprint


class Currency(Blueprint):
    id: Union[str, None] = None
    createdDate: Union[int, None] = None
    lastModifiedDate: Union[int, None] = None
    version: Union[str, None] = None
    currencySymbol: Union[str, None] = None
    name: Union[str, None] = None
