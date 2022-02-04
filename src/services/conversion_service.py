from abc import ABCMeta, abstractmethod

from src.services.decoding_service import BaseDecodingService
from src.services.encoding_service import BaseEncodingService


class BaseConversionService(metaclass=ABCMeta):
    @abstractmethod
    def encode(self, text: int) -> str:
        raise NotImplementedError()

    @abstractmethod
    def decode(self, text: str) -> int:
        raise NotImplementedError()

    @property
    @abstractmethod
    def base(self) -> int:
        raise NotImplementedError()


class ConversionService(BaseConversionService):
    def __init__(self, encoding_service: BaseEncodingService, decoding_service: BaseDecodingService):
        if encoding_service.base != decoding_service.base:
            raise ValueError(f"EncodingService base '{encoding_service.base}' "
                             f"is not equal to DecodingService base '{decoding_service.base}'")
        self._base = decoding_service.base
        self._encoding_service = encoding_service
        self._decoding_service = decoding_service

    def encode(self, text: int) -> str:
        return self._encoding_service.encode(text)

    def decode(self, text: str) -> int:
        return self._decoding_service.decode(text)

    @property
    def base(self) -> int:
        return self._base
