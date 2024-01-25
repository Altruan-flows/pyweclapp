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
			with open("src/pyWeclapp/examples/customAttributes/catData/SalesOrder.json", "r") as f:
				data = json.load(f)


		# Abw. WhiteLabel Einstellungen
		self.whiteLabelCity           = namedtuple("whiteLabelCity",            ["id", "valueName"])(**data["whiteLabelCity"]) # 12602749
		self.whiteLabelAddress        = namedtuple("whiteLabelAddress",         ["id", "valueName"])(**data["whiteLabelAddress"]) # 12602505
		self.whiteLabelSender         = namedtuple("whiteLabelSender",          ["id", "valueName"])(**data["whiteLabelSender"]) # 12602239
		self.whiteLabelNotiz          = namedtuple("whiteLabelNotiz",           ["id", "valueName"])(**data["whiteLabelNotiz"]) # 9723902
		self.whitelabelVersand        = namedtuple("whitelabelVersand",         ["id", "valueName"])(**data["whitelabelVersand"]) # 9407397

		# Automation
		self.SalesOrderActions        = namedtuple("SalesOrderActions",         ["id", "valueName", "LieferungSplitten"])(**data["SalesOrderActions"]) # 76242754
		self.loopLoc                  = namedtuple("loopLoc",                   ["id", "valueName"])(**data["loopLoc"]) # 31395449

		# Flow Aktionen
		self.errorMessages            = namedtuple("errorMessages",             ["id", "valueName"])(**data["errorMessages"]) # 23781824
		self.actionLog                = namedtuple("actionLog",                 ["id", "valueName"])(**data["actionLog"]) # 16608320
		self.weclappError             = namedtuple("weclappError",              ["id", "valueName", "MIP_declined", "NoBilling", "MissingData", "Else", "OK", "UnknownType", "NotPermitted", "WrongData", "Permit_failed", "MIP_modified", "Cancelled", "MIP_rejected", "MIP_new", "Fraud", "ExternalStatus", "Ads", "Warning", "Note", "ValidationError", "FlowFailed", "SyncFailed", "NotDue"])(**data["weclappError"]) # 16601935
		self.just4Testing             = namedtuple("just4Testing",              ["id", "valueName"])(**data["just4Testing"]) # 24523768
		self.LoopVersion              = namedtuple("LoopVersion",               ["id", "valueName"])(**data["LoopVersion"]) # 14568660

		# Flow Fehler Finder
		self.actionsPerformedSalesOrders= namedtuple("actionsPerformedSalesOrders", ["id", "valueName", "Gclidhochgeladen", "AuftragskomplettworkflowmitRckstellung", "Auftragskomplettworkflow", "RechnungzuMarktplatzhochgeladen", "KostenHinzugefgt", "AuftragZurckgestellt", "Ticketerstellt", "KlavioUpload", "NachrichtanUmsatzfeedwurdegesendet"])(**data["actionsPerformedSalesOrders"]) # 31281788

		# ITEMS_Artikeleinheiten und Versandinformationen
		self.VsInfoEbenenString       = namedtuple("VsInfoEbenenString",        ["id", "valueName"])(**data["VsInfoEbenenString"]) # 5211548
		self.VsInfoEbene              = namedtuple("VsInfoEbene",               ["id", "valueName", "Artikel", "Packung", "Karton", "Versand", "Keine"])(**data["VsInfoEbene"]) # 5211352
		self.articlePercentageOfLabel = namedtuple("articlePercentageOfLabel",  ["id", "valueName"])(**data["articlePercentageOfLabel"]) # 52575402

		# ITEMS_Automation
		self.shopapothekePricing      = namedtuple("shopapothekePricing",       ["id", "valueName"])(**data["shopapothekePricing"]) # 58038422
		self.versandArt               = namedtuple("versandArt",                ["id", "valueName", "v_3", "v_4", "v_450", "v_5", "v_6", "v_2", "v_1"])(**data["versandArt"]) # 25290810

		# ITEMS_Einkauf
		self.alternativeMpn           = namedtuple("alternativeMpn",            ["id", "valueName"])(**data["alternativeMpn"]) # 29797748

		# ITEMS_Pharma Daten
		self.sprechstundenbedarf      = namedtuple("sprechstundenbedarf",       ["id", "valueName"])(**data["sprechstundenbedarf"]) # 16191192
		self.contractItemGroup        = namedtuple("contractItemGroup",         ["id", "valueName", "PG54", "PG51", "PG15", "InkoSample"])(**data["contractItemGroup"]) # 16604713
		self.aidPosNumber             = namedtuple("aidPosNumber",              ["id", "valueName"])(**data["aidPosNumber"]) # 17313403
		self.pboxWeight               = namedtuple("pboxWeight",                ["id", "valueName"])(**data["pboxWeight"]) # 17314244
		self.PZN                      = namedtuple("PZN",                       ["id", "valueName"])(**data["PZN"]) # 4983654

		# ITEMS_Preisgestaltung
		self.clearanceFinancialDiscount= namedtuple("clearanceFinancialDiscount", ["id", "valueName"])(**data["clearanceFinancialDiscount"]) # 56723791

		# ITEMS_Shop
		self.wooProductId             = namedtuple("wooProductId",              ["id", "valueName"])(**data["wooProductId"]) # 23486352

		# Logistik App
		self.rueckstellungsDatum      = namedtuple("rueckstellungsDatum",       ["id", "valueName"])(**data["rueckstellungsDatum"]) # 21213686

		# Referenzen
		self.originalEntity           = namedtuple("originalEntity",            ["id", "valueName"])(**data["originalEntity"]) # 17000528
		self.isMasterContract         = namedtuple("isMasterContract",          ["id", "valueName"])(**data["isMasterContract"]) # 24184084
		self.masterContract           = namedtuple("masterContract",            ["id", "valueName"])(**data["masterContract"]) # 24183186

		# Retouren / Reklamation
		self.Picker                   = namedtuple("Picker",                    ["id", "valueName", "N02GGGeaninaChiorean", "N03TWThorstenWeindl", "N04JEJannisEicher", "N05ChristophHaslbeck", "N06NiklasHellenbarth", "N07ManuelHammerstingl", "N08TinaKerscher", "N09JudithRadl", "N10LauraHrhaber", "v_36", "N12WoldemarLoginow", "N13Ali", "N14AlexRadl", "N15FelixPlankl"])(**data["Picker"]) # 4963782
		self.ResponsiblePacker        = namedtuple("ResponsiblePacker",         ["id", "valueName", "N02GGGeaninaChiorean", "N03TWThorstenWeindl", "N04JEJannisEicher", "N05ChristophHaslbeck", "N06NiklasHellenbarth", "N07ManuelHammerstingl", "N08TinaKerscher", "N09JudithRadl", "N10LauraHrhaber", "N12WoldemarLoginow", "N13Ali", "N14AlexRadl", "N15FelixPlankl"])(**data["ResponsiblePacker"]) # 4963830
		self.returnedGoodsActionDescriptions= namedtuple("returnedGoodsActionDescriptions", ["id", "valueName"])(**data["returnedGoodsActionDescriptions"]) # 4678470
		self.returnedGoodsDescription = namedtuple("returnedGoodsDescription",  ["id", "valueName"])(**data["returnedGoodsDescription"]) # 4664053
		self.returnedGoodsReason      = namedtuple("returnedGoodsReason",       ["id", "valueName", "nichtausPackstationabgeholt", "WaredurchTransportbeschdigt", "Kundenrcksendung", "ZulangeLieferzeit", "Empfngernichtermittelt", "FalschesProduktgeliefert", "PaketabgelehntKundewillnichtmehr", "KundehatPaketvonanderemKundenerhalten", "Zuweniggeliefert", "Waredefekt", "Versandbedingungen", "Doppelbestellung", "Paketwurdenichtversandt", "falscheAdressangabe", "Packstationnichtkorrektangegeben", "DHLFehler"])(**data["returnedGoodsReason"]) # 4663977
		self.returnedGoodsAction      = namedtuple("returnedGoodsAction",       ["id", "valueName", "NeuversandzuzglichVersandkosten", "SendungneuerWare", "Kundekontaktiert", "Gutschrifterstellt", "Betragrckerstattet", "Nachsendung", "Nichts", "Storniert", "FehlendeWarewirdnachversandt", "ErstattetabzglichVersandkosten"])(**data["returnedGoodsAction"]) # 4664235
		self.returnedGoodsDate        = namedtuple("returnedGoodsDate",         ["id", "valueName"])(**data["returnedGoodsDate"]) # 4679020

		# Shop Meta Daten
		self.offlineConversion        = namedtuple("offlineConversion",         ["id", "valueName"])(**data["offlineConversion"]) # 13129390
		self.idAuftragWoo             = namedtuple("idAuftragWoo",              ["id", "valueName"])(**data["idAuftragWoo"]) # 18041919
		self.ShopKommentar            = namedtuple("ShopKommentar",             ["id", "valueName"])(**data["ShopKommentar"]) # 8691
		self.utmSource                = namedtuple("utmSource",                 ["id", "valueName"])(**data["utmSource"]) # 13129088
		self.TicketSystemLog          = namedtuple("TicketSystemLog",           ["id", "valueName"])(**data["TicketSystemLog"]) # 10392722
		self.glcid                    = namedtuple("glcid",                     ["id", "valueName"])(**data["glcid"]) # 4157692
		self.customerUserAgent        = namedtuple("customerUserAgent",         ["id", "valueName"])(**data["customerUserAgent"]) # 3708258
		self.shopLandingPage          = namedtuple("shopLandingPage",           ["id", "valueName"])(**data["shopLandingPage"]) # 96940816
		self.EU_VTA                   = namedtuple("EU_VTA",                    ["id", "valueName"])(**data["EU_VTA"]) # 3813213
		self.shop_kanal               = namedtuple("shop_kanal",                ["id", "valueName"])(**data["shop_kanal"]) # 16054458
		self.linkAuftrag              = namedtuple("linkAuftrag",               ["id", "valueName"])(**data["linkAuftrag"]) # 18040079
		self.ShopTransaktionsID       = namedtuple("ShopTransaktionsID",        ["id", "valueName"])(**data["ShopTransaktionsID"]) # 8676
		self.landing_page             = namedtuple("landing_page",              ["id", "valueName"])(**data["landing_page"]) # 4157903

		# Versand
		self.VersandArt               = namedtuple("VersandArt",                ["id", "valueName"])(**data["VersandArt"]) # 5259530
		self.marketPlaceId            = namedtuple("marketPlaceId",             ["id", "valueName"])(**data["marketPlaceId"]) # 24344199
		self.VersandLabelsAnz         = namedtuple("VersandLabelsAnz",          ["id", "valueName"])(**data["VersandLabelsAnz"]) # 5241354
		self.VersandID                = namedtuple("VersandID",                 ["id", "valueName"])(**data["VersandID"]) # 5264608
		self.VersandStatusPlus        = namedtuple("VersandStatusPlus",         ["id", "valueName"])(**data["VersandStatusPlus"]) # 5264748
		self.VersandGeplant           = namedtuple("VersandGeplant",            ["id", "valueName"])(**data["VersandGeplant"]) # 5260043
		self.VersandStatus            = namedtuple("VersandStatus",             ["id", "valueName"])(**data["VersandStatus"]) # 5259755
		self.metroID                  = namedtuple("metroID",                   ["id", "valueName"])(**data["metroID"]) # 41881869
		self.VersandLabelsRecieved    = namedtuple("VersandLabelsRecieved",     ["id", "valueName"])(**data["VersandLabelsRecieved"]) # 5241472
		self.Versanddatum             = namedtuple("Versanddatum",              ["id", "valueName"])(**data["Versanddatum"]) # 5260019

		# Vertrieb
		self.anzahlMitarbeiter        = namedtuple("anzahlMitarbeiter",         ["id", "valueName"])(**data["anzahlMitarbeiter"]) # 17744750
		self.erstkontaktvertriebdatum = namedtuple("erstkontaktvertriebdatum",  ["id", "valueName"])(**data["erstkontaktvertriebdatum"]) # 15493960
		self.brancheShop              = namedtuple("brancheShop",               ["id", "valueName"])(**data["brancheShop"]) # 17751779
		self.vertriebkontaktstatus    = namedtuple("vertriebkontaktstatus",     ["id", "valueName", "KeineAktion", "Nichterreicht", "KeinInteresse", "AktivesAccountmanagement", "InBearbeitung"])(**data["vertriebkontaktstatus"]) # 15493188

		# Zahlung
		self.daysToPayment            = namedtuple("daysToPayment",             ["id", "valueName"])(**data["daysToPayment"]) # 5056302
		self.Mahnstufe                = namedtuple("Mahnstufe",                 ["id", "valueName", "Rechnungversendet", "nach14Tagen", "nach21Tagen", "nach28Tagen", "nach35Tagen", "nach42Tage"])(**data["Mahnstufe"]) # 5056455

		# other
		self.invoiceComment           = namedtuple("invoiceComment",            ["id", "valueName"])(**data["invoiceComment"]) # 13225320
		self.ignoreForDispoTool       = namedtuple("ignoreForDispoTool",        ["id", "valueName"])(**data["ignoreForDispoTool"]) # 57074259
		self.permitIdReference        = namedtuple("permitIdReference",         ["id", "valueName"])(**data["permitIdReference"]) # 50852810
