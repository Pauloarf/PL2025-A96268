import ply.lex as lex
import json
import math
from datetime import datetime

#region === Print stock information ===
"""

"""
def betterPrint(tipo):
    tipoSize = len(tipo)
    while tipoSize < 13:
        if tipoSize % 2 == 0:
            tipo += ' '
        else:
            tipo = ' ' + tipo
        tipoSize += 1 
    return tipo

def betterPrintNome(tipo):
    tipoSize = len(tipo)
    while tipoSize < 25:
        if tipoSize % 2 == 0:
            tipo += ' '
        else:
            tipo = ' ' + tipo
        tipoSize += 1 
    return tipo

def listStock(stock):
    print("maq:")
    print("     cod     |          nome           |  quantidade |    preço    ")
    print("-------------------------------------------------------------")
    for item in stock:
        cod = item['cod']
        nome = item['nome']
        quantidade = str(item['quant'])
        preco = str(item['preco'])
        print(f'{betterPrint(cod)}|{betterPrintNome(nome)}|{betterPrint(quantidade)}|{betterPrint(preco)}')

#endregion

#Ler o JSON
with open("stock.json", "r", encoding="utf-8") as json_file:
    machineData = json.load(json_file)


#region === Internal Operations ===
saldo = 0

def addEuro(num):
    global saldo
    saldo = saldo + int(num)*100

def addCent(num):
    global saldo
    saldo += int(num)

def printSaldo():
    global saldo
    r = "maq: Saldo = "
    if saldo < 100:
        r = r + str(saldo) + 'c'
    else:
        cents = saldo % 100
        euro = math.floor(saldo/100)
        r = r + str(euro) + 'e' + str(cents) + 'c'
    print(r)

def printSaldoIns(preco):
    global saldo
    r = "maq: Saldo = "
    if saldo < 100:
        r = r + str(saldo) + 'c'
    else:
        cents = saldo % 100
        euro = math.floor(saldo/100)
        r = r + str(euro) + 'e' + str(cents) + 'c'
    
    p = "; Pedido = "
    if preco < 100:
        p = p + str(preco) + 'c'
    else:
        cents = preco % 100
        euro = math.floor(preco/100)
        p = p + str(euro) + 'e' + str(cents) + 'c'

    print(r + p)

def validateCod(cod):
    for item in machineData['stock']:
        if item['cod']==cod:
            return True
    return False

def validateQuant(cod):
    for item in machineData['stock']:
        if item['cod']==cod and item['quant']>0:
            return True
    return False

def buy(cod):
    global saldo
    for item in machineData['stock']:
        if item['cod']==cod and item['quant']>0:
            preco = int(item['preco']*100)
            if saldo>=preco:
                saldo -= preco
                nome = item['nome']
                print(f'maq: Pode retirar o produto dispensado "{nome}"')
                printSaldo()
                item['quant'] -= 1 
            else:
                printSaldoIns(preco)
        
def sair():
    global saldo
    values = [200,100,50,20,10,5,2,1]
    troco = {
        "200":0,
        "100":0,
        "50":0,
        "20":0,
        "10":0,
        "5":0,
        "2":0,
        "1":0,
    }
    i = 0
    while saldo != 0 and i < len(values)-1:
        if(saldo - values[i] >= 0):
            saldo -= values[i]
            troco[str(values[i])] = troco.get(str(values[i]), 0) + 1
        else:
            i += 1
    
    linha = ''
    for key, value in troco.items():
        if value > 0:
            linha = linha + str(value) + 'x ' + key + 'c' + ','
    print(f'maq: Pode retirar o troco: {linha[:-1]}.')
    print("maq: Até à próxima")

    with open("stock.json", "w", encoding="utf-8") as file:
        json.dump(machineData, file, indent=4, ensure_ascii=False)  # The `indent` argument makes the output readable
        print("Os dados foram guardados em stock.json")
#endregion


#region === Define lexer ===
states = (
    ("carregar", "exclusive"),
)

tokens = (
    "LISTAR", # Mostra os detalhes dos produtos que existem
    "MOEDA", # Ativa o modo de carregamento
    "PONTO", # Desliga o modo de carregamento
    "SELECIONAR", # Selecion
    "SAIR",
    "EURO",
    "CENTIMO"
)

t_ANY_ignore = ' ,'

def t_INITIAL_LISTAR(t):
    r"^LISTAR$"
    listStock(machineData['stock'])
    return t

def t_INITIAL_MOEDA(t):
    r"MOEDA"
    t.lexer.begin('carregar')
    return t

def t_INITIAL_SELECIONAR(t):
    r"SELECIONAR\s*[\w]+"
    product_code = t.value.split()[1]
    if(not validateCod(product_code)):
        print("O codigo não existe")
        return t
    if(not validateQuant(product_code)):
        print("Não existe mais stock desse produto")
        return t
    buy(product_code)
    return t

def t_INITIAL_SAIR(t):
    r"^SAIR"
    sair()
    return t

def t_carregar_PONTO(t):
    r"\."
    printSaldo()
    t.lexer.begin('INITIAL')
    return t

def t_carregar_EURO(t):
    r"(1|2)e"
    addEuro(t.value[:-1])
    print("Euro colocado")
    return t


def t_carregar_CENTIMO(t):
    r"(1|2|5|10|20|50)c"
    addCent(t.value[:-1])
    print("Centimo colocado")
    return t


def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#endregion === Define lexer ===


lexer = lex.lex()

date = datetime.today().strftime('%Y-%m-%d')
print(f'maq: {date}, Stock carregado, Estado atualizado.')
print(f'maq: Bom dia. Estou disponível para atender o seu pedido.')
while True:
    user_input = input(">>> ")

    lexer.input(user_input)

    while True:
        token = lexer.token()
        if not token:
            break
    
    if user_input.lower() == 'sair':
        break