import random
from typing import TextIO, Tuple, List, Union
from functools import cached_property

from src.checkErrors import read_until_space, read_char, ACCEPTABLE_CHARS
from src.text import Text


class CharEncryption(Text):
    MAX_REPLACEMENTS = 50

    def __init__(self, text: str,
                 replacements: List[Tuple[str, Union[int, str]]],
                 to_int: bool) -> None:
        super().__init__(text)
        self.replacements = replacements
        self.to_int = to_int

    @classmethod
    def from_file(cls, text: str, input_file: TextIO) -> Text:
        return cls.file_to_int(text, input_file, False)

    @classmethod
    def file_to_int(cls, text: str, input_file: TextIO,
                    to_int: bool) -> Text:
        try:
            count_replaces = int(read_until_space(input_file))
            if count_replaces < 0:
                raise
        except Exception:
            raise ValueError("Invalid container parameters")
        arr = []
        try:
            for _ in range(count_replaces):
                char = read_char(input_file)
                read_char(input_file)
                to_symbol = read_until_space(
                    input_file) if to_int else read_char(input_file)
                if to_int:
                    to_symbol = int(to_symbol)
                    if 0 <= to_symbol <= 255:
                        pass
                    else:
                        raise
                else:
                    space = input_file.read(1)
                    if space.isspace() or space == '':
                        pass
                    else:
                        raise
                arr.append((char, to_symbol))
        except Exception:
            raise ValueError("Incorrect parameter")
        text = cls(text, arr, to_int)
        if text.check_validation():
            return text
        raise ValueError("Cypher has duplicates")

    @classmethod
    def random_to_int(cls, text: str, to_int: bool) -> Text:
        rnd = random.randint(0, 20)
        pos = set()
        pos1 = [False] * 256 if to_int else set()
        arr = []
        for _ in range(rnd):
            while True:
                from_symbol = random.choice(ACCEPTABLE_CHARS)
                if from_symbol not in pos:
                    break
            pos.add(from_symbol)
            while True:
                to_symbol = random.randint(0, 255) \
                    if to_int else random.choice(ACCEPTABLE_CHARS)
                if to_int and not pos1[to_symbol] or \
                        not to_int and to_symbol not in pos1:
                    break
            if to_int:
                pos1[to_symbol] = True
            else:
                pos1.add(to_symbol)
            arr.append((from_symbol, to_symbol))
        return cls(text, arr, to_int)

    def check_validation(self) -> bool:
        return False if len(
            self.replacements) > CharEncryption.MAX_REPLACEMENTS or len(
            set(pair[0] for pair in self.replacements)) < len(
            self.replacements) or len(
            set(pair[1] for pair in self.replacements)) < len(
            self.replacements) else True

    def replacement_string(self, index: int) -> str:
        return f"{self.replacements[index][0]} <-> {self.replacements[index][1]}"

    @cached_property
    def encrypted_text(self) -> str:
        pair_map = {couple[0]: couple[1] for couple in self.replacements}
        encrypted = [
            pair_map.get(symbol, ord(symbol) if self.to_int else symbol)
            for symbol in self.text]
        return encrypted if self.to_int else ''.join(encrypted)

    @classmethod
    def random_encryption(cls, text: str) -> Text:
        return cls.random_to_int(text, False)

    def output(self, output_file: TextIO) -> None:
        super().output(output_file)
        print("Count of replacements: ", len(self.replacements), "; Symbols: ",
              ' '.join(self.replacement_string(index) for index in
                       range(len(self.replacements))), " ; Result: ", end=' ', file=output_file)
        if not self.to_int:
            print(self.encrypted_text, file=output_file)
        else:
            print("[", ' '.join(map(str, self.encrypted_text)), "]",
                  file=output_file)
