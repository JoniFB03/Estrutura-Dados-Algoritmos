# criação da classe Cliente
class Cliente:
    def __init__(self, nome_completo, n_cartao, seccao, prioridade=False):

        self.n = nome_completo
        self.c = n_cartao
        self.s = seccao
        # parâmetro do tipo booleano
        self.p = prioridade



    ## consulta dos parâmetros de um objeto do tipo Cliente (apenas experimental)

    def nome_completo(self):
        return self.n

    def n_cartao(self):
        if len(self.c) != 8 or len(self.c) != 9:
            raise ValueError('O número de identificação deve ter 8 números')
        return self.c

    def seccao(self):
        return self.s

    def prioridade(self):
        return self.p

    # criação da string relativa ao objeto do tipo Cliente
    def __str__(self):
        return f'{self.n},{self.c},{self.s},{self.p}'





