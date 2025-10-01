from socket import *
import threading
import random
import json

def service(socket):
  while True:
    command = socket.recv(1024).decode().strip()
    if not command:  # Client disconnected
            break
    print('Received:', command)
    
    request = json.loads(command)    
    method = request.get("method")
    num1 = request.get("Num1")
    num2 = request.get("Num2")
    
    response = {}
    
    if method == "Random": #{"method": "Random", "Num1": 10, "Num2": 20}
      randNum = random.randint(num1, num2)
      response = {"result": randNum}
      print('Sent Random Number:', randNum)
      
    elif method == "Add": #{"method": "Add", "Num1": 10, "Num2": 20}
      sumNum = num1 + num2
      response = {"result": sumNum}
      print('Sent Sum:', sumNum)
      
    elif method == "Subtract": #{"method": "Subtract", "Num1": 10, "Num2": 20}
      subNum = num1 - num2
      response = {"result": subNum}
      print('Sent Subtraction:', subNum)
      
    socket.send((json.dumps(response) + "\n").encode())


serverport = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(2)
print('The server is ready to receive')
while True:
  connectionSocket, addr = serverSocket.accept()
  #connectionSocket.settimeout(20)
  print('Connection from:', addr)
  
  try:
    # Use threading to handle multiple clients
    threading.Thread(target=service, args=(connectionSocket,)).start()
    #service(connectionSocket)
  
  except timeout:
    print('Socket timed out, closing connection')
    connectionSocket.close()