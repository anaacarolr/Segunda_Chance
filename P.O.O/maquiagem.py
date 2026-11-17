class Maquiagem:
    def __init__(self, marca, modelo, tamanho, nome, valor, textura, validade):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        self.valor = valor
        self.textura = textura
        self.validade = validade

    def apresentar(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tamanho do produto: {self.tamanho}")
        print(f"Valor do produto: {self.valor}")
        print(f"Textura: {self.textura}")
        print(f"Validade: {self.validade}")
        print("......................")
        print("")

m1 = Maquiagem(" Sephora Collection", 'Batom', '5 ml', 'Lip Blush','89,00.','Mousse (chantilly) ','6 a 12 meses após a abertura')
m2 = Maquiagem(' Mari Maria Makeup','Blush','10g','Sunny Cheeks','50,00', 'Em pó','2 anos')
m3 = Maquiagem("Ruby Rose", 'Iluminador' , '6,5g','Baked Crystal Glow','26,99.','Baked (Assado)','08/2029')

m1.apresentar()
m2.apresentar()
m3.apresentar()