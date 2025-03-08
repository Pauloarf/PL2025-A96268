import ply.lex as lex
import re
import sys

#region ============== Declarations ==============

tokens = (
    "SELECT",
    "WHERE",
    "LIMIT",
    "VARIABLE",
    "STRING",
    "URI",
    "DOT",
    "LBRACE",
    "RBRACE",
    "A",
    "SKIP",
    "COMMENT",
)
#endregion ============== Declarations ==============

#region ============== Initializations ==============
def t_SELECT(t): 
    r"SELECT"
    return t

def t_WHERE(t):
    r"WHERE"
    return t

def t_LIMIT(t):
    r"LIMIT\s\d+"
    return t

def t_VARIABLE(t):
    r"\?\w+"
    return t
    
def t_STRING(t):
    r'"[^"]+"@\w+'
    return t
    
def t_URI(t):
    r"\w+:\w+"
    return t
    
def t_DOT(t):
    r"\."
    return t
    
def t_LBRACE(t):
    r"\{"
    return t
    
def t_RBRACE(t):
    r"\}"
    return t
    
def t_A(t):
    r"a"
    return t

def t_SKIP(t):
    r"\s+"
    return t

def t_COMMENT(t):
    r"\#[^\n]*"
    return t

def t_ANY_error(t): 
    print(f"\x1b[31mERROR @{t.lexer.lexstate} #{t.lexer.lexpos}:\x1b[0m Unexpected character: {repr(t.value[0])}")
    t.lexer.skip(1)
    pass
#endregion ============== Initializations ==============

#region ============== Processing ==============
# --- TESTING ---
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

# Inicializar o lexer
lexer = lex.lex()
lexer.input(query)

while True:
    tok = lexer.token()
    if not tok: break

    if (tok.type == 'SKIP'):
        continue
    else:
        print(f"\x1b[36mTOKEN:\x1b[0m {tok}")

#endregion ============== Processing ==============