import json
from . import cat_Settings
from collections import namedtuple

class CAT_SalesOrder(cat_Settings.CAT_Settings):

	@staticmethod
	def is_namedtuple(obj):
		try:
			return isinstance(obj, tuple) and hasattr(obj, "_fields")
		except:
			return False

	def __init__(self, data:dict=None):
		super().__init__()
		if data is None:
			with open("pyWeclapp/examples/cat/catData_SalesOrder.json", "r") as f:
				data = json.load(f)


		# SalesOrder - Abw. WhiteLabel Einstellungen
		self.exampleAttribute        = namedtuple("exampleAttribute",         ["id", "valueName", "MySelectableOption"])(**data["exampleAttribute"]) # 1234

