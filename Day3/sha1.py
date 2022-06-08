def sha1_encrypt(msg: str):
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
    bin512split = splitter(list(bin512bit), block_size)
    list32split = [splitter(i, word_size) for i in bin512split]
    words = []
    for item in list32split:
        words.append([''.join(i) for i in item])
    words80 = to_80_words(words)
    digest = core_counting(words80)
    return digest


def core_counting(wrd: list):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    msg = []
    for w in wrd:
        w = [int(i, 2) for i in w]
        for i in range(0, 80):
            f, k = None, None
            if 0 <= i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i < 80:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = (
                left_rot(a, 5) + f + e + k + w[i] & 0xFFFFFFFF,
                a,
                left_rot(b, 30),
                c,
                d,
            )
        h0 = h0 + a & 0xFFFFFFFF
        h1 = h1 + b & 0xFFFFFFFF
        h2 = h2 + c & 0xFFFFFFFF
        h3 = h3 + d & 0xFFFFFFFF
        h4 = h4 + e & 0xFFFFFFFF
        print(hex(h0)[2:])
        digest = hex(h0)[2:].zfill(8) + \
                 hex(h1)[2:].zfill(8) + \
                 hex(h2)[2:].zfill(8) + \
                 hex(h3)[2:].zfill(8) + \
                 hex(h4)[2:].zfill(8)
        msg.append(digest)
    return msg


def splitter(message: list, size: int) -> list:
    return [message[i:i + size] for i in range(0, len(message), size)]


def left_rot(num: int, s: int) -> int:
    return ((num << s) | (num >> (32 - s))) & 0xFFFFFFFF


def to_80_words(wrd: list) -> list:
    result = []
    for w in wrd:
        w = w + ['0' * 32] * 64
        for i in range(16, 80):
            w[i] = bin(left_rot(int(w[i - 3], 2) ^ int(w[i - 8], 2) ^ int(w[i - 14], 2) ^ int(w[i - 16], 2), 1))[2:]
        result.append(w)
    return result
