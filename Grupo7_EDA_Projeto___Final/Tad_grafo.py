# Fase 1

# Fase 1
# a
# Implementar o TAD Grafo numa classe em Python, de acordo com a implementação feita em
# aula nos exercícios do módulo 10, exercícios 1, 2 e 3. a) (usando a representação de mapas de
# adjacências). Devem usar a interface e as classes Vertex e Edge, como indicado na aula.

# No Facebook, a pessoa é o vértice e a amizade é uma aresta não direcionada
# Classe Vertex - vértice do grafo, corresponde a uma pessoa

# Esta implementação usa um dicionário de par (chave=vértice, valor=dicionário de adjacências)
# Cada aresta é inserida nos dois vértices extremos para otimizar a procura de arestas incidentes num dado vértice
# (mesmo que seja dirigido, evitando ter de procurar as arestas incoming no restante grafo)

# Exercício 1:
# Classe Vértice
class Vertex:
    # Contrutor do Vertex - só tem um atributo elemento que guarda o objeto que pretendenmos guardar nesse vértice
    def __init__(self, pessoa):
        '''O vértice será inserido no Grafo usando o método insert_vertex(pessoa) que cria um Vertex'''
        self._pessoa = pessoa

    # Getter para obter a identificação de um Vértice feito chamando as funções hash() e id() do Python

    def __hash__(self):
        # devolve um inteiro que identifica este vértice como uma chave num dicionário
        return hash(id(self._pessoa))

    def __str__(self):
        return '{0}'.format(self._pessoa)

    # Função booleana que diz se um Vértice de elemento pessoa dado é igual ao Vértice em que estamos (o do self)
    # É obrigatório definir a função __eq__ quando se define a função __hash__

    def __eq__(self, pessoa):
        return pessoa == self._pessoa  # pessoa é um objeto- quero saber com esta função
        # se é igual ao objeto que está guardado no self

    def pessoa(self):
        '''Devolve o elemento  neste vértice'''
        return self._pessoa


# Exercício 2:
# Classe Edge
class Edge:
    '''Estrutura de Aresta - (origem, destino), com peso  - para um grafo'''

    # Contrutor - inicializa os atributos vértice de origem (pessoa_1), vértice de destino (pessoa_2) e peso (amizade)
    def __init__(self, pessoa_1, pessoa_2, amizade):
        '''A aresta será inserida no no Grafo usando insert_edge(pessoa_1,pessoa_2,amizade)'''
        self._pessoa_1 = pessoa_1
        self._pessoa_2 = pessoa_2
        self._amizade = amizade

    # Função que devolve um identificador único para a edge/aresta usando a função hash() do
    # Python sobre o tuplo (vértice origem, vértice destino) -> (pessoa_1, pessoa_2)

    def __hash__(self):
        return hash((self._pessoa_1, self._pessoa_2))

    # Função que devolve a informação (origem, destino) -> (pessoa_1, pessoa_2) em string

    def __str__(self):
        return '({0},{1})'.format(self._pessoa_1, self._pessoa_2)

    # Função que devolve num tuple os dois vértices associados à aresta

    def endpoints(self):
        # devolve um tuplo (pessoa_1, pessoa_2) para os vértices pessoa_1 e pessoa_2
        return (self._pessoa_1, self._pessoa_2)

    # Dado um vértice pessoa (que pode ser origem ou destino desta aresta)
    # devolve o vértice que está na outra ponta da aresta

    def opposite(self, pessoa):
        # O if-else compacto lê-se - se: pessoa é o vértice origem (pessoa_1) da aresta, a função devolve o
        # vértice destino (pessoa_2). Caso contrário devolve o vértice origem (pessoa_1)
        return self._pessoa_2 if pessoa is self._pessoa_1 else self._pessoa_1

    # O método amizade para as edges/arestas devolve o peso da aresta se existir
    def amizade(self):
        # devolve o elemento associado com esta aresta
        return self._amizade

    def mostra_edge(self):
        print('(', self._pessoa_1, ', ', self._pessoa_2, ')')

    def __eq__(self, other):
        return self._pessoa_1 == other._pessoa_1 and self._pessoa_2 == other._pessoa_2


# Exercício 3 a)
# Classe Grafo -   Representacao de um grafo usando mapas de adjacências (associações)'''
# No caso do Facebook, as arestas são não direciona

class Graph:
    # Construtor do Grafo que inicializa os atributos directed, number e vertices
    def __init__(self, directed=False):
        '''Cria um grafo vazio (contentor _vertices); é orientado se o parâmetro directed tiver o valor True'''
        self._directed = directed   # indica se o grafo é dirigido (valor True) ou não (valor False)
        self._number = 0  # quantidade de nós
        self._vertices = {}  # dicionário com os vários vértices como chaves e em que o valor
        # associado a cada vértice é o dicionário de adjacências desse vértice
        # (associação: outro_vértice -> aresta que os liga)
        # para o kruskal
        self._edges = {}
        self.graph = []
        self._pai = {}
        self._rank = {}

    def insert_vertex(self, pessoa=None):
        '''Insere e devolve um novo vértice com o elemento pessoa'''
        v = Vertex(pessoa)  #  Criar um vértice chamando o seu construtor e passando o objeto pessoa a guardar no vértice
        self._vertices[v] = {}  # Inicializar o dicionário/mapa de adjacências correspondente ao vértice pessoa a vazio
        return v

    def insert_edge(self, pessoa_1, pessoa_2, amizade=None):
        '''Cria pessoa_1 e pessoa_2 e insere e devolve uma nova aresta entre pessoa_1 e pessoa_2 com peso amizade'''
        e = Edge(pessoa_1, pessoa_2, amizade)
        self._vertices[pessoa_1][pessoa_2] = e  # vai colocar nas incidências de pessoa_1
        self._vertices[pessoa_2][pessoa_1] = e  # e nas incidências de pessoa_2 (para facilitar a
        # procura de todos os arcos incidentes)
        self.graph.append([pessoa_1, pessoa_2, amizade])
        return e

    def incident_edges(self, pessoa, outgoing=True):
        '''Gerador: indica todas as arestas (outgoing) incidentes no vértice pessoa
        Se for um grafo dirigido e outgoing for False, devolve as arestas em incoming
        '''
        for edge in self._vertices[pessoa].values():  # para todas as arestas relativas ao vértice pessoa:
            if not self._directed:
                yield edge
            else:  # senão deve ir procurar em todas as arestas para saber quais entram ou saiem
                x, y = edge.endpoints()
                if (outgoing and x == pessoa) or (not outgoing and y == pessoa):
                    yield edge

    def is_directed(self):
        '''com base na criação original da instância, devolve True se o Grafo é dirigido; False senão '''
        return self._directed  # True se os dois contentores são distintos

    def vertex_count(self):
        '''Devolve a quantidade de vértices no grafo'''
        return len(self._vertices)

    def vertices(self):
        '''Devolve um iterável sobre todos os vértices do Grafo'''
        return self._vertices.keys()

    def edge_count(self):
        '''Devolve a quantidade de arestas do Grafo'''
        total = sum(len(self._vertices[v]) for v in self._vertices)
        # para grafos não direcionados, para não contar duas vezes as mesmas arestas
        return total if self._directed else total // 2

    def edges(self):
        '''Devolve o conjunto de todas as arestas do Grafo'''
        result = set()  # evitar reportar duas vezes a mesma aresta num grafo não direcionado
        for secondary_map in self._vertices.values():
            result.update(secondary_map.values())  # adicionar arestas ao conjunto resultante
        return result

    def get_edge(self, pessoa_1, pessoa_2):
        '''Devolve a aresta que liga pessoa_1 e pessoa_2 ou None se não forem adjacentes'''
        edge = self._vertices[pessoa_1].get(pessoa_2)  # returns None se não existir nenhuma aresta entre pessoa_1 e pessoa_2
        if edge != None and self._directed:  # se é dirigido
            _, x = edge.endpoints  # vai confirmar se é pessoa_1 --> pessoa_2
            if x != pessoa_2:
                edge = None
        return edge

    def degree(self, pessoa, outgoing=True):
        '''quantidade de arestas incidentes no vértice pessoa
        Se for um grafo dirigido, conta apenas as arestas outcoming ou em incoming, de acordo com o valor de outgoing
        '''
        adj = self._vertices
        if not self._directed:
            count = len(adj[pessoa])
        else:
            count = 0
            for edge in adj[pessoa].values():
                x, y = edge.endpoints()
                if (outgoing and x == pessoa) or (not outgoing and y == pessoa):
                    count += 1
        return count

    def remove_edge(self, pessoa_1, pessoa_2):
        '''Remove a aresta entre pessoa_1 e pessoa_2 '''
        if pessoa_1 in self._vertices.keys() and pessoa_2 in self._vertices[pessoa_1].keys():
            del self._vertices[pessoa_1][pessoa_2]
            del self._vertices[pessoa_2][pessoa_1]

    def remove_vertex(self, pessoa):
        '''remove o vértice pessoa'''
        # remover todas as arestas de [pessoa]
        # remover todas as arestas com pessoa noutros vertices
        # remover o vértice
        lst = [i for i in self.incident_edges(pessoa)]
        for i in lst:
            x, y = i.endpoints()
            self.remove_edge(x, y)
        del self._vertices[pessoa]
        return pessoa

    def make_set(self, pessoa):
        self._pai[pessoa] = pessoa              # pai do vértice
        self._rank[pessoa] = 0                  # rank do vértice

    def find(self, pessoa):
        if self._pai[pessoa] != pessoa:
            self._pai[pessoa] = self.find(self._pai[pessoa])
        return self._pai[pessoa]
        # encontrar o pai do vértice

    def union(self, pessoa_1, pessoa_2):                 # ligar pessoa_1 e pessoa_2 ao mesmo pai
        raiz_1 = self.find(self._pai[pessoa_1])
        raiz_2 = self.find(self._pai[pessoa_2])

        if raiz_1 != raiz_2:                             # diferentes pais dos vértices
            if self._rank[raiz_1] > self._rank[raiz_2]:
                self._pai[raiz_2] = raiz_1
            else:
                self._pai[raiz_1] = raiz_2
        if self._rank[raiz_1] == self._rank[raiz_2]:
            self._rank[raiz_2] += 1


    def kruskal(self):                                             # para ter a árvore de cobertura mínima
        minimum_spanning_tree = Graph()
        self.graph = sorted(self.graph, key=lambda item: item[2])  # ordenar toodas as arestas por peso

        for node in self._vertices:
            self.make_set(node.__str__())                          # definir o valor inicial do pai e rank

        for edge in self.graph:
            pessoa_1, pessoa_2, amizade = edge
            x = self.find(pessoa_1.__str__())
            y = self.find(pessoa_2.__str__())                      # para ter os pais dos 2 vértices x, y
            if x != y:                                             # se os 2 nós estão no mesmo grupo de conexão
                minimum_spanning_tree.insert_edge(minimum_spanning_tree.insert_vertex(pessoa_1._pessoa), minimum_spanning_tree.insert_vertex(pessoa_2._pessoa), amizade)
                self.union(x, y)                                   # ligar os 2 nós
        return minimum_spanning_tree

    def print(self):                                               # imprimir aresta com peso
        t_amizade = 0                                              # peso do grafo
        for edge in self.graph:
            pessoa_1, pessoa_2, amizade = edge
            t_amizade += amizade


if __name__ == "__main__":
    # main()
    print('\n')










