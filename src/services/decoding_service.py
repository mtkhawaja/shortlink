from abc import ABCMeta, abstractmethod


class BaseDecodingService(metaclass=ABCMeta):
    @abstractmethod
    def decode(self, text: str) -> int:
        raise NotImplementedError()

    @property
    @abstractmethod
    def base(self) -> int:
        raise NotImplementedError()


class DecodingConfig:
    def __init__(self, base: int, alphabet_map: dict[str, int]):
        if base != len(alphabet_map):
            raise ValueError(f"Alphabet Map length: '{len(alphabet_map)}' is not equal to base:'{base}'")
        self._base = base
        self._alphabet_map = alphabet_map

    @property
    def base(self) -> int:
        return self._base

    @property
    def alphabet_map(self) -> dict[str, int]:
        return self._alphabet_map

    def __str__(self) -> str:
        return f"{'base': '{self._base}', 'alphabet_map': '{self._alphabet_map}'}"


class DecodingService(BaseDecodingService):

    def __init__(self, config: DecodingConfig):
        self._base = config.base
        self._alphabet_map = config.alphabet_map

    def decode(self, text: str) -> int:
        num = 0
        for index, symbol in enumerate(reversed(text)):
            if symbol in self._alphabet_map:
                num += self._alphabet_map[symbol] * (self._base ** index)
            else:
                raise ValueError(f"Unknown symbol '{symbol}' encountered while decoding text!")
        return num

    @property
    def base(self) -> int:
        return self._base
