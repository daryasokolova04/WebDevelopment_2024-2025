import socket

def start_client():
    client_socket = socket.socket()
    
    client_socket.connect(('localhost', 8085))
    
    message = "Hello, server"
    client_socket.send(message.encode('utf-8'))
    
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Ответ от сервера: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

