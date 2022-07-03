from posixpath import split
import socket
from tokenize import String


class Nadador:
    def __init__(self,idade) -> None:
        self.idade = idade
        self.categoria = ''
        self.tipo_cliente = '#5'
    
    def codifica_nadador(self) -> String:
        return str.encode( self.idade + ',' + self.tipo_cliente)
    
    @staticmethod
    def encode_varivel (vari) -> String:
        return str.encode(vari)

    def contar_bytes (self) -> None:
        print (len(self.codifica_Calc_peso_ideal(self)))
    
    def print_Nadador (self) -> None:
        print ('Informações da Pessoa:')
        print ('idade:', self.idade)
        print ('Este inviduo esta na categoria:', self.categoria)


    def decodifica_mensagem (self,mensagem) -> None:
        self.categoria =  mensagem.decode()


def criar_objeto () -> object:
    print('Entre com os dados da Pessoa:')
    idade = input( 'Digite aqui a sua idade\n')
    return Nadador(idade)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    #individuo = Nadador('8')
    individuo = criar_objeto()

    soquete.sendall(individuo.codifica_nadador())
    mensagem = soquete.recv(1024)
    individuo.decodifica_mensagem(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Nadador()