import socket
import threading
import re
from dashboard import Dashboard

dashboard = Dashboard()

# Detection patterns
sql_pattern = re.compile(r".*(DROP|DELETE|UNION|SELECT|INSERT|UPDATE|ALTER|<|>|;|--).*", re.IGNORECASE)
xss_pattern = re.compile(r".*(<script>|<img|onerror=|onload=|javascript:|alert\(|document\.|window\.).*", re.IGNORECASE)
cmd_pattern = re.compile(r".*(;|&&|\|\||\||`|\$\(.*\)|\b(cat|ls|rm|whoami|pwd|cp|mv|wget|curl|ping|nc|netcat|bash|sh)\b).*", re.IGNORECASE)

def handle_client(client_socket, address):
    print(f"[+] Connection from {address}")
    failed_attempts = 0

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print(f"[{address}] {message}")

            # Detection logic
            if sql_pattern.match(message):
                dashboard.add_alert(f"SQL Injection Detected from {address}: {message}")
            elif xss_pattern.match(message):
                dashboard.add_alert(f"XSS Attack Detected from {address}: {message}")
            elif cmd_pattern.match(message):
                dashboard.add_alert(f"Command Injection Detected from {address}: {message}")
            elif "login failed" in message.lower():
                failed_attempts += 1
                if failed_attempts > 5:
                    dashboard.add_alert(f"Brute Force Detected from {address}: {failed_attempts} failed attempts")
            elif "login successful" in message.lower():
                failed_attempts = 0
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    client_socket.close()

def start_server(port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[+] IDS server listening on port {port}")

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.daemon = True
        thread.start()

# Start the GUI and server concurrently
threading.Thread(target=start_server, daemon=True).start()
dashboard.run()
