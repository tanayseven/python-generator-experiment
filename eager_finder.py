from typing import List, Tuple

from constants import NEWLINE_CHARACTERS


def locations_of_newline_characters(text: str) -> List[Tuple[int, int]]:
    locations: List[Tuple[int, int]] = []
    for index, char in enumerate(text):
        if char in NEWLINE_CHARACTERS:
            locations.append((index, char,))
    return locations
