import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port to connect to
    host = '127.0.0.1'  # Localhost
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send data to the server
    message = "hi my name is kiddo"
    client_socket.send(message.encode())
    
    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print("Received from server:", response)
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
