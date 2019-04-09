import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        if self.path == '/':

            f = open("ex1-form.html", 'r')
            contents = f.read()

        elif self.path.startswith('/echo'):
            f = open("ex1-response.html", 'w')
            path = self.path
            msg = path.split('=')[1]

            content = """<!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Echo Page</title>
                      </head>
                      <body>
                        <h1>Echo of the received message</h1>
                        <p>{}<p>
                        <a href="/">Main page</a>
                      </body>
                    </html>""".format(msg)
            f.write(content)
            f.close()
            f = open('ex1-response.html', 'r')
            contents = f.read()

        else:
            f = open("ex1-error.html", "r")
            contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # --Sending the body of the response message
        self.wfile.write(str.encode(contents))


# --Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
