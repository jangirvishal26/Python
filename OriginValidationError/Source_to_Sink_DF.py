from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def get_origin(self):
        # Extract the origin from the request headers
        return self.headers.get('Origin', '')

    def send_response_with_cors(self, origin):
        # Allow requests from any origin (vulnerable)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', origin)
        self.end_headers()

        # Send a simple response
        self.wfile.write(b'Hello, this is the server!')

    def do_GET(self):
        # Insecure origin validation
        origin = self.get_origin()

        # Send the response with CORS headers
        self.send_response_with_cors(origin)

if __name__ == '__main__':
    try:
        # Start an insecure HTTP server
        server_address = ('localhost', 8080)
        httpd = HTTPServer(server_address, SimpleHandler)
        print('Starting server on {}:{}'.format(*server_address))
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('\nShutting down the server')
        httpd.server_close()
