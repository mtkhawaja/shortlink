from collections import deque
from app.db.models.util.constants import ALPHABET, BASE


class Encoder:
    @staticmethod
    def encode(pk: int) -> str:
        target_base_digits = deque()
        while pk:
            remainder = pk % BASE
            target_base_digits.appendleft(ALPHABET[remainder])
            pk //= BASE
        return "".join(target_base_digits)
