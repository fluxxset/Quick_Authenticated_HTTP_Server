# Quick_Authenticated_HTTP_Server



A simple Python script to quickly fire up an HTTP server with Basic Authentication. Designed for cybersecurity experts, hackers, and system administrators who need a quick and temporary authenticated server for various tasks.

## Features

- Quick setup of an HTTP server.
- Basic Authentication to restrict access.
- Command-line arguments for customization.

## Prerequisites

- Python 3.x

## Usage

### Quick Method

Run the following command, replacing the placeholders with appropriate values:

```bash
curl -Ls https://5f5.in/Ej8H | python3 - --username [USERNAME] --password [PASSWORD] --port [PORT]
```
or 

```bash
curl -Ls https://5f5.in/Ej8H | python3 -
```

### Traditional Method

1. Clone the repository:

   ```bash
   git clone https://github.com/fluxx03/Quick_Authenticated_HTTP_Server.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd Quick_Authenticated_HTTP_Server
   ```

3. Run the script:

   ```bash
   python3 server.py --username [USERNAME] --password [PASSWORD] --port [PORT]
   ```

Replace `[USERNAME]`, `[PASSWORD]`, and `[PORT]` with your desired values. The `--port` argument is optional and defaults to `8000` if not provided.

## Security Note

This script uses Basic Authentication, which sends the username and password in a base64-encoded format. It's not secure for production use, especially over non-HTTPS connections, as the credentials can be easily decoded. This tool is intended for temporary use in controlled environments. Always ensure you're following best practices for security.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

You can copy and paste the above content into your `README.md` file on GitHub. Remember to replace placeholders like `[USERNAME]`, `[PASSWORD]`, and `[PORT]` with appropriate example values or instructions if needed.
