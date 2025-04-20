import socket

import os
import pathlib
import sys

here = pathlib.Path(__file__).parent
repo_root_dir = here.parent

sys.path.insert(0, os.path.join(repo_root_dir / "tests"))
sys.path.insert(0, os.path.join(repo_root_dir))

from tests import TEST_CONFIG


IP = str(TEST_CONFIG.get("test_server", "IP")).strip()
print(IP)
PORT = int(TEST_CONFIG.get("test_server", "PORT").strip())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    print("Type any message to be sent to the server:")

    while True:
        msg = input()

        s.sendall(str.encode(msg + "\x1E"))
        print(f"Send [\"{msg}\"] to server!")

        data = s.recv(1024)
        print(f"Received [\"{data.decode()}\"] from server!")
