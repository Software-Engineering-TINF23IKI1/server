import sys
import os
import pathlib
from configparser import ConfigParser
import bbc_server.packages

here = pathlib.Path(__file__).parent

# read config
CONFIG = ConfigParser()
CONFIG.read(here / "config.ini")


