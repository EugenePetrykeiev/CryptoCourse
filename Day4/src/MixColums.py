from gfp import gfp2, gfp3, gfp11, gfp13, gfp9, gfp14


def mix_columns(input_state: list, Nb: int = 4) -> list:
    dec_state = [[int(i, 16) for i in j] for j in input_state]
    new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
    for i in range(Nb):
        s0 = gfp2[dec_state[0][i]] ^ gfp3[dec_state[1][i]] ^ dec_state[2][i] ^ dec_state[3][i]
        s1 = dec_state[0][i] ^ gfp2[dec_state[1][i]] ^ gfp3[dec_state[2][i]] ^ dec_state[3][i]
        s2 = dec_state[0][i] ^ dec_state[1][i] ^ gfp2[dec_state[2][i]] ^ gfp3[dec_state[3][i]]
        s3 = gfp3[dec_state[0][i]] ^ dec_state[1][i] ^ dec_state[2][i] ^ gfp2[dec_state[3][i]]

        new_state[0][i] = hex(s0)[2:].zfill(2)
        new_state[1][i] = hex(s1)[2:].zfill(2)
        new_state[2][i] = hex(s2)[2:].zfill(2)
        new_state[3][i] = hex(s3)[2:].zfill(2)
    return new_state


def inv_mix_columns(input_state: list) -> list:
    Nb = 4
    dec_state = [[int(i, 16) for i in j] for j in input_state]
    new_state = [[None for _ in range(Nb)] for _ in range(Nb)]
    for i in range(Nb):
        s0 = gfp14[dec_state[0][i]] ^ gfp11[dec_state[1][i]] ^ gfp13[dec_state[2][i]] ^ gfp9[dec_state[3][i]]
        s1 = gfp9[dec_state[0][i]] ^ gfp14[dec_state[1][i]] ^ gfp11[dec_state[2][i]] ^ gfp13[dec_state[3][i]]
        s2 = gfp13[dec_state[0][i]] ^ gfp9[dec_state[1][i]] ^ gfp14[dec_state[2][i]] ^ gfp11[dec_state[3][i]]
        s3 = gfp11[dec_state[0][i]] ^ gfp13[dec_state[1][i]] ^ gfp9[dec_state[2][i]] ^ gfp14[dec_state[3][i]]

        new_state[0][i] = hex(s0)[2:].zfill(2)
        new_state[1][i] = hex(s1)[2:].zfill(2)
        new_state[2][i] = hex(s2)[2:].zfill(2)
        new_state[3][i] = hex(s3)[2:].zfill(2)
    return new_state


def gf_mul_3(numb: int) -> int:
    return gf_mul_2(numb) ^ numb


def gf_mul_2(numb: int) -> int:
    if numb < 127:
        numb = (numb << 1) & 0xff
    else:
        numb = ((numb << 1) ^ 0x1b) & 0xff
    return numb
