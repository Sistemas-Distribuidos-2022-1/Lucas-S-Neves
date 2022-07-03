from posixpath import split
import socket
from tokenize import String


class Banco:
    def __init__(self,saldo_medio) -> None:
        self.saldo_medio = saldo_medio
        self.credito = ''
        self.tipo_cliente = '#8'
    
    def codifica_Banco(self) -> String:
        return str.encode( self.saldo_medio + ',' + self.tipo_cliente)
    
    def print_Banco (self) -> None:
        print ('Informações da Pessoa:')
        print ('saldo_medio:', self.saldo_medio)
        print (f'Valor de credito {float(self.credito):.2f}')

    def decodifica_mensagem (self,mensagem) -> None:
        self.credito =  mensagem.decode()

def criar_objeto () -> object:
    print('Entre com os dados da Pessoa:')
    saldo_medio = input( 'Digite aqui a sua saldo_medio\n')
    return Banco(saldo_medio)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    individuo = Banco('201')
    #individuo = criar_objeto()

    soquete.sendall(individuo.codifica_Banco())
    mensagem = soquete.recv(1024)
    individuo.decodifica_mensagem(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Banco()