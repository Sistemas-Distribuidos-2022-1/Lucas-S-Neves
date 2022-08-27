import Pyro5.api

exerc = Pyro5.api.Proxy("PYRONAME:exercicios")

while(True):
    saldoMedio = float(input("Digite o saldo medio: "))

    message = exerc.saldoMedio(saldoMedio)
    print(message)
    