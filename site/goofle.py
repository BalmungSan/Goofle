from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "rb") as index:
            self.wfile.write((index.read()))

if __name__ == "__main__" :
    myServer = HTTPServer((hostName, hostPort), MyServer)
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()