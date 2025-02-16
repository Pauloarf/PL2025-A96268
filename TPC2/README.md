# Manifesto TPC2

## 📌 Informação do TPC e do Aluno  

- **Título:** Análise de um dataset de obras musicais  
- **Data:** 2025/02/16  
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

Com a realização deste trabalho pretende-se criar um programa que trate e processe um conjunto de dados fornecido em um arquivo CSV. Os requisitos do programa são:  
1. **Proibição do uso do módulo CSV do Python**: O tratamento do CSV deve ser feito manualmente.  
2. **Processamento dos dados**: O programa deve ler e organizar o dataset para produzir três resultados principais:
    - Uma lista ordenada alfabeticamente dos compositores musicais presentes no dataset.
    - A distribuição do número de obras por período musical.
    - Um dicionário associando cada período a uma lista alfabética dos títulos das obras correspondentes.  

## 📂 **Resultados**  

Para processar o dataset das obras, utilizou-se **expressões regulares (regex)**, uma vez que o CSV original estava mal formatado e continha inconsistências, como quebras de linha dentro de campos e delimitadores irregulares.  

### **Processo de Extração e Limpeza dos Dados**  
1. **Uso de Regex**  
   - Foi criada uma expressão regular capaz de identificar os campos de cada linha do CSV, garantindo que os dados fossem extraídos corretamente, mesmo com formatações inconsistentes.  

2. **Normalização dos Nomes dos Compositores**  
   - Os nomes foram extraídos e organizados alfabeticamente.  
   - Foram removidos espaços em excesso e caracteres inconsistentes.  
   - Os nomes foram invertidos para o formato "Nome Sobrenome" e duplicações foram eliminadas para garantir uma lista única de compositores.  

3. **Distribuição das Obras por Período**  
   - Cada obra foi categorizada com base no seu período musical.  
   - O número total de obras por período foi contabilizado.  

4. **Listagem das Obras por Período**  
   - Para cada período musical, foi criada uma lista das obras correspondentes.  
   - Os títulos das obras foram ordenados alfabeticamente para melhor organização.  


## 📎 **Anexos**  

### **Saída do Programa**

```txt
CSV file generated successfully!

Lista ordenada dos compositores:
Antonio Caldara
Barbara Strozzi
Carlos Seixas
Claude Balbastre
Claudio Monteverdi
Duarte Lôbo
Filpe Da Madre De Deus
Francesco Cavalli
Francesco Durante
Franz Benda
(... lista continua ...)

Distribuição das obras por período:
Barroco: 26
Clássico: 15
Medieval: 45
Renascimento: 40
Romântico: 19
Contemporâneo: 6

Obras por período:
Barroco:
  - Ab Irato
  - Die Ideale, S.106
  - Fantasy No. 2
  - Hungarian Rhapsody No. 16
  - Hungarian Rhapsody No. 5
  - Impromptu Op.51
  - In the Steppes of Central Asia
  - Mazurkas, Op. 30
  - Nocturne in C minor
  - Paganini Variations, Book I
  - Polonaises Op.71
  - Preludes Op. 11
  - The Rondo
  - Transcendental Études
  - Études Op.10

Clássico:
  - Bamboula, Op. 2
  - Capriccio Italien
  - Czech Suite
  - Hungarian Rhapsody No. 14
  - Impromptu, Op. 29
  - Serenade for Strings
  - Serenata Notturna
  - Stabat Mater
  - Suite for Orchestra in B minor
  - Zärtliche Liebe

(... lista continua para outros períodos ...)


