import xmlrpc.client

# porta = 50000

with xmlrpc.client.ServerProxy("http://127.0.0.1:50000/") as conexao:
    saldoMedio = float(input("Digite o saldo medio: "))
    message = conexao.saldoMedio(saldoMedio)
    print(message)