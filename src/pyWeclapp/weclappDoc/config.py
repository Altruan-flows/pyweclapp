from typing import Literal


ALLOWED_DOC_TYPES = ['anlage2', 'anlage4', 'signature', 'pod', 'reciept', 'tzmo_LS', 'reciept2', '-', "kkDoc", "abrechnung"]
ALLOWED_DOC_TYPES_LITERAL = Literal['anlage2', 'anlage4', 'signature', 'pod', 'reciept', 'tzmo_LS', 'reciept2', '-', "kkDoc", "abrechnung"]
ALLOWED_DOC_FORMATS = ['pdf', 'png', 'tiff', "txt", 'jpg']
ALLOWED_DOC_FORMATS_LITERAL = Literal['pdf', 'png', 'tiff', "txt", 'jpg']
