 # Nao esqueca de abrir primeiro outro terminal com o servidor de nomes
 # Comando: python -m Pyro5.nameserver

import Pyro5.api

@Pyro5.api.expose
class Exerc(object):
    def saldoMedio(self, saldoMedio):
        saldoMedio = float(saldoMedio)
        credito = 0.00

        if saldoMedio >= 0 and saldoMedio <= 200:
            credito = 0.00
        elif saldoMedio >= 201 and saldoMedio <= 400:
            credito = (saldoMedio*20)/100
        elif saldoMedio >= 401 and saldoMedio <= 600:
            credito = (saldoMedio*30)/100
        else:
            credito = (saldoMedio*40)/100
            
        return "Foi aprovado pelo banco o credito de: " + str(credito) + "\n"
	
daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(Exerc)
ns.register("exercicios", uri)

print("Server ativo")
daemon.requestLoop()
	
