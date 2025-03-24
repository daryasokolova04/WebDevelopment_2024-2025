import socket

def start_server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 7007))
    server_socket.listen(1)
    
    print("Сервер запущен и ожидает подключения...")
    
    while True:
        conn, address = server_socket.accept()
        print(f"Подключен к {address}")
        
        request = conn.recv(1024).decode('utf-8')
        print(f"Запрос: {request}")
        
        try:
            with open('index.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html; charset=utf-8\r\n"
            response += f"\r\n{html_content}"
        except Exception as e:
            response = "HTTP/1.1 500 Internal Server Error\r\n"
            response += "Content-Type: text/html; charset=utf-8\r\n"
            response += "\r\n<h1>500 Internal Server Error</h1>"
            print(f"Ошибка при чтении файла: {e}")
        
        conn.send(response.encode('utf-8'))
        conn.close()

if __name__ == "__main__":
    start_server()

