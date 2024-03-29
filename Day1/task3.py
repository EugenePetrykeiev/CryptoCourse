import time
from task2 import keys

HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
start_time = time.perf_counter()


def broot(k):
    found_keys = []
    for key in k:
        list_num = list(key[2:])
        mask = list(['0'] * len(list_num))
        res = list(['0'] * len(list_num))
        for dig in HEX:
            if dig in list_num:
                for index in reversed(range(0, len(mask))):
                    if index + 1 != len(mask):
                        mask[index + 1] = 0
                    mask[index] = dig
                    if list_num[index] == str(mask[index]):
                        res[index] = mask[index]
            else:
                continue
        result = '0x' + ''.join([str(i) for i in res])
        found_keys.append(result)
        print(f'Founded key! {result}')
        print(f'in: {(time.perf_counter() - start_time) * 1000:.4f} ms')

    print('Generated keys: \n', keys)
    print('Founded kyes: \n', found_keys)
    print('List Hashes:', a := hash(tuple(found_keys)), b := hash(tuple(keys)), a == b)


if __name__ == '__main__':
    broot(keys)
