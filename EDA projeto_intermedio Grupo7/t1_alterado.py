# Membros do grupo - CDA1:
# Eliane Susso Efraim Gabriel, Nº 103303 - implementação e análise na fase 2
# João Francisco Marques Gonçalves da Silva Botas, Nº104782- implementação dos métodos 1 a 8 da fase 1
# Maria João Ferreira Lourenço, Nº 104716- organização e escrita do relatório do projeto
# Umeima Adam Mahomed, Nº99239- implementação da pesquisa binária e métodos de ordenamento
# Data de entrega: 22/04/2022

# Trabalho de grupo intermédio:

# Fase 1 - TAD Lista: implementações
# TAD Lista duplamente ligada e circular

import time
import random


#  criação da class Node
class Node:
    def __init__(self, value):  # vamos atribuir um valor
        self.data = value  # atributo para guardar valor do elemento
        self.next = None  # aponta para o próximo
        self.prev = None  # aponta para o anterior

    @property
    def data(self):  # getter para data
        return self.__data

    @property
    def next(self):  # getter para next
        return self.__next

    @property
    def prev(self):  # getter para prev
        return self.__prev

    @data.setter
    def data(self, new_data):  # setter para data
        self.__data = new_data

    @next.setter
    def next(self, new_next):  # setter para next
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev):  # setter para prev
        self.__prev = new_prev


# TAD Lista - duplamente ligada

class ListaDL:
    def __init__(self):
        self.__head = None  # aponta para o início
        self.__tail = None  # aponta para o fim
        self.__size = 0  # tamanho da lista

    # comprimento ou tamanho: quantos itens estão na lista – len()

    def __len__(self):
        return self.__size

    # indicar se a lista está vazia – vazia()

    def vazia(self):
        return self.__size == 0

    #  esvaziar a lista – limpar()

    def limpar(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # consultar (devolver) elemento na posição p – ver(p)

    def ver(self, p):
        if p > self.__size or p < 1:  # se o index p é maior que o comprimento da lista ou se é menor que um
            print("Erro - o índice pretendido está errado")
            return
        pointer = self.__head  # começa na head
        while p > 1:  # enquanto o índice está compreendido entre 0 e o tamanho da lista
            pointer = pointer.next  # percorre os nós
            p -= 1  # para apontar para o elemento e não para o próximo
        print(pointer.data)  # para ter o valor do nó pretendido

    # inserir um dado item na lista - ins(item)

    # inserir no início

    def ins_front(self, item):
        new_node = Node(item)  # cria new_node
        if self.__head is None:  # se a lista está vazia
            self.__head = new_node  # a head passa a ser o new_node
        else:  # se a lista não está vazia
            new_node.next = self.__head  # ajusta a posição dos nós existentes
            self.__head.prev = new_node  # ajusta a posição dos nós existentes
            self.__head = new_node  # o novo nó passa a ser a cabeça
        self.__size += 1  # aumenta o comprimento

    # inserir no meio

    def ins_middle(self, item):
        # criar novo nó
        new_node = Node(item)

        # se a lista está vazia
        if self.__head == None:
            # a head e a tail apontam para o new_node
            self.__head = self.__tail = new_node
            # anterior da head aponta para None
            self.__head.prev = None
            # o seguinte da tail aponta para None, porque é o último nó da lista
            self.__tail.next = None
        else:
            # pointer aponta para head
            pointer = self.__head

            # guarda a posição do meio da lista
            meio = (self.__size // 2) if (self.__size % 2 == 0) else ((self.__size + 1) // 2)

            # Itera sobre a lista da posição do pointer para o meio
            for i in range(1, meio):
                pointer = pointer.next

            # Nó temp aponta para o nó depois do pointer
            temp = pointer.next
            temp.prev = pointer

            # new_node vai ser adicionado entre pointer e temp
            pointer.next = new_node
            new_node.prev = pointer
            new_node.next = temp
            temp.prev = new_node
        self.__size += 1

    # inserir no fim

    def ins_end(self, item):
        new_node = Node(item)  # cria new_node
        if self.__head is None:  # se a lista está vazia
            self.__head = new_node  # novo nó passa a ser a cabeça
        else:  # se a lista não está vazia
            pointer = self.__head
            while pointer.next is not None:  # enquanto houver nó seguinte
                pointer = pointer.next  # percorre a lista
            pointer.next = new_node  # o nó depois do pointer é o novo nó
            new_node.prev = pointer  # ajuste do ponteiro
        self.__size += 1  # aumenta o comprimento

    # remover um determinado item da lista - rem(item)

    def rem(self, item):
        if self.__head is None:  # se a lista estiver vazia
            print("A lista não têm elementos para remover")
            return
        pointer = self.__head
        while pointer is not None:  # lista com elementos
            nxt = pointer.next  # percorre a lista
            if pointer.data == item:  # se o valor do nó é igual ao item
                if pointer.prev:  # anterior
                    pointer.prev.next = pointer.next  # muda o anterior apenas se o nó a eliminar não
                # é o primeiro nó
                else:
                    self.__head = pointer.next  # se a head é para ser removida, o nó seguinte passa a ser a nova head
                if pointer.next:  # seguinte
                    pointer.next.prev = pointer.prev  # muda o seguinte apenas se o nó que é para eliminar não é
                # o último nó
                else:
                    self.__tail = pointer.prev  # se a tail é para ser removida o nó antes da tail passa a
                    # ser a nova tail
            pointer = nxt
        self.__size -= 1  # ajusta o comprimento

    # mostrar o conteúdo completo da lista – mostrar()

    def __str__(self):
        values = '['  # como quero mostrar a lista
        pointer = self.__head  # percorrer a partir da cabeça
        if pointer == None:  # se a lista estiver vazia
            return values + "]"
        while pointer is not None:  # enquanto não chegarmos ao fim da lista
            values += "{0} ".format(pointer.data)  # mostrar cada elemento
            pointer = pointer.next  # passar ao elemento seguinte da lista
        values += ']'  # fechar
        return values  # mostrar os valores

    # indicar se existe na lista um item com um dado valor – existe(item)

    def existe(self, item):
        i = 1  # começa no início
        found = False
        pointer = self.__head  # ponteiro aponta para a cabeça

        # se a lista está vazia
        if self.__head == None:
            print("A lista está vazia")
            return

        # lista com elementos
        while pointer != None:
            # compara o valor do item com o valor do nó presente na lista
            if pointer.data == item:  # se o valor for igual ao item
                found = True
                break
            pointer = pointer.next  # percorre os nós
            i += 1

        if found:  # se encontrou devolve a mensagem em baixo
            print("O item " + str(item) + " está na posição " + str(i))
        else:  # se não encontrou
            print("0")
            print("Explicação: o item procurado não se encontra na lista, pelo que retornou 0")

    # Bubble Sort

    def ordenar_bubble_sort(self):
        if self.__head is None:  # lista vazia
            print("A lista está vazia!")
            return

        swap = 0
        last_pointer = None
        while True:  # continuar iterações até a lista estar ordenada
            swap = 0
            aux_pointer = self.__head  # primeiro nó
            while aux_pointer.next != last_pointer:  # enquanto seguinte diferente do último
                if aux_pointer.data > aux_pointer.next.data:  # valor do nó maior que o valor do nó seguinte
                    aux_data = aux_pointer.data
                    aux_pointer.data = aux_pointer.next.data
                    aux_pointer.next.data = aux_data
                    swap = 1  # troca com o nó adjacente
                aux_pointer = aux_pointer.next  # percorre a lista
            last_pointer = aux_pointer
            if swap == 0:  # quando está tudo ordenado
                break

    # Merge Sort

    # obter o meio da lista

    def get_middle(self, aux_head):
        if aux_head == None:  # se vazia
            return aux_head

        slow_pointer = fast_pointer = aux_head  # ponteiros

        while fast_pointer.next != None and fast_pointer.next.next != None:  # percorre a lista
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

    #  função recursiva que funde nós de 2 listas ordenadas em 1 única lista ordenada

    def sorted_merge(self, left, right):
        result_node = None

        # casos base
        if left == None:
            return right

        if right == None:
            return left

        # escolher right ou left

        if left.data <= right.data:  # valores da esquerda menores ou iguais aos valores da direita
            result_node = left
            result_node.next = self.sorted_merge(left.next, right)
        else:
            result_node = right
            result_node.next = self.sorted_merge(left, right.next)

        return result_node

    # para fazer Merge Sort

    def ordenar_merge_sort(self, aux_pointer_head):
        if aux_pointer_head is None or aux_pointer_head.next is None:  # lista vazia
            return aux_pointer_head

        middle = self.get_middle(aux_pointer_head)  # chama o método get_middle

        middle_next = middle.next

        middle.next = None
        # middle_next.prev = None

        # recorrer às metades da esquerda e da direita

        left_list = self.ordenar_merge_sort(aux_pointer_head)
        right_list = self.ordenar_merge_sort(middle_next)

        # juntar as metades da esquerda e da direita já ordenadas

        sorted_list = self.sorted_merge(left_list, right_list)
        # -> -> ->

        walker = sorted_list
        prev = None
        # node: 1 -> 2 -> 3 -> 4
        # prev: N -> 1 -> 2 -> 3
        while walker:
            walker.prev = prev
            prev = walker
            walker = walker.next

        return sorted_list  # lista ordenada

    # ordenar a lista – ordenar_()

    def ordenar_(self, sort_method='m'):

        # Bubble Sort

        if sort_method == 'b' or sort_method == 'B':
            self.ordenar_bubble_sort()
            return True

        # Merge Sort

        elif sort_method == 'm' or sort_method == 'M':
            self.__head = self.ordenar_merge_sort(self.__head)
            return True

        # solução mais eficaz

        else:
            print("Método de ordenação não identificado")
            return False

    # estes 4 métodos seguintes servem para o ficheiro tempo
    # testar quanto tempo demoram os seguintes métodos dado o número de elementos da lista
    # só retorna o tempo que demora a fazer para uma lista com o número de elementos que dei como atributo

    # Merge Sort

    def performance_merge_sort(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.ordenar_('m')  # chama o método ordenar_merge_sort(aux_pointer_head)
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Bubble Sort

    def performance_bubble_sort(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.ordenar_('b')  # chama o método ordenar_bubble_sort()
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Pesquisa binária

    def performance_binary_search(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números  aleatórios
        item_a_procurar = 1  # valor que se quer procurar
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.existe_binary_search(item_a_procurar, 'm')  # chama o método
        # existe_binary_search(item, sort_method='m')
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Pesquisa linear

    def performance_linear_search(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        item_a_procurar = 1  # valor que se quer procurar
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.existe_linear_search(item_a_procurar)  # chama o método existe_linear_search(item)
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Pesquisa binária

    # encontrar o meio

    def find_middle(self, beginning, end):
        if beginning is None:  # lista vazia
            return None

        slow_pointer = beginning  # ponteiro para o primeiro nó
        fast_pointer = beginning.next  # ponteiro para o nó depois do primeiro nó

        while fast_pointer != end:  # enquanto fast_pointer diferente do último nó

            fast_pointer = fast_pointer.next  # percorre a lista
            if fast_pointer != end:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next

        return slow_pointer

    def existe_binary_search(self, item, sort_method='m'):

        # Bubble Sort

        if sort_method == 'b' or sort_method == 'B':
            self.ordenar_bubble_sort()

        # Merge Sort

        elif sort_method == 'm' or sort_method == 'M':
            self.__head = self.ordenar_merge_sort(self.__head)

        # método mais eficaz

        else:
            print("Método de ordenação não identificado. Merge Sort será utilizado")
            self.__head = self.ordenar_merge_sort(self.__head)

        start = self.__head
        end = None
        start_pos = 1  # começa no início
        end_pos = self.__len__()  # acaba quando atingue o tamanho da lista
        while True:
            middle = self.find_middle(start, end)  # vai buscar o método find_middle
            middle_pos = (start_pos + end_pos) // 2  # como calcular middle_pos

            if middle is None:  # se lista vazia
                return 0
            if middle.data == item:  # se valor igual ao item
                return middle_pos

            if middle.data < item:  # valor menor que item
                start = middle.next
                start_pos = middle_pos + 1
            else:  # valor maior que item
                end = middle
                end_pos = middle_pos - 1

            if not (end is None or end != start):
                break
        return "0 - Devolve zero porque o item não foi encontrado"

    # este método serve para não retornar nada ao ser feita a complexidade dos searchers(), ou seja,
    # este método tem o mesmo intuito do existe(item) mas não irá dar print a nada na tela

    # Pesquisa linear

    def existe_linear_search(self, item):
        i = 1  # começa na posição 1
        found = False
        pointer = self.__head  # ponteiro aponta para a cabeça

        # se a lista está vazia
        if self.__head == None:
            print("A lista está vazia")
            return

        # lista com elementos
        while pointer != None:
            # compara o valor do item com o valor do nó presente na lista
            if pointer.data == item:  # se o valor for igual ao item
                found = True
                break
            pointer = pointer.next  # percorre os nós
            i += 1

        if found:  # se encontrou devolve a mensagem em baixo
            pass
        else:  # se não encontrou
            pass


# teste - lista duplamente ligada

if __name__ == '__main__':
    lst = ListaDL()
    lst.ins_front(1)
    lst.ins_end(2)
    lst.ins_middle(9)
    lst.ins_end(4)
    print(lst)
    lst.ordenar_('b')
    lst.existe(1)
    print(lst)
    print(lst.existe_binary_search(1, 'b'))
#     lst.ordenar_('M')
#     print(lst)
#     lst.rem(1)
#     print(lst)
#     print(lst.__len__())
#     lst.ver(-7)


# TAD Lista - lista duplamente ligada circular

class ListaDLC:
    def __init__(self):
        self.__size = 0  # comprimento da lista
        self.__head = None  # aponta para o início
        self.__tail = None  # aponta para o fim

    # comprimento ou tamanho: quantos itens estão na lista – len()

    def __len__(self):
        return self.__size

    # indicar se a lista está vazia – vazia()

    def vazia(self):
        return self.__size == 0

    #  esvaziar a lista – limpar()

    def limpar(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    # consultar (devolver) elemento na posição p – ver(p)

    def ver(self, p):
        if p < 0 or p >= self.__size:  # se o index p é maior que o comprimento da lista ou se é menor que z
            print("Erro - o índice pretendido está errado")
        pointer = self.__head  # começa na head
        while p > 0:  # enquanto o índice está compreendido entre 0 e o tamanho da lista
            pointer = pointer.next  # percorre os nós
            p -= 1  # para apontar para o elemento e não para o próximo
        print(pointer.data)  # para ter o valor do nó pretendido

    # inserir um dado item na lista - ins(item)

    # inserir no fim da fila

    def ins_end(self, item):
        new_node = Node(item)  # criar nó
        if self.__head is None:  # lista vazia
            self.__head = new_node  # head é o new_node
            self.__tail = new_node  # tail é o new_node
            self.__size += 1  # corrige o tamanho
            return
        # lista com elementos
        new_node.prev = self.__tail  # ajuste da posição da tail
        new_node.next = self.__head  # ajuste da posição da head
        self.__tail.next = new_node  # o seguinte da tail passa a ser o new_node
        self.__head.prev = new_node  # o antes da head é o new_node
        self.__tail = new_node  # tail é o novo nó
        self.__size += 1  # aumenta o comprimento

    # remover um determinado item da lista - rem(item)

    def rem(self, item):
        # se a fila estiver vazia
        if self.__head == None:
            print('A fila está vazia!')
            return None
        # começa no primeiro nó(head) e irá andar de next em next até encontrar o elemento
        passo = self.__head
        # posição anterior ao elemento que encontrar (começa em None e vai adquirindo o valor de passo)
        previous = None
        # ciclo que procura o nó ao longo da lista DLC
        while passo.data != item:  # enquanto o valor do nó for diferente do item
            # Se o ciclo terminar e encontrar a head: não existe o elemento a pesquisar
            if passo.next == self.__head:
                print('A lista não tem este elemento!')
                return self.__head
            # avanço do ciclo (next)
            previous = passo
            passo = passo.next
        # Caso seja o primeiro
        if passo.next == self.__head and previous == None:
            return None
        # Caso exista mais de um nó na lista
        if passo == self.__head:
            # alteração dos nós na remoção com utilização do previous e do próximo elemento
            previous = self.__head.prev
            next_elem = self.__head.next
            previous.next = next_elem
            next_elem.prev = previous
        # Caso seja o último elemento da lista DLC
        elif passo.next == self.__head:
            # troca entre nós do início e fim (head e tail)
            previous.next = self.__head
            self.__head.prev = previous
            self.__tail = previous
        else:
            # caso contrário irá alterar utilizando o next e o previous
            temp = passo.next
            previous.next = temp
            temp.prev = previous
        # retirar sempre um tamanho à lista
        self.__size -= 1
        return self.__head

    # mostrar o conteúdo completo da lista – mostrar()

    def __str__(self):
        values = '['  # como quero mostrar a lista
        pointer = self.__head = self.__tail.next  # percorrer
        if self.__head is None:
            return values + "]"
        while pointer:  # enquanto não chegarmos ao fim da lista
            values += "{0} ".format(pointer.data)  # mostrar cada elemento
            pointer = pointer.next  # passar ao elemento seguinte da lista
            if pointer == self.__head.prev:
                values += "{0} ".format(pointer.data)  # mostrar cada elemento
                break
        values += ']'  # fechar
        return values  # mostrar os valores

    # indicar se existe na lista um item com um dado valor – existe(item)

    def existe(self, item):
        position = 0  # começa na posição 0
        if self.__head is None:  # lista vazia
            print("A lista está vazia!")
        else:  # lista com nós
            pointer = self.__head
            while pointer:  # enquanto a lista não acaba
                position += 1
                if pointer.data == item:  # se o valor do nó é igual ao item
                    print("O item " + str(item) + " está na posição " + str(position))
                    break
                if pointer == self.__tail:  # se não tem o item procurado
                    print("0")
                    print("Explicação: o item procurado não se encontra na lista, pelo que retornou 0")
                    break
                pointer = pointer.next  # percorre a lista

    # ordenar a lista – ordenar_()

    # Bubble Sort

    def ordenar_bubble_sort(self):
        if self.__head is None:  # lista vazia
            print("A lista está vazia!")
            return

        swap = 0
        last_pointer = self.__head
        while True:  # continuar iterações até a lista estar ordenada
            swap = 0
            aux_pointer = self.__head  # primeiro nó
            while aux_pointer.next != last_pointer:  # enquanto seguinte diferente do último
                if aux_pointer.data > aux_pointer.next.data:  # valor do nó maior que o valor do nó seguinte
                    aux_data = aux_pointer.data
                    aux_pointer.data = aux_pointer.next.data
                    aux_pointer.next.data = aux_data
                    swap = 1  # troca com o nó adjacente
                aux_pointer = aux_pointer.next  # percorre a lista
            last_pointer = aux_pointer
            if swap == 0:  # quando está tudo ordenado
                break

    # Merge Sort

    # juntar as partes

    def merge(self, a, b):

        # se a primeira lista ligada estiver vazia
        if a is None:
            return b

        # se a segunda lista ligada estiver vazia
        if b is None:
            return a

        # escolher o valor mais pequeno
        if a.data < b.data:
            a.next = self.merge(a.next, b)
            a.next.prev = a
            a.prev = None
            return a
        else:
            b.next = self.merge(a, b.next)
            b.next.prev = b
            b.prev = None
            return b

    # dividir a lista em duas listas com metade do tamanho

    def split(self, head):
        # head.prev.next = None
        # head.prev = None

        f = s = head
        while True:
            if f.next is None:
                break
            if f.next.next is None:
                break
            f = f.next.next
            s = s.next

        pointer = s.next
        s.next = None
        pointer.prev = None

        return pointer

    # implementar Merge Sort

    def ordenar_merge_sort(self, head):
        if head is None:  # lista vazia
            return head
        if head.next is None:
            return head

        # quebrar a conexão circular para que a ordenação seja facilitada
        if head.prev:
            head.prev.next = None
            head.prev = None

        s = self.split(head)

        # voltar às metades da esquerda e da direita
        head = self.ordenar_merge_sort(head)
        s = self.ordenar_merge_sort(s)

        # fundir as duas metades já ordenadas
        return self.merge(head, s)

    # ordenar a lista – ordenar_()

    def ordenar_(self, sort_method='m'):

        # Bubble Sort

        if sort_method == 'b' or sort_method == 'B':
            self.ordenar_bubble_sort()
            return True

        # Merge Sort

        elif sort_method == 'm' or sort_method == 'M':
            self.__head = self.ordenar_merge_sort(self.__head)

            walker = self.__head
            while walker.next:
                walker = walker.next

            # fazer update do anterior da head e do seguinte da tail
            # porque perdeu a conexão durante o ordenamento

            walker.next = self.__head
            self.__head.prev = walker

            return True
        else:
            print("Método de ordenação não identificado")
            return False

    # estes 4 métodos seguintes servem para o ficheiro tempo

    # Merge Sort

    def performance_merge_sort(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.ordenar_('m')  # chama o método ordenar_merge_sort(head)
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Bubble Sort

    def performance_bubble_sort(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.ordenar_('b')  # chama o método ordenar_bubble_sort()
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Pesquisa Binária

    def performance_binary_search(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        item_a_procurar = 1  # valor que se quer procurar
        random.shuffle(random_numbers1)  # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.existe_binary_search(item_a_procurar, 'm')  # chama o método
        # existe_binary_search(item, sort_method='m')
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # Pesquisa Linear

    def performance_linear_search(self, tamanho):
        random_numbers1 = random.sample(range(10000), tamanho)  # números aleatórios
        item_a_procurar = 1  # valor que se quer procurar
        random.shuffle(random_numbers1)   # reorganiza a ordem dos elementos
        for n in random_numbers1:
            self.ins_end(n)  # chama o método ins_end(item)
        tic = time.perf_counter()  # retorna o valor decimal do tempo do tic
        self.existe_linear_search(item_a_procurar)  #  # chama o método
        # existe_linear_search(item)
        tac = time.perf_counter()  # retorna o valor decimal do tempo do tac
        self.limpar()  # chama o método limpar()
        return tac - tic

    # pesquisa binária

    # encontrar o meio

    def find_middle(self, beginning, end):
        if beginning is None:  # lista vazia
            return None

        slow_pointer = beginning  # ponteiro para o primeiro nó
        fast_pointer = beginning.next  # ponteiro para o nó depois do primeiro nó

        while fast_pointer != end:  # enquanto fast_pointer diferente do último nó

            fast_pointer = fast_pointer.next  # percorre a lista
            if fast_pointer != end:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next

        return slow_pointer

    def existe_binary_search(self, item, sort_method='m'):

        # Bubble Sort

        if sort_method == 'b' or sort_method == 'B':
            self.ordenar_bubble_sort()

        # Merge Sort

        elif sort_method == 'm' or sort_method == 'M':
            self.__head = self.ordenar_merge_sort(self.__head)

        # método mais eficaz

        else:
            print("Método de ordenação não identificado. Merge Sort será utilizado")
            self.__head = self.ordenar_merge_sort(self.__head)

        start = self.__head
        end = None
        start_pos = 1  # começa no início
        end_pos = self.__len__()  # acaba quando atingue o tamanho da lista
        while True:
            middle = self.find_middle(start, end)  # vai buscar o método find_middle
            middle_pos = (start_pos + end_pos) // 2  # como calcular middle_pos

            if middle is None:  # se lista vazia
                return 0
            if middle.data == item:  # se valor igual ao item
                return middle_pos

            if middle.data < item:  # valor menor que item
                start = middle.next
                start_pos = middle_pos + 1
            else:  # valor maior que item
                end = middle
                end_pos = middle_pos - 1

            if not (end is None or end != start):
                break
        return "0 - Devolve zero porque o item não foi encontrado"

    # este método serve para não retornar nada ao ser feita a complexidade dos searchers(),
    # ou seja, este método tem o mesmo intuito do existe(item) mas não irá dar print a nada na tela

    def existe_linear_search(self, item):
        position = 0  # começa na posição 0
        if self.__head is None:  # lista vazia
            print("A lista está vazia!")
        else:  # lista com nós
            pointer = self.__head
            while pointer:  # enquanto a lista não acaba
                position += 1
                if pointer.data == item:  # se o valor do nó é igual ao item
                    break
                if pointer == self.__tail:  # se não tem o item procurado
                    break
                pointer = pointer.next  # percorre a lista


# teste - lista duplamente ligada circular
if __name__ == '__main__':
    lsta = ListaDLC()
    lsta.ins_end(2)
    lsta.ins_end(9)
    lsta.ins_end(7)
    print(lsta)
    lsta.existe(2)
    print(lsta.existe_binary_search(2, 'm'))
    #print(lsta)
    #lsta.ordenar_('b')
    #print(lsta)
    #lsta.rem(1)
    #print(lsta)
    #print(lsta.__len__())
    #lsta.ver(-7)
    #lsta.existe(2)