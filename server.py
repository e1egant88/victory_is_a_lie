import random
import socket
from utility import receiveJsonData

# Predefined valid password
HOST = '127.0.0.1'
PORT = 12345
BACKLOG = 2 # the maximum number of conn acceptance queue can contain

def isLosePoint(goal):
    if (goal - 1) % 3 == 0:
        return True
    return False

def start_server():
    isGameOver = False
    goal = 0
    while True:
        num = random.randint(1, 100)
        if isLosePoint(num):
            goal = num
            break
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(BACKLOG)
    print("Server is listening...")

    while not isGameOver:
        
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive and store messages from authorized clients
        client_socket.send(f"{goal} left. Your turn.".encode('utf-8'))

        while True:
            operand = client_socket.recv(1024).decode('utf-8')
            if not operand:
                break
            goal -= int(operand)
            if goal <= 1:
                client_socket.send("You Lose".encode('utf-8'))
                isGameOver = True
                break
            client_socket.send("Waiting for your opponent...".encode('utf-8'))
            goal -=1 if isLosePoint(goal-1) else 2

            print(goal)

        client_socket.close()
    
    print("Game Over")

if __name__ == "__main__":
    start_server()
