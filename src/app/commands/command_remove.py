"""
This module provides functions to remove an OC from the list of OCs either by its ID or name.

Functions:
- remove_by_id(character_id: int) -> None
    Remove an OC from the list of OCs by the given character_id.

- remove_by_name(name: str) -> None
    Remove an OC from the list of OCs by the given name.

- save(ocs: list[OC]) -> None
    Save the list of OCs to a JSON file.

- entry(character_id: Optional[int], name: Optional[str]) -> None
    Remove an OC by either its ID or name.
"""
from os import system
from typing import Optional

from fuzzywuzzy import fuzz

from app import tools
from app.classes import OC
from app.commands.command_parse import output_json
from app.commands.command_random import get_ocs


def remove_by_id(character_id: int):  # pylint: disable=inconsistent-return-statements
    """
    Remove an OC from the list of OCs by the given character_id.

    Args:
        character_id (int): An integer representing the ID of the character to be removed.
    """
    ocs: list[OC] = get_ocs()
    if not ocs:
        return tools.error("No OCs found! Did you filled plaintext.txt?")
    oc: OC = sorted(ocs, key=lambda x: x.character_id)[character_id - 1]
    print(oc)
    while True:
        answer: str = input("Process? [Y/n] ").lower()
        match answer:
            case "y" | "":
                break
            case "n":
                return
            case _:
                continue
    del ocs[character_id - 1]

    save(ocs)
    print(f"OC {oc.name} by {oc.author} was deleted!")


def remove_by_name(name: str):  # pylint: disable=inconsistent-return-statements
    """
    Remove an OC from the list of OCs by the given name.

    Args:
        name (str): A string representing the name of the character to be removed.
    """
    ocs: list[OC] = get_ocs()
    if not ocs:
        return tools.error("No OCs found! Did you filled plaintext.txt?")
    ocs: list[OC] = sorted(
        ocs,
        key=lambda x: fuzz.partial_token_set_ratio(name, x.name + " " + x.description), \
        reverse=True
    )
    oc = OC()
    for oc in ocs:
        system("clear")
        print(oc)
        answer: str = input("This one? [y/N] ").lower()
        match answer:
            case "y":
                break
            case "n" | "":
                continue
            case _:
                return
    else:
        return tools.error("No OCs found")

    ocs.remove(oc)  # type: ignore
    ocs = sorted(ocs, key=lambda x: x.character_id)

    save(ocs)
    print(f"OC {oc.name} by {oc.author} was deleted!")


def save(ocs: list[OC]):
    """
    Save the list of OCs to a JSON file.

    Args:
        ocs (list[OC]): A list of OC objects to be saved.
    """
    for ind, oc in enumerate(ocs):
        oc.character_id = ind + 1

    output_json(ocs)


@tools.timer
def entry(  # pylint: disable=inconsistent-return-statements
        character_id: Optional[int],
        name: Optional[str]
    ) -> None:
    """
    Remove an OC by either its ID or name.

    Args:
        character_id (Optional[int]): The ID of the OC to be removed. Defaults to None.
        name (Optional[str]): The name of the OC to be removed. Defaults to None.
    """
    if character_id is not None:
        remove_by_id(character_id)
    elif name is not None:
        remove_by_name(name)
    else:
        return tools.error("You should specify OC's id or name")
