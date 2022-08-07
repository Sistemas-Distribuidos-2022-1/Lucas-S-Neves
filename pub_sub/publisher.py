import zmq, time

HOST = '127.0.0.1'
PORT = '52000' 

context = zmq.Context()
socket = context.socket(zmq.PUB) # cria um pub soquete
address = "tcp://"+ HOST +":"+ PORT  #comunicação
socket.bind(address) # bucando no endereço passado


print("Publishers ativos!\n")
salario = "230.0"


while True:
    time.sleep(5) #timing de 5 segundos
    socket.send_string("#9" + "," + salario) # pub o tempo atual