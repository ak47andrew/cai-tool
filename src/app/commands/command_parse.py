"""
This module contains functions for parsing data about original characters (OCs) 
and formatting it into a JSON file.

Functions:
- data_to_oc: Convert a list of data to an instance of the OC class.
- parse_plain: Parse a plain text file containing data about OCs 
and convert it to a list of instances of the OC class.
- output_json: Write a list of instances of the OC class to a JSON file.
- entry: A timer decorator that parses a plain text file and formats the data into a JSON file.
"""

import json
import re

import colorama

from src import config
from src.app import tools
from src.app.classes import OC, OcJson


def data_to_oc(data: list[str], character_id: int) -> OC:
    """
    Converts a list of data to an instance of the OC class.

    Args:
        data (list[str]): A list of strings containing data about the OC.
        character_id (int): The ID of the character.

    Returns:
        OC: An instance of the OC class with the provided data.

    Raises:
        None.
    """
    char = OC()

    char.character_id = character_id

    # messages
    match data[0][-1]:
        case "K":
            multiplier = 1_000
        case "M":
            multiplier = 1_000_000
        case _:
            multiplier = 1
    char.messages = int(float(data[0][:-1]) * multiplier)

    char.memories = int(data[1] or 0)
    char.name = data[2]
    char.description = data[3]
    char.author = data[4]
    char.tags = data[5].splitlines()

    return char


def parse_plain() -> list[OC]:
    """
    Parses a plain text file containing data about OCs and converts it to 
    a list of instances of the OC class.

    Returns:
        list[OC]: A list of instances of the OC class.

    Raises:
        None.

    Note:
        This function reads from a file specified in the config module.
    """
    with open(config.INPUT_PLAIN, encoding="utf-8") as f:
        test_str: str = f.read()

    matches = re.findall(config.REGEX, test_str, re.MULTILINE)

    return [data_to_oc(i, ind + 1) for ind, i in enumerate(matches)]


def output_json(ocs: list[OC]) -> None:
    """
    Writes a list of instances of the OC class to a JSON file.

    Args:
        ocs (list[OC]): A list of instances of the OC class to be written to the JSON file.

    Returns:
        None.

    Raises:
        None.

    Note:
        This function writes to a file specified in the config module.
    """
    data: dict[str, list[OcJson]] = {
        "chars": [i.to_dict() for i in ocs]
    }
    with open(config.INPUT_OCS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


@tools.timer
def entry() -> None:  # pylint: disable=inconsistent-return-statements
    """
    This function, entry(), is a timer decorator that parses a plain text file 
    and formats the data into a JSON file. 

    Returns:
        None

    Raises:
        FileNotFoundError: If the plaintext.txt file is not found.
        ValueError: If no characters are found in the plaintext.txt file.
    """
    tools.set_color(colorama.Fore.BLUE)
    print("Starting parsing....")

    try:
        ocs: list[OC] = parse_plain()
    except FileNotFoundError:
        return tools.error("plaintext.txt is not found! Did you created it?")

    if not ocs:
        return tools.error("No characters found! Did you filled up plaintext.txt?")

    print(f"Parsed {len(ocs)} characters! Formatting...")
    output_json(ocs)
    print("Formatted!")
