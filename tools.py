from typing import Any, TypeVar
from time import time
import colorama


def setColor(color: str):
    print(color, end="")

def resetColor():
    print(colorama.Fore.RESET, end="")
    print(colorama.Back.RESET, end="")

def error(msg: Any):
    setColor(colorama.Fore.RED)
    print(msg)
    resetColor()


function_type = TypeVar("function_type")
def timer(func: function_type) -> function_type:
    def wrapper():
        start = time()

        func()  # type: ignore

        setColor(colorama.Fore.GREEN)
        print(f"Done in {time() - start} sec...")

    return wrapper  # type: ignore
