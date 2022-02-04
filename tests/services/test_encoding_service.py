import pytest

from src.services import BaseEncodingService, EncodingConfig


class TestEncodingService:

    def test_should_encode_to_binary_when_given_a_decimal_number(self, binary_encoder: BaseEncodingService):
        assert binary_encoder.encode(31) == "11111"

    def test_should_encode_to_octal_when_given_a_decimal_number(self, octal_encoder: BaseEncodingService):
        assert octal_encoder.encode(32_767) == "77777"

    def test_should_encode_to_decimal_when_given_a_decimal_number(self, decimal_encoder: BaseEncodingService):
        assert decimal_encoder.encode(99_999) == "99999"

    def test_should_encode_to_hex_when_given_a_decimal_number(self, hex_encoder: BaseEncodingService):
        assert hex_encoder.encode(1_048_575) == "fffff"

    def test_should_encode_to_base_32_when_given_a_decimal_number(self, base_32_encoder: BaseEncodingService):
        assert base_32_encoder.encode(33_554_431) == "vvvvv"

    def test_should_encode_to_base_64_when_given_a_decimal_number(self, base_64_encoder: BaseEncodingService):
        assert base_64_encoder.encode(1_073_741_823) == "-----"

    def test_should_get_base_when_queried_for_base(self, base_64_encoder: BaseEncodingService):
        assert base_64_encoder.base == 64

    def test_should_raise_value_error_when_creating_an_encoding_config_where_the_alphabet_count_does_not_match_the_base(
            self
    ):
        base = 2
        alphabet = "012"
        with pytest.raises(ValueError) as ex:
            EncodingConfig(base, alphabet)
        assert str(ex.value) == f"Alphabet length: '{len(alphabet)}' is not equal to base:'{base}'"
