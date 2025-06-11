import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)

    #Создаем пустой список при создании сервера, куда будем складывать входящие сообщения
    response = []

    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        response.append(data)
        client_socket.send('\n'.join(response).encode())

        client_socket.close()


if __name__ == '__main__':
    server()
