import random
import json
from classes import OC, from_dict
import config
import tools


def get_ocs() -> list[OC]:
    data = json.load(open(config.input_ocs))
    return [from_dict(i) for i in data.get("chars", [])]


def entry():
    try:
        ocs: list[OC] = get_ocs()
        if not ocs:
            return tools.error("No OCs found! Did you filled plaintext.txt?")
        oc: OC = random.choice(ocs)
        print(oc)
    except FileNotFoundError:
        tools.error("No parsed OCs found! use cai parse")
