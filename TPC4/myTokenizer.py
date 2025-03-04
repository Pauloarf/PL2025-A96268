import re

def tokenize(input_string):
    tokens = [
        {"id": "SELECT", "expreg": r"SELECT"},
        {"id": "WHERE", "expreg": r"WHERE"},
        {"id": "LIMIT", "expreg": r"LIMIT"},
        {"id": "VARIABLE", "expreg": r"\?\w+"},
        {"id": "STRING", "expreg": r'"[^"]+"@\w+'},
        {"id": "URI", "expreg": r"\w+:\w+"},
        {"id": "DOT", "expreg": r"\."},
        {"id": "LBRACE", "expreg": r"\{"},
        {"id": "RBRACE", "expreg": r"\}"},
        {"id": "A", "expreg": r"a"},
        {"id": "SKIP", "expreg": r"\s+"},
        {"id": "COMMENT", "expreg": r"#[^\n]*"},
    ]

    # Combina todas as expressões regulares em uma única
    tokens_regex = '|'.join([f'(?P<{t["id"]}>{t["expreg"]})' for t in tokens])

    reconhecidos = []
    linha = 1

    # Usa re.finditer para encontrar todos os tokens na string
    for m in re.finditer(tokens_regex, input_string):
        dic = m.groupdict()
        for token_id, value in dic.items():
            if value:
                if token_id == "SKIP" or token_id == "COMMENT":
                    continue  # Ignora espaços e comentários
                t = (token_id, value, linha, m.span())
                reconhecidos.append(t)
                break

    return reconhecidos


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

tokens = tokenize(query)
for token in tokens:
    print(token)