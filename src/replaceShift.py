import random
from typing import TextIO
from functools import cached_property

from src.checkErrors import read_until_space
from src.text import Text


class ShiftEncryption(Text):
    CODE_POINT_SIZE = 6

    def __init__(self, text: str, shift: int):
        super().__init__(text)
        self.shift = shift

    @classmethod
    def from_file(cls, text: str, input_file: TextIO) -> Text:
        try:
            shift = int(read_until_space(input_file))
        except Exception:
            raise ValueError("Incorrect shift")
        return cls(text, shift)

    @cached_property
    def encrypted_text(self) -> str:
        begin = self.shift % self.CODE_POINT_SIZE
        end = self.CODE_POINT_SIZE - self.shift % self.CODE_POINT_SIZE
        return ''.join(chr(((ord(symbol) << begin) | (
                ord(symbol) >> end)) & (
                                   (1 << self.CODE_POINT_SIZE) - 1)) for
                       symbol in self.text)

    @classmethod
    def random_encryption(cls, text: str) -> Text:
        return cls(text, random.randint(0, 20))

    def output(self, output_file: TextIO) -> None:
        super(ShiftEncryption, self).output(output_file)
        print(f'ReplaceShift: {self.shift}; Result: "{self.encrypted_text}"', file=output_file)
