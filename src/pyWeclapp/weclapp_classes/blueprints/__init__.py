"""Core module for Blueprint class, which serves as a base class for Weclapp entities."""

import logging
import re
from typing import Any, Union, Literal, Optional, List, get_args
from pydantic import BaseModel
from types import SimpleNamespace
from ...weclapp import Weclapp
from .custom_attributes_model import WeclappMetaData


class Blueprint(BaseModel):
    """Base class for Weclapp entities, providing methods for handling custom
    attributes and entity updates."""
    used_attributes: Union[dict, None] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.used_attributes = {}

    def custom_attribute(
        self, attribute_identifier: Union[str, int, tuple]
    ) -> WeclappMetaData:
        """Iterates through the customAttributes and returns the first item
        where the name matches the attribute_identifier.
        Args:
            attribute_identifier (Union[str, int, tuple]): The identifier of the
                custom attribute. If string or integer is provided, it will be used
                as the name of the custom attribute. If a tuple of custom attribute
                is provided, it will be used to get the id of the custom attribute.
        """
        if hasattr(self, "customAttributes"):
            if isinstance(attribute_identifier, str):
                attribute_id = attribute_identifier
            elif isinstance(attribute_identifier, int):
                attribute_id = str(attribute_identifier)
            elif isinstance(attribute_identifier, SimpleNamespace):
                attribute_id = attribute_identifier.id
            else:
                raise TypeError(
                    f"Value must be a string, an integer, or a SimpleNamespace, "
                    f"not {type(attribute_identifier).__name__}"
                )

            for custom_attribute in self.customAttributes:
                if (
                    isinstance(custom_attribute, WeclappMetaData)
                    and custom_attribute.attributeDefinitionId == attribute_id
                ):
                    return custom_attribute
            raise KeyError(f"Custom attribute with id {attribute_id} not found")

        raise KeyError(f"Attribute customAttributes not found in {type(self).__name__}")

    def cat(self, attribute_identifier: Union[str, int, tuple]) -> WeclappMetaData:
        """Returns the custom attribute with the given identifier. Shorter alias
        for custom_attribute.

        Args:
            attribute_identifier (Union[str, int, tuple]): The identifier of the
                custom attribute. If string or integer is provided, it will be used
                as the name of the custom attribute. If a tuple of custom attribute
                is provided, it will be used to get the id of the custom attribute.
        """

        return self.custom_attribute(attribute_identifier=attribute_identifier)

    def reset_used_attributes(self) -> None:
        """Resets the used_attributes dictionary to an empty state."""
        self.used_attributes = {}

    def reset_all_used_attributes(self) -> None:
        """Resets the used_attributes dictionary of the current instance
        and all its subclasses."""
        self.reset_used_attributes()
        for _, value in self.__dict__.items():
            if isinstance(value, list):
                for list_item in value:
                    if hasattr(list_item, "reset_used_attributes"):
                        list_item.reset_used_attributes()
                    elif (
                        hasattr(list_item, "updated")
                        and getattr(list_item, "updated") is True
                    ):
                        list_item.updated = False
            elif hasattr(value, "resetUsedAtts"):
                value.resetUsedAtts()

    def add_used_attribute(self, attribute_name: str) -> None:
        """Adds an attribute to the used_attributes dictionary if it exists in
        the instance."""
        if hasattr(self, attribute_name):
            self.used_attributes[attribute_name] = getattr(self, attribute_name)

    def remove_used_attribute(self, attribute_name: str) -> None:
        """Deletes an attribute from the used_attributes dictionary if it exists."""
        if attribute_name in self.used_attributes:
            del self.used_attributes[attribute_name]

    def update_custom_attribute(self, key: str, value: Any) -> None:
        """Updates a custom attribute with the given key and value."""
        if not hasattr(self, key):
            raise KeyError(
                f"{type(self).__name__} has no attribute {key} -> "
                "check spelling of the custom attribute, "
                "make sure it is included in the customAttributes list"
            )
        setattr(self, key, value)

    def add_tag(self, new_tag: str) -> None:
        """Adds a tag to a list of tags. Allowed characters are a-z, 0-9 and
        "-", "-", " " -> others will be replaced by "_"
        """

        if hasattr(self, "tags"):
            new_tag = re.sub(r"[^a-zA-Z0-9\-_ ]", "_", str(new_tag).strip())
            current_tags = self.__dict__.get("tags", [])

            if isinstance(current_tags, list):
                if new_tag not in current_tags:
                    current_tags.append(str(new_tag).strip())
                    self.__dict__["tags"] = current_tags
                    self.add_used_attribute("tags")
                else:
                    logging.warning("Tag %s is already in tags!", new_tag)
            else:
                raise TypeError("Tags attribute of the entity is not a list!")
        else:
            raise KeyError("No tags attribute found in this class")

    def replace_tag(self, new_tag: str, tag_identifier: str = None, regex: str = None):
        """Replaces and adds new_tag. Allowed characters are a-z, 0-9 and "-",
        "-", " " -> others will be replaced by "_".
        1. If tag_identifier is provided, it will replace the tag that contains
        the tag_identifier.
        2. If regex is provided, it will replace all tags that match the regex.
        3. If neither is provided, it will add the new_tag to the list of tags.
        """

        if hasattr(self, "tags"):
            current_tags = self.__dict__.get("tags", [])
            if isinstance(current_tags, list):
                tag_value = re.sub(r"[^a-zA-Z0-9\-_ ]", "_", str(new_tag).strip())

                if regex is not None:
                    current_tags_set = {
                        str(tag) for tag in current_tags if not re.match(regex, tag)
                    }
                elif tag_identifier and isinstance(tag_identifier, str):
                    current_tags_set = {
                        str(tag)
                        for tag in current_tags
                        if str(tag_identifier).lower() not in str(tag).lower()
                    }
                else:
                    current_tags_set = set(current_tags)

                current_tags_set.add(tag_value)

                if not all(tag in current_tags_set for tag in current_tags) or len(
                    current_tags
                ) != len(current_tags_set):
                    self.__dict__["tags"] = list(current_tags_set)
                    self.add_used_attribute("tags")
            else:
                raise TypeError("Tags attribute of the entity is not a list!")

        else:
            raise KeyError("No tags attribute found in this class")

    def delete_tag(
        self, tag_to_remove: str = None, regex: str = None, allow_empty: bool = False
    ) -> None:
        """Deletes a tag from the list of tags.
        Args:
            tag_to_remove (str, optional): The tag to remove. If provided, it will
                remove the tag that matches this value.
            regex (str, optional): A regex pattern to match tags to remove. If
                provided, it will remove all tags that match this regex.
            allow_empty (bool, optional): If True, allows the tags list to be
                empty after deletion. If False, will not update the tags list if
                it becomes empty.
        """
        if tag_to_remove is None and regex is None:
            raise AssertionError("Please provide a tag_to_remove or a regex")

        if hasattr(self, "tags"):
            current_tags = self.__dict__.get("tags", [])
            if isinstance(current_tags, list):
                initial_length = len(current_tags)
                if regex is not None:
                    current_tags = [
                        str(tag) for tag in current_tags if not re.match(regex, tag)
                    ]
                else:
                    try:
                        tag_to_remove = re.sub(
                            r"[^a-zA-Z0-9\-_ ]", "_", str(tag_to_remove).strip()
                        )
                        current_tags.remove(tag_to_remove)
                    except ValueError:
                        pass

                if current_tags == [] and not allow_empty:
                    logging.warning("Tags list is empty! -> list will not be updated")
                    return

                if len(current_tags) != initial_length:
                    self.__dict__["tags"] = current_tags
                    self.add_used_attribute("tags")
            else:
                raise TypeError("Tags attribute of the entity is not a list!")
        else:
            raise KeyError("No tags attribute found in this class")

    def __setattr__(self, __name: str, __value: Any) -> None:
        """Sets an attribute of the instance.
        Args:
            __name (str): The name of the attribute to set.
            __value (Any): The value to set the attribute to.
        """

        if type(__value) in [int, str, float, bool]:
            target_type = self.__annotations__.get(__name, type(__value))
            args = get_args(target_type)

            # Converting value if necessary
            if int in args:
                if not isinstance(__value, int):
                    __value = int(float(__value))
            elif str in args:
                if not isinstance(__value, str):
                    __value = str(__value)
            elif bool in args:
                if not isinstance(__value, bool):
                    __value = bool(__value)
            elif float in args:
                if not isinstance(__value, float):
                    __value = float(__value)
            else:
                raise TypeError(
                    f"You tried to assign {type(__value).__name__} to "
                    f"the {target_type.__name__} attribute {__name} -> could "
                    f"not correct it."
                )

        if __value != getattr(self, __name):
            if __name not in ["used_attributes"]:
                self.used_attributes[__name] = getattr(self, __name)

            object.__setattr__(self, __name, __value)

    def _handle_list_values(
        self, value: list, update_type: Literal["full", "used", "used+"] = "used"
    ) -> List[dict]:
        """Handles the update of list of dictionaries or objects. If the list
        contains objects that are subclasses of Blueprint, it will call their
        build_update_dictionary method. If the list contains dictionaries, it
        will return them as is. Versions of the objects will not be included to
        avoid optimistic lock errors.
        """
        items = []

        for item in value:
            if isinstance(item, Blueprint):
                if update_type == "full":
                    item_dict = item.build_update_dictionary(update_type=update_type)
                    del item_dict["version"]  # Remove version if present
                    items.append(item_dict)
                elif update_type in ["used+", "used"]:
                    item.add_used_attribute("id")
                    item_dict = item.build_update_dictionary(update_type="used")
                    if len(item_dict) > 1:
                        items.append(item_dict)
            elif isinstance(item, dict):
                items.append(item)

        return items

    def _handle_custom_attributes(
        self, value: list, update_type: Literal["full", "used", "used+"] = "used"
    ) -> List[dict]:
        """Handles the update of custom attributes. Iterates through the list of
        custom attributes, and adds their update dictionaries to the list of
        custom attributes if they were changed, or if update_type is "full".
        Args:
            value (list): List of custom attributes. Can be a list of
                WeclappMetaData instances or dictionaries.
            update_type (Literal["full", "used", "used+"]): Type of update.
        Returns:
            List[dict]: List of dictionaries representing the updated custom attributes.
        """
        updated_custom_attributes = []
        for custom_attribute in value:
            if isinstance(custom_attribute, WeclappMetaData):
                cat = custom_attribute.build_update_dictionary(update_type=update_type)
                if cat:
                    updated_custom_attributes.append(cat)
                elif update_type == "full":
                    updated_custom_attributes.append(cat)
            elif isinstance(custom_attribute, dict) and hasattr(
                custom_attribute, "attributeDefinitionId"
            ):
                updated_custom_attributes.append(custom_attribute)
        return updated_custom_attributes

    def build_update_dictionary(
        self,
        update_type: Literal["full", "used", "used+"] = "used",
        creation_mode: bool = False,
    ) -> dict:
        """Builds a dictionary for updating or creating an entity in Weclapp.
        Args:
            update_type (Literal[full, used, used+]): Type of update. Defaults to
                "used".
                - "full": Update dictionary will include all attributes of the
                    instance. This type of update should be used with caution as it
                    may lead to optimistic lock errors and could potentially overwrite
                    some values to empty if they are not set in the instance.
                - "used": Update dictionary will include only attributes that have been used.
                - "used+": Update dictionary will include used attributes and version.
                    This type of update should be used cautiously as it may lead to
                    optimistic lock errors.
            creation_mode (bool): If True, the dictionary will be built for creating
                a new entity. Defaults to False.
        Returns:
            dict: Dictionary representing the entity to be updated or created.
        """
        if creation_mode:
            update_type = "full"

        excluded_keys = [
            "used_attributes",
            "used_keys",
            "statusHistory",
        ]

        data_to_send = {}
        for key, value in self.__dict__.items():
            if key in excluded_keys:
                continue
            if key == "customAttributes":
                updated_custom_attributes = self._handle_custom_attributes(
                    value, update_type=update_type
                )
                if len(updated_custom_attributes) > 0:
                    data_to_send[key] = updated_custom_attributes

            elif isinstance(value, list):
                # Handle regular lists.
                if self.__annotations__.get(key, list) == list:
                    if (
                        len(value) > 0
                        or update_type == "full"
                        or key in self.used_attributes
                    ):
                        data_to_send[key] = value
                # Handle lists of Weclapp subclasses or dictionaries.
                else:
                    items = self._handle_list_values(value, update_type=update_type)
                    if len(items) > 0:
                        data_to_send[key] = items

            # Handle Weclapp subclasses.
            elif hasattr(value, "build_update_dictionary"):
                object_dictionary = value.build_update_dictionary(
                    update_type=update_type
                )
                if object_dictionary:
                    del object_dictionary["version"]  # Remove version if present
                    data_to_send[key] = object_dictionary

            # Handle regular attributes.
            elif (
                key in self.used_attributes
                or update_type == "full"
                or (key in ["version"] and update_type == "used+")
            ):
                if creation_mode and key in ["id", "version"]:
                    raise AssertionError(
                        f"Can not post new entity {type(self).__name__} -> "
                        "id or version already set"
                    )
                data_to_send[key] = value

        # Remove keys that are not needed for the update.
        data_to_send = {k: v for k, v in data_to_send.items() if k not in excluded_keys}

        if len(data_to_send) == 1 and "version" in data_to_send:
            data_to_send = {}
        return data_to_send

    @property
    def __entity_name__(self) -> str:
        class_type = type(self)
        entity_name = str(class_type.__name__)
        entity_name = entity_name[:1].lower() + entity_name[1:]
        return entity_name

    def apply_entity_updates(self, entity: Union[dict, object]) -> None:
        """Updates the current instance with the values from the provided entity."""
        if isinstance(entity, dict):
            entity = type(self)(**entity)

        if type(entity) is type(self):
            self.__dict__.update(entity.__dict__)
            self.reset_all_used_attributes()

        else:
            raise AssertionError(
                f"Updated entity type is {type(entity).__name__}, "
                f"but expected {type(self).__name__}"
            )

    def update_entity(
        self,
        update_type: Literal["full", "used", "used+"] = "used",
        enable_logging: bool = False,
    ) -> None:
        """Updates the entity in Weclapp with the attributes set in the instance.
        Args:
            update_type (Literal[full, used, used+]): Type of update. Defaults to 'used'.
                - 'full': Update dictionary will include all attributes of the instance.
                    This type of update should be used with caution as it may lead
                    to optimistic lock errors and could potentially overwrite
                    some values to empty if they are not set in the instance.
                - 'used': Update dictionary will include only attributes that have been used.
                - 'used+': Update dictionary will include used attributes and version.
                    This type of update should be used cautiously as it may lead
                    to optimistic lock errors.
            enable_logging (bool): If True, logs the update action. Defaults to False.
        """

        body = self.build_update_dictionary(update_type=update_type)
        if len(body) == 0:
            logging.warning(
                "No changes detected in %s -> nothing to update", self.__entity_name__
            )
            return
        if hasattr(self, "id"):
            updated_entity = Weclapp().put(
                entity_name=self.__entity_name__, entity_id=self.id, body=body
            )
            self.apply_entity_updates(entity=updated_entity)
            if enable_logging:
                logging.warning("Updated %s with body: %s", type(self).__name__, body)
            return
        raise KeyError(f"Can not update {self.__entity_name__} -> no id found")

    def create_entity(self, enable_logging: bool = False) -> dict:
        """Creates a new entity in Weclapp with the attributes set in the instance.
        Returns:
            dict: The created entity as a dictionary.
        """

        body = self.build_update_dictionary(update_type="full", creation_mode=True)
        if enable_logging:
            logging.warning(
                "Posting new %s to Weclapp with body: %s", type(self).__name__, body
            )
        entity_creation = Weclapp().post(entity_name=self.__entity_name__, body=body)

        self.apply_entity_updates(entity=entity_creation)
        return entity_creation

    @classmethod
    def from_weclapp(cls, entity_id: str):
        """Gets an entity from weclapp by its id and returns a new instance of
        the corresponding class with the attributes set to the values."""
        if not entity_id:
            raise AssertionError(
                "Entity ID must not be None or empty for from_weclapp()"
            )
        entity_name = cls.__name__
        entity_name = entity_name[:1].lower() + entity_name[1:]
        response = Weclapp().get(
            entity_name=entity_name, entity_id=entity_id, as_type=dict
        )
        if not isinstance(response, dict):
            raise AssertionError(
                f"Response from weclapp is not a dict, but a {type(response).__name__}"
            )
        return cls(**response)

    @classmethod
    def from_blank(cls):
        """Creates a new empty instance of the class with all attributes set to
        their default values. This is useful for creating new entities without
        having to specify all attributes manually.
        """
        blank_entity = {}
        nullified_attributes = []

        for attribute, field_info in cls.model_fields.items():

            if getattr(field_info.annotation, "__origin__", None) in [List, list]:
                pass

            # Handle attributes that are weclapp subclasses (e.g. SalesOrderItems)
            elif isinstance(field_info.annotation, type) and issubclass(
                field_info.annotation, Blueprint
            ):
                blank_entity[attribute] = field_info.annotation.from_blank()

            # Handle regular attributes
            elif (
                getattr(field_info.annotation, "__origin__", None) in [Optional, Union]
            ):
                blank_entity[attribute] = None
                nullified_attributes.append(attribute)

            else:
                raise ValueError(
                    f"Unexpected attribute: {attribute} - {field_info.annotation}"
                )

        new_entity = cls(**blank_entity)

        for attribute in nullified_attributes:
            setattr(new_entity, attribute, None)

        new_entity.used_attributes = {}
        return new_entity
