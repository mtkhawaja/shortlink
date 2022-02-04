from enum import Enum, IntEnum

BINARY_ALPHABET: str = "01"
OCTAL_ALPHABET: str = "01234567"
DECIMAL_ALPHABET: str = "0123456789"
HEX_ALPHABET: str = "0123456789abcdef"
BASE_32_ALPHABET: str = "0123456789abcdefghijklmnopqrstuv"
BASE_64_ALPHABET: str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~-"


class Environment(Enum):
    DEV = "DEV"
    QA = "QA"
    STG = "STG"
    PROD = "PROD"


class ConversionBase(IntEnum):
    @staticmethod
    def create_alphabet_mapping(alphabet: str) -> dict[str, int]:
        return {char: index for index, char in enumerate(alphabet)}

    def __new__(cls, value, *args, **kwargs):
        obj = int.__new__(cls, value)
        obj._value_ = value
        return obj

    def __init__(self, value: int, alphabet: str, alphabet_map: dict[str, int] = None) -> None:
        self._alphabet = alphabet
        self._alphabet_map = self.create_alphabet_mapping(alphabet) if alphabet_map is None else alphabet_map

    @property
    def alphabet(self) -> str:
        return self._alphabet

    @property
    def alphabet_map(self) -> dict[str, int]:
        return self._alphabet_map

    BINARY = (2, BINARY_ALPHABET, None)
    OCTAL = (8, OCTAL_ALPHABET, None)
    DECIMAL = (10, DECIMAL_ALPHABET, None)
    HEX = (16, HEX_ALPHABET, None)
    BASE_32 = (32, BASE_32_ALPHABET, None)
    BASE_64 = (64, BASE_64_ALPHABET, None)
