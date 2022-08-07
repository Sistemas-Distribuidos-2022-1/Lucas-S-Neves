from xmlrpc.server import SimpleXMLRPCServer

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

PORT = 50000
HOST = '127.0.0.1'

server = SimpleXMLRPCServer((HOST, PORT))
print("Server ativo")
print("Porta: ", PORT)

server.register_function(saldoMedio, "saldoMedio")

server.serve_forever()