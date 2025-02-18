import socket

def option_1(client_socket):
    operand = '1'
    client_socket.send(operand.encode('utf-8'))

def option_2(client_socket):
    operand = '2'
    client_socket.send(operand.encode('utf-8'))

def send_message_to_server():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    start_info = client_socket.recv(1024).decode('utf-8')
    print(start_info)

    # Send the message after authentication
    option = input("")
    if option == "1":
        option_1(client_socket)
    elif option == "2":
        option_2(client_socket)

    # Receive the server's acknowledgment
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    client_socket.close()

if __name__ == "__main__":
    send_message_to_server()
    
