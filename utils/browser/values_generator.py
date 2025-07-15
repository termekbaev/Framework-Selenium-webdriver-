import random
import string
import logging
from datetime import datetime

class ValuesGenerator:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def generate_random_text(self, length: int = 20) -> str:
        random_text = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.logger.info(f"Generated random text '{random_text}'")
        return random_text
    
    def generate_random_int_value(self, minimum: int, maximum: int) -> int:
        random_int_value = random.randint(minimum, maximum)
        self.logger.info(f"Generated random value '{random_int_value}'")
        return random_int_value
    
    def generate_current_datetime_string_in_format(self, format_string="%d.%m.%Y %H:%M:%S") -> str:
        return datetime.strftime(datetime.now(), format_string)
    
    def generate_datetime_string_in_format(self, year=0, month=0, day=0, hour=0, minute=0, second=0, format_string="%d.%m.%Y %H:%M:%S") -> str:
        return datetime.strftime(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second), format_string)