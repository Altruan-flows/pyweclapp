from pyWeclapp import weclapp
from pydantic import BaseModel
from .weclappClassCustomAttribute import WeclappMetaData
import logging
from typing import Any, Union, Literal, Optional, List, get_origin, get_args
import re


class Blueprint(BaseModel):
    USED_ATTRIBUTES: dict = dict()
    ITEMS_NAME: Optional[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def incrementVersion(self):
        if hasattr(self, "version"):
            version = int(float(getattr(self, "version")))
            setattr(self, "version", str(version + 1))
            logging.info(f"Incremented Version to {version + 1}")
        else:
            logging.info("No Version Attribute found")

    def queryMetaData(
        self, value, raiseError: bool = True, addToMetaData: bool = False
    ) -> WeclappMetaData:
        """Returns the first item customAttribute where a given attributeDefinitionId equals value

        Args:
            value (Any): any Value of the key (eg. 123)
            addToMetaData (bool): adds an empty customAttribute if not found
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
        if hasattr(self, "customAttributes"):
            try:
                try:
                    # Intrgrate CAT more easily by directly inserting the named tuple
                    valueId = value
                    if (
                        isinstance(value, tuple)
                        and hasattr(value, "_fields")
                        and hasattr(value, "id")
                    ):
                        valueId = value.id
                except Exception:
                    valueId = value
                for cAttribute in self.customAttributes:
                    if (
                        isinstance(cAttribute, WeclappMetaData)
                        and cAttribute.name == valueId
                    ):
                        return cAttribute
                raise KeyError(f"Custom Attribute {value} not found")

            except KeyError as e:
                if addToMetaData and hasattr(self, "customAttributes"):
                    item = WeclappMetaData(attributeDefinitionId=value)
                    self.customAttributes.append(item)
                    return item
                elif raiseError:
                    raise e
                else:
                    return WeclappMetaData(attributeDefinitionId=value)

        else:
            raise KeyError(
                f"Attribute customAttributes not found in {type(self).__name__}"
            )

    def qmd(
        self, value, raiseError: bool = True, addToMetaData: bool = False
    ) -> WeclappMetaData:
        """Short Version for queryMetaData Function. Returns the first item
        customAttribute where a given attributeDefinitionId equals value.

        Args:
            value (Any): any Value of the key (eg. 123)
            addToMetaData (bool): adds an empty customAttribute if not found
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.

        Raises: KeyError if not found
        """
        return self.queryMetaData(
            value=value, raiseError=raiseError, addToMetaData=addToMetaData
        )

    def query(self, entity: str, raiseError: bool = True, **kwargs):
        """Returns the first item in the entity (eg. orderItem) that satisfies all kwargs (e.g. id='123', name='test')

        Args:
            entity (str): list of items (eg. orderItems)
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.
            **kwargs: any Attribute of the Child Attribute (eg. id='123', name='test')

        Raises: KeyError if not found
        """
        try:
            if not kwargs:
                logging.warning(
                    f"No keywordQueries provided {entity} -> this will return the first element"
                )
            if hasattr(self, entity):
                listAttributes = getattr(self, entity)
                if isinstance(listAttributes, list):
                    for item in listAttributes:
                        if all(
                            [
                                getattr(item, key) == value
                                for key, value in kwargs.items()
                            ]
                        ):
                            return item
                else:
                    raise KeyError(f"Attribute >{entity}< is not a list")

            qString = " & ".join([f"{key}={value}" for key, value in kwargs.items()])
            raise KeyError(f"no element found in {qString} for {entity=}")

        except KeyError as e:
            if raiseError:
                raise e
            else:
                return None

    def queryItems(self, raiseError: bool = True, **kwargs):
        """Returns the first item in the list specified by ITEMS_NAME (eg.
        orderItem) that satisfies all kwargs (e.g. id='123', name='test')

        Args:
            raiseError (bool, optional): Returns None if nothing found. Defaults to True.
            **kwargs: any Attribute of the Child Attribute (eg. id='123', name='test')

        Raises: KeyError if not found
        """
        try:
            if not hasattr(self, self.ITEMS_NAME):
                raise KeyError(f"Attribute {self.ITEMS_NAME=} not found or invalid")

            return self.query(entity=self.ITEMS_NAME, raiseError=raiseError, **kwargs)

        except KeyError as e:
            if raiseError:
                raise e
            else:
                return None

    # ------------- Used Attributes Handling -------------

    def resetUsedAtts(self):
        self.USED_ATTRIBUTES = {}

    def resetAllUsedAtt(self):
        self.resetUsedAtts()
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                for listItem in value:
                    if hasattr(listItem, "resetUsedAtts"):
                        listItem.resetUsedAtts()
                    elif (
                        hasattr(listItem, "updated")
                        and getattr(listItem, "updated") is True
                    ):
                        listItem.updated = False
            elif hasattr(value, "resetUsedAtts"):
                value.resetUsedAtts()

    def addUsedAtt(self, attName):
        if hasattr(self, attName):
            self.USED_ATTRIBUTES[attName] = getattr(self, attName)

    def delUsedAttr(self, attName, suppressWarning: bool = False):
        if attName in self.USED_ATTRIBUTES:
            del self.USED_ATTRIBUTES[attName]
            if not suppressWarning:
                logging.warning(f"Deleted Attribute {attName} from Used Attributes")

    def setValue(self, key, value):
        if not hasattr(self, key):
            raise KeyError(
                f"{type(self).__name__} has no attribute {key} -> check spelling, make sure it is included"
            )
        setattr(self, key, value)
        # self.USED_ATTRIBUTES[key] = value # -> not necessary because of __setattr__

    def restoreValue(self, key):
        if not hasattr(self, key):
            raise KeyError(
                f"{type(self).__name__} has no attribute {key} -> check spelling, make sure it is included"
            )
        value = self.USED_ATTRIBUTES.get(key)
        logging.warning(f"Restoring {key} to {value}")
        setattr(self, key, value)

    # ------------- Tag Handling -------------

    def addTag(self, newTag: str):
        """Adds a tag to tags if available
        - allowed charaters are a-z, 0-9 and "-", "-", " " -> others will be replaced by "_"
        """

        if hasattr(self, "tags"):
            # strip and remove invalid characters
            newTag = re.sub(r"[^a-zA-Z0-9\-_ ]", "_", str(newTag).strip())
            currentTags = self.__dict__.get("tags", [])
            if newTag not in currentTags:
                if isinstance(currentTags, list):
                    currentTags.append(str(newTag).strip())
                    self.__dict__["tags"] = currentTags
                    self.addUsedAtt("tags")
                else:
                    raise TypeError("Tags is not list!")
            else:
                logging.warning(f"{newTag} is already in tags!")
        else:
            raise KeyError("No tags in this class")

    def replaceTag(self, newTag: str, tagIdenitier: str = None, regrex: str = None):
        """Replaces and adds newTag:
        1. replaces any tag that contains tagIdenitier or regrex (case insensitive);
        if tagIdenitier is None it skips this part.
        2. adds newTag to Tags if possible
            - allowed charaters are a-z, 0-9 and "-", "-", " " -> others will be replaced by "_"
        3. it also encures uniqueness of Tags (no duplicates)"""

        if hasattr(self, "tags"):
            currentTags = self.__dict__.get("tags", [])
            if isinstance(currentTags, list):
                tagValue = re.sub(r"[^a-zA-Z0-9\-_ ]", "_", str(newTag).strip())

                # get unique Tags without Tags containing TagId
                if regrex is not None:
                    currentTagsSet = set(
                        [str(tag) for tag in currentTags if not re.match(regrex, tag)]
                    )
                elif tagIdenitier and isinstance(tagIdenitier, str):
                    currentTagsSet = set(
                        [
                            str(tag)
                            for tag in currentTags
                            if str(tagIdenitier).lower() not in str(tag).lower()
                        ]
                    )
                else:
                    currentTagsSet = set(currentTags)

                # Add newTag to Tags
                currentTagsSet.add(tagValue)

                # Update Tags if something changed
                if not all(tag in currentTagsSet for tag in currentTags) or len(
                    currentTags
                ) != len(currentTagsSet):
                    self.__dict__["tags"] = list(currentTagsSet)
                    self.addUsedAtt("tags")
            else:
                raise TypeError("Type is not list!")

        else:
            raise KeyError("No tags in this class")

    def deleteTag(self, tagToRemove: str = None, regrex: str = None):
        """Deletes a tag if it is in the list of Tags or matches the regrex
        - regrex will be prioritized over tagToRemove"""
        if tagToRemove is None and regrex is None:
            raise AssertionError("Please provide a tagToRemove or a regrex")

        if hasattr(self, "tags"):
            currentTags = self.__dict__.get("tags", [])
            if isinstance(currentTags, list):
                initialLength = len(currentTags)
                if regrex is not None:
                    currentTags = [
                        str(tag) for tag in currentTags if not re.match(regrex, tag)
                    ]
                else:
                    try:
                        tagToRemove = re.sub(
                            r"[^a-zA-Z0-9\-_ ]", "_", str(tagToRemove).strip()
                        )
                        currentTags.remove(tagToRemove)
                    except ValueError:
                        pass

                if currentTags == []:
                    logging.warning("Tags list is empty! -> list will not be updated")

                if len(currentTags) != initialLength:
                    self.__dict__["tags"] = currentTags
                    self.addUsedAtt("tags")
            else:
                raise TypeError("Type is not list!")
        else:
            raise KeyError("No tags in this class")

    # ------------- Core Functions -------------

    def __setattr__(self, __name: str, __value: Any) -> None:

        # Ensure type consistancy
        if type(__value) in [int, str, float, bool]:
            targetType = self.__annotations__.get(__name, type(__value))
            # Check if targetType is a Union and extract its arguments
            if get_origin(targetType) in [Union, Optional]:
                args = []
                for arg in get_args(targetType):
                    if get_origin(arg) in [Literal]:
                        args.append(str)
                    else:
                        args.append(arg)
            # simple args
            elif get_origin(targetType) is None:
                args = [targetType]
            elif get_origin(targetType) is Literal:
                args = [str]
            else:
                logging.warning(
                    f"Could not parse type {targetType} allowed are Union, Optional, Literal, None and base types"
                )
                args = []

            # Converting value if necessary
            if int in args:
                if not isinstance(__value, int):
                    logging.warning(
                        f"Autoconverting {__value} ({type(__value).__name__}) to required type int"
                    )
                    __value = int(float(__value))
            elif str in args:
                if not isinstance(__value, str):
                    logging.warning(
                        f"Autoconverting {__value} ({type(__value).__name__}) to required type str"
                    )
                    __value = str(__value)
            elif bool in args:
                if not isinstance(__value, bool):
                    logging.warning(
                        f"Autoconverting {__value} ({type(__value).__name__}) to required type bool"
                    )
                    __value = bool(__value)
            elif float in args:
                if not isinstance(__value, float):
                    logging.warning(
                        f"Autoconverting {__value} ({type(__value).__name__}) to required type float"
                    )
                    __value = float(__value)
            else:
                logging.error("failed to correct it...")
                raise TypeError(
                    f"You tried to assign {type(__value).__name__} to "
                    f"the {targetType.__name__} attribute {__name} -> could not correct it"
                )

        # Check if somthing would change
        if __value != getattr(self, __name):
            if isinstance(__value, tuple):
                if len(__value) == 2:
                    __value, justUsedKeys = __value
                    if justUsedKeys:
                        if __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
                            self.USED_ATTRIBUTES[__name] = getattr(self, __name)
                    else:
                        logging.warning(
                            f"Not Adding >{__name}< in >{type(self).__name__}< to used keys"
                        )
            elif __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
                self.USED_ATTRIBUTES[__name] = getattr(self, __name)

            object.__setattr__(self, __name, __value)
        elif __name not in ["USED_ATTRIBUTES", "ITEMS_NAME"]:
            logging.info(
                f"Attribute {__name} is already set to {__value} -> nothing changed"
            )

    def getUpdateDict(
        self,
        updateType: Literal["full", "used", "used+"] = "used+",
        creationMode: bool = False,
    ):
        """Returns a drictionary with all attributes that should be updated, excludes all None Values

        Args:
            updateType (Literal[full, used, used+, optional): Mode of update. Defaults to 'used+'.
            creationMode (bool, optional): Used for creating post requests to handle differentces. Defaults to False.
        """
        if creationMode:
            updateType = "full"

        alwaysToExclude = [
            "USED_ATTRIBUTES",
            "ITEMS_NAME",
            "USED_KEYS",
            "statusHistory",
        ]  # statusHistory

        data = {}
        for key, value in self.__dict__.items():
            # excludes Empty Values and uninitialized classes
            if (
                (value or value is False)
                and not isinstance(value, type)
                and key not in alwaysToExclude
            ):
                # try:
                # handl custom Attributes
                if key == "customAttributes":
                    helper = []
                    for customAttribute in value:
                        if issubclass(type(customAttribute), WeclappMetaData):
                            cat = customAttribute.getUpdateDict(updateType=updateType)
                            if updateType == "full":
                                helper.append(cat)
                            elif cat:
                                helper.append(cat)
                        elif isinstance(customAttribute, dict) and hasattr(
                            customAttribute, "attributeDefinitionId"
                        ):
                            helper.append(customAttribute)
                    if len(helper) > 0:
                        data[key] = helper

                # handle contract Items
                elif (
                    isinstance(value, list)
                    and self.__annotations__.get(key, list) != list
                ):
                    helper = []
                    itemsUpdateNecessary = False
                    for listItem in value:
                        if issubclass(type(listItem), Blueprint):
                            if updateType == "full":
                                helper.append(
                                    listItem.getUpdateDict(updateType=updateType)
                                )
                            elif updateType == "used+":
                                oldUsedItems = listItem.USED_ATTRIBUTES
                                listItem.addUsedAtt("id")
                                listItem.addUsedAtt("version")
                                item = listItem.getUpdateDict(updateType="used+")
                                if len(item) > 2:
                                    itemsUpdateNecessary = True
                                helper.append(item)
                                listItem.delUsedAttr("version", suppressWarning=True)
                                listItem.USED_ATTRIBUTES = oldUsedItems
                            elif updateType == "used":
                                oldUsedItems = listItem.USED_ATTRIBUTES
                                listItem.addUsedAtt("id")
                                item = listItem.getUpdateDict(updateType="used")
                                # item = el.getUsedAttributes(add=['id'])
                                if len(item) > 1:
                                    itemsUpdateNecessary = True
                                helper.append(item)
                                listItem.USED_ATTRIBUTES = oldUsedItems
                        elif isinstance(listItem, dict):
                            helper.append(listItem)
                            itemsUpdateNecessary = True
                    if len(helper) > 0:
                        if updateType in ["used", "used+"] and not itemsUpdateNecessary:
                            pass
                        else:
                            # Update Type "full" or items changed
                            data[key] = helper

                # handle list of dict
                elif isinstance(value, list) and (
                    updateType in ["full"] or key in self.USED_ATTRIBUTES
                ):
                    helper = []
                    for listItem in value:
                        if isinstance(listItem, dict):
                            helper.append(listItem)
                        else:
                            if key not in ["tags"]:
                                logging.warning(
                                    f"handled Error: {listItem} is not a dict"
                                )
                            helper.append(listItem)
                    if len(helper) > 0:
                        data[key] = helper

                # handl Other classes
                elif hasattr(value, "getUpdateDict"):
                    ocls = value.getUpdateDict(updateType=updateType)
                    if ocls:
                        data[key] = ocls

                # Normal attributes
                elif (
                    key in self.USED_ATTRIBUTES
                    or updateType == "full"
                    or (key in ["version"] and updateType == "used+")
                ):
                    if value is not None:
                        if creationMode:
                            if key in ["id", "version"]:
                                raise AssertionError(
                                    f"Can not post new Entity {type(self).__name__} -> id or version already set"
                                )
                        data[key] = value

        if "ITEMS_NAME" in data:
            del data["ITEMS_NAME"]

        if "USED_KEYS" in data:
            del data["USED_KEYS"]

        if "USED_ATTRIBUTES" in data:
            del data["USED_ATTRIBUTES"]

        # remove version if mothing updated
        if len(data) == 1 and "version" in data and updateType in ["used+", "used"]:
            data = {}
        return data

    # ----------------- Change Management version -----------------

    @property
    def __entityName__(self) -> str:
        classType = type(self)
        entityName = str(classType.__name__)
        entityName = entityName[:1].lower() + entityName[1:]
        return entityName

    @staticmethod
    def assessChanges(first, other):
        """Updates recursively the first entity with the values of the second
        entity if they are not critical; else raises Error"""

        if (
            hasattr(first, "USED_ATTRIBUTES")
            and hasattr(first, "version")
            and hasattr(other, "version")
            and issubclass(type(first), type(Blueprint))
        ):
            if not type(first) == type(other):
                raise AssertionError(
                    f"{type(first)} and {type(other)} types are not equal"
                )

            for key, value in first.__dict__.items():
                if key not in [
                    "USED_ATTRIBUTES",
                    "ITEMS_NAME",
                    "customAttributes",
                    "version",
                ]:
                    other_value = getattr(other, key)
                    if isinstance(value, list):
                        for listItem in value:
                            try:
                                if hasattr(listItem, "id"):
                                    Blueprint.assessChanges(
                                        listItem,
                                        other.query(id=listItem.id, entity=key),
                                    )
                                else:
                                    logging.warning(
                                        f"List Item {listItem} has no id -> can not be assesed"
                                    )
                            except AttributeError:
                                pass
                            except AssertionError as ae:
                                logging.error(f"Error while assesing {key}: {ae}")
                    elif issubclass(type(value), type(Blueprint)):
                        Blueprint.assessChanges(value, other_value)

                    elif not isinstance(value, dict):
                        if value != other_value:
                            if first.USED_ATTRIBUTES.get(key) is None:
                                logging.warning(
                                    f"Uncrittical ChangeFound {key} changed from {value} to {getattr(other, key)}"
                                )
                                setattr(first, key, getattr(other, key))
                            elif first.USED_ATTRIBUTES.get(key) != other_value:
                                raise AssertionError(
                                    f"Valid Optimistic-Loc Error found: {key} "
                                    f"changed from {value} to {getattr(other, key)}"
                                )

            first.version = other.version

    def refreshEntity(self):
        """Refreshes the version and updates Changes from weclapp and includes
        changes if they are not critical; else raises Error"""
        if hasattr(self, "id"):
            logging.warning(f"Refreshing Version of {type(self).__name__}")
            currentEntity = type(self).fromWeclapp(entityId=self.id)
            self.assessChanges(
                self, currentEntity
            )  # Custom error Type when changes are deteced!!
        else:
            logging.warning(
                f"Can not refresh Version of {type(self).__name__} -> no id found"
            )

    # ----------------- Change Management Update -----------------

    def updateEntity(self, updateType: Literal["full", "used", "used+"] = "used+"):
        """Mirrors changes to weclapp with the specified updateType and includes any possible change from weclapp
        - updateType (Literal[full, used, used+, optional): Mode of update. Defaults to 'used+'.
        """

        logging.warning(
            f"Updating {self.__entityName__} in conjunction with webhooks can lead to loops! -> Please take precautions"
        )
        body = self.getUpdateDict(updateType=updateType)
        if len(body) == 0:
            logging.warning(f"No fields to update for {self.__entityName__}")
        elif hasattr(self, "id"):
            newEntity = weclapp.PUT(
                entityName=self.__entityName__, entityId=self.id, body=body
            )
            self.updateEntityFromNewEntity(newEntity=newEntity)
        else:
            raise KeyError(f"Can not update {self.__entityName__} -> no id found")

    def fetchEntity(self):
        """Fetches changes that may have occured in weclapp (overwrites everything that was changed in self)"""
        if hasattr(self, "id"):
            response = weclapp.GET(
                entityName=self.__entityName__, entityId=self.id, asType=dict
            )
            self.updateEntityFromNewEntity(newEntity=response)
            logging.warning(f"{self.__entityName__} refreshed")
        raise KeyError(f"Can not update {self.__entityName__} -> no id found")

    def updateEntityFromNewEntity(self, newEntity: Union[dict, object]):
        logging.warning(f"Updateing entity {type(self).__name__}")
        if isinstance(newEntity, dict):
            newEntity = type(self)(**newEntity)
        if type(newEntity) == type(self):
            self.__dict__.update(newEntity.__dict__)
            # reset Used Keys
            self.resetAllUsedAtt()
            logging.warning(f"Entity {type(self).__name__} updated; all fields resetet")

        else:
            raise AssertionError("No Matching entity Provided to update the self")

    def updateWeclapp(
        self, updateType: Literal["full", "used", "used+"] = "full"
    ) -> dict:
        """Updates weclapp with the specified updateType, without updating self"""
        body = self.getUpdateDict(updateType=updateType)
        if hasattr(self, "id"):
            return weclapp.PUT(
                entityName=self.__entityName__, entityId=self.id, body=body
            )
        raise KeyError(f"Can not update {self.__entityName__} -> no id found")

    def postNewEntity(self) -> dict:
        """Posts a new Entity to weclapp, and updates the wecalppClass and
        usedAtts are reset. In addition the new entity is returned"""

        body = self.getUpdateDict(updateType="full", creationMode=True)
        logging.warning(f"Posting new Entity {type(self).__name__} {body=}")
        newEntityDict = weclapp.POST(entityName=self.__entityName__, body=body)

        # Update Entity with values from weclapp
        self.updateEntityFromNewEntity(newEntity=newEntityDict)
        return newEntityDict

    # ----------------- Recreation -----------------

    @classmethod
    def fromWeclapp(cls, entityId: str):
        """initializes the class from a weclapp entity"""
        if entityId is None:
            raise AssertionError(
                "EntityId in .fromWeclapp() is None. Please provide a valid id."
            )
        entityName = cls.__name__
        entityName = entityName[:1].lower() + entityName[1:]
        response = weclapp.GET(entityName=entityName, entityId=entityId, asType=dict)
        if not isinstance(response, dict):
            raise AssertionError(
                f"Response from weclapp is not a dict, but a {type(response).__name__}"
            )
        return cls(**response)

    @classmethod
    def fromBlank(cls):
        """Creates a blank item with all attributes set to None or empty list
        or empty nested attributes
        -> used for creating new items and after setting the attributes in
        conjunction  with self.postNewEntity()
        """
        blankItem = {}
        NoneAtts = []

        for att, fieldInfo in cls.model_fields.items():

            # Normal Attributes
            if fieldInfo.annotation in [str, int, float, bool]:
                blankItem[att] = fieldInfo.annotation()
                NoneAtts.append(att)

            # List Attributes
            elif fieldInfo.annotation in [list, dict]:
                if str(fieldInfo.default) == "PydanticUndefined":
                    blankItem[att] = fieldInfo.annotation()

            # init bank lists
            elif getattr(fieldInfo.annotation, "__origin__", None) in [List, list]:
                pass

            # add other blank types
            elif isinstance(fieldInfo.annotation, type) and issubclass(
                fieldInfo.annotation, Blueprint
            ):
                blankItem[att] = (
                    fieldInfo.annotation.fromBlank()
                )  # replace with .blank()

            # Handle Optional and Union fields -> inti with None
            elif getattr(fieldInfo.annotation, "__origin__", None) in [Optional, Union]:
                blankItem[att] = None
                NoneAtts.append(att)

            else:
                fieldInfo
                raise Exception(f"Other Att found: {att} - {fieldInfo.annotation}")

        # init Att
        item = cls(**blankItem)

        # Set all values to None for creation
        for att in NoneAtts:
            setattr(item, att, None)

        item.USED_ATTRIBUTES = {}
        return item
