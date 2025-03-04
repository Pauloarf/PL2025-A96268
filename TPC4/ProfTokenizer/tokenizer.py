import sys
import re

def tokenize(code):
    token_specification = [
        ('NUM',   r'\d+'),             # Integer or decimal number
        ('ATRIB',   r'='),             # Assignment operator            # Statement terminator
        ('ID',       r'[_A-Za-z]\w*'), # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('ERRO', r'.'),                # Any other character
    ]
    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    for m in mo:
        dic = m.groupdict()
        if dic['NUM'] is not None:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['OP']:
            t = ("OP", dic['OP'], linha, m.span())
        elif dic['ATRIB'] is not None:
            t = ("ATRIB", "=", linha, m.span())
        elif dic['ID'] is not None:
            t = ("ID", dic['ID'], linha, m.span())
        elif dic['SKIP'] is not None:
            pass
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)

    return reconhecidos


for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)
