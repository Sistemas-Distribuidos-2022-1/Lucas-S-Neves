from posixpath import split
import socket
from tokenize import String


class Calc_peso_ideal:
    def __init__(self,altura,sexo) -> None:
        self.altura = altura
        self.sexo = sexo
        self.peso_ideal = ''
        self.tipo_cliente = '#4'
    
    def codifica_Calc_peso_ideal(self) -> String:
        return str.encode( self.altura + ',' +  self.sexo + ',' + self.tipo_cliente)
    
    @staticmethod
    def encode_varivel (vari) -> String:
        return str.encode(vari)

    def contar_bytes (self) -> None:
        print (len(self.codifica_Calc_peso_ideal(self)))
    
    def print_Calc_peso_ideal (self) -> None:
        print ('Informações da Pessoa:')
        print ('Altura:', self.altura)
        print ('Sexo: ', self.sexo)
        print (f'Este inviduo tem como peso ideal: {float(self.peso_ideal):.2f}kg')


    def atualiza_mensagem_decodificada (self,mensagem) -> None:
        d_mensagem =  mensagem.decode()
        self.altura, self.sexo, self.peso_ideal, self.tipo_cliente = d_mensagem.split(',')












def criar_objeto () -> object:
    print('Entre com os dados da Pessoa:')
    altura = input( 'Digite aqui a sua altura (cm)\n')
    sexo = input('Digite aqui o seu Sexo\n"F" para feminino e "M" para masculino\n')
    return Calc_peso_ideal(altura,sexo)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 50000
    soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soquete.connect((HOST, PORT))

    #individuo = Calc_peso_ideal('1.76','M')
    individuo = criar_objeto()

    soquete.sendall(individuo.codifica_Calc_peso_ideal())
    mensagem = soquete.recv(1024)
    individuo.atualiza_mensagem_decodificada(mensagem)
    print('Mensagem Ecoada:')
    individuo.print_Calc_peso_ideal()