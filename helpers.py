import random
from string import ascii_uppercase
from typing import Dict


def generate_unique_code(length: int, rooms: Dict) -> str:
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code
