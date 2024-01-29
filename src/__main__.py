from typing import Optional

import click
import colorama

from src.app import tools
from src.app.commands.command_parse import entry as parse
from src.app.commands.command_random import entry as random
from src.app.commands.command_remove import entry as remove

colorama.init(autoreset=False)


@click.command("parse")
def parse_command():
    """parsing OCs from plaintext.txt to ocs.json"""
    parse()

@click.command("random")
def random_command():
    """pick random OC from parsed and output it"""
    random()

@click.command("remove")
@click.option("--id", "character_id", help="OC's id", type=int)
@click.option("--name", help="OC's name")
@click.option("--confirm/--no-confirm", show_default=True, default=True, 
              help="Only if using id, is prompting for removal.")
def remove_command(character_id: Optional[int], name: Optional[str], confirm: bool):
    """remove OC by id or name"""
    try:
        character_id = int(character_id)  # type: ignore
    except ValueError:
        return tools.error(f"id must be a number, not {character_id}!")
    except TypeError:
        character_id = None

    try:
        remove(character_id, name, confirm)
    except IndexError as e:
        if character_id is not None:
            return tools.error("id is not found!")
        raise e

@click.group()
def group():
    pass


if __name__ == "__main__":
    group.add_command(parse_command)
    group.add_command(random_command)
    group.add_command(remove_command)
    group()
