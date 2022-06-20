def from_blocks_to_text(blocks: list, Nb: int = 4) -> str:
    text = []
    for block in blocks:
        for i in range(Nb):
            for symbol in block:
                if symbol[i] != '0x00':
                    text.append(chr(int(symbol[i][2:], 16)))
    return ''.join([i for i in text])
