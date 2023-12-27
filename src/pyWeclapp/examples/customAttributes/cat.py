from . import cat_Article
from . import cat_SalesOrder
from . import cat_Settings
import json
# dynamic File please do not edit


class CAT(cat_Article.CAT_Article, cat_SalesOrder.CAT_SalesOrder, cat_Settings.CAT_Settings):
	def __init__(self):
		with open("src/pyWeclapp/examples/customAttributes/catData/all.json", "r") as f:
			self.data = json.load(f)
		super().__init__(self.data)


