def divide_into_blocks(text: str, extend: str = None) -> list:
    block_size = 16
    input_block = []
    col_size = 4
    div16blocks = [text[i:i + block_size] for i in range(0, len(text), block_size)]
    for block in div16blocks:
        block = [hex(ord(i)) for i in block]
        while len(block) < block_size:
            if extend is None:
                block.append(block[-1])
            else:
                block.append(extend)
        div_block = [block[i:i + col_size] for i in range(0, len(block), col_size)]
        for i in range(len(div_block)):
            for j in range(i):
                temp = div_block[i][j]
                div_block[i][j] = div_block[j][i]
                div_block[j][i] = temp
        input_block.append(div_block)
    return input_block


def div_hex_into_blocks(text: str) -> list:
    Nb = 4
    input_block = [[None for _ in range(Nb)] for _ in range(Nb)]
    div16blocks = [text[i:i + 2] for i in range(0, len(text), 2)]
    blocks = [div16blocks[i:i + Nb] for i in range(0, len(div16blocks), Nb)]
    for i in range(Nb):
        for j in range(Nb):
            input_block[j][i] = blocks[i][j]
    return input_block
