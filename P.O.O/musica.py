class Musica:
    def __init__(self, nome, cantor, genero, data_lancamento, album, tocando=True, pausando=False):
        self.nome = nome
        self.cantor = cantor
        self.genero = genero
        self.data_lancamento = data_lancamento
        self.album = album
        self.tocando = tocando
        self.pausando = pausando

    def apresentar(self):
        print(f"nome: {self.nome}")
        print(f"cantor: {self.cantor}")
        print(f"genero: {self.genero}")
        print(f"data_lancamento: {self.data_lancamento}")
        print(f"abum: {self.album}")
        print(f"pausar: {self.pausando}")
        print(f"tocar: {self.tocando}")
        print("-" * 20)

    def tocar(self):
        if self.tocando == True:
            print('Tocando')
        else:
            if self.pausando == False:
                print('Está pausado')
        print("-" * 20)

    def pausar(self):
        if self.pausando == True:
            print('Pausado')
        else:
            if self.tocando == False:
                print('está tocando')
        print("-" * 20)


m1 = Musica("wanna be yours", 'artic monkeys', 'romantica', '1982', 'AM', tocando=True, pausando=True)
m2 = Musica("friends", 'chase atlantic', 'pop rock', '2015', 'Phases', tocando=False, pausando=True)
m3 = Musica("one kiss", 'Dua Lipa', 'romantica', '2018', 'Dua Lipa: Complete Edition ', tocando=False, pausando=False)

m1.tocar()
m2.tocar()
m3.tocar()

m1.pausar()
m2.pausar()
m3.pausar()

m1.apresentar()
m2.apresentar()
m3.apresentar()