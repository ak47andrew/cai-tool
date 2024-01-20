"""
This module provides various tools for terminal output and function timing.

Functions:
- set_color(color: str): Sets the color for the terminal output.
- reset_color(): Resets the color for the terminal output to default.
- error(msg: Any): Prints an error message in red color.
- timer(func: _CallableT) -> _CallableT: Decorator function that times the execution 
of a given function.

Type variables:
- _CallableT: Type variable used to represent a callable object.

Dependencies:
- typing
- time
- colorama
"""


from time import time
from typing import Any, TypeVar

import colorama


def set_color(color: str):
    """
    Sets the color for the terminal output.

    Parameters:
    color (str): A string representing the color to be set.

    Returns:
    None
    """
    print(color, end="")

def reset_color():
    """
    Resets the color for the terminal output to default.

    Parameters:
    None

    Returns:
    None
    """
    print(colorama.Fore.RESET, end="")
    print(colorama.Back.RESET, end="")

def error(msg: Any):
    """
    Prints an error message in red color.

    Parameters:
    msg (Any): The error message to be printed.

    Returns:
    None
    """
    set_color(colorama.Fore.RED)
    print(msg)
    reset_color()


_CallableT = TypeVar("_CallableT")
def timer(func: _CallableT) -> _CallableT:
    """
    timer(func: _CallableT) -> _CallableT

    Decorator function that times the execution of a given function.

    Args:
    - func: A callable object to be timed.

    Returns:
    - A wrapped version of the input function that prints the execution time in seconds 
    after the function completes.

    Example usage:
    @timer
    def my_func():
        # code to be timed

    The above code will print the execution time of my_func() in seconds after it completes.
    """
    def wrapper(*args, **kwargs):
        start = time()

        func(*args, **kwargs)  # type: ignore

        set_color(colorama.Fore.GREEN)
        print(f"Done in {time() - start} sec...")

    return wrapper  # type: ignore
