from collections import deque

s1 = "100001"
s2 = "101100"


# print(''.join(['1' if i == '0' else '0' for i in s2]))


def bit_and(a: str, b: str) -> str:
    return ''.join([str(int(a) & int(b)) for a, b in zip(a, b)])


def bit_not(a: str) -> str:
    return ''.join(['1' if i == '0' else '0' for i in a])


def bit_or(a: str, b: str) -> str:
    return ''.join([str(int(a) | int(b)) for a, b in zip(a, b)])


def left_rot(num: list, k: int) -> str:
    new_word = deque(num)
    new_word.rotate(-k)
    return ''.join([str(i) for i in list(new_word)])


def bin_add(*args):
    return bin(sum([int(i, 2) for i in args]))[2:].zfill(32)


def bin_hex(h: str) -> str:
    return hex(int(h, 2))[2:]


# print(bin_add('1010101','1010111'))
# a=int('11101111110011011010101110001001',2)
# b=int('10011000101110101101110011111110',2)
# print(bin(a+b)[2:])
# print(left_rot(list('1234'),2))

# print([str(~int(i)) for i in s2])
# print([i for i in s2])
l = []
l = [int(a) & int(b) for a, b in zip(s1, s2)]
# print(l)
# for a,b in zip(s1,~s2):
#     print(int(a), int(b))
#     l.append(int(a)^int(b))
# print(l)

# from collections import deque
# x = [0, 1, 2, 3]
# y=deque(x)
# y.rotate(2)
# print(y)

# from collections import deque
# k = 0
# l = [1, 2, 3, 4, 5]
# z=deque(l)
# z.rotate(-1)
# z=''.join([str(i) for i in list(z)])
# print(z)

#
# a = bin(int('0x67452301', 16))[2:].zfill(32)
# b = bin(int('0xEFCDAB89', 16))[2:].zfill(32)
# c = bin(int('0x98BADCFE', 16))[2:].zfill(32)
# d = bin(int('0x10325476', 16))[2:].zfill(32)
# e = bin(int('0xC3D2E1F0', 16))[2:].zfill(32)
# print(a,b,c,d,e)
print(bin(1).zfill(4))
print(1<<2)
print((1<<2)&0xFFFFFFFF)
print(bytes("Hello",'UTF-8'))