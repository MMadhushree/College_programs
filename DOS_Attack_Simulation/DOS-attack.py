import socket
import time

# Set the target IP address and port
target_ip = "127.0.0.1"
target_port = 5500

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the target
    client_socket.connect((target_ip, target_port))

    # Send multiple GET requests
    for _ in range(10):
        # Craft a malicious payload
        payload = "GET / HTTP/1.1\r\nHost: " + target_ip + "\r\n\r\n"

        # Send the payload to the target
        client_socket.send(payload.encode())

        # Receive and print the response
        response = client_socket.recv(4096)
        print(response.decode())

         # Introduce a delay between each request
        time.sleep(1)

except ConnectionRefusedError:
    print("Connection refused. The target is not listening on the specified port.")

finally:
    # Close the socket
    client_socket.close()