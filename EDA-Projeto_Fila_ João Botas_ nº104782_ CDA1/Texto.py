import time # utilização da biblioteca time para a função *sleep()* que permite criar intervalos entre ações

# texto a introduzir quando o ficheiro _*Menu.py*_ for corrido

string='\nOlá eu sou o João Botas, nº104782 de CDA1 e esta é uma implementação de uma fila à loja do cidadão.' \
       ' Espero que gostem! :)'

def texto_inicial():
    for i in string:
        print(i,end='')
        time.sleep(0.03)
    time.sleep(1)
    print('\n')

## Informação:
# Foram utilizados códigos de cores para strings ao longo do trabalho. Estes códigos foram retirados da tabela de cores
# ANSI (python) e são puramente estéticos, de forma a deixar o menu com a fonte mais realçado entre uma ação aceita e
# uma ação não aceita e no menu de opções






















