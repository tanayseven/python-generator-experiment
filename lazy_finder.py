from typing import Tuple, Generator

from constants import NEWLINE_CHARACTERS


def locations_of_newline_characters_generator_function(text: str) -> Generator[Tuple[int, str], None, None]:
    for index, char in enumerate(text):
        if char in NEWLINE_CHARACTERS:
            yield index, char


def locations_of_newline_characters_generator_expression(text: str) -> Generator[Tuple[int, str], None, None]:
    return (
        (index, char)
        for index, char in enumerate(text)
        if char in NEWLINE_CHARACTERS
    )
