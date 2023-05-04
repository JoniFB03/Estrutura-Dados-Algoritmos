from Cliente import * # importação do ficheiro com a classe Cliente


# criação da fila de espera, quer a global, quer as das secções
class Fila:
    def __init__(self):
        # lista da fila de espera global (clientes das três secções)--> métodos são todos a partir desta fila
        self.__data=[]
        # lista de clientes da secção RC
        self.__rc=[]
        # lista de clientes da secção RP
        self.__rp = []
        # lista de clientes da secção QC
        self.__qc = []

    # inserção de um cliente, não prioritário, à fila de espera global
    def insert_client(self,client):
        if not client.p:
            self.__data.append(client)
        else:
            print('O cliente é prioritário!')

    # inserção de um cliente, prioritário à fila de espera global; clientes prioritários adicionados vão para trás dos
    # clientes prioritários que já estão na fila através de um iterador
    def insert_p_client(self, client):
        iter=0
        if client.p:
            if self.is_empty():
                self.__data.append(client)
            else:
                for i in self.__data:
                    if i.p:
                        iter+=1
                inicio=self.__data
                self.__data=self.__data[:iter]
                self.__data.append(client)
                self.__data+=inicio[iter:]
        else:
            print('O cliente não é prioritário!')

    # atender o próximo cliente da fila global
    def serve_client(self):
        if self.is_empty():
            print('\033[91Não há ninguém na fila de espera!\033[0m')
        else:
            self.__data.pop(0)

    # ver o próximo cliente da fila global
    def view_next_client(self):
        if self.is_empty():
            print('\033[91mFila vazia!\033[0m')
        else:
            print (self.__data[0])

    # abandonar lugar na fila global, dada qualquer posição na fila
    def abandon_queue(self, index):
        if index > len(self.__data) or index<=0:
            print('\033[91mA fila não atinge este valor\033[0m')
        else:
            self.__data.pop((index)-1) # index é visto como o primeiro cliente da fila sendo index=1
            print(f'\033[92mCliente da posição\033[0m *{index}* \033[92mretirado com sucesso!\033[0m')

    # fechar a fila sem exportar qualquer ficheiro; perdem-se os clientes lá colocados
    def close(self):
        self.__data = []

    # verificar se a fila está vazia
    def is_empty(self):
        return len(self.__data) == 0

    # tamanho da fila global
    def __len__(self):
        return len(self.__data)

    # visualizar fila global
    def __str__(self):
        lst1=[]
        traco="="*len(self.__data*25)
        proximo=" "*7+"<----- Próximo cliente inserido nesta direção"
        for idx, j in enumerate(self.__data): # comando *enumerate()* para enumerar os clientes à sua posição na fila
                lst1.append((f'{idx + 1}|{j.n}- [{j.s}]'))
        if len(self.__data)!=0:
            return f'{traco}|\n \033[94m Fila de espera:\033[0m  \n{lst1} {proximo}\n{traco}|'
        else:
            return f'=================|\n \033[94m Fila de espera:\033[0m  \n\033[91mFila vazia!\033[0m{proximo}\n' \
                   f'=================|'

    # ver se o número dado já está associado a um cliente na fila
    def numero_repetido(self,numero):
        for i in self.__data:
            if str(numero) == str(i.c):
                return True
        return False

    # método para adicionar às filas das secções os clientes da fila global
    def seccoes(self):
        self.__rc=[]
        self.__rp=[]
        self.__qc=[]
        for i in self.__data:
            if i.s=="RC":
                self.__rc.append(i)
            elif i.s=="RP":
                self.__rp.append(i)
            elif i.s=="QC":
                self.__qc.append(i)

        print('\n\033[96mSecção da [RC]-Criação / Renovação do cartão de cidadão:\033[0m')
        for idx1,i1 in enumerate(self.__rc):
                print(f'{idx1+1}|{i1.n}')

        print('\n\033[96mSecção da [RP]-Criação / Renovação do passaporte:\033[0m')
        for idx2,i2 in enumerate(self.__rp):
                print(f'{idx2+1}|{i2.n}')

        print('\n\033[96mSecção das [QC]-Questões judiciais:\033[0m')
        for idx3,i3 in enumerate(self.__qc):
                print(f'{idx3+1}|{i3.n}')
        print('\n'+'='*56)

    # importar os clientes do ficheiro "clientes.txt" para a fila global; caso a fila global não estiver vazia este
    # método não irá transportar os clientes do ficheiro (ordem ficaria desorganizada)
    def importar_ficheiros(self):
        arquivo = open("clientes.txt", "r")
        if self.is_empty():
            for linha in arquivo:
                linha_limpa=linha.strip()
                atributos = linha_limpa.split(",")
                add=Cliente(atributos[0],atributos[1],atributos[2],atributos[3])
                self.__data.append(add)
            open("clientes.txt","w")
            arquivo.close()
        else:
            print('\033[91mFila não está vazia! *É necessário a fila estar vazia para importar os clientes*\033[0m')

    # exportação de todos os clientes da fila global para o ficheiro "clientes.txt"
    def exportar_ficheiros(self):
        arquivo = open("clientes.txt", "w")
        for i in self.__data:
            arquivo.write(str(i)+'\n')
        self.close()
        arquivo.close()


