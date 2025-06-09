import logging
import os
from typing import Generator
import pytest

class Logger:
    _log_file_cleared = False

    @classmethod
    def setup_logging(cls, request: pytest.FixtureRequest) -> Generator[logging.Logger, None, None]:
        if not cls._log_file_cleared:
            with open("test.log", "w") as f:
                f.write("")
            cls._log_file_cleared = True

        test_file = os.path.basename(request.node.fspath.strpath)
        logger = logging.getLogger(request.node.nodeid)

        if not logger.handlers:
            with open("test.log", "a") as f:
                f.write(f"\n======= Test {test_file} starts =======\n")

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%H:%M:%S",
            handlers=[
                logging.FileHandler("test.log", "a"),
                logging.StreamHandler()
            ],
            force=True
        )

        yield logger