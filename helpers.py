import random
from string import ascii_uppercase


def generate_unique_code(length, rooms):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code
