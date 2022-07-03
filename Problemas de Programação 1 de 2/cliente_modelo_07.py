from posixpath import split
import socket
from tokenize import String


class Aposentado:
    def __init__(self,idade,tempo_serv) -> None:
        self.idade = idade
        self.conseguiu = ''
        self.tempo_serv = tempo_serv
        self.tipo_cliente = '#7'
    
    def codifica_Aposentado(self) -> String:
        return str.encode( self.idade + ',' +  self.tempo_serv + ',' + self.tipo_cliente)
    
    def print_Aposentado (self) -> None:
        print ('Informações da Pessoa:')
        print ('idade:', self.idade)
        print ('tempo de serviço:', self.tempo_serv)
        if self.conseguiu == 'True':
            print ('Este inviduo já pode aposentar')
        else:
            print('Este individuo ainda não pode aposentar')

    def decodifica_mensagem (self,mensagem) -> None:
        self.conseguiu =  mensagem.decode()

def criar_objeto () -> object:
    print('Entre com os dados da Pessoa:')
    idade = input( 'Digite aqui a sua idade\n')
    tempo_serv = input( 'Digite aqui a sua tempo de serviço\n')
    return Aposentado(idade,tempo_serv)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    #individuo = Aposentado('66','22')
    individuo = criar_objeto()

    soquete.sendall(individuo.codifica_Aposentado())
    mensagem = soquete.recv(1024)
    individuo.decodifica_mensagem(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Aposentado()