from task1 import SEQUENCE
import random


def key_generator(rng: list) -> list:
    return list(map(lambda x: hex(random.getrandbits(x)), rng))


keys = key_generator(SEQUENCE)

if __name__ == '__main__':
    keys = key_generator(SEQUENCE)
    print(keys)
