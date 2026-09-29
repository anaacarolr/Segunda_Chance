from quarto_hotel import QuartoHotel, lista_quartos

quarto_hotel = QuartoHotel

while True:
    print("\n1 - Quartos disponíveis")
    print("2 - Quartos que permitem pets")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        for q in lista_quartos:
            if q.disponivel == True:
                q.apresentar()

        escolha = input("Número do quarto para usar: ")
        for q in lista_quartos:
            if q.numero == escolha:
                q.disponivel = False  # Muda o valor para False
                print(f"\nO quarto {q.numero} agora está sendo usado!")
                print(f"Status: {q._disponivel()}")

    elif opcao == '2':
        for q in lista_quartos:
            if q._pets_permitidos == True:
                q.apresentar()

    elif opcao == '3':
        break

