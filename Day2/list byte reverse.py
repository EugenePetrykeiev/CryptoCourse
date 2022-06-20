from numpy import ravel


def reverse_bytes(d):
    hex_num = []
    d = list(str(d))
    print(d)
    rev_byte_dec = [d[i:i + 2] for i in range(0, len(d), 2)][::-1]
    rev_byte_dec = list(ravel([i if len(i) % 2 == 0 else ['0', i[0]] for i in rev_byte_dec]))
    dec_bytes = int(''.join([i for i in rev_byte_dec]))
    print(dec_bytes)
    while dec_bytes > 0:
        remainder = dec_bytes % 16
        dec_bytes //= 16
        hex_num.append(str(remainder))
    print(hex_num)
