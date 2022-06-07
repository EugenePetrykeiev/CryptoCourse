import numpy as np
from collections import deque


def to_sha1(msg: str):
    byte_size = 8
    block_size = 512
    mod = 448
    word_size = 32
    bin_msg = [bin(ord(i))[2:] for i in list(msg)]

    bin8bit = [i.zfill(byte_size) for i in bin_msg]
    bin512bit = ''.join(bin8bit) + '1'
    while len(bin512bit) % block_size != mod:
        bin512bit += '0'
    bin_length = bin(len(bin8bit) * byte_size)[2:]
    bin_length64 = bin_length.zfill(64)
    bin512bit += bin_length64
    bin512split = [bin512bit[i:i + block_size] for i in range(0, len(bin512bit), block_size)]
    list32split = [np.array_split(list(i), block_size / word_size) for i in bin512split]
    words = []
    for item in list32split:
        words.append([''.join(i) for i in item])
    words80 = to_80_words(words)
    core_counting(words80)


def to_80_words(wrd: list) -> list:
    result = []
    for w in wrd:
        for i in range(16, 80):
            word_a = w[i - 3]
            word_b = w[i - 8]
            word_c = w[i - 14]
            word_d = w[i - 16]

            xor_a = bit_xor(word_a, word_b)
            xor_b = bit_xor(xor_a, word_c)
            xor_c = bit_xor(xor_b, word_d)
            new_word = left_rot(list(xor_c), 1)
            w.append(new_word)
        result.append(w)
    return result


def core_counting(wrd: list):
    h0 = hex2bin32('0x67452301')
    h1 = hex2bin32('0xEFCDAB89')
    h2 = hex2bin32('0x98BADCFE')
    h3 = hex2bin32('0x10325476')
    h4 = hex2bin32('0xC3D2E1F0')
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    print(len(b), len(c))
    for w in wrd:
        for i in range(0, 80):
            f = None
            k = None
            if 0 <= i <= 19:
                and_bc = bit_and(b, c)  #
                and_bd = bit_and(bit_not(b), d)  #
                f = bit_or(and_bc, and_bd)  #
                k = hex2bin32('0x5A827999')  #
            elif 20 <= i <= 39:
                xor_bc = bit_xor(b, c)
                f = bit_xor(xor_bc, d)
                k = hex2bin32('0x6ED9EBA1')
            elif 40 <= i <= 59:
                and_bc = bit_and(b, c)
                and_bd = bit_and(b, d)
                and_cd = bit_and(c, d)
                bc_or_bd = bit_or(and_bc, and_bd)
                f = bit_or(bc_or_bd, and_cd)
                k = hex2bin32('0x8F1BBCDC')
            elif 60 <= i <= 79:
                xor_bc = bit_xor(b, c)
                f = bit_xor(xor_bc, d)
                k = hex2bin32('0xCA62C1D6')
            temp_a = bin_add(left_rot(list(a), 5), f)
            temp_b = bin_add(temp_a, e)
            temp_c = bin_add(temp_b, k)
            temp = bin_add(temp_c, w[i])
            e = d
            d = c
            c = left_rot(list(b), 30)
            b = a
            a = temp
        h0 = bin_add(h0, a)
        h1 = bin_add(h1, b)
        h2 = bin_add(h2, c)
        h3 = bin_add(h3, d)
        h4 = bin_add(h4, e)
        print('\n', h0)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        digest = bin2hex(h0) + bin2hex(h1) + bin2hex(h2) + bin2hex(h3) + bin2hex(h4)
        print(len(digest))


def splitter(message: list, size: int) -> list:
    return [message[i:i + size] for i in range(0, len(message), size)]


def hex2bin32(h: str) -> str:
    return bin(int(h, 16))[2:].zfill(32)


def bit_and(a: str, b: str) -> str:
    size = max(len(a), len(b))
    return ''.join([str(int(a) & int(b)) for a, b in zip(a, b)]).zfill(size)


def bit_not(a: str) -> str:
    return ''.join(['1' if i == '0' else '0' for i in a])


def bit_or(a: str, b: str) -> str:
    size = max(len(a), len(b))
    return ''.join([str(int(a) | int(b)) for a, b in zip(a, b)]).zfill(size)


def bit_xor(a: str, b: str) -> str:
    size = max(len(a), len(b))
    return ''.join([str(int(a) ^ int(b)) for a, b in zip(a, b)]).zfill(size)


def left_rot(num: list, k: int) -> str:
    new_word = deque(num)
    new_word.rotate(-k)
    return ''.join([str(i) for i in list(new_word)])


def bin_add(*args: str) -> str:
    size = max([len(arg) for arg in args])
    return bin(sum([int(i, 2) for i in args]))[2:].zfill(size)


def bin2hex(h: str) -> str:
    return hex(int(h, 2))[2:]


to_sha1('A Test')
print(bin(0b11101111110011011010101110001001 & 0b10011000101110101101110011111110))
