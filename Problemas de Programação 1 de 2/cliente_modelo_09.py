from posixpath import split
import socket
from tokenize import String


class baralho:
    def __init__(self,valor_da_carta,naipe) -> None:
        self.valor_da_carta = valor_da_carta

        # 1 = ouros, 2 = paus, 3 = copas e 4 = espadas
        self.naipe = naipe
        self.tipo_cliente = '#9'
    
    def codifica_baralho(self) -> String:
        return str.encode( self.valor_da_carta + ',' + self.naipe + ','+ self.tipo_cliente)
    
    def print_baralho (self) -> None:
        print ('-----------------------:')
        print ('valor_da_carta:', self.valor_da_carta)
        print ('Naipe:', self.naipe)


    def decodifica_mensagem (self,mensagem) -> None:
        self.naipe =  mensagem.decode()


def criar_objeto () -> object:
    print('Entre com os dados da Carta:')
    valor_da_carta = input( 'Digite aqui a sua valor_da_carta\n')
    naipe = input( 'Digite aqui o naipe dela\n')
    return baralho(valor_da_carta,naipe)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    #individuo = baralho('11','2')
    # individuo = [] 
    # for i in range(4):
    #     individuo.append (baralho('11','2'))
        
    individuo = criar_objeto()

    soquete.sendall(individuo.codifica_baralho())
    mensagem = soquete.recv(1024)
    individuo.decodifica_mensagem(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_baralho()