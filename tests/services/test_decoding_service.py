import pytest

from src.services import BaseDecodingService, DecodingConfig


class TestDecodingService:

    def test_should_decode_to_decimal_when_given_a_binary_string(self, binary_decoder: BaseDecodingService):
        assert binary_decoder.decode("11111") == 31

    def test_should_decode_to_decimal_when_given_an_octal_string(self, octal_decoder: BaseDecodingService):
        assert octal_decoder.decode("77777") == 32_767

    def test_should_decode_to_decimal_when_given_a_decimal_string(self, decimal_decoder: BaseDecodingService):
        assert decimal_decoder.decode("99999") == 99_999

    def test_should_decode_to_decimal_when_given_a_hex_string(self, hex_decoder: BaseDecodingService):
        assert hex_decoder.decode("fffff") == 1_048_575

    def test_should_decode_to_decimal_when_given_a_base_32_string(self, base_32_decoder: BaseDecodingService):
        assert base_32_decoder.decode("vvvvv") == 33_554_431

    def test_should_decode_to_decimal_number_when_given_a_base_64_string(self, base_64_decoder: BaseDecodingService):
        assert base_64_decoder.decode("-----") == 1_073_741_823

    def test_should_get_base_when_queried_for_base(self, base_64_decoder: BaseDecodingService):
        assert base_64_decoder.base == 64

    def test_should_raise_value_error_when_decoding_a_string_with_unrecognized_symbols(
            self, binary_decoder: BaseDecodingService
    ):
        unknown_symbol = "$"
        with pytest.raises(ValueError) as ex:
            binary_decoder.decode(f"111{unknown_symbol}11")
        assert str(ex.value) == f"Unknown symbol '{unknown_symbol}' encountered while decoding text!"

    def test_should_raise_value_error_when_creating_a_decoding_config_where_the_alphabet_map_count_does_not_match_the_base(
            self
    ):
        base = 2
        alphabet_map = {"0": 0, "1": 1, "2": 3}
        with pytest.raises(ValueError) as ex:
            DecodingConfig(base, alphabet_map)
        assert str(ex.value) == f"Alphabet Map length: '{len(alphabet_map)}' is not equal to base:'{base}'"
