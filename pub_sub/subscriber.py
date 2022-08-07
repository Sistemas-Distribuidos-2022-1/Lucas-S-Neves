import zmq
def saldoMedio(saldo):
    saldo = float(saldo)
    credito = 0.00

    if saldo >= 0 and saldo <= 200:
        credito = 0.00
    elif saldo >= 201 and saldo <= 400:
        credito = (saldo*20)/100
    elif saldo >= 401 and saldo <= 600:
        credito = (saldo*30)/100
    else:
        credito = (saldo*40)/100
        
    return "Foi aprovado pelo banco o credito de: " + str(credito) + "\n"



HOST = '127.0.0.1'
PORT = '52000' 

context = zmq.Context()
socket = context.socket(zmq.SUB) # cria um sub tokem
adress = "tcp://"+ HOST +":"+ PORT  #comunicação
socket.connect(adress) #Conectando
socket.setsockopt_string(zmq.SUBSCRIBE, "#9") # SUB mensagens

while(True): # iterações
    data = socket.recv().decode() # Recebendo mensagem
    identificador, salario = data.split(',')
    print ('Mensagem recebida!')
    print("Problema: ", identificador," Recebido")
    print(saldoMedio(salario))