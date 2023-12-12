from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Insecure origin validation
        origin = self.headers.get('Origin', '')
        
        # Allow requests from any origin (vulnerable)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # Send a simple response
        self.wfile.write(b'Hello, this is the server!')

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
