from bbc_server.packages import BasePackage, PACKAGE_DICT
from bbc_server._typing import BBCPackage
import json


def deserialize(input_str: str) -> BBCPackage:
    parsed_dict = json.loads(input_str)
    package_class = PACKAGE_DICT[parsed_dict["type"]]
    param_dict = {package_class.JSON_PARAM_MAP[key]: value for key, value in parsed_dict["body"].items()}
    return package_class(**param_dict)

