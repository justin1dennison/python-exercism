from itertools import chain
from typing import Iterable, List, Any

gifts = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]


ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def number_to_ordinal(n: int) -> str:
    if n not in range(1, 13):
        raise ValueError("Only the number 1 through 12 are supported")
    return ordinals[n - 1]


def verse(n: int) -> List[str]:
    ordinal = number_to_ordinal(n)
    message = f"On the {ordinal} day of Christmas my true love gave to me: "
    if n == 1:
        gift = gifts[n - 1]
        return message + f"{gift}."
    else:
        gs = gifts[:n]
        first, *rest = gs
        return message + ", ".join(reversed(rest)) + f", and {first}."


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [verse(i) for i in range(start_verse, end_verse + 1)]
