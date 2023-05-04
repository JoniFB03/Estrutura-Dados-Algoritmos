from Fila import *
from Cliente import *
from Texto import *

# import dos restantes ficheiros relativos ao projeto e utilização do objeto Fila
f=Fila()

# menu para "printar" as operações de forma a que o utilizador escolha a opção
def menu():
    # sempre que chamada a função *menu()* com o print das opções (abaixo), será dado print na tela a instrução:
    for j in '\n\033[91mAbrindo menu...\033[0m':
        print(j,end='')
        time.sleep(0.05)
    print('\n\033[92mMenu aberto com sucesso!\033[0m')
    # print das opções válidas
    print('\n\033[1m[0]-\033[4mFecha o menu\033[0m \n[1]-Adicionar cliente \n[2]-Atender próximo cliente da fila '
          '\n[3]-Ver próximo cliente\n[4]-Abandonar lugar na fila \n[5]-Fechar a fila '
          '\n[6]-Verificar se a fila está vazia \n[7]-Número de pessoas na fila '
          '\n[8]-\033[4mVisualizar fila e secções\033[0m \n[9]-Exportar clientes \n[10]-Importar clientes')

######################## experimentar o código com o *run*########################################
if __name__=="__main__":
    texto_inicial()
    menu()
    escolha=input('Seleciona a opção que deseja realizar:')
##################################################################################################

# atribuição de variáveis global para se poder utilizar em várias instâncias no ficheiro de código
global prioridade, numero, seccao

# ciclo para definir as ações da função *menu()* quando esta for chamada. Se a escolha for 0 o programa termina.
while escolha != "0":
    if escolha == "1":
        # pedido de input para o nome completo
        nome = str(input('\nDigite o seu nome completo:'))

        # pedido de input do tipo *int* para  receber nº identificação com condição de 7 ou 8 números, sem números
        # repetidos na fila
        while True:
            # exceção para no caso de o valor recebido pelo input não for do tipo *int*, o programa não dar erro e
            # lançar uma exceção para este caso
            try:
                numero = int(input('\nDigite o seu número de ID civil .(Lembre-se que o número de ID civil deve ter 7 '
                                   'ou 8 números não iniciados em 0, apenas!) :'))
                # condição dada neste intervalo assumida desta forma, pois (Os números mais antigos têm apenas 7 números
                #  por isso foi levado em conta tanto os 7 ou 8 dígitos. E o número nunca pode começar com 0.)
                if 999999 < numero < 100000000 and not f.numero_repetido(numero):
                    break # para encerrar o ciclo while True:
                elif f.numero_repetido(numero):
                    print('\033[91mO número colocado já está associado a um cliente da fila.\033[0m')
            except ValueError:
                continue  # para continuar no loop while True:

        # pedido de input para digitação da secção, só em maiúsculas, como pedido
        print('\n\033[93m[RC]-Criação / Renovação do cartão de cidadão \n[RP]-Criação / Renovação do passaporte'
              '\n[QC]-Questões judiciais\033[0m')
        print('Escolha a opção que quer realizar, só em maiúsculas.\n Exemplo: escrever -RC- apenas\n')
        # ciclo para criar uma exceção e só aceitar os valores dados no *print* acima
        while True:
            try:
                seccao = input('Escolha a opção:')
                if seccao == "RC" or seccao == 'RP' or seccao == 'QC':
                    break # para encerrar o ciclo while True:
                else:
                    print('Selecione uma das expressões possíveis! Ex: -RC-')
            except:
                continue # para continuar no loop while True:

        # pedido de input do tipo *int* para o cliente referir se tem prioridade ou não
        print('É um cliente prioritário?\nSelecione apenas a opção que lhe satisfazer')
        print('\033[93m[1]-Sim \n[2]-Não\033[0m')
        while True:
            # tal como no pedido do número de ID civil, lança uma exceção para valores que não são do tipo *int*, de
            # forma a o programa não encerrar
            try:
                prioridade = int(input('Escolha a opção face à sua prioridade:'))
                # Se o cliente preencher com 1 que corresponde a SIM, irá ser inserido como cliente prioritário
                if prioridade == 1:
                    prioridade = True
                    pri = Cliente(nome, numero, seccao, prioridade)
                    f.insert_p_client(pri)
                    print \
                        (f'\033[92mCliente\033[0m {nome} \033[92madicionado à fila, como prioritário.\033[0m\n')
                    break # para encerrar o ciclo while True:
                # Se o cliente preencher com 2 que corresponde a NÃO, irá ser inserido como cliente não prioritário
                elif prioridade == 2:
                    prioridade = False
                    npri = Cliente(nome, numero, seccao, prioridade)
                    f.insert_client(npri)
                    print((f'\033[92mCliente\033[0m {nome} \033[92madicionado à fila, '
                           f'como não prioritário.\033[0m\n'))
                    break # para encerrar o ciclo while True:
                else:
                    print('Opção inválida. Escolha uma das opções possíveis!')
            except ValueError:
                print('Deve ser escrito em formato de número.')
                continue # para continuar no loop while True:

    # funções chamadas do ficheiro _*Fila.py*_

    # atender o próximo cliente da fila global
    elif escolha == "2":
        f.serve_client()

    # ver o próximo cliente da fila global
    elif escolha == "3":
        (f.view_next_client())

    # abandonar a fila, dada a posição
    elif escolha == "4":
        print(f)
        index = int(input('Introduza a posição da fila que deseja retirar. '
                          'Selecione a posição face ao número da lista acima. Ex: 1|Nome- [ ] --> selecionar nº *1* :'))
        f.abandon_queue(index)

    # fechar a fila global, sem exportação de ficheiros
    elif escolha == "5":
        f.close()
        print('\033[92mFila foi limpa com sucesso!\033[0m\n')

    # verificar se a fila está vazia
    elif escolha == "6":
        vazio = (f.is_empty())
        if vazio:
            print('\033[91mA fila está vazia.\033[0m\n')
        else:
            print('\033[92mHá clientes na fila.\033[0m\n')

    # ver números de clientes na fila de espera (global)
    elif escolha == "7":
        print(f'\nA fila tem {len(f)} clientes.\n')

    # ver a string da fila de espera e ver os clientes por secção
    elif escolha == "8":
        print(f)
        f.seccoes()

    # exportar clientes
    elif escolha == "9":
        f.exportar_ficheiros()
        print('\033[92mTodos os clientes foram exportados para o ficheiro.\n\033[0m')

    # importar clientes
    elif escolha == "10":
        f.importar_ficheiros()
        print('\033[92mTodos os clientes foram importados para a fila de espera.\n\033[0m')

    # caso não seja chamada uma opção válida, o programa dirá que não é uma opção válida e voltará a reiniciar o menu
    else:
        print('Opção inválida!\n')
    menu()
    escolha = input('Seleciona a opção que deseja realizar:')

# quando selecionado o 0, irá dar print na tela a seguinte instrução:
for k in ('\033[91mFinalizando...'):
    print(k, end='')
    time.sleep(0.07)
print('\n\033[92mMenu finalizado com sucesso\033[0m')
