# from main import input_list
BASE = 2
SEQUENCE = list(map(lambda x: 2 ** x, [i for i in range(3, 13)]))


def keys_field(seq: list) -> list:
    return list(map(lambda x: BASE ** x, [val for val in seq]))


trials_val = keys_field(SEQUENCE)

if __name__ == '__main__':
    print('Sequence size', SEQUENCE)
    trials_val = keys_field(SEQUENCE)
    print('Key trials value: ', trials_val)
