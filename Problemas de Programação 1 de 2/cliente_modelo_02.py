from posixpath import split
import socket
from tokenize import String

HOST = '127.0.0.1'
PORT = 50000
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.connect((HOST, PORT))

class pessoa:
    def __init__(self,nome, sexo, idade) -> None:
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.maturidade = 'Nao Definido'
        self.tipo_cliente = '#2'
    
    def criar_objeto () -> object:
        print('Entre com os dados da Pessoa:')
        nome = input('Digite aqui o seu Nome\n')
        sexo = input('Digite aqui o seu Sexo\n"F" para feminino e "M" para masculino\n')
        idade = input('Digite aqui a sua Idade\n')
        funcio = pessoa(nome,sexo,idade)
        return funcio
    
    def codifica_pessoa(self) -> String:
        return str.encode(self.nome + ',' + self.sexo + ',' + str(self.idade) + ',' + self.tipo_cliente)
    
    def encode_varivel (vari) -> String:
        return str.encode(vari)

    def contar_bytes (self) -> None:
        print (len(self.codifica_pessoa(self)))
    
    def print_pessoa (self) -> None:
        print ('Informações da Pessoa:')
        print ('Nome:', self.nome)
        print ('sexo:', self.sexo)
        print ('idade: {:.0f}'.format(self.idade))
        if self.maturidade == 'True':
            print('Este individuo é maior de idade')
        if self.maturidade == 'False':
            print('Este individuo é menor de idade')

    def atualiza_mensagem_decodifica (self,mensagem) -> None:
        d_mensagem =  mensagem.decode()
        self.nome,self.sexo, self.idade, self.maturidade, self.tipo_cliente = d_mensagem.split(',')
        self.idade = float (self.idade)


# if __name__ == '__main__':
#individuo = pessoa('Lu', 'F',22)
individuo = pessoa.criar_objeto()

soquete.sendall(individuo.codifica_pessoa())
mensagem = soquete.recv(1024)
individuo.atualiza_mensagem_decodifica(mensagem)
print('Mensagem Ecoada:')
individuo.print_pessoa()