from typing import List, TextIO

from src.encryptor import input_text, random_symbols
from src.text import Text


class Container:
    def __init__(self, array: List[Text]) -> None:
        self.array = array

    @classmethod
    def from_file(cls, input_file: TextIO):
        try:
            length = int(input_file.readline())
            if length < 0:
                raise
        except Exception:
            raise ValueError("Invalid container parameters")
        return cls([input_text(input_file) for _ in range(length)])

    @classmethod
    def random_symbols(cls, length: int):
        return cls([random_symbols() for _ in range(length)])

    def __len__(self) -> int:
        return len(self.array)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i].hash
            tmp = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j].hash:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = tmp

    def output(self, output_file: TextIO) -> None:
        print("There are ", len(self), "elements in container", file=output_file)
        for index in range(len(self)):
            print(index + 1, end=". ", file=output_file)
            self.array[index].output(output_file)
