from socketserver import TCPServer, BaseRequestHandler

class TCPHandler(BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        print(f">>> Handling new client from [{self.client_address}]")

        # self.request is the TCP socket connected to the client
        while True:
            try:
                self.data = self.request.recv(1024).strip()
            except ConnectionResetError:
                break # Error: Eine vorhandene Verbindung wurde vom Remotehost geschlossen

            if not self.data: break # Exit on no data

            print(f"[{self.client_address}] {self.data.decode()}")
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

        print(f">>> Client [{self.client_address}] lost connection")

if __name__ == "__main__":
    HOST, PORT = "", 65432

    with TCPServer((HOST, PORT), TCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()