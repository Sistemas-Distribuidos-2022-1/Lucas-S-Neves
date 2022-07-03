from posixpath import split
import socket
from tokenize import String



class Notas:
    def __init__(self,n1, n2, n3) -> None:
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.aprovacao = ''
        self.tipo_cliente = '#3'
    
    def codifica_Notas(self) -> String:
        return str.encode(self.n1 + ',' + self.n2 + ',' + self.n3 + ',' + self.tipo_cliente)
    
    def encode_varivel (vari) -> String:
        return str.encode(vari)

    def contar_bytes (self) -> None:
        print (len(self.codifica_Notas(self)))
    
    def print_Notas (self) -> None:
        print ('Informações da Notas:')
        print ('n1:', self.n1)
        print ('n2:', self.n2)
        print ('n3:', self.n3)
        if self.aprovacao == 'True':
            print('Este individuo foi aprovado')
        if self.aprovacao == 'False':
            print('Este individuo não foi aprovado')

    def atualiza_mensagem_decodifica (self,mensagem) -> None:
        d_mensagem =  mensagem.decode()
        self.n1,self.n2, self.n3, self.aprovacao, self.tipo_cliente = d_mensagem.split(',')


def criar_objeto () -> object:
    print('Entre com os dados da Notas:')
    n1 = input( 'Digite aqui o seu n1\n')
    n2 = input( 'Digite aqui o seu n2\n')
    n3 = input( 'Digite aqui a sua n3\n')
    return Notas(n1,n2,n3)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    #individuo = Notas('6','5','4.5')
    individuo = criar_objeto()

    soquete.sendall(individuo.codifica_Notas())
    mensagem = soquete.recv(1024)
    individuo.atualiza_mensagem_decodifica(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Notas()