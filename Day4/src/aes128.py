from DivBlocks import divide_into_blocks
from RoundKey import add_round_key
from SubWord import sub_word
from ShiftRows import shift_rows
from MixColums import mix_columns
from KeyExpansion import key_expansion
from ConcatBlocks import from_blocks_to_text


def aes_encryption(plain_text: str, secret_key: str, Nb: int = 4, Nr: int = 10) -> str:
    output = []
    if len(plain_text) > 128:
        raise 'Length of plain text greater than 128 bytes'
    if len(secret_key) > 16:
        raise 'Length of secret key greater than 16 bytes'

    state = divide_into_blocks(plain_text, '0x00')
    block_key = divide_into_blocks(secret_key, '0x01')
    hex_key = [[j[2:] for j in i] for i in block_key[0]]
    print('State:',state)
    print('Hex key:', hex_key)
    print('Blocks:', block_key)
    schedule_key = key_expansion(hex_key)
    key = from_blocks_to_text(block_key)

    print('Plain text: ', plain_text)

    print('Key: ', key)

    for block in state:
        round_key = add_round_key(block, block_key[0])
        mix_key = round_key
        for rounds in range(Nr - 1):
            sub_byte = sub_word(mix_key)
            shift = shift_rows(sub_byte)
            mix_col = mix_columns(shift)
            sub_key = [i[Nb * (rounds + 1):Nb * (rounds + 2)] for i in schedule_key]
            mix_key = add_round_key(sub_key, mix_col)

        state = sub_word(mix_key)
        state = shift_rows(state)
        sub_key = [i[Nb * Nr:Nb * (Nr + 1)] for i in schedule_key]
        mix_key = add_round_key(sub_key, state)

        for i in range(4):
            for j in range(4):
                state[j][i] = mix_key[i][j]
        _ = ''.join([''.join([j for j in i]) for i in state])
        output.append(_)

    return ''.join([i for i in output])
