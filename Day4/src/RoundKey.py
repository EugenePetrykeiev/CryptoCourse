# def add_round_key(state: list, key: list) -> list:
#     Nb = 4
#     new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
#     for i, b in enumerate(state):
#         for j, cell in enumerate(b):
#             new_state[i][j] = hex(int(cell, 16) ^ int(key[i][j], 16))[2:].zfill(2)
#     return new_state


def add_round_key(state: list, key: list) -> list:
    Nb = 4
    new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
    for i in range(Nb):
        temp = [hex(int(a[i], 16) ^ int(b[i], 16))[2:].zfill(2) for a, b in zip(state, key)]
        for j in range(4):
            new_state[j][i] = temp[j]
    return new_state
