from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pymongo import MongoClient
from urllib.parse import urlparse, parse_qs
from bson import json_util

# Connect to MongoDB
mongo_client = MongoClient("mongodb://mongodb:27017")
db = mongo_client['mydb']
collection = db['items']

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_content = json.dumps(content, default=json_util.default)
        self.wfile.write(response_content.encode('utf-8'))

    def do_GET(self):
        if self.path == '/items':
            self.get_items()
        else:
            self._send_response({"error": "Not Found"}, 404)

    def do_POST(self):
        if self.path == '/items':
            self.post_item()
        else:
            self._send_response({"error": "Not Found"}, 404)

    def get_items(self):
        items = list(collection.find({}, {'_id': False}))
        self._send_response(items)

    def post_item(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            item_data = json.loads(post_data.decode('utf-8'))
            if not item_data:
                raise ValueError("No data provided")
            result = collection.insert_one(item_data)
            item_data['_id'] = str(result.inserted_id)
            self._send_response(item_data, 201)
        except Exception as e:
            self._send_response({"error": str(e)}, 400)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving HTTP on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

