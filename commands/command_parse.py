import json
import re

import colorama

import config
from classes import OC, oc_json
import tools

character_id = 1


def data_to_oc(data: list[str]) -> OC:
    global character_id
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

    character_id += 1
    return char


def parse_plain() -> list[OC]:
    with open(config.input_plain) as f:
        test_str: str = f.read()

    matches = re.findall(config.regex, test_str, re.MULTILINE)

    return [data_to_oc(i) for i in matches]


def output_json(ocs: list[OC]) -> None:
    data: dict[str, list[oc_json]] = {
        "chars": [i.to_dict() for i in ocs]
    }
    json.dump(data, open(config.input_ocs, "w"), indent=4)



@tools.timer
def entry() -> None:
    tools.setColor(colorama.Fore.BLUE)
    print("Starting parsing....")
    ocs: list[OC] = parse_plain()
    print(f"Parsed {character_id - 1} characters! Formatting...")
    output_json(ocs)
    print("Formatted!")
