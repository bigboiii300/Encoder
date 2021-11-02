from abc import ABC, abstractmethod
from functools import cached_property
from typing import TextIO
from enum import IntEnum


class Text(ABC):
    class Key(IntEnum):
        REPLACE_CHAR = 1
        REPLACE_SHIFT = 2
        REPLACE_DIGIT = 3

    def __init__(self, text: str) -> None:
        self.text = text

    def __len__(self) -> object:
        return len(self.text)

    @classmethod
    @abstractmethod
    def from_file(cls, text: str, input_file: TextIO):
        pass

    @cached_property
    def hash(self):
        return sum(map(ord, self.text)) / len(self) if len(self) != 0 else 0.0

    @classmethod
    @abstractmethod
    def random_encryption(cls, text: str):
        pass

    @abstractmethod
    def encrypted_text(self) -> str:
        pass

    def output(self, output_file: TextIO) -> None:
        hash_string = '{:.0f}'.format(self.hash)
        print(f'"{self.text}", Hash={hash_string};', end=' ', file=output_file)
