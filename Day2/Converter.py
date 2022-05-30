from numpy import ravel

hex_literals = {'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15', 'A': '10', 'B': '11', 'C': '12',
                'D': '13', 'E': '14', 'F': '15'}
hex_digits = {v: k for k, v in hex_literals.items()}
base = 16


class Converter:
    @classmethod
    def hex_to_binary_be(cls, h: str) -> list:
        num = bin(int(h, 16))[2:]
        size = 2
        num = (len(num) % size) * '0' + num if len(num) % size != 0 else num
        return [num[i:i + size] for i in range(0, len(num), size)]

    @classmethod
    def hex_to_binary_le(cls, h: str) -> list:
        num = bin(int(h, 16))[2:]
        size = 8
        num = (len(num) % size) * '0' + num if len(num) % size != 0 else num
        return [num[i:i + size] for i in range(0, len(num), size)][::-1]

    @classmethod
    def to_big_endian(cls, h: str) -> int:
        hex_number = [hex_literals.get(i, i) for i in list(h)[2:]][::-1]
        result = sum([int(hex_number[i]) * (base ** i) for i in range(len(hex_number) - 1, -1, -1)])
        print('Value to big endian: ', result)
        return result

    @classmethod
    def to_little_endian(cls, h: str) -> int:
        hex_str = [hex_literals.get(i, i) for i in list(h)[2:]]
        hex_str = hex_str if len(hex_str) % 2 == 0 else ['0'] + hex_str
        hex_number = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)][::-1]
        print(hex_number)
        hex_number = list(ravel(hex_number))[::-1]
        print(hex_number)
        result = sum([int(hex_number[i]) * (base ** i) for i in range(len(hex_number) - 1, -1, -1)])
        print('Value to little endian: ', result)
        return result

    @classmethod
    def from_big_endian(cls, d: int) -> str:
        hex_num = []
        while d > 0:
            remainder = d % 16
            d //= 16
            hex_num.append(str(remainder))
        hex_num.reverse()
        result = [hex_digits.get(i, i) for i in hex_num]
        result = '0x' + ''.join([i for i in result])
        print('Value from big endian: ', result)
        return result

    @classmethod
    def from_little_endian(cls, d: int, lit_num) -> str:
        hex_num = []
        while d > 0:
            remainder = d % 16
            d //= 16
            hex_num.append(str(remainder))
        hex_num.reverse()
        result = [hex_digits.get(i, i) for i in hex_num]
        result = list(ravel([result[i:i + 2] for i in range(0, len(result), 2)][::-1]))
        result = result[1:] if result[0] == '0' else result
        while len(result) < lit_num:
            result.append('0')
        result = '0x' + ''.join([i for i in result])
        print('Value from little endian: ', result)
        return result

    @classmethod
    def hex_to_int(cls, h: str, end: str) -> None:
        h = h[:2] + h[2:].upper()
        if end == 'little':
            to_l = cls.to_little_endian(h)
            from_l = cls.from_little_endian(to_l, len(h) - 2)
            print('Checksum: ', a := hash(h), b := hash(from_l), a == b)
        if end == 'big':
            to_b = cls.to_big_endian(h)
            from_b = cls.from_big_endian(to_b)
            print('Checksum: ', a := hash(h), b := hash(from_b), a == b)

    @classmethod
    def int_to_hex(cls, d: int, end: str, bytes_num: int = 0) -> None:
        """Enter the number of bytes for little-endian"""
        if end == 'little':
            if bytes_num == 0:
                print("Byte size cannot be a zero")
                return
            from_l = cls.from_little_endian(d, bytes_num * 2)
            to_l = cls.to_little_endian(from_l)
            print('Checksum: ', a := hash(d), b := hash(to_l), a == b)
        if end == 'big':
            from_d = cls.from_big_endian(d)
            to_d = cls.to_big_endian(from_d)
            print('Checksum: ', a := hash(d), b := hash(to_d), a == b)
