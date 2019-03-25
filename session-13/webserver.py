import http.server
import socketserver

PORT = 8001


class TestHandler (http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line: " + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        content = "I am the happy server! :-)"

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("192.168.1.42", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

    print("")
    print("Server Stopped")
