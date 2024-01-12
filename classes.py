from typing import Self


oc_json = dict[str, int | str | list[str]]


class OC:
    character_id: int
    messages: int
    memories: int
    name: str
    description: str
    author: str
    tags: list[str]

    def __str__(self) -> str:
        return f"id: {self.character_id}\n\nmessages: ~ {self.messages} msg\nmemories: {self.memories}\n\nname: {self.name}\nby {self.author}\n\n" \
               f"description: {self.description}\n\ntags: {', '.join(self.tags)}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Self):
            return self.character_id == __value.character_id and self.name == __value.name
        elif isinstance(__value, int):
            return self.character_id == __value
        elif isinstance(__value, str):
            return self.name == __value
        return False

    def to_dict(self) -> oc_json:
        return {
            "character_id": self.character_id,
            "messages": self.messages,
            "memories": self.memories,
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "tags": self.tags
        }
    


def from_dict(data: oc_json) -> OC:
    obj = OC()

    obj.character_id = data.get("character_id")  # type: ignore
    obj.messages = data.get("messages")  # type: ignore
    obj.memories = data.get("memories")  # type: ignore
    obj.name = data.get("name")  # type: ignore
    obj.description = data.get("description")  # type: ignore
    obj.author = data.get("author")  # type: ignore
    obj.tags = data.get("tags")  # type: ignore

    return obj
