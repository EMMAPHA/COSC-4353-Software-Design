def blocker(char_to_block):
    return lambda text: text.replace(char_to_block, '')
