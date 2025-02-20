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

1. **Leitura e Correção do CSV**
   - Manipulação manual de caracteres para lidar com:
     - Campos entre aspas com quebras de linha
     - Delimitadores ';' dentro de campos citados
     - Aspas duplas como caracteres de escape
   - Função `parseFile()` realiza pré-processamento crítico

2. **Normalização de Compositores**
   - Extração de nomes do campo 4 do CSV
   - Formatação para "Nome Sobrenome"
   - Remoção de duplicatas com `set()`

3. **Organização por Período Musical**
   - Contagem de obras por período (campo 3)
   - Agrupamento de títulos (campo 0) em dicionários
   - Ordenação alfabética automática

4. **Notas**
- Manipulação direta de caracteres para parsing CSV
- Uso de flags (`escape` e `textCapture`) para controle de contexto
- Estruturas de dados otimizadas:
  - `set()` para compositores únicos
  - Dicionários para agrupamento por período
- Ordenação nativa com `sorted()` e `list.sort()`


## 📎 **Anexos**  

### **Saída do Programa**

```txt
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
Gaspar Fernandes
Gaspar Sanz
George Frideric Handel
Giacomo Carissimi
Giovanni Battista Bononcini
Giovanni Battista Martini
Giovanni Battista Pergolesi
Giovanni Battista Sammartini
Giuseppe Sammartini
Guillaume-Gabriel Nivers
Heinrich Ignaz Franz Biber
Jacopo Peri
(--- ... ---)

Distribuição das obras por período:
periodo: 1
Barroco: 26
Clássico: 15
Medieval: 48
Renascimento: 41
Século XX: 18
Romântico: 19
Contemporâneo: 7

Obras por período:
periodo:
  - nome
Barroco:
  - Ab Irato
  - Die Ideale, S.106
  - Fantasy No. 2
  - Hungarian Rhapsody No. 16
  - Hungarian Rhapsody No. 5
  - Hungarian Rhapsody No. 8
  (--- ... ---)

Clássico:
  - Bamboula, Op. 2
  - Capriccio Italien
  - Czech Suite
  - French Overture
  - Hungarian Rhapsody No. 14
  (--- ... ---)

Medieval:
  - Adagio in B minor
  - Ballade No.1
  - Ballades, Op. 10
  - Barcarole Op. 60
  - Coriolan Overture
  - Dixit Dominus
  - Eroica Variations
  - Fantasia and Fugue, BWV 542, G minor
  (--- ... ---)

Renascimento:
  - Bagatelles, Opus 119
  - Bagatelles, Opus 33
  - Cantatas, BWV 141-150
  - Carnival Overture
  - Estampes
  (--- ... ---)

Século XX:
  - Berceuse
  - Eleven Chorale Preludes, Op. 122
  - Fürchte dich nicht
  - Hungarian Rhapsody No. 17
  (--- ... ---)

Romântico:
  - Book II
  - Fantasy No. 4
  - Feu d'artifice
  - Feuilles d'Album
  - Grande Tarantelle
  - Jeux d'enfants
  - Lobet den Herrn, alle Heiden
  (--- ... ---)

Contemporâneo:
  - Impromptu, Op. 36
  - Les cinq doigts
  - Polonaises, Op.40
  - Preludes Opus 51
  - Rhapsodies, Op. 79
  - Sonnerie de Ste-Geneviève du Mont-de-Paris
  - Études Op. 25

```