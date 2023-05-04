import csv
import matplotlib.pyplot as plt
from Tad_grafo import Graph, Edge
import networkx as nx
from networkx import louvain

# import random - para testes apenas

# começamos por abrir o conteúdo dos ficheiros excel para percebermos o que está no seu interior
lista_profile = []  # lista relativa ao ficheiro "Github1.csv"
lista_data = []  # lista relativa ao ficheiro "Data_Facebook.csv"
lista_circle = []  # lista relativa ao ficheiro "facebook_network.csv"

# ficheiro Excel Github1

profile = open("Github1.csv")  # abrir ficheiro
read_profile_excel = csv.reader(profile)  # ler ficheiro

for p in read_profile_excel:
    lista_profile.append(p)  # para acrescentar elemento p à lista_profile
lista_profile.pop(0)  # retirar a primeira linha do Excel com a denominação follower, followed, para só termos os
# conteúdos que realmente interessam

# print(lista_profile)

# ficheiro Excel Data_Facebook

data_excel = open("Data_Facebook.csv")  # abrir ficheiro
read_data_excel = csv.reader(data_excel)  # ler ficheiro

for i in read_data_excel:
    lista_data.append(i)  # acresenta todos os elementos à lista, incluindo os da primeira linha,
    # porque não há "títulos"
# print(lista_data)

# ficheiro Excel facebook_network

network_excel = open("facebook_network.csv")  # abrir ficheiro Excel
read_network_excel = csv.reader(network_excel)  # ler ficheiro Excel

for n in read_network_excel:
     lista_circle.append(n)  # acresenta todos os elementos à lista,
     # incluindo os da primeira linha, porque não há "títulos"


def grafo_csv(nome_f):
    grafo = Graph()  # obter a classe Grafo, já que está definido que o grafo é não direcionado
    data_excel = open(nome_f)  # abrir o ficheiro
    read_data_excel = csv.reader(data_excel)  # ler o ficheiro
    s = set()
    for item in read_data_excel:
        pessoa_1 = item[0]  # ponto de partida da aresta
        pessoa_2 = item[1]  # ponto de chegada da aresta
        if (pessoa_1, pessoa_2) not in s and (pessoa_2, pessoa_1) not in s:

            amizade = item[2]  # peso da aresta
            grafo.insert_edge(grafo.insert_vertex(pessoa_1), grafo.insert_vertex(pessoa_2), int(amizade))
            s.add((pessoa_1, pessoa_2))
    data_excel.close()
    return grafo  # devolve o grafo com a informação anterior


# desenhar o grafo com recurso ao networkx e mathplotlib.pyplot
def nx_teste(graf, show_plot=False):
    print('Número de arestas únicas:', desenhar.edge_count())  # fixo
    nx_g = nx.Graph()  # vai desenhar o grafo do Tad_grafo.py com o recurso ao networkx
    for i in graf.edges():  # se i está nas arestas do grafo
        # print(i._pessoa_1)
        # print(i._pessoa_2)
        nx_g.add_edge(i._pessoa_1._pessoa, i._pessoa_2._pessoa, weight=i._amizade)  # adiciona ao desenho uma aresta com
        # o vérice pessoa_1, o vértice pessoa_2 e com peso amizade
        print(i._pessoa_1, "->", i._pessoa_2, "=", i._amizade)
    # desenhar
    if show_plot:
        desenho = nx.spring_layout(nx_g)  # desenho das posições dos nós de acordo com a disposição spring_layout
        nx.draw_networkx_nodes(nx_g, desenho, node_size=400, node_color="#32CD32", edgecolors="#8DEEEE")
        # desenha apenas os nós do grafo, com tamanho e cor definido por nós
        nx.draw_networkx_labels(nx_g, desenho, font_size=7)  # põe a legenda nos nós grafo, o tamnaho da letra é 7
        nx.draw_networkx_edges(nx_g, desenho, width=3)  # desenha as arestas do grafo, com largura igual a 3
        nx.draw_networkx_edge_labels(nx_g, desenho, font_size=6)  # põe a legenda nas arestas, neste caso o peso
        plt.axis("off")  # remover os eixos do x e y do desenho
        plt.show()  # para mostrar o grafo


# draw the graph using networkx and mathplotlib.pyplot
def nx_teste_kruskal(graf, show_plot=False):
    print('Número de arestas únicas:', desenhar.edge_count())  # fixo
    nx_g = nx.Graph()  # desenha o grafo da Tad_grafo.py utilizando networkx
    graph_amizade = 0  # peso do grafo
    for i in graf.edges():  # se i está nas arestas do grafo
        graph_amizade += i._amizade
        nx_g.add_edge(i._pessoa_1._pessoa, i._pessoa_2._pessoa, weight=i._amizade)  # adiciona um aresta ao desenho
        print(i._pessoa_1, "->", i._pessoa_2, "=", i._amizade)  # adiciona uma aresta ao desenho
    print("*****************************")
    print("O peso da árvore geradora mínima é: ", graph_amizade)

    # o vértice pessoa_1, o vértice pessoa_2 e o peso amizade
    if show_plot:
        desenho = nx.spring_layout(nx_g)  # desenho das posições dos nós de acordo com a disposição spring_layout
        nx.draw_networkx_nodes(nx_g, desenho,
                               node_size=400,
                               node_color="#32CD32", edgecolors="#8DEEEE")  #  desenha apenas os nós do grafo,
        # com tamanho e cor definido por nós
        nx.draw_networkx_labels(nx_g, desenho,
                                font_size=7)  # põe a legenda nos nós grafo, o tamnaho da letra é 7
        nx.draw_networkx_edges(nx_g, desenho, width=3)  # desenha as arestas do grafo, com largura igual a 3
        nx.draw_networkx_edge_labels(nx_g, desenho,
                                     font_size=6)  #  põe a legenda nas arestas, neste caso o peso
        plt.axis("off")  # remover os eixos do x e y do desenho
        plt.show()  # para mostrar o grafo


def clusters(graph, k=2, show_plot=False):
    n_clusters = k
    print('Número de arestas únicas:',desenhar.edge_count())  # fixo
    nx_g = nx.Graph() # vai desenhar o grafo do Tad_grafo.py com o recurso ao networkx
    max = Edge(0, 0, 0) # cria um objeto da classe Edge com as pessoas e a amizade em 0
    graph_w_kruskal = graph.kruskal() # vai aplicar o algoritmo de kruskal ao grafo que foi construído a partir dos dados
    # do ficheiro
    if k <= 1:
        raise ValueError('O número de clusters só pode tomar valores naturais, superiores a 1.')
    while k - 1 != 0: # ciclo para percorrer as partições dos clusters (k-1 partições; k=nª de clusters)
        for i in graph_w_kruskal.edges(): # percorrer as arestas do grafo com o kruskal implementado
            if i._amizade > max.amizade(): # comparar o número da amizade a procurar com o valor do *max*
                max = i # caso for maior que a amizado do *max* vai substituir o valor da amizade no *max*
        print('Retirar:',(max), max.amizade()) # dar print do elemento maior dps de percorrer o grafo todo
        graph_w_kruskal.remove_edge(max._pessoa_1, max._pessoa_2) # remove a aresta com maior peso
        max = Edge(0, 0, 0) # reset do *max*, objeto da classe Edge (apenas para a continuação do ciclo)
        k -= 1 # diminuição do k para a continuação do ciclo
    print('\n')
    for j in graph_w_kruskal.edges():  # se i está nas arestas do grafo
        nx_g.add_edge(j._pessoa_1._pessoa, j._pessoa_2._pessoa, weight=j._amizade)  # adiciona ao desenho uma aresta com
        # o vértice pessoa_1, o vértice pessoa_2 e com peso amizade
        #print(j._pessoa_1, "->", j._pessoa_2, "=", j._amizade)

    print('=====================================\nComunidades com o número de clusters:\n'
          '=====================================\n')
    k_cliques(nx_g,n_clusters)
    # se o k for maior ou igual a 3 ele irá apenas ver as comunidades, usando o louvain
    louvain(nx_g)

    if show_plot:
        desenho = nx.spring_layout(nx_g)  # desenho das posições dos nós de acordo com a disposição spring_layout
        nx.draw_networkx_nodes(nx_g, desenho, node_size=400, node_color="#32CD32", edgecolors="#8DEEEE")
        # desenha apenas os nós do grafo, com tamanho definido por nós
        nx.draw_networkx_labels(nx_g, desenho, font_size=7)  # põe a legenda nos nós grafo, o tamnaho da letra é 7
        nx.draw_networkx_edges(nx_g, desenho, width=3)  # desenha as arestas do grafo, com largura igual a 3
        nx.draw_networkx_edge_labels(nx_g, desenho, font_size=6)  # põe a legenda nas arestas, neste caso o peso
        plt.axis("off")  # remover os eixos do x e y do desenho
        plt.show()  # para mostrar o grafo


def k_cliques(graph, k):
    community = nx.community.k_clique_communities(graph,k) # k=2 porque os grafos dispersos terão sempre 2 vértices;
    # se colocado k maior ou igual a 3, não irá imprimir nada visto que os subgrafos não têm todos 3 vertices
    for i in community:
        print(i)


def louvain(graph):
    community = nx.community.louvain_communities(graph)
    for i in community:
        print(i)


if __name__ == '__main__':
    nome_f = "facebook_network.csv"
    desenhar = grafo_csv(nome_f)
    clusters(desenhar, 7, show_plot=True)

# teste grafo normal

# nome_f = "facebook_network.csv"
# desenhar = grafo_csv(nome_f)
# print(desenhar)
# nx_teste(desenhar, show_plot=True)

# teste grafo com kruskal

# nome_f = "facebook_network.csv"
# desenhar = grafo_csv(nome_f)
# minimum_spanning_tree = desenhar.kruskal()
# minimum_spanning_tree.print()
# nx_teste_kruskal(minimum_spanning_tree, show_plot=True)

# teste grafo com clustering (kruskal implementado)

# nome_f = "facebool_network.csv"
# desenhar = grafo_csv(nome_f)
# clusters(desenhar, 2, show_plot=True)
