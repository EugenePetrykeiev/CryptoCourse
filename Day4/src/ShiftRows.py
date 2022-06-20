def shift_rows(input_state: list) -> list:
    Nb = 4
    new_state = [input_state[0]]
    for i in range(1, Nb):
        new_state.append(input_state[i][i:] + input_state[i][:i])
    return new_state


def inv_shift_rows(input_state: list) -> list:
    Nb = 4
    new_state = [input_state[0]]
    for i in range(1, Nb):
        new_state.append(input_state[i][-i:] + input_state[i][:-i])
    return new_state
