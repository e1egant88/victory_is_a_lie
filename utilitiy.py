
# Serialization methods 
def normalSend(client_socket):
    ''' Normal simple string message '''
    message = input("Enter your message: ")
    client_socket.send(message.encode('utf-8'))

def serializeUsingJSON(client_socket, obj):
    ''' Method1: Serialize using JSON module '''
    data = json.dumps(obj) # Convert Python object to JSON string
    client_socket.send(data.encode('utf-8'))

def serializeUsingPickle(client_socket, obj):
    ''' Method1: Serialize using Pickle module '''
    data = pickle.dumps(obj) # Convert Python object to JSON string
    client_socket.send(data.encode('utf-8'))

def serializeUsingMessagePack(client_socket, obj):
    ''' Method1: Serialize using MessagePack module '''
    data = msgpack.packb(obj)
    client_socket.send(data)

def serializeUsingProtobuf(client_socket):
    ''' Method1: Serialize using MessagePack module '''
    # Create a Protobuf object
    person = data_pb2.Person()
    person.name = "Alice"
    person.age = 25
    person.city = "New York"
    data = person.SerializeToString()
    client_socket.send(data)

# Reduction methods
def receiveNormalMsg(client_socket):
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")
    with open("messages.txt", "a") as file:
        file.write(message + '\n')

def receiveJsonData(client_socket):
    ''' Receive the serialized data with JSON '''
    data = client_socket.recv(1024).decode('utf-8')
    if data:
        obj = json.loads(data)  # Convert JSON string to Python object
        print(f"Received object: {obj}")
    return data

def receivePickleData(client_socket):
    ''' Receive the serialized data with Pickle '''
    data = client_socket.recv(1024).decode('utf-8')
    if data:
        obj = pickle.loads(data)  # Convert Pickle string to Python object
        print(f"Received object: {obj}")
    return data

def receiveMessagePackData(client_socket):
    ''' Receive the serialized data with MessagePack '''
    data = client_socket.recv(1024)
    if data:
        obj = msgpack.unpackb(data)  # Convert binary data to Python object
        print(f"Received object: {obj}")
    return data

def receiveProtobufData(client_socket):
    ''' Receive the serialized data with Protobuf '''
    data = client_socket.recv(1024)
    person = data_pb2.Person()
    if data:
        person.ParseFromString(data) # protobuf
        print(f"Received object: Name={person.name}, Age={person.age}, City={person.city}")
    return data
