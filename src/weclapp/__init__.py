# Keep imported at all Times!!!
from .weclappRequests import GET, POST, PUT, DELETE
from .weclappRequests.weclappError import WeclappError
from .legacyWeclappRequests import askWeclapp, updateWeclapp, deleteWeclapp, uploadFile, getDocumentFiles
from .iterator import iterator
from .legacyOrderCompleteWorkflow import orderCompleteWorkflow


# depricated, but still in use

from .customAttHandling_depricated import *
