from posixpath import split
import socket
from tokenize import String

HOST = '127.0.0.1'
PORT = 50000
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.connect((HOST, PORT))

class funcionario:
    def __init__(self,nome, cargo, salario) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.tipo_cliente = '#1'
    
    def criar_objeto () -> object:
        print('Entre com os dados do funcionário:')
        nome = input('Digite aqui o seu Nome\n')
        cargo = input('Digite aqui o seu Cargo\n')
        salario = input('Digite aqui o seu Salário\n')
        funcio = funcionario(nome,cargo,salario)
        return funcio
    
    def codifica_funcionario(self) -> String:
        return str.encode(self.nome + ',' + self.cargo + ',' + str(self.salario) + ',' + self.tipo_cliente)
    
    def encode_varivel (vari) -> String:
        return str.encode(vari)

    def contar_bytes (self) -> None:
        print (len(self.codifica_funcionario(self)))
    
    def print_funcionario (self) -> None:
        print ('Informações do Funcionário:')
        print ('Nome:', self.nome)
        print ('Cargo:', self.cargo)
        print ('Salario: {:.2f}'.format(self.salario))

    def atualiza_mensagem_decodifica (self,mensagem) -> None:
        d_mensagem =  mensagem.decode()
        self.nome,self.cargo, self.salario, self.tipo_cliente = d_mensagem.split(',')
        self.salario = float (self.salario)

# if __name__ == '__main__':
#individuo = funcionario('Lucas', 'programador',1212.00)
individuo = funcionario.criar_objeto()

soquete.sendall(individuo.codifica_funcionario())
mensagem = soquete.recv(1024)
individuo.atualiza_mensagem_decodifica(mensagem)
print('Mensagem Ecoada:')
individuo.print_funcionario()