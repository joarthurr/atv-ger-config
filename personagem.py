class Personagem:
    def __init__(self, nome, vida_maxima):
        self.nome = nome
        self.vida = vida_maxima
    
    def receber_dano(self, dano):
        self.vida -= dano
        
        if (self.vida <= 0):
            print(f"{self.nome} recebeu {dano} de dano!\n{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano!\nVida restante: {self.vida}")

    def atacar(self):
        print(f"{self.nome} atacou!")

class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima, forca):
        super().__init__(nome, vida_maxima)
        self.forca = forca

    def atacar(self, forca):
        print(f"{self.nome} atacou!\nCausou {self.forca} de dano!")

class Mago(Personagem):
    def __init__(self, nome, vida_maxima, mana):
        super().__init__(nome, vida_maxima)
        self.mana = mana

    def atacar(self):
        if (self.mana >= 10):
            self.mana -= 10
            print(f"{self.nome} conjura uma bola de fogo!\nMana restante: {self.mana}")
        else:
            print(f"{self.nome} tenta conjurar uma magia, mas está sem mana!")

#NÃO SEI SE TÁ FUNCIONANDO, MAS NÃO PRECISA FUNCIONAR, BASTA ESTAR LÁ.

    