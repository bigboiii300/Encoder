import random
from typing import TextIO

from src.replaceShift import ShiftEncryption
from src.replaceChar import CharEncryption
from src.checkErrors import not_space, read_char, ACCEPTABLE_CHARS
from src.text import Text


def input_text(input_file: TextIO) -> Text:
    try:
        key = int(not_space(input_file))
        if key < 1 or key > 3 or \
                not_space(input_file) != '"':
            raise
    except Exception:
        raise ValueError("Invalid cypher type")
    arr = []
    while True:
        current_symbol = read_char(input_file)
        if current_symbol == '\\':
            current_symbol = read_char(input_file)
        elif current_symbol == '"':
            break
        arr.append(current_symbol)
    content = ''.join(arr)
    text: Text
    if key == Text.Key.REPLACE_CHAR:
        text = CharEncryption.from_file(content, input_file)
    elif key == Text.Key.REPLACE_DIGIT:
        text = CharEncryption.file_to_int(content, input_file, True)
    else:
        text = ShiftEncryption.from_file(content, input_file)
    return text


def random_symbols() -> Text:
    content = ''.join([random.choice(ACCEPTABLE_CHARS) for _ in
                       range(random.randint(0, 20))])
    key = random.randint(1, 3)
    text: Text
    if key == Text.Key.REPLACE_CHAR:
        text = CharEncryption.random_encryption(content)
    elif key == Text.Key.REPLACE_DIGIT:
        text = CharEncryption.random_to_int(content, True)
    else:
        text = ShiftEncryption.random_encryption(content)
    return text
