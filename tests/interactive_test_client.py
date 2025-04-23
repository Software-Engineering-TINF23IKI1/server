# this file is an interactive client for testing the BBC Server software

import pathlib
import sys
import os
import typing
from typing import Any
import types
import ast
import socket

BBC_SERVER_DIR = pathlib.Path(__file__).parent.parent / "src"

sys.path.insert(0, os.path.join(BBC_SERVER_DIR))
sys.path.insert(0, os.path.join(pathlib.Path(__file__).parent.parent))

import bbc_server

from tests import TEST_CONFIG


IP = str(TEST_CONFIG.get("test_server", "IP")).strip()
print(IP)
PORT = int(TEST_CONFIG.get("test_server", "PORT").strip())


package_str = ""
packages = bbc_server.packages.PACKAGE_DICT
for idx, package in enumerate(packages.keys()):
    package_str += f"{package} [{idx}]; "

def cast_objects(value: str, target_type: Any):
    if target_type == int:
        return int(value)
    elif target_type == float:
        return float(value)
    elif target_type == bool:
        return bool(value)
    elif target_type == str:
        return value


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((IP, PORT))
    print("Interactive test client. This Client is meant for testing package handling of the BBC server")

    while True:
        print("Please select from the list of packages:")
        print(package_str)
        selection = int(input("Type number to select: "))
        package_class = list(packages.values())[selection]
        cls_parameters = {}
        hints = typing.get_type_hints(package_class.__init__)

        for key, parameter in package_class.JSON_PARAM_MAP.items():
            param_type = hints[parameter]
            if isinstance(param_type, types.GenericAlias) and "dict" in str(param_type):
                # handle dict inputs
                cls_parameters[parameter] = dict(ast.literal_eval(input(f"{key} (as raw dict): ")))
            else:
                param_in = input(f"{key}: ")
                cls_parameters[parameter] = cast_objects(param_in, param_type)

        # create package
        package = package_class(**cls_parameters)
        server.sendall(str.encode(package.to_json() + "\x1E"))

        data = server.recv(1024)
        print(f"\nReceived [\"{data.decode()}\"] from server!\n")
