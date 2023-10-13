from . import cat_SalesOrder
from . import cat_Settings
import json
# dynamic File please do not edit




class CAT(cat_SalesOrder.CAT_SalesOrder, cat_Settings.CAT_Settings):
	def __init__(self):
		with open("pyWeclapp/examples/cat/allCatData.json", "r") as f:
			self.data = json.load(f)
		super().__init__(self.data)




