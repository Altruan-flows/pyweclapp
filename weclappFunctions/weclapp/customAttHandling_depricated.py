import logging
from .legacyWeclappRequests import askWeclapp


class CustomAttributeDefinitions:
    def __init__(self):
        self.customAttributeDefinitions = {}
        
    def getAttribute(self, attDefId:str):
        if not self.customAttributeDefinitions.get(str(attDefId)):
            self.customAttributeDefinitions[str(attDefId)] = askWeclapp(query_params={}, body={},
                                endpoint=f'customAttributeDefinition/id/{attDefId}',
                                method='GET')
        
        return self.customAttributeDefinitions.get(str(attDefId))




# class for custom field processing
class CustomAtt:
    def __init__(self, customField: dict, customAttributeDefinition:CustomAttributeDefinitions=None):
        # Get Attribute ID
        self.attDefId = str(customField['attributeDefinitionId'])

        # define Variables
        self.selectable = {}
        self.value = []
        self.typeDict = {
            "LIST":             "selectedValueId",
            "MULTISELECT_LIST": "selectedValues",
            "DECIMAL":          "numberValue",
            "INTEGER":          "numberValue",
            "BOOLEAN":          "booleanValue",
            "STRING":           "stringValue",
            "LARGE_TEXT":       "stringValue",
            "URL":              "stringValue",
            "DATE":             "dateValue",
            "ENTITY":           "entityId",
            "REFERENCE":        "entityReferences"
        }
        # get Atribute by Calling 
        if not customAttributeDefinition:
            customAttributeDefinition = CustomAttributeDefinitions()
            
        self.attribute = customAttributeDefinition.getAttribute(self.attDefId)
        
        self.label = self.attribute['attributeLabels'][0]['labelText']
        self.attKey = self.attribute['attributeKey']
        self.type = self.attribute['attributeType']
        self.valueKey = self.typeDict[self.type]
        self.initValue(customField)
        self.initValueGroup()

        # Look if group exists
        try:
            self.group = self.attribute['groupName']
        except:
            self.group = None

    def initValue(self, customField:dict):

        # Get selectable Options
        if self.type == "LIST" or self.type == "MULTISELECT_LIST":
            for el in self.attribute['selectableValues']:
                self.selectable[str(el['id'])] = str(el["value"])

        try:
            # if selectables are a list of objects
            if self.type == "MULTISELECT_LIST" or self.type == "REFERENCE":
                """"Example: 
                entityReferences": [
                    {
                        "entityId": "354058",
                        "entityName": "salesOrder"
                    },
                    {
                        "entityId": "4519188",
                        "entityName": "salesOrder"
                    }
                ]"""
                self.value = customField[self.valueKey]

            # The rest
            else:
                self.value.append(customField[self.valueKey])
        except KeyError:
            # raise ValueError(f'--def-- initValue error ---{e}---')
            pass

    def initValueGroup(self):
        if self.type == "LIST" or self.type == "ENTITY":
            self.valueGroup = "select"
        elif self.type == "REFERENCE" or self.type == "MULTISELECT_LIST":
            self.valueGroup = "multiSelect"
        else:
            self.valueGroup = "simple"

    def example(self):
        return """
                    self.attDefId: "5211352"
                    self.attribute: Weclapp customAttributeDefinition endpoint
                        -> https://www.weclapp.com/api/#!/customAttributeDefinition/get_customAttributeDefinition
                    self.label: "VsInfo - Ebene - Auf welche Ebene bezieht sich der Preis?"
                    self.attKey = "VsInfoEbene"
                    self.type = "LIST"
                    self.group = "Artikeleinheiten und Versandinformationen"
                    self.value = "5211366"
                    self.selectable = {"5211366": "(Versand)", "5211365": "Karton", ...}
                    self.valueKey = "selectedValueId"
                    """

    def getSelectableID(self, name: str):
        for key, value in self.selectable.items():
            if name.lower() in value.lower():
                return key
        return None

    def setValue(self, value):
        logging.info("---util.weclapp.CustomAtt->setValue()---")
        # insert Numbers
        if self.valueKey == "numberValue":
            assert str(
                value).isnumeric(), f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.attKey}) is not nummeric"
            self.value = [str(value)]

        # insert booleans
        elif self.valueKey == "booleanValue":
            assert isinstance(value,
                              bool), f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.attKey}) is not boolean"
            self.value = [value]

        # insert strings
        elif self.valueKey == "stringValue":
            self.value = [str(value)]

        # if date is selected
        elif self.valueKey == "dateValue":
            assert isinstance(value, int), 'date needs to be int'
            self.value = [int(value)]

        # select value -> ether by id or by value
        elif self.valueKey == "selectedValueId":
            if str(value) in self.selectable.keys():
                self.value = [str(value)]
            elif str(value) in self.selectable.values():
                self.value = [self.getSelectableID(str(value))]
            else:
                raise ValueError(f"Error in cAtt.setValue(): Given Value ({str(value)} in object {self.attKey}) not found in Selectable Values")

        # if entity is selected -> be carefull no validation
        elif self.valueKey == "entityId":
            self.value = [str(value)]

        # Multiselect -> the whole list of dicts needs to be passed!!!
        elif self.valueKey == "selectedValueId" or self.valueKey == "entityReferences":
            assert isinstance(value, list), f"Type needs to be list of dicts"
            for el in value:
                assert isinstance(el, dict), f"Type needs to be list of dicts - invalid dict"
            self.value = value

        else:
            raise ValueError("Error in cAtt.setValue(): Something is seriously wrong")

    def appendValue(self, value, separator:str=";"):
        logging.info("---util.weclapp.CustomAtt->appendValue()---")

        # insert strings
        if self.valueKey == "stringValue":
            try:
                currentValue = str(self.value[0]).split(separator)
                currentValue.insert(0, str(value))
                self.value = [separator.join(currentValue)]
            except IndexError:
                self.value.append(str(value))

        # Multiselect -> the whole list of dicts needs to be passed!!!
        elif self.valueKey == "selectedValueId" or self.valueKey == "entityReferences":
            assert isinstance(value, dict), f"Type needs to be list of dicts - invalid dict"
            self.value.append(value)
        else:
            logging.error(f"appendValue method to custom Attributes class is only supported for sring and multiple select")

    # get Value in readable format
    def getReadableValue(self):
        if len(self.value) > 0:
            # List
            if self.valueGroup == "select":
                try:
                    return self.selectable[self.value[0]]
                except KeyError:
                    return self.value[0]


            # Simple Attribute
            elif self.valueGroup == "simple":
                return self.value[0]

            # multiselect list
            elif self.valueGroup == "multiSelect":
                try:
                    toReturn = []
                    for item in self.value:
                        toReturn.append(self.selectable[item['id']])
                    return toReturn
                except KeyError:
                    return self.value
        else:
            return None
    def getValue(self):
        if len(self.value) == 1:
            return self.value[0]
        else:
            return self.value
    # return the custom Attribute in Weclapp format
    def getCAtt(self):
        base = {
            "attributeDefinitionId": self.attDefId
        }
        if len(self.value) > 0:
            # Simple Attributes and simple Lists
            if self.valueGroup != "multiSelect":
                base[self.valueKey] = self.value[0]

            # multiselect list
            else:
                base[self.valueKey] = self.value

        return base
    
    
def parseCustomAtt(customAttributes: list, cAttDescription: dict):
    logging.info('--def--- parseCustomAtt')
    '''    
    cAttDescription = {
        "5211283": "WooOrderID",
        "5210860": "ActionHistory",
        "5210736": "",
        "5208433": "",
        "5211310": ""
    }
    '''
    attributesDict = {}
    for customAttribute in customAttributes:
        attDefId = customAttribute['attributeDefinitionId']
        if attDefId in cAttDescription.keys():
            # logging.info(attDefId)
            cAttObject = CustomAtt(customAttribute)
            try:
                description = cAttDescription[attDefId]
            except:
                description = cAttObject.attDefId
            attributesDict[description] = CustomAtt(customAttribute)
    logging.info("Parsed cAtt")
    return attributesDict