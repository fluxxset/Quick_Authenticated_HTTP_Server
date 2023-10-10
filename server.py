import base64
import http.server
import argparse

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
    parser.add_argument('--username', required=True, help='Username for authentication')
    parser.add_argument('--password', required=True, help='Password for authentication')
    parser.add_argument('--port', type=int, default=8000, help='Port to run the server on (default: 8000)')
    args = parser.parse_args()

    AuthHTTPRequestHandler.credentials = base64.b64encode(f"{args.username}:{args.password}".encode()).decode()
    http.server.test(HandlerClass=AuthHTTPRequestHandler, port=args.port)
