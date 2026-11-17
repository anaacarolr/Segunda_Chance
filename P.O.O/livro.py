class Livro:
    def __init__(self, nome, autor, data_lancamento, genero, material, idioma_original, abrir=True, lendo=True):
        self.nome = nome
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.genero = genero
        self.material = material
        self.idioma_original = idioma_original
        self.abrir = abrir
        self.lendo = lendo

    def apresentar(self):
        print(f"Nome do livro: {self.nome}")
        print(f"Autor do livro: {self.autor}")
        print(f"Data de lançamento : {self.data_lancamento}")
        print(f"Gênero: {self.genero}")
        print(f"Material do livro: {self.material}")
        print(f"Idioma original: {self.idioma_original}")
        print(f"Abrir: {self.abrir}")
        print(f"Lendo: {self.lendo}")
        print("......................")
        print("")

        def abrir(self):
            if self.abrir:
                self.abrir = True
                print(f'{self.nome} Livro esta abrindo')
            else:
                print(f'{self.nome} Livro não esta abrindo')

        def lendo(self):
            if self.lendo:
                self.lendo = True
                print(f'{self.nome} Lendo livro')
            else:
                print(f'{self.nome} Não estou lendo')

l1 = Livro("Alice no País das Maravilhas", 'DarkSide Books', '4 de outubro de 2019','Fantasia','Capa dura','Português '  )
l2 = Livro("Coraline", 'Neil Gaiman', '2 de julho de 2002', 'Conto de fadas','Capa dura','Inglês' )
l3 = Livro("Vermelho, Branco e Sangue Azul", 'Casey McQuiston', '14 de maio de 2019', 'Literatura LGBT','Brochura','Português ')

l1.apresentar()
l2.apresentar()
l3.apresentar()

