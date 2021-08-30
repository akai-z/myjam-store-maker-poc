from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import subprocess

PORT = 8080

class FormRequestHandler(SimpleHTTPRequestHandler):
    FORM = """
    <div style="margin: 80px auto; width: 400px">
        <h4>Myjam Store Maker (POC)</h4>
        <form style="margin: 0" method="post" action="">
            <span>Store Name:</span>
            <input type="text" name="store_name" id="store_name"/>
            <button type="submit" id="submit">Submit</button>
        </form>
        {}
    </div>
    """

    SUCCESS_MSG = """
    <div style="color: green; font-size: small">Store "{}" create request has been received.</div>
    """

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.FORM.format(''))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        storeLabel, store = body.split('=')
        successMsg = self.SUCCESS_MSG.format(store)
        command = 'bash ./src/store-maker --store-name={store}'.format(store=store)

        subprocess.call(command, shell=True)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.FORM.format(successMsg))

if __name__ == '__main__':
    BaseHTTPServer.HTTPServer(('', PORT), FormRequestHandler).serve_forever()
