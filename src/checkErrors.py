import string
from typing import TextIO

ACCEPTABLE_CHARS = " " + string.digits + string.ascii_letters


def not_space(input_file: TextIO) -> str:
    while 1:
        following = read_char(input_file)
        if following.isspace():
            continue
        return following


def read_char(input_file: TextIO) -> str:
    following = input_file.read(1)
    if following != '':
        return following
    raise EOFError("Unexpected end of file")


def read_until_space(input_file: TextIO) -> str:
    content = [not_space(input_file)]
    while 1:
        following = input_file.read(1)
        if not following.isspace() and following != '':
            content.append(following)
            continue
        return ''.join(content)
