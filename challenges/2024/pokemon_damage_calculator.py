from __future__ import annotations
from typing import Literal, Union
from beginnercodes.challenges import test


Types = Union[Literal["electric"], Literal["fire"], Literal["grass"], Literal["water"]]


def calculate_damage(my_type: Types, their_type: Types, my_attack: int, their_defence: int) -> int:
    return 0  # Put your code here!!!


test(805, calculate_damage)  # Tell it which challenge to test against