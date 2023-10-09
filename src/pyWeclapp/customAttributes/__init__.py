import json
from .task import CAT_Task
from .article import CAT_Article

class CAT(CAT_Task, CAT_Article):
    
    def __init__(self):
        with open("util/customAttributes/attributeData.json", "r") as f:
            data = json.load(f)
            
        CAT_Task.__init__(self, data)
        CAT_Article.__init__(self, data)


        # Mappers
        # self.taskPermitStatus_NameMapper = {
        #     self.taskPermitStatus.current: "current",
        #     self.taskPermitStatus.future: "future",
        #     self.taskPermitStatus.past: "past",
        #     self.taskPermitStatus.cancelled: "cancelled",
        #     self.taskPermitStatus.inactive: "inactive"
        #     }
        
        self.taskPermitInterval_IntMapper = {
            self.taskPermitInterval.Month : 1, 
            self.taskPermitInterval.Quarter : 3,
            self.taskPermitInterval.Semiannual : 6,
            self.taskPermitInterval.Annual : 12
        }
        
    @staticmethod
    def is_namedtuple(obj):
        try:
            return isinstance(obj, tuple) and hasattr(obj, "_fields")
        except:
            return False