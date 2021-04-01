from __future__ import annotations
from app.db.models.util.constants import ALPHABET_MAP, BASE


class Decoder:
    @staticmethod
    def decode(key_str: str) -> int:
        num = 0
        for index, symbol in enumerate(reversed(key_str)):
            if symbol not in ALPHABET_MAP:
                return -1
            num += ALPHABET_MAP[symbol] * (BASE ** index)
        return num
