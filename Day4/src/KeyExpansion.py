from RotWord import rot_word
from SubWord import sub_word


def key_expansion(key: list) -> list:
    wi1 = []
    Nb = 4
    Nr = 10
    Nk = 4
    for r in range(Nb, (Nr + 1) * Nb):
        if r % Nk == 0:
            w0 = [k[r - Nb] for k in key]
            wi = [k[r - 1] for k in key]
            rotated = rot_word(wi)
            # print('rot', rotated)
            s_box = sub_word([rotated])[0]
            # print('rnk', s_box)
            # print('w0', w0)
            wi = list(hex(int(a, 16) ^ int(b, 16)) for a, b in zip(w0, s_box))
            # print('xor w0,wi: ', wi)
            temp = [int(a, 16) ^ b for a, b in zip(wi, [i[(r // Nk) - 1] for i in rcon])]
            wi1 = [hex(i)[2:].zfill(2) for i in temp]
            # print('wi+1: ', wi1)
            # print('')
            for i in range(Nk):
                key[i].append(wi1[i])
                # print('key', key[i])
        else:
            keys = [k[r - Nb] for k in key]
            # print('keys', keys)
            for i in range(Nk):
                # print(temp[i], keys[i])
                wi1[i] = hex(int(wi1[i], 16) ^ int(keys[i], 16))[2:].zfill(2)
                key[i].append(wi1[i])
    # for i in key:
    #     print(i)
    return key


rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ]
