import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<SELECT>SELECT)|(?P<WHERE>WHERE)|(?P<LIMIT>LIMIT)|(?P<VARIABLE>\?\w+)|(?P<STRING>"[^"]+"@\w+)|(?P<URI>\w+:\w+)|(?P<DOT>\.)|(?P<LBRACE>\{)|(?P<RBRACE>\})|(?P<A>a)|(?P<SKIP>\s+)|(?P<COMMENT>#[^\n]*)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['VARIABLE']:
            t = ("VARIABLE", dic['VARIABLE'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['URI']:
            t = ("URI", dic['URI'], linha, m.span())
    
        elif dic['DOT']:
            t = ("DOT", dic['DOT'], linha, m.span())
    
        elif dic['LBRACE']:
            t = ("LBRACE", dic['LBRACE'], linha, m.span())
    
        elif dic['RBRACE']:
            t = ("RBRACE", dic['RBRACE'], linha, m.span())
    
        elif dic['A']:
            t = ("A", dic['A'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], linha, m.span())
    
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)
    return reconhecidos



query = """
# DBPedia: obras de Chuck Berry  
SELECT ?nome ?desc WHERE {  
  ?s a dbo:MusicalArtists.  
  ?s foaf:name "Chuck Berry"@en .  
  ?w dbo:artist ?s.  
  ?w foaf:name ?nome.  
  ?w dbo:abstract ?desc  
} LIMIT 1000
"""

tokens = tokenize(query)
for token in tokens:
    print(token)