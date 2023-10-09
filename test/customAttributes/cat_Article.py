import json
from collections import namedtuple

class CAT_Article:

	@staticmethod
	def is_namedtuple(obj):
		try:
			return isinstance(obj, tuple) and hasattr(obj, "_fields")
		except:
			return False

	def __init__(self, data:dict=None):
		if data is None:
			with open("test/customAttributes/customAttributes/catData_Article.json", "r") as f:
				data = json.load(f)


		# Article - Artikeleinheiten und Versandinformationen
		self.VsInfoVersandAnz         = namedtuple("VsInfoVersandAnz",          ["id", "valueName"])(**data["VsInfoVersandAnz"]) # 5211283
		self.VsInfoVersandEinheit     = namedtuple("VsInfoVersandEinheit",      ["id", "valueName", "PaletteLabel", "Palette", "Label", "UnbekannteEinheitUnbekannteEinheiten"])(**data["VsInfoVersandEinheit"]) # 5211310
		self.VsInfoArtikelEinheit     = namedtuple("VsInfoArtikelEinheit",      ["id", "valueName", "mlml", "ll", "gg", "kgkg", "mm", "cmcm", "StckStck", "TestTests", "BeutelBeutel", "SackScke", "MaskeMasken", "KittelKittel", "HandschuhHandschuhe", "PaarPaare", "FlascheFlaschen", "KanisterKanister", "PackungPackungen", "EimerEimer", "RolleRollen", "BindeBinden", "TuchTcher", "TupferTupfer", "KompresseKompressen", "BehlterBehlter", "TabTabs", "GertGerte", "BlattBltter", "SchwammSchwmme", "HaubeHauben", "BoxBoxen", "TascheTaschen", "KastenKasten", "DseDsen", "TeilTeile", "MeterMeter", "UnbekannteEinheitUnbekannteEinheiten"])(**data["VsInfoArtikelEinheit"]) # 5213586
		self.VsInfoKartonEinheit      = namedtuple("VsInfoKartonEinheit",       ["id", "valueName", "KartonKartons", "BeutelBeutel", "SackScke", "TragepackungTragepackungen", "KanisterKanister", "BndelBndel", "UnbekannteEinheitUnbekannteEinheiten"])(**data["VsInfoKartonEinheit"]) # 5211018
		self.articlePercentageOfLabel = namedtuple("articlePercentageOfLabel",  ["id", "valueName"])(**data["articlePercentageOfLabel"]) # 52575402
		self.VsInfoPackEinheit        = namedtuple("VsInfoPackEinheit",         ["id", "valueName", "BeutelBeutel", "BundBund", "BndelBndel", "DoseDosen", "EimerEimer", "FaltschachtelFaltschachteln", "FlascheFlaschen", "GertGerte", "HalterHalter", "KanisterKanister", "KitKits", "KofferKoffer", "LiterLiter", "PackungPackungen", "PuppePuppen", "RolleRollen", "SackScke", "SchachtelSchachteln", "SchrankSchrnke", "ServietteServietten", "SetSet", "SetSets", "SoftpackSoftpacks", "SpenderSpender", "StckStck", "TascheTaschen", "TubeTuben", "UnbekannteEinheitUnbekannteEinheiten", "WanneWannen", "kgkg"])(**data["VsInfoPackEinheit"]) # 5210753
		self.VsInfoEbenenString       = namedtuple("VsInfoEbenenString",        ["id", "valueName"])(**data["VsInfoEbenenString"]) # 5211548
		self.VsInfoPackAnz            = namedtuple("VsInfoPackAnz",             ["id", "valueName"])(**data["VsInfoPackAnz"]) # 5210736
		self.VsInfoKartonAnz          = namedtuple("VsInfoKartonAnz",           ["id", "valueName"])(**data["VsInfoKartonAnz"]) # 5210860
		self.VsInfoEbene              = namedtuple("VsInfoEbene",               ["id", "valueName", "Artikel", "Packung", "Karton", "Versand", "Keine"])(**data["VsInfoEbene"]) # 5211352
		self.VsInfoArtikelNum         = namedtuple("VsInfoArtikelNum",          ["id", "valueName"])(**data["VsInfoArtikelNum"]) # 5208433

		# Article - Automation
		self.excludedCheck24          = namedtuple("excludedCheck24",           ["id", "valueName"])(**data["excludedCheck24"]) # 23599012
		self.shippingClass            = namedtuple("shippingClass",             ["id", "valueName"])(**data["shippingClass"]) # 26441872
		self.excludedMetro            = namedtuple("excludedMetro",             ["id", "valueName"])(**data["excludedMetro"]) # 24172715
		self.amazonManufacturer       = namedtuple("amazonManufacturer",        ["id", "valueName"])(**data["amazonManufacturer"]) # 59243154
		self.excludedAmazon           = namedtuple("excludedAmazon",            ["id", "valueName"])(**data["excludedAmazon"]) # 23598615
		self.versandArt               = namedtuple("versandArt",                ["id", "valueName", "X3€", "X4€", "X4,50€", "X5€", "X6€", "X2", "X3", "X4", "X5", "X1"])(**data["versandArt"]) # 25290810
		self.excludedEbay             = namedtuple("excludedEbay",              ["id", "valueName"])(**data["excludedEbay"]) # 23598731
		self.excludedShopApotheke     = namedtuple("excludedShopApotheke",      ["id", "valueName"])(**data["excludedShopApotheke"]) # 23598826
		self.excludedOtto             = namedtuple("excludedOtto",              ["id", "valueName"])(**data["excludedOtto"]) # 23599029
		self.amazonCategory           = namedtuple("amazonCategory",            ["id", "valueName"])(**data["amazonCategory"]) # 60702681
		self.famId                    = namedtuple("famId",                     ["id", "valueName"])(**data["famId"]) # 24463329
		self.excludedHood             = namedtuple("excludedHood",              ["id", "valueName"])(**data["excludedHood"]) # 23598813
		self.shopapothekePricing      = namedtuple("shopapothekePricing",       ["id", "valueName"])(**data["shopapothekePricing"]) # 58038422
		self.amazonBrand              = namedtuple("amazonBrand",               ["id", "valueName"])(**data["amazonBrand"]) # 59243075
		self.eanAmazon                = namedtuple("eanAmazon",                 ["id", "valueName"])(**data["eanAmazon"]) # 34627770
		self.excludedKaufland         = namedtuple("excludedKaufland",          ["id", "valueName"])(**data["excludedKaufland"]) # 23598752
		self.ARTICLE_TYPE_OF_PRODUCT  = namedtuple("ARTICLE_TYPE_OF_PRODUCT",   ["id", "valueName", "Ware", "Dienstleistung"])(**data["ARTICLE_TYPE_OF_PRODUCT"]) # 3628377
		self.marketplaceCartFaktor    = namedtuple("marketplaceCartFaktor",     ["id", "valueName"])(**data["marketplaceCartFaktor"]) # 33874718

		# Article - Einkauf
		self.dispoMinMax              = namedtuple("dispoMinMax",               ["id", "valueName"])(**data["dispoMinMax"]) # 44253602
		self.ekPriceDefault           = namedtuple("ekPriceDefault",            ["id", "valueName"])(**data["ekPriceDefault"]) # 26144201
		self.inventoryLevelGross      = namedtuple("inventoryLevelGross",       ["id", "valueName"])(**data["inventoryLevelGross"]) # 23072493
		self.ekPriceDyn               = namedtuple("ekPriceDyn",                ["id", "valueName"])(**data["ekPriceDyn"]) # 23072955
		self.inventoryLevelNet        = namedtuple("inventoryLevelNet",         ["id", "valueName"])(**data["inventoryLevelNet"]) # 23072998
		self.availabilityTimeManu     = namedtuple("availabilityTimeManu",      ["id", "valueName"])(**data["availabilityTimeManu"]) # 26464385
		self.gebundesKapital          = namedtuple("gebundesKapital",           ["id", "valueName"])(**data["gebundesKapital"]) # 16353419
		self.alternativeMpn           = namedtuple("alternativeMpn",            ["id", "valueName"])(**data["alternativeMpn"]) # 29797748
		self.dispoTool                = namedtuple("dispoTool",                 ["id", "valueName"])(**data["dispoTool"]) # 12342327
		self.stockToTarget            = namedtuple("stockToTarget",             ["id", "valueName"])(**data["stockToTarget"]) # 57108269
		self.availabilityTime         = namedtuple("availabilityTime",          ["id", "valueName", "Sofort", "D3", "D5", "D7", "D10", "D14", "D21", "D28", "D60", "D90"])(**data["availabilityTime"]) # 26457250

		# Article - Flow Aktionen
		self.weclappError             = namedtuple("weclappError",              ["id", "valueName", "MIP_declined", "NoBilling", "MissingData", "Else", "OK", "UnknownType", "NotPermitted", "WrongData", "Permit_failed", "MIP_modified", "Cancelled", "MIP_rejected", "MIP_new", "Fraud", "ExternalStatus", "Ads", "Warning", "Note", "ValidationError", "FlowFailed", "SyncFailed", "NotDue"])(**data["weclappError"]) # 16601935
		self.LoopVersion              = namedtuple("LoopVersion",               ["id", "valueName"])(**data["LoopVersion"]) # 14568660
		self.errorMessages            = namedtuple("errorMessages",             ["id", "valueName"])(**data["errorMessages"]) # 23781824
		self.articleActions           = namedtuple("articleActions",            ["id", "valueName", "CreateSalesList"])(**data["articleActions"]) # 41953259
		self.createNewSBArticle       = namedtuple("createNewSBArticle",        ["id", "valueName"])(**data["createNewSBArticle"]) # 42135008
		self.actionLog                = namedtuple("actionLog",                 ["id", "valueName"])(**data["actionLog"]) # 16608320
		self.just4Testing             = namedtuple("just4Testing",              ["id", "valueName"])(**data["just4Testing"]) # 24523768

		# Article - Pharma Daten
		self.sprechstundenbedarf      = namedtuple("sprechstundenbedarf",       ["id", "valueName"])(**data["sprechstundenbedarf"]) # 16191192
		self.aidPosNumber             = namedtuple("aidPosNumber",              ["id", "valueName"])(**data["aidPosNumber"]) # 17313403
		self.pboxWeight               = namedtuple("pboxWeight",                ["id", "valueName"])(**data["pboxWeight"]) # 17314244
		self.bauaNummer               = namedtuple("bauaNummer",                ["id", "valueName"])(**data["bauaNummer"]) # 36397617
		self.contractItemGroup        = namedtuple("contractItemGroup",         ["id", "valueName", "PG54", "PG51", "PG15", "InkoSample"])(**data["contractItemGroup"]) # 16604713
		self.PZN                      = namedtuple("PZN",                       ["id", "valueName"])(**data["PZN"]) # 4983654

		# Article - Preisgestaltung
		self.clearanceFinancialDiscount= namedtuple("clearanceFinancialDiscount", ["id", "valueName"])(**data["clearanceFinancialDiscount"]) # 56723791
		self.ekPriceManu              = namedtuple("ekPriceManu",               ["id", "valueName"])(**data["ekPriceManu"]) # 8661018
		self.financialDiscount        = namedtuple("financialDiscount",         ["id", "valueName"])(**data["financialDiscount"]) # 28307238
		self.priceScaleQuantity       = namedtuple("priceScaleQuantity",        ["id", "valueName"])(**data["priceScaleQuantity"]) # 23073798
		self.vkPriceDyn               = namedtuple("vkPriceDyn",                ["id", "valueName"])(**data["vkPriceDyn"]) # 8759685
		self.sjThirdColumn            = namedtuple("sjThirdColumn",             ["id", "valueName"])(**data["sjThirdColumn"]) # 33681583
		self.shippingCost             = namedtuple("shippingCost",              ["id", "valueName"])(**data["shippingCost"]) # 23073697
		self.percentagePriceRules     = namedtuple("percentagePriceRules",      ["id", "valueName"])(**data["percentagePriceRules"]) # 33677123
		self.priceScaleType           = namedtuple("priceScaleType",            ["id", "valueName"])(**data["priceScaleType"]) # 23073850
		self.priceScaleStep           = namedtuple("priceScaleStep",            ["id", "valueName"])(**data["priceScaleStep"]) # 28304277
		self.financialYield           = namedtuple("financialYield",            ["id", "valueName"])(**data["financialYield"]) # 23073429
		self.vkPriceManu              = namedtuple("vkPriceManu",               ["id", "valueName"])(**data["vkPriceManu"]) # 23073376

		# Article - Shop
		self.unitPriceBaseMeasure     = namedtuple("unitPriceBaseMeasure",      ["id", "valueName"])(**data["unitPriceBaseMeasure"]) # 17530775
		self.customTitle              = namedtuple("customTitle",               ["id", "valueName"])(**data["customTitle"]) # 22728607
		self.LinkBild                 = namedtuple("LinkBild",                  ["id", "valueName"])(**data["LinkBild"]) # 17535769
		self.LinkShop                 = namedtuple("LinkShop",                  ["id", "valueName"])(**data["LinkShop"]) # 7073904
		self.unitPricingMeasure       = namedtuple("unitPricingMeasure",        ["id", "valueName"])(**data["unitPricingMeasure"]) # 17530711
		self.wooProductId             = namedtuple("wooProductId",              ["id", "valueName"])(**data["wooProductId"]) # 23486352
		self.kurzbeschreibung         = namedtuple("kurzbeschreibung",          ["id", "valueName"])(**data["kurzbeschreibung"]) # 4986635

		# Article - other
		self.X8610if0vh2ndd7d6al      = namedtuple("X8610if0vh2ndd7d6al",       ["id", "valueName"])(**data["X8610if0vh2ndd7d6al"]) # 8611
		self.X45569263i3tfdrhqqj1hpt  = namedtuple("X45569263i3tfdrhqqj1hpt",   ["id", "valueName"])(**data["X45569263i3tfdrhqqj1hpt"]) # 45569274
		self.X1527226i9bof8118sgsim   = namedtuple("X1527226i9bof8118sgsim",    ["id", "valueName"])(**data["X1527226i9bof8118sgsim"]) # 1527232
		self.X45569263i9p9kss9dgi5v4  = namedtuple("X45569263i9p9kss9dgi5v4",   ["id", "valueName"])(**data["X45569263i9p9kss9dgi5v4"]) # 45569270
		self.X7646100i8cheb0omskl79   = namedtuple("X7646100i8cheb0omskl79",    ["id", "valueName"])(**data["X7646100i8cheb0omskl79"]) # 22982509
		self.X1527226if0ucjo8bfabqi   = namedtuple("X1527226if0ucjo8bfabqi",    ["id", "valueName"])(**data["X1527226if0ucjo8bfabqi"]) # 1527230
		self.X1527226ibgqf0a2ns7j00   = namedtuple("X1527226ibgqf0a2ns7j00",    ["id", "valueName"])(**data["X1527226ibgqf0a2ns7j00"]) # 1527229
		self.X7646100i3qcise0ij710r   = namedtuple("X7646100i3qcise0ij710r",    ["id", "valueName"])(**data["X7646100i3qcise0ij710r"]) # 26423400
		self.X7646100i6vjtmhn8vhtc    = namedtuple("X7646100i6vjtmhn8vhtc",     ["id", "valueName"])(**data["X7646100i6vjtmhn8vhtc"]) # 26236091
		self.X7646100i8i0kvd8dcgqen   = namedtuple("X7646100i8i0kvd8dcgqen",    ["id", "valueName"])(**data["X7646100i8i0kvd8dcgqen"]) # 26326071
		self.X1527226i7754oph3j3geb   = namedtuple("X1527226i7754oph3j3geb",    ["id", "valueName"])(**data["X1527226i7754oph3j3geb"]) # 1527227
		self.FORMER_SERVICE           = namedtuple("FORMER_SERVICE",            ["id", "valueName"])(**data["FORMER_SERVICE"]) # 2174360
		self.X45569263id3vm8jeafl0it  = namedtuple("X45569263id3vm8jeafl0it",   ["id", "valueName"])(**data["X45569263id3vm8jeafl0it"]) # 45569272
		self.X45569263i7knfapjm30rjn  = namedtuple("X45569263i7knfapjm30rjn",   ["id", "valueName"])(**data["X45569263i7knfapjm30rjn"]) # 45569268
		self.X7646100ia28ne3gmed2dr   = namedtuple("X7646100ia28ne3gmed2dr",    ["id", "valueName"])(**data["X7646100ia28ne3gmed2dr"]) # 26423399
		self.X12718588iatgv2funl0u8l  = namedtuple("X12718588iatgv2funl0u8l",   ["id", "valueName"])(**data["X12718588iatgv2funl0u8l"]) # 22982508
		self.X45569263ibahgngi20rqqa  = namedtuple("X45569263ibahgngi20rqqa",   ["id", "valueName"])(**data["X45569263ibahgngi20rqqa"]) # 45569264
		self.X8610ib1hekr2bg6vui      = namedtuple("X8610ib1hekr2bg6vui",       ["id", "valueName"])(**data["X8610ib1hekr2bg6vui"]) # 8613
		self.X1527226i7v8amo88ogn06   = namedtuple("X1527226i7v8amo88ogn06",    ["id", "valueName"])(**data["X1527226i7v8amo88ogn06"]) # 1527228
		self.X7646100iuhhgnkgn1rbm    = namedtuple("X7646100iuhhgnkgn1rbm",     ["id", "valueName"])(**data["X7646100iuhhgnkgn1rbm"]) # 26205446
		self.X8610i4l3pivfenq70h      = namedtuple("X8610i4l3pivfenq70h",       ["id", "valueName"])(**data["X8610i4l3pivfenq70h"]) # 291457
		self.X1527226i6ctq7b7daedtk   = namedtuple("X1527226i6ctq7b7daedtk",    ["id", "valueName"])(**data["X1527226i6ctq7b7daedtk"]) # 1527231
		self.X7646100i59pu1h831k8go   = namedtuple("X7646100i59pu1h831k8go",    ["id", "valueName"])(**data["X7646100i59pu1h831k8go"]) # 26162197
		self.X12718588i64evdjqaaf7do  = namedtuple("X12718588i64evdjqaaf7do",   ["id", "valueName"])(**data["X12718588i64evdjqaaf7do"]) # 26162196
		self.X8610iasan9qd3559uj      = namedtuple("X8610iasan9qd3559uj",       ["id", "valueName"])(**data["X8610iasan9qd3559uj"]) # 8612
		self.X7646100ifeh1cq2bf7i4h   = namedtuple("X7646100ifeh1cq2bf7i4h",    ["id", "valueName"])(**data["X7646100ifeh1cq2bf7i4h"]) # 26205447
		self.X7646100iapl7dfs108a91   = namedtuple("X7646100iapl7dfs108a91",    ["id", "valueName"])(**data["X7646100iapl7dfs108a91"]) # 26326072
		self.X45569263i191lgvcclqd1c  = namedtuple("X45569263i191lgvcclqd1c",   ["id", "valueName"])(**data["X45569263i191lgvcclqd1c"]) # 45569266
		self.X7646100i2k7ra51g8pntf   = namedtuple("X7646100i2k7ra51g8pntf",    ["id", "valueName"])(**data["X7646100i2k7ra51g8pntf"]) # 26236090
