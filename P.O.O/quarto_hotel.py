class QuartoHotel:
    def __init__(self, numero, tipo, preco, andar, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.andar = andar
        self._disponivel_valor = disponivel

    def disponivel(self):
        if self._disponivel_valor == True:
            return "Quarto está disponível"
        else:
            return "Quarto já está ocupado"


    def apresentar(self):
        print(f"Número do quarto: {self.numero}")
        print(f"Tipo do quarto: {self.tipo}")
        print(f"Preço do quarto : {self.preco}")
        print(f"Andar do quarto: {self.andar}")
        print(f"Disponibilidade do quarto: {self.disponivel}")
        print("......................")


q1 = QuartoHotel('1', 'Luxo', 'R$3.500', '1', disponivel=True)
q2 = QuartoHotel('2', 'Standard', 'R$300,00.', '1')
q3 = QuartoHotel('3', 'Deluxe', 'R$620,00', '1')
q4 = QuartoHotel('4', 'Suíte', 'R$450,00', '2')
q5 = QuartoHotel('5', 'Luxo', 'R$3.700', '2')
q6 = QuartoHotel('6', 'Standard', 'R$300,00.', '2')
q7 = QuartoHotel('7', 'Deluxe', 'R$620,00', '3')
q8 = QuartoHotel('8', 'Suíte', 'R$450,00', '3')
q9 = QuartoHotel('9', 'Luxo', 'R$4.000', '3')

lista_quartos = [q1, q2, q3, q4, q5, q6, q7, q8, q9]

while True:
    print("OLÁ, bem vindo ao hotel 5 Estrelas!!")
    print("Escoha uma opção!")
    print("")
    print("1 - Quartos disponíveis")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        print(" DISPONÍVEIS ")
        for q in lista_quartos:
            if q._disponivel_valor == True:
                q.apresentar()

        num = input("Escolha o número do quarto para usar: ")
        for q in lista_quartos:
            if q.numero == num:
                q._disponivel_valor = False
                print(f"Quarto {q.numero} no andar {q.andar} agora está sendo usado!")
                print(f"Status: {q.disponivel}")

    elif opcao == '3':
        break
