from functools import reduce

def process_text(text, *blocks):
    def apply_block(text, block):
        return ''.join(map(block, text))

    return reduce(apply_block, blocks, text)
