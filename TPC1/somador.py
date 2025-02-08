import math

text1 = '''
LoReM 123 ipsum dOlOr sit amet, ONward adipiscing elit. Nullam 456 vehicula ofFice ligula sed ultricies. Integer 789 
maximus oNline turpis, nec fringilla 321 arcu. Praesent ofFbeat feugiat orci a 654 auctor malesuada. Nam oNset viverra,
erat et fermentum 987 cursus, metus ofFence felis = tincidunt odio, nec 432 sagittis est eros oNtology nec turpis. 
Aliquam 876 erat volutpat. Nulla oNboard accumsan, justo in ofFload congue sodales, = libero oNsite urna molestie justo, 
sed 111 vulputate odio ofFline magna eget nisl.
'''

text2 = '''
Vestibulum suscipit OFF justo sit amet 543 fringilla. Donec interdum ONboard lectus ut 876 cursus. Sed a nisi ONline sapien.
Duis 432 feugiat magna OFFroad ut eros 210 condimentum. Nulla ONward eget tortor 678 et justo cursus tincidunt. Suspendisse
ut 901 lacus OFFice id elit 345 bibendum volutpat. Integer ONfire vitae quam OFFbeat eget felis tristique 765 suscipit non
eu elit. = Fusce OFFset lacinia nunc ONair nec justo fermentum 987 scelerisque. Ut 654 dictum, odio id 321 ullamcorper, 
risus ONpoint eros iaculis erat, OFFbeat in facilisis nulla 789 justo non ligula. Nam 147 tincidunt lacus ONcall sapien non,
963 tempus risus OFFline vehicula.
'''

text3 = '''
Phasellus dictum 951 odio ONgoing et lacus facilisis, eget 753 blandit nisi OFFice laoreet. Duis tristique ONward sapien nec
852 ullamcorper scelerisque. Nam 741 bibendum elit OFFbeat ac tortor condimentum 963 luctus. Nulla facilisi. Donec 147 vel
diam ONfire a lorem gravida tincidunt. Integer dictum 258 justo ONpoint eros 789 dapibus, et 456 rhoncus elit OFFset dapibus.
= Cras sagittis 654 sem ONboard in nunc volutpat 741 hendrerit. Suspendisse 852 tincidunt erat OFFline odio fermentum, at 147 aliquet
justo 258 posuere. = Morbi ONair viverra nisl 321 et dui venenatis, in 753 scelerisque magna OFFtime tristique. Aenean facilisis 
lorem ONcall id elit posuere molestie. Vestibulum = posuere nisi OFFload sed lectus venenatis.
'''

# Função que soma todos os números de um texto

# Começamos por definir o compurtamento a ON
# Começamos a percorrer o texto, caracter a caracter
# Se o caracter for um dígito vamos acumulando o valor até encontrar um caracter que não seja um dígito
# Quando encontramos um caracter que não é um dígito, vamos somar o valor acumulado até ao momento
# Se os carateres seguintes forem 'off' desligar o comportamento
# Se os carateres seguintes forem 'on' ligar o comportamento
# No caso de existir um sinal de igual, imprimir o valor acumulado até ao momento
def somador(text):
    is_active = True
    total_sum = 0
    number = ''
    is_number = False
    for i, c in enumerate(text):
        if is_active:
            if c.isdigit():
                number += c
                is_number = True
            if not c.isdigit() and is_number:
                total_sum += int(number)
                number = ''
                is_number = False
            if i+2 < len(text) and c.lower() == 'o' and text[i+1].lower() == 'f' and text[i+2].lower() == 'f':
                is_active = False
        else:
            if c.lower() == 'o' and i+1 < len(text) and text[i+1].lower() == 'n':
                is_active = True
        if c == '=':
            print(f'Valor acumulado: {total_sum}')

    print(f'Valor acumulado final: {total_sum}')


# Testar a função
print(f'Resultado do texto 1:\n')
somador(text1)
print('---------------------------------')
print(f'Resultado do texto 2:\n')
somador(text2)
print('---------------------------------')
print(f'Resultado do texto 3:\n')
somador(text2)
