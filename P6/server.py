import http.server
import socketserver
import termcolor
from P1.Seq import Seq


PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')
        contents = ''
        info = {}


        if self.path == '/':

            f = open("mainform.html", 'r')
            contents = f.read()

        elif self.path.startswith('/Seq') and '=' in self.path:
            things = self.path.split('&')
            msg = things[0]
            dna = msg[9:]
            base = things[-2].split('=')[1]
            seq = Seq(dna)

            if 'count' or 'perc' in things[-1]:
                count = seq.count(base)
                info.update




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
