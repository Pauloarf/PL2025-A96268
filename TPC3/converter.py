import re

# No bold apanhamos tudo o que estiver entre quatro asteriscos de forma lazy
# Este exemplo teve interferencia de IA, havia um caso que nao dava mas o lookahead resolveu
bold = r'\*\*(.*?)\*\*(?!\*)'
# No itálico apanhamos tudo o que estiver entre dois asteriscos de forma lazy
italic = r'\*(.*?)\*'
# No header apanhamos entre 1 a 6 #. Um ou mais espaços uma qualquer quantidade de carateres
header = r'^(#{1,6})\s+(.*)'
# Na numlist vamos apanhar um elemento de cada vez... Desde que seja ^(numero)(ponto)(whitespace)(caraters) entao funciona
numList = r'^\d+\.\s+(.*)'
# links e imagens sao similares, so acrescentamos um ! as imagens
# Aqui é qualquer quantidade de coisas dentro de [] seguidas sem espaço de ()
link = r'\[(.*?)\]\((.*?)\)'
image = r'!\[(.*?)\]\((.*?)\)'

def markdown_to_html(markdown_text):
    # Começamos por separar linhas
    lines = markdown_text.split('\n')
    html_lines = []
    in_list = False

    for line in lines:
        line = re.sub(bold, r'<b>\1</b>', line)
        line = re.sub(italic, r'<i>\1</i>', line)
        line = re.sub(link, r'<a href="\2">\1</a>', line)
        line = re.sub(image, r'<img src="\2" alt="\1">', line)

        # Header Verification
        header_match = re.search(header, line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            html_lines.append(f"<h{level}>{text}</h{level}>")
            continue

        # NumbList Verification
        numlist_match = re.search(numList, line)
        if numlist_match:
            if not in_list:
                html_lines.append("<ol>")
                in_list = True
            text = numlist_match.group(1)
            html_lines.append(f"<li>{text}</li>")
            continue
        elif in_list:
            html_lines.append("</ol>")
            in_list = False

        html_lines.append(line)

    if in_list:
        html_lines.append("</ol>")

    return '\n'.join(html_lines)

# Example Usage
markdown_text = """
# Header 1
## Header 2
This is **bold** and *italic*.
1. First item
2. Second item
[Google](https://www.google.com)
![Markdown Logo](https://markdown-here.com/img/icon256.png)
"""

html_output = markdown_to_html(markdown_text)
print(html_output)

with open("TPC3/test.md") as file:
    text = file.read()
    html_output = markdown_to_html(text)
    print(html_output)