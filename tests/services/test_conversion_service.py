import pytest

from src.services import BaseEncodingService, BaseDecodingService
from src.services.conversion_service import BaseConversionService, ConversionService


class TestConversionService:
    def test_should_encode_and_decode_between_base_64_when_given_an_equivalent_decimal_number_and_base_64_string(
            self, base_64_conversion_service: BaseConversionService):
        base_10_whole_number: int = 68_719_476_735
        base_64_whole_number: str = "------"
        assert base_64_conversion_service.decode(base_64_whole_number) == base_10_whole_number
        assert base_64_conversion_service.encode(base_10_whole_number) == base_64_whole_number

    def test_should_raise_value_error_when_created_with_decoding_and_encoding_services_with_different_bases(
            self, base_64_encoder: BaseEncodingService, base_32_decoder: BaseDecodingService
    ):
        with pytest.raises(ValueError) as ex:
            ConversionService(base_64_encoder, base_32_decoder)
        assert (str(ex.value)) == f"EncodingService base '{base_64_encoder.base}' " \
                                  f"is not equal to DecodingService base '{base_32_decoder.base}'"

    def test_should_get_encoder_decoder_base_when_queried_for_base(
            self, base_64_conversion_service: BaseConversionService
    ):
        assert base_64_conversion_service.base == 64
