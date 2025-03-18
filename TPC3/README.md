# Manifesto TPC3

## 📌 Informação do TPC e do Aluno  

- **Título:** Conversor de MarkDown para HTML 
- **Data:** 2025/02/24
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

Com a realização deste trabalho pretende-se criar um programa que converta textos `markdown` para textos `html`. Este programa tem de converter os elementos descritos na "Basic Syntax" da seguinte *cheat sheet*:

> - Cabeçalhos (linhas iniciadas com #):
>   - `# Exemplo` <=> `<h1>Exemplo</h1>`
> - Bold (pedaços de texto entre **):
>   - `**Exemplo**` <=> `<b>Exemplo</b>`
> - Itálico (pedaços de texto entre *):
>   - `*Exemplo*` <=> `<i>Exemplo</i>`
> - Link:
>   - `[Exemplo](www.exemplo.com)` <=> `<a href="www.exemplo.com">exemplo</a>`
> - Iamgem:
>   - `[imagem](www.exemplo.com)` <=> `<img src="www.exemplo.com" alt="imagem"/>`
> - Lista Numerada:  
>   `1. Primeiro Ponto`  
>   `2.  Segundo Ponto`   
>   `3. Terceiro Ponto`  
>   \<==>   
>   `<ol>`  
>   `<li>Primeiro Ponto</li>`  
>   `<li>Segundo Ponto</li>`  
>   `<li>Terceiro Ponto</li>`  
>   `<ol>`  

## 📂 **Resultados**  

Para resolver este trabalho da melhor maneira possível e de forma a corresponder aos requisitos propostos, o problema foi dividido em três partes principais:  
1. **Identificar as expressões regulares** capazes de reconhecer cada um dos elementos de Markdown.  
2. **Compreender a conversão** necessária, estabelecendo a relação entre cada elemento de Markdown e o seu correspondente em HTML.  
3. **Implementar um ciclo simples** que percorra o texto linha a linha, realizando as alterações necessárias.  

### 1. Identificação das Expressões Regulares  
A primeira etapa revelou-se uma das mais desafiadoras, uma vez que foi necessário validar uma variedade de cenários para garantir que as expressões regulares cobrissem todos os casos possíveis. Após várias tentativas e testes realizados no site [Regex101](https://regex101.com/), chegou-se a uma configuração que se mostrou satisfatória. Até à data de escrita deste relatório, não foram detetados problemas nos múltiplos testes realizados.  

Os padrões obtidos foram os seguintes:  

#### Padrões/Expressões Regulares  
- **Bold** => `\*\*(.*?)\*\*(?!\*)`  
- **Italic** => `(?<!\*)\*(.*?)\*(?!\*)`  
- **Headers** => `^(#{1,6})\s+(.*)`  
- **Numbered Lists** => `^\d+\.\s+(.*)`  
- **Links** => `\[(.*?)\]\((.*?)\)`  
- **Image** => `!\[(.*?)\]\((.*?)\)`  

### 2. Conversão de Markdown para HTML  
Após a definição dos padrões e a correspondência dos grupos capturados com a respetiva conversão para HTML (conforme apresentado no resumo deste relatório), procedeu-se à implementação do conversor em código.  

### 3. Implementação do Conversor  
Para iniciar a conversão, optou-se por iterar o texto, fornecido como parâmetro, linha a linha. Em cada linha, são realizados os *matches* dos vários padrões, começando pelos mais diretos, que não requerem lógica adicional, nomeadamente:  
- **Bold**  
- **Italic**  
- **Links**  
- **Imagens**  

Devido a uma incoerência no *matching* do itálico (que poderia capturar asteriscos vazios, por exemplo, `**`), decidiu-se processar primeiro o **bold**, seguindo-se os restantes elementos, de forma a evitar problemas no *parsing* dos dados.  

Após a substituição destes elementos, procedeu-se à conversão dos **headers** (cabeçalhos) e das **numbered lists** (listas numeradas). Nestes casos, foi necessário:  
- **Para os cabeçalhos**: Avaliar o número de `#` no início da linha, de modo a determinar o nível do cabeçalho (de `<h1>` a `<h6>`).  
- **Para as listas numeradas**: Avaliar o número da lista e garantir a introdução das tags `<ol>` no início e no fim da lista.  

### Conclusão  
Após testar o programa com diversos textos em Markdown, verificou-se que a conversão está correta e não apresenta erros quando interpretada por um *browser*. Assim, conclui-se que o TPC foi executado com sucesso, cumprindo todos os requisitos propostos.  