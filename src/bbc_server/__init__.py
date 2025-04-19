from pathlib import Path
from configparser import ConfigParser

__here = Path(__file__).parent

# read config
CONFIG = ConfigParser()
CONFIG.read(__here / "config.ini")
