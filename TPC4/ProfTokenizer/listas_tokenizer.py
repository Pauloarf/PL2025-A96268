import sys
import re

def tokenize(code):
    token_specification = [
        ('NUM',   r'\d+'),  
        ('PA',    r'\['),             
        ('PF',    r'\]'),
        ('VIRG',  r','),      
        # ('NEWLINE',  r'\n'),           
        ('SKIP',  r'[ \t]+'),       
        ('ERRO',  r'.')
    ]
    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    for m in mo:
        dic = m.groupdict()
        if dic['NUM']:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())
        elif dic['PF']:
            t = ("PF", dic['PF'], linha, m.span())
        elif dic['VIRG']:
            t = ("VIRG", ',', linha, m.span())
        elif dic['SKIP']:
            pass
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)

    return reconhecidos


for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)
