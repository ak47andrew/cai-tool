"""
This module provides functions to generate a random OC object from a list of OC objects loaded 
from a JSON file. 
The JSON file is specified in the config module.

Functions:
- get_ocs(): Returns a list of OC objects loaded from a JSON file specified in the config module.
- entry(): Generates a random OC object from a list of OC objects loaded from a JSON file. 
           The JSON file is specified in the config module.

Classes:
- None
"""
import json
import random

import config  # type: ignore
from app import tools  # type: ignore
from app.classes import OC, from_dict  # type: ignore


def get_ocs() -> list[OC]:
    """
    Returns a list of OC objects loaded from a JSON file specified in the config module.

    Returns:
        A list of OC objects loaded from a JSON file.

    Return Type:
        list[OC]

    Raises:
        FileNotFoundError: If the specified file in the config module cannot be found.
    """
    with open(config.INPUT_OCS, encoding="utf-8") as f:
        data = json.load(f)
    return [from_dict(i) for i in data.get("chars", [])]


def entry():  # pylint: disable=inconsistent-return-statements
    """
    Generates a random OC object from a list of OC objects loaded from a JSON file. 
    The JSON file is specified in the config module.

    Returns:
        A randomly generated OC object.

    Return Type:
        OC
    """
    try:
        ocs: list[OC] = get_ocs()
        if not ocs:
            return tools.error("No OCs found! Did you filled plaintext.txt?")  # type: ignore
        oc: OC = random.choice(ocs)
        print(oc)
    except FileNotFoundError:
        tools.error("No parsed OCs found! use `cai parse`")
