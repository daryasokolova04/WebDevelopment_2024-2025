import socket

def start_server():
    server_socket = socket.socket()
    
    server_socket.bind(('localhost', 8085))
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения...")
    
    conn, address = server_socket.accept()
    print(f"Подключен к {address}")
    
    data = conn.recv(1024).decode('utf-8')
    print(f"Сообщение от клиента: {data}")
    
    response = "Hello, client"
    conn.send(response.encode('utf-8'))
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

