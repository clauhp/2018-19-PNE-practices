import http.server
import socketserver

PORT = 8003


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")

        print("Request line: " + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        if self.path == "/":
            f = open("index.html", 'r')
            content = f.read()
            f.close()

        else:
            f = open("error.html", 'r')
            content = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
