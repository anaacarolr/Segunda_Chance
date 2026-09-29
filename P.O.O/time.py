
class Time:  # class começa com letra maiuscula
    def __init__(self, jogadores, treinador, esporte, nome, genero, jogando=True, treinando=False):
        self.jogadores = jogadores
        self.treinador = treinador
        self.esporte = esporte
        self.nome = nome
        self.genero = genero
        self.jogando = jogando
        self.treinando = treinando

    def apresentar(self):
        print(f"quantidade de jogadores: {self.jogadores}")
        print(f"Treinador: {self.treinador}")
        print(f"Nome do esporte : {self.esporte}")
        print(f"Nome do time: {self.nome}")
        print(f"Gênero dos jogadores do esporte: {self.genero}")
        print("......................")
        print("")

    def jogar(self):
        # alterar status de trabalho
        if self.jogando == True:
            print("jogando")
        else:
            if self.treinando == False:
                print(" está jogando")

    def treinar(self):
        # alterar status de trabalho
        if self.treinando == True:
            print("treinando")
        else:
            if self.jogando == False:
                print(" está treinando")


t1 = Time("7", 'Alonso', 'futsal', 'sesi237', 'masculino', jogando=True, treinando=False)
t2 = Time("12", 'Anderson', 'volei', 'praia-clube', 'feminino', jogando=True, treinando=False)

t1.jogar()
t2.jogar()

t1.treinar()
t2.treinar()

t1.apresentar()
t2.apresentar()
