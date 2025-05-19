"""logging for the tests"""

from tests import TEST_CONFIG
import logging

formatter = logging.Formatter(
    fmt='[%(asctime)s] [%(levelname)s] [source=%(source)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(str(TEST_CONFIG.get("test_logging", "STREAM_LEVEL")))

file_handler = logging.FileHandler(str(TEST_CONFIG.get("test_logging", "FILE")))
stream_handler.setFormatter(formatter)
file_handler.setLevel(str(TEST_CONFIG.get("test_logging", "FILE_LEVEL")))

TEST_LOGGER = logging.getLogger("TEST_LOGGER")
TEST_LOGGER.setLevel(logging.DEBUG)
TEST_LOGGER.addHandler(stream_handler)
TEST_LOGGER.addHandler(file_handler)
