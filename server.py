import base64
import http.server
import argparse
import random
import string

def generate_random_string(length=4):
    """Generate a random string of given length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    credentials = ""

    def do_HEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Authorization required\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Authorization required')

    def do_GET(self):
        if self.headers.get('Authorization') == f'Basic {self.credentials}':
            super().do_GET()
        else:
            self.do_HEAD()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start an authenticated HTTP server.')
    parser.add_argument('--username', default=generate_random_string(), help='Username for authentication (default: random 4 characters)')
    parser.add_argument('--password', default=generate_random_string(), help='Password for authentication (default: random 4 characters)')
    parser.add_argument('--port', type=int, default=8002, help='Port to run the server on (default: 8002)')
    args = parser.parse_args()

    AuthHTTPRequestHandler.credentials = base64.b64encode(f"{args.username}:{args.password}".encode()).decode()
    print(f"Starting server with username: {args.username}, password: {args.password} on port {args.port}")
    http.server.test(HandlerClass=AuthHTTPRequestHandler, port=args.port)
