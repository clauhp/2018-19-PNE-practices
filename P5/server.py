import http.server
import socketserver

PORT = 8005


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")

        print("Request line: " + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        if self.path == '/':
            f = open("index.html", 'r')
            content = f.read()
            f.close()
        elif self.path == '/blue.html':
            f = open("blue.html", 'r')
            content = f.read()
            f.close()
        elif self.path == '/pink.html':
            f = open("pink.html", 'r')
            content = f.read()
            f.close()
        else:
            f = open("error.html", 'r')
            content = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("192.168.81.218", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
