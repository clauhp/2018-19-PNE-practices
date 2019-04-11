import http.server
import socketserver
import termcolor
from P1.Seq import Seq


PORT = 8000


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
            f = open('response.html', 'w')
            things = self.path.split('&')
            msg = things[0]
            dna = msg[9:]
            base = things[-2].split('=')[1]
            s = Seq(dna.upper())
            operation = things[-1].split('=')[1]

            for x in things:
                if 'count' in x:
                    number = s.count()
                    info.update({operation: number[base]})
                    print(number)

                elif 'perc' in x:
                    percentage = s.perc(base)
                    info.update({operation: percentage})

                elif 'chk=on' in x:
                    info.update({'length': s.len()})

            content = """<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Sequence</title>
    </head>
    <body>
      <h1>Sequence analysis</h1>
      <p>Sequence: {}</p>
      <p></p>
      <p>{}</p>
      <p></p>
      <p>Operation {} on the {} base: {}</p>
      <a href="/">Main page</a>
    </body>
  </html>""".format(dna, info.get('length'), operation, base, info.get(operation))
            f.write(content)
            f.close()
            f = open('response.html', 'r')
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
