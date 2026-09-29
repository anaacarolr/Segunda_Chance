class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False, salario=0):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = float()

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Código: {self.codigo}")
        print(f"Estudando: {self.estudando}")
        print(f"Trabalhando: {self.trabalhando}")
        print(f"Sálario: {self.salario}")
        print("......................")
        print("")

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += (100)
            print(f'{self.nome} Começou a trabalhar')
        else:
            print(f'{self.nome} Já esta trabalhando')

    def estudar(self):
        if self.trabalhando == True:
            print('Já esta estudando')
            if self.trabalhando == True:
                self.salario = (self.salario)
                print(f'{self.nome} recebeu')
        else:
            self.estudando = True
            print('Estudando')


p1 = Pessoa("Júlia", '2008/12/18', 'JJK')
p2 = Pessoa("Ana", '2008/11/15' , 'AAB', estudando=True, trabalhando=False)
p3 = Pessoa("Geovana", '2008/10/28' , 'GGT')
p4 = Pessoa("Carol", '2009/05/11', 'AAC')
p5 = Pessoa("Hugo", '2008/29/02', 'HHH')
p6 = Pessoa(data_nascimento='2008/06/08', nome='João', codigo='JJP', estudando=True, trabalhando=False)

p1.apresentar()
p2.apresentar()
p3.apresentar()
p4.apresentar()
p5.apresentar()
p6.apresentar()

p1.trabalhar()
p1.estudar()