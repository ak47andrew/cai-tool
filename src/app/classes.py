"""
This module contains the OC class which represents a character in an online chat platform.

OC has the following attributes:
- character_id: An integer representing the unique ID of the character.
- messages: An integer representing the number of messages sent by the character.
- memories: An integer representing the number of memories associated with the character.
- name: A string representing the name of the character.
- description: A string representing the description of the character.
- author: A string representing the author who created the character.
- tags: A list of strings representing the tags associated with the character.

OC has the following methods:
- __str__(self) -> str: Returns a string representation of the character object.
- __eq__(self, __value) -> bool: Returns True if the character object is equal to the input value, 
False otherwise.
- to_dict(self) -> ocJson: Returns a dictionary representation of the character object.

from_dict(data: ocJson) -> OC: Creates an OC object from a dictionary representation.

ocJson is a type alias for dict[str, int | str | list[str]].
"""


from typing import Self

OcJson = dict[str, int | str | list[str]]


class OC:
    """
    OC class represents a character in an online chat platform.

    Attributes:
    - character_id: An integer representing the unique ID of the character.
    - messages: An integer representing the number of messages sent by the character.
    - memories: An integer representing the number of memories associated with the character.
    - name: A string representing the name of the character.
    - description: A string representing the description of the character.
    - author: A string representing the author who created the character.
    - tags: A list of strings representing the tags associated with the character.

    Methods:
    - str(self) -> str: Returns a string representation of the character object.
    - eq(self, __value) -> bool: Returns True if the character object is equal to the input value, 
    False otherwise.
    - to_dict(self) -> ocJson: Returns a dictionary representation of the character object.
    """
    character_id: int
    messages: int
    memories: int
    name: str
    description: str
    author: str
    tags: list[str]

    def __str__(self) -> str:
        return f"id: {self.character_id}\n\nmessages: ~ {self.messages} msg\n" \
               f"memories: {self.memories}\n\nname: {self.name}\nby {self.author}\n\n" \
               f"description: {self.description}\n\ntags: {', '.join(self.tags)}"

    def __eq__(self, __value) -> bool:
        if isinstance(__value, Self):  # pylint: disable=isinstance-second-argument-not-valid-type
            return self.character_id == __value.character_id and self.name == __value.name
        if isinstance(__value, int):
            return self.character_id == __value
        if isinstance(__value, str):
            return self.name == __value
        return False

    def to_dict(self) -> OcJson:
        """
        Returns a dictionary representation of the OC object.

        Returns:
            A dictionary with keys representing the attributes of the OC object 
            and their corresponding values.
            - "character_id": An integer representing the unique ID of the character.
            - "messages": An integer representing the number of messages sent by the character.
            - "memories": An integer representing the number of memories 
            associated with the character.
            - "name": A string representing the name of the character.
            - "description": A string representing the description of the character.
            - "author": A string representing the author who created the character.
            - "tags": A list of strings representing the tags associated with the character.

        Return Type:
            ocJson (type alias for dict[str, int | str | list[str]])
        """
        return {
            "character_id": self.character_id,
            "messages": self.messages,
            "memories": self.memories,
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "tags": self.tags
        }


def from_dict(data: OcJson) -> OC:
    """
    Creates an OC object from a dictionary representation.

    Args:
        data (ocJson): A dictionary with keys representing the attributes of the OC object 
        and their corresponding values.
        - "character_id": An integer representing the unique ID of the character.
        - "messages": An integer representing the number of messages sent by the character.
        - "memories": An integer representing the number of memories associated with the character.
        - "name": A string representing the name of the character.
        - "description": A string representing the description of the character.
        - "author": A string representing the author who created the character.
        - "tags": A list of strings representing the tags associated with the character.

    Returns:
        An OC object with attributes set according to the values in data.

    Return Type:
        OC
    """
    obj = OC()

    obj.character_id = data.get("character_id")  # type: ignore
    obj.messages = data.get("messages")  # type: ignore
    obj.memories = data.get("memories")  # type: ignore
    obj.name = data.get("name")  # type: ignore
    obj.description = data.get("description")  # type: ignore
    obj.author = data.get("author")  # type: ignore
    obj.tags = data.get("tags")  # type: ignore

    return obj
