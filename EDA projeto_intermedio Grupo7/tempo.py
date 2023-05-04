from t1_alterado import ListaDL
from t1_alterado import ListaDLC

from tabulate import tabulate
from matplotlib import pyplot as plt


# este ficheiro testa o tempo que demoram os métodos abaixo a realizar as operações com diferentes
# números de elementos na sua composição. Quanto mais nós,
# mais tempo vai ser dispendido para realizar as operações

# Merge Sort

def merge_sort():
    plt.close()
    lst = ListaDL()
    lsta = ListaDLC()
    n_elementos = list(range(1, 500, 10))

    # listas para guardar os valores para desenhar o gráfico (duplamente ligada)
    # uso de matplotlib
    listaxdl = []
    listaydl = []
    for i in n_elementos:
        listaxdl.append(i)
        listaydl.append(lst.performance_merge_sort(i))  # chama o método performance_merge_sort(tamanho)
    plt.plot(listaxdl, listaydl, "-g", label='Lista duplamente ligada')  # legenda e cor da linha
    plt.legend(loc="upper left")  # localização da legenda
    plt.title('Merge sort')  # título do gráfico
    plt.show()  # para mostrar o gráfico

    # tabela com os valores do tempo duplamente ligada
    # uso de tabulate
    table1 = [['Lista DL', '10 elementos', '100 elementos', '500 elementos'],
              ['Merge sort', lst.performance_merge_sort(10),
               lst.performance_merge_sort(100), lst.performance_merge_sort(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_merge_sort(tamanho)
    print(tabulate(table1))  # mostrar a tabela

    # listas para guardar os valores para desenhar o gráfico (duplamente ligada circular)
    # uso do matplotlib
    listaxdlc = []
    listaydlc = []
    for i in n_elementos:
        listaxdlc.append(i)
        listaydlc.append(lst.performance_merge_sort(i))  # chama o método performance_merge_sort(tamanho)
    plt.plot(listaxdlc, listaydlc, "-b", label='Lista duplamente ligada circular')  # legenda e cor da linha
    plt.legend(loc="upper left")  # localização da legenda
    plt.title('Merge sort')  # título do gráfico
    plt.xlabel('Nº elementos da lista')  # legenda eixo x
    plt.ylabel('Tempo de execução')  # legenda eixo y
    plt.show()  # mostrar o gráfico

    # tabela com os valores do tempo - duplamente ligada circular
    # uso do tabulate
    table2 = [['Lista DLC', '10 elementos', '100 elementos', '500 elementos'],
              ['Merge sort', lsta.performance_merge_sort(10),
               lsta.performance_merge_sort(100), lsta.performance_merge_sort(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_merge_sort(tamanho)
    print(tabulate(table2))  # mostrar a tabela


# Bubble Sort


def bubble_sort():
    plt.close()
    lst = ListaDL()
    lsta = ListaDLC()
    n_elementos = list(range(1, 500, 10))

    # listas para guardar os valores para desenhar o gráfico (duplamente ligada)
    # uso de matplotlib
    listaxdl = []
    listaydl = []
    for i in n_elementos:
        listaxdl.append(i)
        listaydl.append(lst.performance_bubble_sort(i))  # chama o método performance_bubble_sort(tamanho)
    plt.plot(listaxdl, listaydl, "-g", label='Lista duplamente ligada')  # legenda e cor da linha
    plt.legend(loc="upper left")  # localização da legenda
    plt.title('Bubble sort')  # título do gráfico
    plt.show()  # mostrar gráfico

    # construção tabela duplamente ligada bubble sort
    # uso de tabulate
    table1 = [['Lista DL', '10 elementos', '100 elementos', '500 elementos'],
              ['Bubble sort', lst.performance_bubble_sort(10),
               lst.performance_bubble_sort(100), lst.performance_bubble_sort(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_bubble_sort(tamanho)
    print(tabulate(table1))  # mostrar tabela

    # listas para guardar os valores para desenhar o gráfico (duplamente ligada circular)
    # uso de matplotlib
    listaxdlc = []
    listaydlc = []
    for i in n_elementos:
        listaxdlc.append(i)
        listaydlc.append(lst.performance_bubble_sort(i))  # chama o método performance_bubble_sort(tamanho)
    plt.plot(listaxdlc, listaydlc, "-b", label='Lista duplamente ligada circular')  # legenda e cor da linha
    plt.legend(loc="upper left")  # localização da legenda
    plt.title('Bubble sort')  # título do gráfico
    plt.xlabel('Nº elementos da lista')  # legenda eixo x
    plt.ylabel('Tempo de execução')  # legenda eixo y
    plt.show()  # mostrar o gráfico

    # construção tabela duplamente ligada circular bubble sort
    # uso do tabulate
    table2 = [['Lista DLC', '10 elementos', '100 elementos', '500 elementos'],
              ['Bubble sort', lsta.performance_bubble_sort(10),
               lsta.performance_bubble_sort(100), lsta.performance_bubble_sort(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_bubble_sort(tamanho)
    print(tabulate(table2))  # mostar tabela


# Pesquisa Linear e Pesquisa Binária


def searchers():
    plt.close()
    lst = ListaDL()
    lsta = ListaDLC()
    n_elementos = list(range(1, 500, 10))

    # listas para guardar os valores para desenhar o gráfico - pesquisa binária duplamente ligada circular
    # uso de matplotlib
    listaxdlcbinary = []
    listaydlcbinary = []
    for i in n_elementos:
        listaxdlcbinary.append(i)
        listaydlcbinary.append(lsta.performance_binary_search(i))  # chama o método performance_binary_search(tamanho)
    plt.plot(listaxdlcbinary, listaydlcbinary, "-r", label='Binary search DLC')  # legenda e cor linha
    plt.legend(loc="upper left")  # localização da legenda

    # listas para guardar os valores para desenhar o gráfico - pesquisa binária duplamente ligada
    # uso de matplotlib

    listaxdlbinary = []
    listaydlbinary = []
    for i in n_elementos:
        listaxdlbinary.append(i)
        listaydlbinary.append(lst.performance_binary_search(i))  # chama o método performance_binary_search(tamanho)
    plt.plot(listaxdlbinary, listaydlbinary, "-b", label='Binary search DL')  # legenda e cor linha
    plt.legend(loc="upper left")  # localização da legenda

    # listas para guardar os valores para desenhar o gráfico - pesquisa linear duplamente ligada
    # uso de matplotlib

    listaxdlclinear = []
    listaydlclinear = []
    for i in n_elementos:
        listaxdlclinear.append(i)
        listaydlclinear.append(lsta.performance_linear_search(i))  # chama o método performance_linear_search(tamanho)
    plt.plot(listaxdlclinear, listaydlclinear, "-y", label='Linear search DLC')  # legenda e cor linha
    plt.legend(loc="upper left")  # localização da legenda

    # listas para guardar os valores para desenhar o gráfico - pesquisa linear duplamente ligada
    # uso de matplotlib

    listaxdllinear = []
    listaydllinear = []
    for i in n_elementos:
        listaxdllinear.append(i)
        listaydllinear.append(lst.performance_linear_search(i))  # chama o método performance_linear_search(tamanho)
    plt.plot(listaxdllinear, listaydllinear, "-g", label='Linear search DL ')  # legenda e cor linha
    plt.legend(loc="upper left")  # localização da legenda

    # tabelas

    # tabela binary search duplamente ligada circular
    # uso do tabulate
    table1 = [['Lista DLC', '10 elementos', '100 elementos', '500 elementos'],
              ['Binary search', lsta.performance_binary_search(10),
               lsta.performance_binary_search(100), lsta.performance_binary_search(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_binary_search(tamanho)
    print(tabulate(table1))

    # tabela binary search duplamente ligada
    # uso do tabulate
    table2 = [['Lista DL', '10 elementos', '100 elementos', '500 elementos'],
              ['Binary search', lst.performance_binary_search(10),
               lst.performance_binary_search(100), lst.performance_binary_search(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_binary_search(tamanho)
    print(tabulate(table2))

    # tabela linear search duplamente ligada circular
    # uso do tabulate
    table3 = [['Lista DLC', '10 elementos', '100 elementos', '500 elementos'],
              ['Linear search', lsta.performance_linear_search(10),
               lsta.performance_linear_search(100), lsta.performance_linear_search(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_binary_search(tamanho)
    print(tabulate(table3))

    # tabela linear search duplamente ligada
    # uso do tabulate
    table4 = [['Lista DL', '10 elementos', '100 elementos', '500 elementos'],
              ['Linear search', lst.performance_linear_search(10),
               lst.performance_linear_search(100), lst.performance_linear_search(500)]]
    # teste de tempo com 10, 100 e 500 elementos
    # chama o método performance_linear_search(tamanho)
    print(tabulate(table4))

    # instruções do gráfico
    plt.xlabel('Nºelementos da lista')  # legenda eixo x
    plt.ylabel('Tempo de execução')  # legenda eixo y
    plt.title('Searchers da DL e DLC')  # título gráfico
    plt.show()  # mostrar gráfico
