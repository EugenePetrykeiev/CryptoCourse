import time

from task2 import keys

start_time = time.time()
HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def broot(keys: list):
    found_key = []
    founded_keys = []
    iter = 0
    print(keys)
    for key in keys:
        str_num = list(map(str, str(key)))
        for lit in str_num[2:]:
            for digit in HEX:
                iter += 1
                if lit == digit:
                    found_key.append(digit)
                    break
        print('Iter:', iter)
        founded_keys.append('0x' + ''.join([str(item) for item in found_key]))
    print(founded_keys)
    print('Time', round((time.time() - start_time) * 1000, 1), ' ms')


broot(keys)
