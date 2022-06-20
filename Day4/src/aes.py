from PaddingBlocks import *
from ConcatBlocks import *
from BlockToHex import *
from RoundKey import *
from SubWord import *
from ShiftRows import *
from MixColums import *
from KeyExpansion import key_expansion

# plain_text = 'Lorem ipsum dolor sit amets'
plain_text = 'Lorem ipsum dolo'
secret_key = 'Hello,world'
Nr = 10
Nb = 4
if __name__ == '__main__':
    if len(plain_text) > 128:
        raise 'Length of plain text greater than 128 bytes'
    state = padding_blocks(plain_text, '0x00')
    text = from_blocks_to_text(state)
    hex_str = block_hex(state)
    print('Input Text: ', text)
    print('Hex Input Text: ', hex_str)
    print(plain_text)

    if len(secret_key) > 16:
        raise 'Length of secret key greater than 16 bytes'
    block_key = padding_blocks(secret_key, '0x00')
    key = from_blocks_to_text(block_key)
    hex_str = block_hex(block_key)
    print('Text key: ', key)
    print('Hex Key: ', hex_str)
    print('Key block: ')
    hex_key = [[j[2:] for j in i] for i in block_key[0]]
    for i in hex_key:
        print(i)
    print('Exp block')
    schedule_key = key_expansion(hex_key)
    for i in schedule_key:
        print(i)
    print('')
    output = []

    for block in state:
        round_key = add_round_key(block, block_key[0])
        mix_key = round_key
        # iterator
        for rounds in range(0, 9):
            print(f'\n Round: {rounds + 1} \n')

            hex_key = block_hex([mix_key])
            print('Round key: ', mix_key)

            sub_byte = sub_word(mix_key)
            hex_word = block_hex([sub_byte])
            print('Sub word: ', hex_word)
            print('\n Sub word bytes:', sub_byte)

            shift = shift_rows(sub_byte)
            hex_shift = block_hex([shift])
            print('Shift Rows: ', hex_shift)
            print('\n Shift words:', shift)

            mix_col = mix_columns(shift)
            mix_hex = block_hex([mix_col])
            print('Mix cols: ', mix_hex)
            print('\n Mult words:', mix_col)

            sub_key = [i[Nb * (rounds + 1):Nb * (rounds + 2)] for i in schedule_key]
            print('Sub key: ')
            for i in sub_key:
                print(i)
            mix_key = add_round_key(sub_key, mix_col)

            print('Mixed sub key: ')
            for i in mix_key:
                print(i)
        state = sub_word(mix_key)
        print('Last sub byte: ', state)
        state = shift_rows(state)
        print('Last shift: ', state)

        sub_key = [i[Nb * (9 + 1):Nb * (9 + 2)] for i in schedule_key]
        print('Sub key: ')
        for i in sub_key:
            print(i)
        mix_key = add_round_key(sub_key, state)

        print('Mixed sub key: ')
        for i in mix_key:
            print(i)
        print('')
        res = ''
        for i in range(4):
            for j in range(4):
                state[j][i] = mix_key[i][j]
        res = ''.join([''.join([j for j in i]) for i in state])
        output.append(res)

    print(output)
