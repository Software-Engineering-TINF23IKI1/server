from pathlib import Path
from configparser import ConfigParser
import bbc_server.packages
import bbc_server.tcp_server
import bbc_server.tcp_client
import bbc_server._typing

__here = Path(__file__).parent

# read config
CONFIG = ConfigParser()
CONFIG.read(__here / "config.ini")
