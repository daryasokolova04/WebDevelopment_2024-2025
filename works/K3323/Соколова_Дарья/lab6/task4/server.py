import socket
import threading

clients = {}

def handle_client(client_socket, client_address):
    print(f"[{client_address}] Подключен.")
    
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    broadcast_message(f"{username} присоединился к чату.", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast_message(f"{username}: {message}", client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        del clients[client_socket]
        print(f"[{client_socket.getpeername()}] Отключен.")
        broadcast_message(f"{username} покинул чат.", client_socket)

def start_server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 1336))
    server_socket.listen(5)
    print("Сервер запущен и ожидает подключения...")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()

