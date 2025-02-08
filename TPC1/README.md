# Manifesto TPC1

## 📌 Informação do TPC e do Aluno  

- **Título:** Somador on/off: Criar o Programa em Python 
- **Data:** 2025/02/08  
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
\
**Resumo:**
\
Com a realização deste trabalho pretende-se criar um programa que some todas as sequências de dígitos que se encontrem num texto. Os requisitos do programa são: 
1. Sempre que encontrar a string "Off", com qualquer combinação de maiúsculas e minúsculas, o comportamento (Somador) é desligado;
2. Sempre que encontrar a string "On", com qualquer combinação de maiúsculas e minúsculas, o comportamento (Somador) é novamente ligado;
3. Sempre que encontrar o caráter "=", o resultado da soma é colocado na saída.
4. O programa deve ignorar números negativos, considerando no caso de "-123" unicamente o número "123".

- (Opcional) No final do texto o programa pode ou não imprimir o resultado obtido.

## 📂 Resultados  

Para a realização de testes foram utilizados 3 textos, cada um com 100, 150 e 200 palavras. Os textos utilizados para estes testes estão disponiveis na secção [Anexos](#-anexos).

Os resultados obtidos foram os seguintes:

> **Resultado do texto 1:**
> 
> Valor acumulado: 1887  
> Valor acumulado: 2763  
> Valor acumulado final: 2874  
> 
> **Resultado do texto 2:**
> 
> Valor acumulado: 2887  
> Valor acumulado final: 5959  
> 
> **Resultado do texto 3:**
> 
> Valor acumulado: 5910  
> Valor acumulado: 7503  
> Valor acumulado: 8577  
> Valor acumulado final: 8577  


## 📎 Anexos

**Texto1:**  
```plaintext
LoReM 123 ipsum dOlOr sit amet, ONward adipiscing elit. Nullam 456 vehicula ofFice ligula sed ultricies. Integer 789 maximus oNline turpis, nec fringilla 321 arcu. Praesent ofFbeat feugiat orci a 654 auctor malesuada. Nam oNset viverra, erat et fermentum 987 cursus, metus ofFence felis = tincidunt odio, nec 432 sagittis est eros oNtology nec turpis. Aliquam 876 erat volutpat. Nulla oNboard accumsan, justo in ofFload congue sodales, = libero oNsite urna molestie justo, sed 111 vulputate odio ofFline magna eget nisl.
```

**Texto2:**  
```plaintext
Vestibulum suscipit OFF justo sit amet 543 fringilla. Donec interdum ONboard lectus ut 876 cursus. Sed a nisi ONline sapien. Duis 432 feugiat magna OFFroad ut eros 210 condimentum. Nulla ONward eget tortor 678 et justo cursus tincidunt. Suspendisse ut 901 lacus OFFice id elit 345 bibendum volutpat. Integer ONfire vitae quam OFFbeat eget felis tristique 765 suscipit non eu elit. = Fusce OFFset lacinia nunc ONair nec justo fermentum 987 scelerisque. Ut 654 dictum, odio id 321 ullamcorper, risus ONpoint eros iaculis erat, OFFbeat in facilisis nulla 789 justo non ligula. Nam 147 tincidunt lacus ONcall sapien non, 963 tempus risus OFFline vehicula.
```

**Texto3:**  
```plaintext
Phasellus dictum 951 odio ONgoing et lacus facilisis, eget 753 blandit nisi OFFice laoreet. Duis tristique ONward sapien nec 852 ullamcorper scelerisque. Nam 741 bibendum elit OFFbeat ac tortor condimentum 963 luctus. Nulla facilisi. Donec 147 vel diam ONfire a lorem gravida tincidunt. Integer dictum 258 justo ONpoint eros 789 dapibus, et 456 rhoncus elit OFFset dapibus. = Cras sagittis 654 sem ONboard in nunc volutpat 741 hendrerit. Suspendisse 852 tincidunt erat OFFline odio fermentum, at 147 aliquet justo 258 posuere. = Morbi ONair viverra nisl 321 et dui venenatis, in 753 scelerisque magna OFFtime tristique. Aenean facilisis lorem ONcall id elit posuere molestie. Vestibulum = posuere nisi OFFload sed lectus venenatis.
```