class Celular:
    def __init__(self, marca, ano, cor, modelo, armazenamento, preco, data_lancamento,ligando=True, jogando=True, assistindo=False):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.data_lancamento = data_lancamento
        self.armazenamento = armazenamento
        self.preco = preco
        self.ligando = ligando
        self.assistindo = assistindo
        self.jogando = jogando


    def apresentar(self):
        print(f"Marca: {self.marca}")
        print(f"Cor: {self.cor}")
        print(f"Armazenamento: {self.armazenamento}")
        print(f"Modelo: {self.modelo}")
        print(f"Data de lançamento: {self.data_lancamento}")
        print(f"Preço: {self.preco}")
        print(f"ligar: {self.ligando}")
        print(f"jogar: {self.jogando}")
        print(f"assistir: {self.assistindo}")

        print("-" * 20)

    def ligar(self):
        if self.ligando == True:
            print('Ligando')
        else:
            print('Desligado')
        print("-" * 20)

    def jogar(self):
        if self.jogando == True:
            print('jogando')
        else:
            if self.assistindo == False:
                print('está assistindo')
        print("-" * 20)

    def assistir(self):
        if self.assistindo == True:
            print('assistindo')
        else:
            if self.jogando == False:
                print('está jogando')
        print("-" * 20)

c1 = Celular("Sansung", 'Preto', '128GB', 'A55', '1980', '900', '2020' )
c2 = Celular("Iphone", 'Branco', '128GB', 'Iphone 15', '2000', '1600', '2012' )
c3 = Celular("Motorola", 'Azul', '128GB', 'moto G84', '1990', '1300','2015' )

c1.apresentar()
c2.apresentar()
c3.apresentar()