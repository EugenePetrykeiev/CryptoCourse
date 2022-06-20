def block_hex(block: list) -> str:
    keys = []
    for i in block:
        for k in range(4):
            for j in i:
                keys.append(j[k][2:])
    return ''.join([i for i in keys])
