from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 12345))
while True:
  request = input('Enter request: ')
  clientSocket.send(request.encode())
  response = clientSocket.recv(1024).decode()
  print(f'Response from server: {response}')
  if request.lower() == 'exit':
      print('Exiting client.')
      break
clientSocket.close()