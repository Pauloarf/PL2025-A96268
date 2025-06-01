import ply.lex as lex

# Seguir o PEMDAS
# Parentises - Expoentes - Multiplicação - Divisão - Adição - Subtração.
# Neste exemplo vamos ignorar o Exponente.
data = """
5 + 3 * 2 * 2 * 7 - 5 * 3
"""

#region === ANALISADOR LÉXICO ===
tokens = (
    "MULT",
    "DIV",
    "ADD",
    "SUB",
    "NUM"
)

t_ignore = ' \t\r\n'

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_MULT(t):
    r'\*'
    return t

def t_ADD(t):
    r'\+'
    return t

def t_DIV(t):
    r'/'
    return t

def t_SUB(t):
    r'\-'
    return t

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    # O programa crasha, por isso usamos catch
    raise ValueError(f"Illegal character '{t.value[0]}'")


lexer = lex.lex()
#endregion

#region === ANALISADOR SINTATICO ===
prox_simb = ('Erro', '', 0, 0)

def avancar():
    global prox_simb
    prox_simb = lexer.token()

def rec_expr():
    global prox_simb
    resultado = rec_term() 
    while prox_simb and prox_simb.type in ['ADD', 'SUB']:
        operador = prox_simb.type
        avancar() 
        termo = rec_term()
        if operador == 'ADD':
            print(str(resultado) + ' + ' + str(termo))
            resultado += termo
        elif operador == 'SUB':
            print(str(resultado) + ' + ' + str(termo))
            resultado -= termo
    return resultado

def rec_term():
    global prox_simb
    global iValue
    resultado = rec_factor()
    while prox_simb and prox_simb.type in ['MULT', 'DIV']:
        operador = prox_simb.type
        avancar()
        fator = rec_factor()
        if operador == 'MULT':
            print(str(resultado) + ' * ' + str(fator))
            resultado *= fator
        elif operador == 'DIV':
            print(str(resultado) + ' / ' + str(fator))
            resultado /= fator
    return resultado

def rec_factor():
    global prox_simb
    if prox_simb and prox_simb.type == 'NUM':
        valor = prox_simb.value
        avancar() 
        print(f'(num) -> O proximo TOKEN é [{prox_simb.type if prox_simb != None else "None"}]')
        return valor
    else:
        raise ValueError("Esperava um número")

def calcular(expressao):
    global prox_simb
    try:
        lexer.input(expressao)
        avancar() 
        return rec_expr()  
    except ValueError as e:
        print(f"Erro: {e}")
        return None

# Função principal
if __name__ == '__main__':
    while True:
        expressao = input('>>> ')
        resultado = calcular(expressao)
        if resultado is not None:
            print(f'Resultado: {resultado}')