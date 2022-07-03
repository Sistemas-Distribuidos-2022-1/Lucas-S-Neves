from posixpath import split
import socket
from tokenize import String


class Funcionario_Salario:
    def __init__(self,nome,nivel,salario_bruto, dependentes) -> None:
        self.nome = nome
        self.nivel = nivel
        self.salario_bruto = salario_bruto
        self.salario_liquido = ''
        self.dependentes = dependentes
        self.tipo_cliente = '#6'
    
    def codifica_Funcionario_Salario(self) -> String:
        return str.encode( self.nome + ',' + self.nivel + ',' + self.salario_bruto + ',' +  self.dependentes + ',' + self.tipo_cliente)
    
    def print_Funcionario_Salario (self) -> None:
        print ('Informações da Pessoa:')
        print ('nome:', self.nome)
        print ('nivel:', self.nivel)
        print (f'Este inviduo tem como salario_liquido: {float(self.salario_liquido):.2f}')

    def decodifica_mensagem (self,mensagem) -> None:
        self.salario_liquido =  mensagem.decode()


def criar_objeto () -> object:
    print('Entre com os dados da Pessoa:')
    nome = input( 'Digite aqui a sua nome\n')
    nivel = input( 'Digite aqui a sua nivel\n')
    salario_bruto = input( 'Digite aqui o seu sálario bruto\n')
    dependentes = input( 'Digite a quantidade de descendentes\n')
    return Funcionario_Salario(nome,nivel,salario_bruto,dependentes)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    individuo = Funcionario_Salario('lucas','A','1000','5')
    #individuo = criar_objeto()

    soquete.sendall(individuo.codifica_Funcionario_Salario())
    mensagem = soquete.recv(1024)
    individuo.decodifica_mensagem(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Funcionario_Salario()