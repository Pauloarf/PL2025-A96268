# Manifesto TPC2

## 📌 Informação do TPC e do Aluno  

- **Título:** Analisador Léxico
- **Data:** 2025/03/04
- **Autor:**  
    <table>
    <tr>
        <td><img src="../Images/Profile.jpg" width="100"></td>
        <td>
        <strong>Nome:</strong> Paulo Alexandre Rodrigues Ferreira<br>
        <strong>Número:</strong> A96268
        </td>
    </tr>
    </table>

**Resumo:** 

Com a realização deste trabalho pretende-se construir um analisador léxico para uma linguagem de query com a qual se podem escrever frases do género:

```sparql
# DBPedia: obras de Chuck Berry  
select ?nome ?desc where {  
  ?s a dbo:MusicalArtists.  
  ?s foaf:name "Chuck Berry"@en .  
  ?w dbo:artist ?s.  
  ?w foaf:name ?nome.  
  ?w dbo:abstract ?desc  
} LIMIT 1000
```
Aqui está o conteúdo formatado em Markdown (`.md`). Para evitar quebra de mensagens, o código foi encapsulado com ` (crases simples) quando necessário.

---

## 📂 Resultados

O primeiro passo de desenvolvimento foi compreender o formato da linguagem a ser analisada. Isso é essencial para identificar os elementos (tokens) que compõem a linguagem e definir como devem ser tratados.

Após analisar o excerto fornecido e realizar pesquisas adicionais, concluiu-se que a linguagem de query em questão é semelhante (ou idêntica) ao SPARQL. Com base nisso, os principais elementos (tokens) a serem reconhecidos foram identificados como sendo:

- **Palavras-Chave**: `SELECT`, `WHERE`, `LIMIT`.
- **Variáveis**: `?nome`, `?desc`, `?s`, `?w`.
- **Strings**: `"Chuck Berry"@en`.
- **Identificadores (URIs)**: `dbo:MusicalArtists`, `foaf:name`, `dbo:artist`, `dbo:abstract`.
- **Símbolos Especiais**: `{`, `}`, `.`, `a`.

O segundo passo consistiu em definir expressões regulares para reconhecer cada tipo de token. Após testes e validações utilizando ferramentas como o [regex101](https://regex101.com/), foram definidas as seguintes expressões:

```python
tokens = [
    {"id": "SELECT", "expreg": r"SELECT"},  # Palavra-chave SELECT
    {"id": "WHERE", "expreg": r"WHERE"},    # Palavra-chave WHERE
    {"id": "LIMIT", "expreg": r"LIMIT"},    # Palavra-chave LIMIT
    {"id": "VARIABLE", "expreg": r"\?\w+"}, # Variáveis (começam com ?)
    {"id": "STRING", "expreg": r'"[^"]+"@\w+'}, # Strings com idioma (ex: "Chuck Berry"@en)
    {"id": "URI", "expreg": r"\w+:\w+"},    # URIs (ex: dbo:MusicalArtists)
    {"id": "DOT", "expreg": r"\."},         # Símbolo .
    {"id": "LBRACE", "expreg": r"\{"},      # Símbolo {
    {"id": "RBRACE", "expreg": r"\}"},      # Símbolo }
    {"id": "A", "expreg": r"a"},            # Palavra-chave 'a'
    {"id": "SKIP", "expreg": r"\s+"},       # Espaços em branco (ignorar)
    {"id": "COMMENT", "expreg": r"#[^\n]*"}, # Comentários (ignorar)
]
```

- Cada token possui um identificador `id` e uma expressão regular `expreg` que define como ele é reconhecido.

De seguida passou-se para o passo 3, onde o lexer foi construído utilizando as expressões regulares definidas. Ele é responsável por percorrer o texto de entrada, reconhecer os tokens e retornar uma lista de tuplos contendo as informações de cada token.

O ultimo passou necessário era testar o lexer, para isto foi utilizado o excerto fornecido.
A saída do lexer será uma lista de tuplos no formato `(tipo_do_token, valor, linha, (início, fim))`.

```
('SELECT', 'SELECT', 2, (1, 7))
('VARIABLE', '?nome', 2, (8, 13))
('VARIABLE', '?desc', 2, (14, 19))
('WHERE', 'WHERE', 2, (20, 25))
('LBRACE', '{', 2, (26, 27))
...
('LIMIT', 'LIMIT', 8, (182, 187))
```

Após analisar o output, podemos concluir que o lexer aparenta ter sido implementado com sucesso, sendo capaz de reconhecer os tokens da linguagem.