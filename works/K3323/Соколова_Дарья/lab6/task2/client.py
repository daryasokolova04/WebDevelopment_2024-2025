import socket

def start_client():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1201))
    
    base = input("Введите основание параллелограмма: ")
    height = input("Введите высоту параллелограмма: ")
    
    client_socket.send(f"{base},{height}".encode('utf-8'))
    
    response = client_socket.recv(1024).decode('utf-8')
    print('Результат: ', response)
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

