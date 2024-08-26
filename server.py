import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    host = '127.0.0.1'  # Localhost
    port = 12345
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(1)
    print("Server is listening on {}:{}".format(host, port))
    
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print("Received from client:", data)
    
    # Respond back to the client
    response = "Hi, Kiddo, how are you?"
    client_socket.send(response.encode())
    
    # Close the connection
    client_socket.close()
    server_socket.close()
    print("Server connection closed.")

if __name__ == "__main__":
    start_server()
