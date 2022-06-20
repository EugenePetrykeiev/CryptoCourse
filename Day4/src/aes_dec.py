from PaddingBlocks import div_hex_into_blocks, padding_blocks
from RoundKey import add_round_key
from SubWord import sub_word, inv_sub_word
from ShiftRows import shift_rows, inv_shift_rows
from MixColums import mix_columns, inv_mix_columns
from KeyExpansion import key_expansion
from BlockToHex import block_hex
from ConcatBlocks import from_blocks_to_text

Nr = 10
Nb = 4
Nk = 4


def decrypt(cipher_text: str, secret_key: str) -> str:
    state = div_hex_into_blocks(cipher_text)
    block_key = padding_blocks(secret_key)
    hex_key = [[j[2:] for j in i] for i in block_key[0]]
    schedule_key = key_expansion(hex_key)
    sub_key = [i[Nb * Nr:Nb * (Nr + 1)] for i in schedule_key]
    for i in sub_key:
        print(i)
    print('')
    for i in state:
        print(i)
    print('')

    inv_state = add_round_key(sub_key, state)

    for rounds in range(Nr - 1, 0, -1):
        inv_state = inv_shift_rows(inv_state)
        print('')
        for i in inv_state:
            print(i)

        inv_state = inv_sub_word(inv_state)
        print('')
        for i in inv_state:
            print(i)

        sub_key = [i[Nb * Nr:Nb * (Nr + 1)] for i in schedule_key]
        inv_state = add_round_key(sub_key, inv_state)
        inv_state = inv_mix_columns(inv_state)

    inv_state = inv_shift_rows(inv_state)
    inv_state = inv_sub_word(inv_state)
    sub_key = [i[:Nb] for i in schedule_key]
    inv_state = add_round_key(inv_state, sub_key)
    print('from blocks')
    print(inv_state)
    res=[]
    for i in inv_state:
        for j in i:
            res.append(chr(int(j,16)))
    print(res)
    # print(from_blocks_to_text(inv_state))


decrypt('98a4a1e58dfdce73c9f8055c7b24b8e3', 'Lorem ipsum dolo')
