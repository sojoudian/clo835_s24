from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
from zoneinfo import ZoneInfo

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        toronto_tz = ZoneInfo("America/Toronto")
        current_time = datetime.datetime.now(toronto_tz)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = f"<html><head><title>Time Service</title></head><body><h1>Current time in Toronto: {current_time.strftime('%Y-%m-%d %H:%M:%S')}</h1></body></html>"
        self.wfile.write(message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=3030):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()