import json
from . import cat_Settings
from collections import namedtuple


class CAT_Article(cat_Settings.CAT_Settings):

	@staticmethod
	def is_namedtuple(obj):
		try:
			return isinstance(obj, tuple) and hasattr(obj, "_fields")
		except:
			return False

	def __init__(self, data:dict=None):
		super().__init__()
		if data is None:
			with open("src/pyWeclapp/examples/customAttributes/catData/Article.json", "r") as f:
				data = json.load(f)


		# Artikeleinheiten und Versandinformationen
		self.VsInfoPackAnz            = namedtuple("VsInfoPackAnz",             ["id", "valueName"])(**data["VsInfoPackAnz"]) # 5210736
		self.VsInfoKartonEinheit      = namedtuple("VsInfoKartonEinheit",       ["id", "valueName", "KartonKartons", "BeutelBeutel", "SackScke", "TragepackungTragepackungen", "KanisterKanister", "BndelBndel", "UnbekannteEinheitUnbekannteEinheiten"])(**data["VsInfoKartonEinheit"]) # 5211018
		self.VsInfoVersandEinheit     = namedtuple("VsInfoVersandEinheit",      ["id", "valueName", "PaletteLabel", "Palette", "Label", "UnbekannteEinheitUnbekannteEinheiten"])(**data["VsInfoVersandEinheit"]) # 5211310
		self.eanCarton                = namedtuple("eanCarton",                 ["id", "valueName"])(**data["eanCarton"]) # 81809218
		self.eanPallet                = namedtuple("eanPallet",                 ["id", "valueName"])(**data["eanPallet"]) # 81809312
		self.pulpoBarcode2            = namedtuple("pulpoBarcode2",             ["id", "valueName"])(**data["pulpoBarcode2"]) # 101711024
		self.VsInfoPackEinheit        = namedtuple("VsInfoPackEinheit",         ["id", "valueName", "BeutelBeutel", "BundBund", "BndelBndel", "DoseDosen", "EimerEimer", "FaltschachtelFaltschachteln", "FlascheFlaschen", "GertGerte", "HalterHalter", "KanisterKanister", "KitKits", "KofferKoffer", "LiterLiter", "PackungPackungen", "PuppePuppen", "RolleRollen", "SackScke", "SchachtelSchachteln", "SchrankSchrnke", "ServietteServietten", "SetSet", "SetSets", "SoftpackSoftpacks", "SpenderSpender", "StckStck", "TascheTaschen", "TubeTuben", "WanneWannen", "kgkg"])(**data["VsInfoPackEinheit"]) # 5210753
		self.pulpoBarcode1            = namedtuple("pulpoBarcode1",             ["id", "valueName"])(**data["pulpoBarcode1"]) # 101710576
		self.eanPackage               = namedtuple("eanPackage",                ["id", "valueName"])(**data["eanPackage"]) # 81809126
		self.VsInfoEbenenString       = namedtuple("VsInfoEbenenString",        ["id", "valueName"])(**data["VsInfoEbenenString"]) # 5211548
		self.pulpoBarcode3            = namedtuple("pulpoBarcode3",             ["id", "valueName"])(**data["pulpoBarcode3"]) # 101711169
		self.VsInfoVersandAnz         = namedtuple("VsInfoVersandAnz",          ["id", "valueName"])(**data["VsInfoVersandAnz"]) # 5211283
		self.VsInfoArtikelNum         = namedtuple("VsInfoArtikelNum",          ["id", "valueName"])(**data["VsInfoArtikelNum"]) # 5208433
		self.articlePercentageOfLabel = namedtuple("articlePercentageOfLabel",  ["id", "valueName"])(**data["articlePercentageOfLabel"]) # 52575402
		self.pulpoBarcode4            = namedtuple("pulpoBarcode4",             ["id", "valueName"])(**data["pulpoBarcode4"]) # 101711221
		self.eanArticle               = namedtuple("eanArticle",                ["id", "valueName"])(**data["eanArticle"]) # 81808996
		self.VsInfoKartonAnz          = namedtuple("VsInfoKartonAnz",           ["id", "valueName"])(**data["VsInfoKartonAnz"]) # 5210860
		self.VsInfoArtikelEinheit     = namedtuple("VsInfoArtikelEinheit",      ["id", "valueName", "mlml", "ll", "gg", "kgkg", "mm", "cmcm", "StckStck", "TestTests", "BeutelBeutel", "SackScke", "MaskeMasken", "KittelKittel", "HandschuhHandschuhe", "PaarPaare", "FlascheFlaschen", "KanisterKanister", "PackungPackungen", "EimerEimer", "RolleRollen", "BindeBinden", "TuchTcher", "TupferTupfer", "KompresseKompressen", "BehlterBehlter", "TabTabs", "GertGerte", "BlattBltter", "SchwammSchwmme", "HaubeHauben", "BoxBoxen", "TascheTaschen", "KastenKasten", "DseDsen", "TeilTeile", "MeterMeter", "SetSets"])(**data["VsInfoArtikelEinheit"]) # 5213586
		self.VsInfoEbene              = namedtuple("VsInfoEbene",               ["id", "valueName", "Artikel", "Packung", "Karton", "Versand", "Keine"])(**data["VsInfoEbene"]) # 5211352

		# Automation
		self.excludedMetro            = namedtuple("excludedMetro",             ["id", "valueName"])(**data["excludedMetro"]) # 24172715
		self.shippingClass            = namedtuple("shippingClass",             ["id", "valueName"])(**data["shippingClass"]) # 26441872
		self.ARTICLE_TYPE_OF_PRODUCT  = namedtuple("ARTICLE_TYPE_OF_PRODUCT",   ["id", "valueName", "Ware", "Dienstleistung"])(**data["ARTICLE_TYPE_OF_PRODUCT"]) # 3628377
		self.excludedOtto             = namedtuple("excludedOtto",              ["id", "valueName"])(**data["excludedOtto"]) # 23599029
		self.excludedShopApotheke     = namedtuple("excludedShopApotheke",      ["id", "valueName"])(**data["excludedShopApotheke"]) # 23598826
		self.marketplaceCartFaktor    = namedtuple("marketplaceCartFaktor",     ["id", "valueName"])(**data["marketplaceCartFaktor"]) # 33874718
		self.excludedKaufland         = namedtuple("excludedKaufland",          ["id", "valueName"])(**data["excludedKaufland"]) # 23598752
		self.eanAmazon                = namedtuple("eanAmazon",                 ["id", "valueName"])(**data["eanAmazon"]) # 34627770
		self.excludedCheck24          = namedtuple("excludedCheck24",           ["id", "valueName"])(**data["excludedCheck24"]) # 23599012
		self.excludedEbay             = namedtuple("excludedEbay",              ["id", "valueName"])(**data["excludedEbay"]) # 23598731
		self.excludedLusini           = namedtuple("excludedLusini",            ["id", "valueName"])(**data["excludedLusini"]) # 75422182
		self.versandArt               = namedtuple("versandArt",                ["id", "valueName", "v_3", "v_4", "v_450", "v_5", "v_6", "v_2", "v_1"])(**data["versandArt"]) # 25290810
		self.conradId                 = namedtuple("conradId",                  ["id", "valueName"])(**data["conradId"]) # 93111098
		self.excludedDocMorris        = namedtuple("excludedDocMorris",         ["id", "valueName"])(**data["excludedDocMorris"]) # 75421628
		self.famId                    = namedtuple("famId",                     ["id", "valueName"])(**data["famId"]) # 24463329
		self.excludedAmazon           = namedtuple("excludedAmazon",            ["id", "valueName"])(**data["excludedAmazon"]) # 23598615
		self.excludedHood             = namedtuple("excludedHood",              ["id", "valueName"])(**data["excludedHood"]) # 23598813
		self.shopapothekePricing      = namedtuple("shopapothekePricing",       ["id", "valueName"])(**data["shopapothekePricing"]) # 58038422
		self.shopapothekeId           = namedtuple("shopapothekeId",            ["id", "valueName"])(**data["shopapothekeId"]) # 94515030

		# Einkauf
		self.inventoryLevelNet        = namedtuple("inventoryLevelNet",         ["id", "valueName"])(**data["inventoryLevelNet"]) # 23072998
		self.inventoryLevelGross      = namedtuple("inventoryLevelGross",       ["id", "valueName"])(**data["inventoryLevelGross"]) # 23072493
		self.starageToolExclusion     = namedtuple("starageToolExclusion",      ["id", "valueName"])(**data["starageToolExclusion"]) # 93614303
		self.stockToTarget            = namedtuple("stockToTarget",             ["id", "valueName"])(**data["stockToTarget"]) # 57108269
		self.ekPriceDefault           = namedtuple("ekPriceDefault",            ["id", "valueName"])(**data["ekPriceDefault"]) # 26144201
		self.availabilityTime         = namedtuple("availabilityTime",          ["id", "valueName", "Sofort", "D3", "D5", "D7", "D10", "D14", "D21", "D28", "D60", "D90"])(**data["availabilityTime"]) # 26457250
		self.ekPriceDyn               = namedtuple("ekPriceDyn",                ["id", "valueName"])(**data["ekPriceDyn"]) # 23072955
		self.availabilityTimeManu     = namedtuple("availabilityTimeManu",      ["id", "valueName"])(**data["availabilityTimeManu"]) # 26464385
		self.palPerMonth              = namedtuple("palPerMonth",               ["id", "valueName"])(**data["palPerMonth"]) # 93619527
		self.dispoTool                = namedtuple("dispoTool",                 ["id", "valueName"])(**data["dispoTool"]) # 12342327
		self.alternativeMpn           = namedtuple("alternativeMpn",            ["id", "valueName"])(**data["alternativeMpn"]) # 29797748
		self.picksPerMonth            = namedtuple("picksPerMonth",             ["id", "valueName"])(**data["picksPerMonth"]) # 93614337
		self.dispoMinMax              = namedtuple("dispoMinMax",               ["id", "valueName"])(**data["dispoMinMax"]) # 44253602
		self.gebundesKapital          = namedtuple("gebundesKapital",           ["id", "valueName"])(**data["gebundesKapital"]) # 16353419

		# Flow Aktionen
		self.actionLog                = namedtuple("actionLog",                 ["id", "valueName"])(**data["actionLog"]) # 16608320
		self.articleActions           = namedtuple("articleActions",            ["id", "valueName", "Verkaufsstcklistenanlegen"])(**data["articleActions"]) # 41953259
		self.createNewSBArticle       = namedtuple("createNewSBArticle",        ["id", "valueName"])(**data["createNewSBArticle"]) # 42135008
		self.LoopVersion              = namedtuple("LoopVersion",               ["id", "valueName"])(**data["LoopVersion"]) # 14568660
		self.errorMessages            = namedtuple("errorMessages",             ["id", "valueName"])(**data["errorMessages"]) # 23781824
		self.just4Testing             = namedtuple("just4Testing",              ["id", "valueName"])(**data["just4Testing"]) # 24523768
		self.weclappError             = namedtuple("weclappError",              ["id", "valueName", "MIP_declined", "NoBilling", "MissingData", "Else", "OK", "UnknownType", "NotPermitted", "WrongData", "Permit_failed", "MIP_modified", "Cancelled", "MIP_rejected", "MIP_new", "Fraud", "ExternalStatus", "Ads", "Warning", "Note", "ValidationError", "FlowFailed", "SyncFailed", "NotDue"])(**data["weclappError"]) # 16601935

		# Pharma Daten
		self.contractItemGroup        = namedtuple("contractItemGroup",         ["id", "valueName", "PG54", "PG51", "PG15", "InkoSample"])(**data["contractItemGroup"]) # 16604713
		self.PZN                      = namedtuple("PZN",                       ["id", "valueName"])(**data["PZN"]) # 4983654
		self.bauaNummer               = namedtuple("bauaNummer",                ["id", "valueName"])(**data["bauaNummer"]) # 36397617
		self.sprechstundenbedarf      = namedtuple("sprechstundenbedarf",       ["id", "valueName"])(**data["sprechstundenbedarf"]) # 16191192
		self.pboxWeight               = namedtuple("pboxWeight",                ["id", "valueName"])(**data["pboxWeight"]) # 17314244
		self.aidPosNumber             = namedtuple("aidPosNumber",              ["id", "valueName"])(**data["aidPosNumber"]) # 17313403

		# Preisgestaltung
		self.percentagePriceRules     = namedtuple("percentagePriceRules",      ["id", "valueName"])(**data["percentagePriceRules"]) # 33677123
		self.priceScaleType           = namedtuple("priceScaleType",            ["id", "valueName"])(**data["priceScaleType"]) # 23073850
		self.shippingCost             = namedtuple("shippingCost",              ["id", "valueName"])(**data["shippingCost"]) # 23073697
		self.clearanceFinancialDiscount= namedtuple("clearanceFinancialDiscount", ["id", "valueName"])(**data["clearanceFinancialDiscount"]) # 56723791
		self.sjThirdColumn            = namedtuple("sjThirdColumn",             ["id", "valueName"])(**data["sjThirdColumn"]) # 33681583
		self.vkPriceDyn               = namedtuple("vkPriceDyn",                ["id", "valueName"])(**data["vkPriceDyn"]) # 8759685
		self.discontinuedProduct      = namedtuple("discontinuedProduct",       ["id", "valueName"])(**data["discontinuedProduct"]) # 104161299
		self.expirationDiscount       = namedtuple("expirationDiscount",        ["id", "valueName"])(**data["expirationDiscount"]) # 103069792
		self.ekPriceManu              = namedtuple("ekPriceManu",               ["id", "valueName"])(**data["ekPriceManu"]) # 8661018
		self.clearanceDiscountStatus  = namedtuple("clearanceDiscountStatus",   ["id", "valueName"])(**data["clearanceDiscountStatus"]) # 102081218
		self.vkPriceManu              = namedtuple("vkPriceManu",               ["id", "valueName"])(**data["vkPriceManu"]) # 23073376
		self.priceScaleQuantity       = namedtuple("priceScaleQuantity",        ["id", "valueName"])(**data["priceScaleQuantity"]) # 23073798
		self.financialYield           = namedtuple("financialYield",            ["id", "valueName"])(**data["financialYield"]) # 23073429
		self.sliderPriceRules         = namedtuple("sliderPriceRules",          ["id", "valueName"])(**data["sliderPriceRules"]) # 78679694
		self.financialDiscount        = namedtuple("financialDiscount",         ["id", "valueName"])(**data["financialDiscount"]) # 28307238
		self.priceScaleStep           = namedtuple("priceScaleStep",            ["id", "valueName"])(**data["priceScaleStep"]) # 28304277

		# STATIC_other
		self.ebay2Available           = namedtuple("ebay2Available",            ["id", "valueName"])(**data["ebay2Available"]) # 26423399
		self.wooDescription           = namedtuple("wooDescription",            ["id", "valueName"])(**data["wooDescription"]) # 291457
		self.amazonASIN               = namedtuple("amazonASIN",                ["id", "valueName"])(**data["amazonASIN"]) # 1527232
		self.wooActive                = namedtuple("wooActive",                 ["id", "valueName"])(**data["wooActive"]) # 8612
		self.shopifyVariantId         = namedtuple("shopifyVariantId",          ["id", "valueName"])(**data["shopifyVariantId"]) # 45569274
		self.wooStockTransfer         = namedtuple("wooStockTransfer",          ["id", "valueName"])(**data["wooStockTransfer"]) # 8613
		self.amazonAvailable          = namedtuple("amazonAvailable",           ["id", "valueName"])(**data["amazonAvailable"]) # 1527227
		self.amazonFbaSku             = namedtuple("amazonFbaSku",              ["id", "valueName"])(**data["amazonFbaSku"]) # 1527230
		self.FORMER_SERVICE           = namedtuple("FORMER_SERVICE",            ["id", "valueName"])(**data["FORMER_SERVICE"]) # 2174360
		self.amazonStockTransfer      = namedtuple("amazonStockTransfer",       ["id", "valueName"])(**data["amazonStockTransfer"]) # 1527228
		self.wooAvailable             = namedtuple("wooAvailable",              ["id", "valueName"])(**data["wooAvailable"]) # 8611
		self.amazonSlSKU              = namedtuple("amazonSlSKU",               ["id", "valueName"])(**data["amazonSlSKU"]) # 1527231
		self.amazonSKU                = namedtuple("amazonSKU",                 ["id", "valueName"])(**data["amazonSKU"]) # 1527229
		self.ebay1Available           = namedtuple("ebay1Available",            ["id", "valueName"])(**data["ebay1Available"]) # 26423400
		self.shopifyId                = namedtuple("shopifyId",                 ["id", "valueName"])(**data["shopifyId"]) # 45569272

		# Shop
		self.unitPriceBaseMeasure     = namedtuple("unitPriceBaseMeasure",      ["id", "valueName"])(**data["unitPriceBaseMeasure"]) # 17530775
		self.LinkShop                 = namedtuple("LinkShop",                  ["id", "valueName"])(**data["LinkShop"]) # 7073904
		self.customTitle              = namedtuple("customTitle",               ["id", "valueName"])(**data["customTitle"]) # 22728607
		self.variantenShopify         = namedtuple("variantenShopify",          ["id", "valueName", "Ja", "Keine"])(**data["variantenShopify"]) # 90732565
		self.wooProductId             = namedtuple("wooProductId",              ["id", "valueName"])(**data["wooProductId"]) # 23486352
		self.LinkBild                 = namedtuple("LinkBild",                  ["id", "valueName"])(**data["LinkBild"]) # 17535769
		self.shopifyProductId         = namedtuple("shopifyProductId",          ["id", "valueName"])(**data["shopifyProductId"]) # 101990562
		self.kurzbeschreibung         = namedtuple("kurzbeschreibung",          ["id", "valueName"])(**data["kurzbeschreibung"]) # 4986635
		self.unitPricingMeasure       = namedtuple("unitPricingMeasure",        ["id", "valueName"])(**data["unitPricingMeasure"]) # 17530711

		# other
		self.v_45569263i9p9kss9dgi5v4 = namedtuple("v_45569263i9p9kss9dgi5v4",  ["id", "valueName"])(**data["v_45569263i9p9kss9dgi5v4"]) # 45569270
		self.v_7646100i8cheb0omskl79  = namedtuple("v_7646100i8cheb0omskl79",   ["id", "valueName"])(**data["v_7646100i8cheb0omskl79"]) # 22982509
		self.v_7646100i8i0kvd8dcgqen  = namedtuple("v_7646100i8i0kvd8dcgqen",   ["id", "valueName"])(**data["v_7646100i8i0kvd8dcgqen"]) # 26326071
		self.v_45569263i191lgvcclqd1c = namedtuple("v_45569263i191lgvcclqd1c",  ["id", "valueName"])(**data["v_45569263i191lgvcclqd1c"]) # 45569266
		self.v_45569263i7knfapjm30rjn = namedtuple("v_45569263i7knfapjm30rjn",  ["id", "valueName"])(**data["v_45569263i7knfapjm30rjn"]) # 45569268
		self.v_7646100ifeh1cq2bf7i4h  = namedtuple("v_7646100ifeh1cq2bf7i4h",   ["id", "valueName"])(**data["v_7646100ifeh1cq2bf7i4h"]) # 26205447
		self.v_12718588i64evdjqaaf7do = namedtuple("v_12718588i64evdjqaaf7do",  ["id", "valueName"])(**data["v_12718588i64evdjqaaf7do"]) # 26162196
		self.v_45569263ibahgngi20rqqa = namedtuple("v_45569263ibahgngi20rqqa",  ["id", "valueName"])(**data["v_45569263ibahgngi20rqqa"]) # 45569264
		self.v_7646100i6vjtmhn8vhtc   = namedtuple("v_7646100i6vjtmhn8vhtc",    ["id", "valueName"])(**data["v_7646100i6vjtmhn8vhtc"]) # 26236091
		self.v_7646100iapl7dfs108a91  = namedtuple("v_7646100iapl7dfs108a91",   ["id", "valueName"])(**data["v_7646100iapl7dfs108a91"]) # 26326072
		self.v_7646100i59pu1h831k8go  = namedtuple("v_7646100i59pu1h831k8go",   ["id", "valueName"])(**data["v_7646100i59pu1h831k8go"]) # 26162197
		self.v_7646100i2k7ra51g8pntf  = namedtuple("v_7646100i2k7ra51g8pntf",   ["id", "valueName"])(**data["v_7646100i2k7ra51g8pntf"]) # 26236090
		self.v_12718588iatgv2funl0u8l = namedtuple("v_12718588iatgv2funl0u8l",  ["id", "valueName"])(**data["v_12718588iatgv2funl0u8l"]) # 22982508
		self.v_7646100iuhhgnkgn1rbm   = namedtuple("v_7646100iuhhgnkgn1rbm",    ["id", "valueName"])(**data["v_7646100iuhhgnkgn1rbm"]) # 26205446
