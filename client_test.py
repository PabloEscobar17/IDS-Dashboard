import socket

client = socket.socket()
client.connect(('localhost', 9999))  # Use same port as your IDS

while True:
    message = input("Enter message to IDS (type 'exit' to quit): ")
    if message.lower() == "exit":
        break
    client.send((message + "\n").encode())

client.close()
