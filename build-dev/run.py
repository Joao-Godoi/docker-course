import getpass
import http.server
import logging
import socketserver
from typing import Any


PORT = 8000


class HTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        logging.info(f"{self.client_address[0]} - - [{self.log_date_time_string()}] {format % args}\n")


logging.basicConfig(filename="/log/http_server.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

logging.getLogger().addHandler(logging.StreamHandler())
logging.info("starting...")

httpd = socketserver.TCPServer(("", PORT), HTTPHandler)
logging.info(f"listening on port: {PORT}")
logging.info(f"user: {getpass.getuser()}")
httpd.serve_forever()
