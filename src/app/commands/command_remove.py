from os import system
from typing import Optional

from fuzzywuzzy import fuzz

from app import tools
from app.classes import OC
from app.commands.command_parse import output_json
from app.commands.command_random import get_ocs


@tools.timer
def entry(character_id: Optional[int], name: Optional[str]) -> None:
    if character_id is None and name is None:
        return tools.error("You should specify OC's id or name")
    ocs: list[OC] = get_ocs()
    if not ocs:
        return tools.error("No OCs found! Did you filled plaintext.txt?")
    if character_id is not None:
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
    else:
        ocs: list[OC] = sorted(ocs, key=lambda x: fuzz.partial_token_set_ratio(name, x.name + " " + x.description), reverse=True)
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
            tools.error("No OCs found")
        
        ocs.remove(oc)  # type: ignore
        ocs = sorted(ocs, key=lambda x: x.character_id)
    
    for ind, oc in enumerate(ocs):
        oc.character_id = ind + 1

    output_json(ocs)
    print(f"OC {oc.name} by {oc.author} was deleted!")  # type: ignore
