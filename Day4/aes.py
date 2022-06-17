Nb = 4
Nk = 4
Nr = 10

rcon = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

sbox = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]


def divide_into_blocks(text: str, extend: str = None) -> list:
    block_size = 16
    input_block = []
    div16blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    for block in div16blocks:
        block = [hex(ord(i)) for i in block]
        while len(block) < block_size:
            if extend is None:
                block.append(block[-1])
            else:
                block.append(extend)
        div_block = [block[i:i + Nk] for i in range(0, len(block), Nk)]
        for i in range(len(div_block)):
            for j in range(i):
                temp = div_block[i][j]
                div_block[i][j] = div_block[j][i]
                div_block[j][i] = temp
        input_block.append(div_block)
    return input_block



def key_expansion(key: list) -> list:
    temp = []
    # for i in key:
    #     print(i)
    # print('')
    for r in range(Nb, (Nr + 1) * Nb):
        if r % Nk == 0:
            rotated = rot_word([k[r - Nb] for k in key])
            # print('rot', rotated)
            # print('r', r)
            s_box = sub_word([rotated])[0]
            # print('rnk', r // Nk)
            temp = [hex(int(i, 16) ^ rcon[r // Nk])[2:].zfill(2) for i in s_box]
            for i in range(Nk):
                key[i].append(temp[i])
                # print('key', key[i])
        else:
            keys = [k[r - Nb] for k in key]
            # print('keys', keys)
            for i in range(Nk):
                # print(temp[i], keys[i])
                temp[i] = hex(int(temp[i], 16) ^ int(keys[i], 16))[2:].zfill(0)
                key[i].append(temp[i])
    # for i in key:
    #     print(i)
    return key


def add_round_key(state: list, key: list) -> list:
    new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
    for i, b in enumerate(state):
        for j, cell in enumerate(b):
            new_state[i][j] = hex(int(cell, 16) ^ int(key[i][j], 16))[2:].zfill(2)
            # print(state[i][j], '\t', key[i][j], '\t', new_state[i][j])
    # print('state')
    # for i in state:
    #     print(i)
    # print('key')
    # for i in key:
    #     print(i)
    # print('new state')
    # for i in new_state:
    #     print(i)
    return new_state


def sub_word(key: list) -> list:
    new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
    for i, word in enumerate(key):
        for j, char in enumerate(word):
            col = int(char[0], 16)
            raw = int(char[1], 16)
            # print(char[0], '\t', char[1], '\t', col, '\t', raw, '\t', hex(sbox[col][raw]))
            new_state[i][j] = hex(sbox[col][raw])[2:].zfill(2)
    # for i in new_state:
    #     print(i)
    return new_state


def shift_rows(input_state: list) -> list:
    new_state = [input_state[0]]
    for i in range(1, Nk):
        new_state.append(input_state[i][i:] + input_state[i][:i])
    return new_state


def rot_word(input_state: list) -> list:
    return input_state[1:] + input_state[:1]


def mix_columns(input_state: list) -> list:
    dec_state = [[int(i, 16) for i in j] for j in input_state]
    for i in range(Nb):
        s0 = gf_mul_2(dec_state[i][0]) ^ gf_mul_3(dec_state[i][1]) ^ dec_state[i][2] ^ dec_state[i][3]
        s1 = dec_state[i][0] ^ gf_mul_2(dec_state[i][1]) ^ gf_mul_3(dec_state[i][2]) ^ dec_state[i][3]
        s2 = dec_state[i][0] ^ dec_state[i][1] ^ gf_mul_2(dec_state[i][2]) ^ gf_mul_3(dec_state[i][3])
        s3 = gf_mul_3(dec_state[i][0]) ^ dec_state[i][1] ^ dec_state[i][2] ^ gf_mul_2(dec_state[i][3])
        dec_state[i][0] = hex(s0)[2:].zfill(2)
        dec_state[i][1] = hex(s1)[2:].zfill(2)
        dec_state[i][2] = hex(s2)[2:].zfill(2)
        dec_state[i][3] = hex(s3)[2:].zfill(2)
    return dec_state


def gf_mul_3(numb: int) -> int:
    return gf_mul_2(numb) ^ numb


def gf_mul_2(numb: int) -> int:
    if numb < 127:
        numb = (numb << 1) & 0xff
    else:
        numb = ((numb << 1) ^ 0x1b) & 0xff
    return numb


def aes_encrypt(msg: str, secret_key: str):
    if len(secret_key) > 16:
        raise 'Length more than 16 bytes'
    text_blocks = divide_into_blocks(msg, )[0]
    key_blocks = divide_into_blocks(secret_key, '0x01')[0]
    first_round_key = add_round_key(text_blocks, key_blocks)
    keys = key_expansion(first_round_key)
    key = [i[0:4] for i in keys]
    for r in range(Nr - 1):
        state = sub_word(key)
        state = shift_rows(state)
        state = mix_columns(state)
        key = [i[r:r + Nb] for i in keys]
        key = add_round_key(state, key)
    state = sub_word(key)
    state = shift_rows(state)
    state = mix_columns(state)
    key = [i[40:44] for i in keys]
    state = add_round_key(state, key)
    # print(state)
    output = [None for i in range(4 * Nb)]
    for r in range(4):
        for c in range(Nb):
            output[r + 4 * c] = state[r][c]
    # print(output)
    output = ''.join(output)
    return output


cipher = aes_encrypt('HELLO', '1234567890123456')
print(cipher)
