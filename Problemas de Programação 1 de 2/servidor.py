from ast import match_case
from asyncio.windows_events import NULL
from base64 import encode
import socket
from tokenize import String

def atualiza_mensagem (mensagem) -> String:
    d_mensagem =  mensagem.decode()
    tipo_cliente = d_mensagem[-2:]
    match tipo_cliente:
        case '#1':
            return mensagem_de_funcionario (d_mensagem)
        case '#2':
            return mensagem_de_pessoa_maior_idade (d_mensagem)
        case '#3':
            return mensagem_de_notas (d_mensagem)
        case '#4':
            return mensagem_de_imc (d_mensagem)
        case '#5':
            return mensagem_de_categoria_natacao (d_mensagem)
        case '#6':
            return mensagem_de_calculo_salario (d_mensagem)
        case '#7':
            return mensagem_de_calculo_aposentadoria (d_mensagem)
        case '#8':
            return mensagem_de_banco_saldo (d_mensagem)
        case '#9':
            return mensagem_de_baralho (d_mensagem)

def mensagem_de_funcionario (d_mensagem) -> String:
    nome,cargo, salario,tipo_cliente = d_mensagem.split(',')
    salario = float (salario)
    if cargo == 'operador':
        salario *= 1.2
    if cargo == 'programador':
        salario *= 1.18
    return str.encode(nome + ',' + cargo + ',' + str(salario) + ',' + tipo_cliente)

def mensagem_de_pessoa_maior_idade (d_mensagem) -> String:
    nome,sexo,idade,tipo_cliente = d_mensagem.split(',')
    idade = float (idade)
    if sexo == 'F':
        if idade >= 21:
            maturidade = 'True'
        else:
            maturidade = 'False'
    if sexo == 'M':
        if idade >= 18:
            maturidade = 'True'
        else:
            maturidade = 'False'
    return str.encode(nome + ',' + sexo + ',' + str(idade) + ',' + maturidade + ','+ tipo_cliente)

def mensagem_de_notas(d_mensagem) -> String:
    n1,n2, n3,tipo_cliente = d_mensagem.split(',')
    n1 = float (n1)
    n2 = float (n2)
    n3 = float (n3)
    media_n1_e_n2 = (n1 +n2)/2
    if media_n1_e_n2 >= 7:
        aprovacao = 'True'
    elif media_n1_e_n2 > 3:
        nova_media  = (media_n1_e_n2 + n3)/2
        if nova_media >= 5:
            aprovacao = 'True'
        else:
            aprovacao = 'False'
    else:
        aprovacao = 'False'

    return str.encode(str(n1) + ',' + str(n2) + ',' + str(n3) + ','+ aprovacao + ',' + tipo_cliente)

def mensagem_de_imc (d_mensagem)-> String:
    altura,sexo,tipo_cliente = d_mensagem.split(',')
    altura = float(altura)
    
    if sexo == 'M':
        peso_ideal  = (72.7 * altura) - 58
    if sexo == 'F':
         peso_ideal  = (62.1 * altura) - 44.7

    return str.encode(str(altura) + ',' + sexo + ',' + str(peso_ideal) + ','+ tipo_cliente)

def mensagem_de_categoria_natacao (d_mensagem)-> String:
    idade, _ = d_mensagem.split(',')
    #idade = d_mensagem.split(',')[0]
    
    idade = int (idade)
    
    if idade < 5:
        categoria = 'Não valido'
    elif idade <= 7:
        categoria = 'infantil A'
    elif idade <= 10:
         categoria = 'infantil B'
    elif idade <= 13:
         categoria = 'juvenil A'
    elif idade <= 17:
         categoria = 'juvenil B'
    else:
         categoria = 'Adulto'

    return str.encode (categoria)

def mensagem_de_calculo_salario  (d_mensagem)-> String:
    _, nivel,salario_bruto,dependentes, _ = d_mensagem.split(',')
    dependentes = int(dependentes)
    salario_bruto = float (salario_bruto)
    if nivel == 'A':
        if dependentes == 0:
            salario_liguido = salario_bruto - salario_bruto*0.03
        else:
            salario_liguido = salario_bruto - salario_bruto*0.08
    elif nivel == 'B':
        if dependentes == 0:
            salario_liguido = salario_bruto - salario_bruto*0.05
        else:
            salario_liguido = salario_bruto - salario_bruto*0.1
    elif nivel == 'C':
        if dependentes == 0:
            salario_liguido = salario_bruto - salario_bruto*0.08
        else:
            salario_liguido = salario_bruto - salario_bruto*0.15
    elif nivel == 'D':
        if dependentes == 0:
            salario_liguido = salario_bruto - salario_bruto*0.10
        else:
            salario_liguido = salario_bruto - salario_bruto*0.17
    return str.encode (str(salario_liguido))

def mensagem_de_calculo_aposentadoria  (d_mensagem)-> String:
    idade, tempo_serv, _ = d_mensagem.split(',')
    idade = int (idade)
    tempo_serv = float (tempo_serv)

    conseguiu = 'False'
    if idade >= 65 or tempo_serv >= 30:
        if idade >= 60 and tempo_serv >= 25:
            conseguiu = 'True'
    return str.encode (conseguiu)


def mensagem_de_banco_saldo (d_mensagem) -> String:
    saldo_medio, _ = d_mensagem.split(',')
    saldo_medio = int (saldo_medio)
    print (saldo_medio)

    if saldo_medio < 0:
        print("Credito invalido")
        exit()
    elif saldo_medio >= 0 and saldo_medio <= 200:
        credito = 0
    elif saldo_medio <= 400:
        credito = saldo_medio*0.2
    elif saldo_medio <= 600:
        credito = saldo_medio*0.3
    elif saldo_medio > 600:
        credito = saldo_medio*0.4
    return  str.encode (str(credito))


def mensagem_de_baralho (d_mensagem) -> String:
    _, naipe, _ =  d_mensagem.split(',')
    if naipe == '1':
        naipe = 'ouro'
    elif naipe == '2':
        naipe = 'paus'
    elif naipe == '3':
        naipe = 'copas'
    elif naipe == '4':
        naipe = 'espadas'

    return  str.encode (naipe)


HOST = 'localhost'
PORT = 50000
#Parametros
#IPV4: socket.AF_INET
#TCP : socket.SOCK_STREAM
soquete = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#encotrar.. passar os parâmetros para o 's'
soquete.bind((HOST,PORT))

#colocar s no modo de escuta
soquete.listen()
print('Aguardando conexão de um cliente')

#conexão: conexao
#endereço: endereco
conexao, endereco = soquete.accept()
print('conectado em: ', endereco)

while True:
    mensagem = conexao.recv(1024)
    if not mensagem:
        print('Fechando a conexão')
        conexao.close()
        break
    # enviamos aqui a mensagem encoada pelo servidor
    mensagem = atualiza_mensagem (mensagem)
    conexao.sendall(mensagem)