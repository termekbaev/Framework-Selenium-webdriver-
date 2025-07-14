import random
import string
import logging

class ValuesGenerator:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def generate_random_text(self, length: int = 20) -> str:
        random_text = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.logger.info(f"Generated random text '{random_text}'")
        return random_text
    
    def generate_random_int_value_between_0_and_100(self) -> int:
        random_int_value = random.randint(0, 100)
        self.logger.info(f"Generated random value '{random_int_value}'")
        return random_int_value