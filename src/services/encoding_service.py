from abc import ABCMeta, abstractmethod
from collections import deque


class BaseEncodingService(metaclass=ABCMeta):
    @abstractmethod
    def encode(self, short_link_id: int) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def base(self) -> int:
        raise NotImplementedError()


class EncodingConfig:
    def __init__(self, base: int, alphabet: str):
        if base != len(alphabet):
            raise ValueError(f"Alphabet length: '{len(alphabet)}' is not equal to base:'{base}'")
        self._base = base
        self._alphabet = alphabet

    @property
    def base(self):
        return self._base

    @property
    def alphabet(self):
        return self._alphabet

    def __str__(self) -> str:
        return f"{'base': '{self._base}', 'alphabet': '{self._alphabet}'}"


class EncodingService(BaseEncodingService):

    def __init__(self, config: EncodingConfig):
        self._base = config.base
        self._alphabet = config.alphabet

    def encode(self, whole_number: int) -> str:
        target_base_digits = deque()
        while whole_number:
            remainder = whole_number % self._base
            target_base_digits.appendleft(self._alphabet[remainder])
            whole_number //= self._base
        return "".join(target_base_digits)

    @property
    def base(self) -> int:
        return self._base
