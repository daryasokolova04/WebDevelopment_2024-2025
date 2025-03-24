import socket

def calculate_area(base, height):
    return base * height

def start_server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 1201))
    server_socket.listen(1)
    
    print("Сервер запущен и ожидает подключения...")
    
    conn, address = server_socket.accept()
    print(f"Подключен к {address}")
    
    data = conn.recv(1024).decode('utf-8')
    base, height = map(float, data.split(','))
    
    area = calculate_area(base, height)
    conn.send(f"Площадь параллелограмма: {area}".encode('utf-8'))
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

