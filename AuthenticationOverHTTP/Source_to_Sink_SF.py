from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        # Parse the form data
        form_data = parse_qs(body)

        # Retrieve username and password from form data
        username = form_data.get('username', [''])[0]
        password = form_data.get('password', [''])[0]

        # Authenticate the user
        response_message = self.authenticate(username, password)

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))

    def authenticate(self, username, password):
        if username == 'admin' and password == 'password':
            return '{"message": "Login successful"}'
        else:
            return '{"message": "Login failed"}'

def run_server(port=5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
