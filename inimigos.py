import random


class Froglin:

    def __init__(self):
        self.nome = "Froglin"
        self.vida = 45
        self.dano = 4
        self.poderoso_chance = 0.45

    def acao(self):
        if random.random() < self.poderoso_chance:
            return 'ataque poderoso'
        else:
            return 'ataque'

class Monstro:

    def __init__(self):
        self.nome = "Monstro"
        self.vida = 40
        self.dano = 5
        self.poderoso_chance = 0.30

    def acao(self):
        if random.random() < self.poderoso_chance:
            return 'ataque poderoso'
        else:
            return 'ataque'
        
class Guarda:

     def __init__(self):
         self.nome = "Guarda"
         self.vida =  20
         self.dano = 3
         self.poderoso_chance = 0.30
         
     def acao(self):
        if random.random() < self.poderoso_chance:
            return 'ataque poderoso'
        else:
            return 'ataque'
        
class Velho:

     def __init__(self):
         self.nome = "Velho"
         self.vida =  40
         self.dano = 5
         self.poderoso_chance = 0.30
         
     def acao(self):
        if random.random() < self.poderoso_chance:
            return 'ataque poderoso'
        else:
            return 'ataque'