class atributos:
    def __init__(self, destreza=0, força=0, percepção=0):
        self.destreza = destreza
        self.força = força
        self.percepção = percepção

    def adicionar_destreza(self, pontos):
        self.destreza += pontos

    def adicionar_força(self, pontos):
        self.força += pontos

    def adicionar_percepção(self, pontos):
        self.percepção += pontos

    @property
    def chance_critico(self):
        return self.destreza * 0.06

    @property
    def chance_esquiva(self):
        return self.destreza * 0.04

    @property
    def vida_base(self):
        return self.força * 3.5

    @property
    def dano_base(self):
        return self.força * 2 

    @property
    def chance_percepção(self):
        return self.percepção * 0.05

    def __str__(self):
        return (
            f"Destreza: {self.destreza} (Chance Crítico: {self.chance_critico*100}%, Chance Esquiva: {self.chance_esquiva*100}%)\n"
            f"Força: {self.força} (Vida Base: {self.vida_base}, Dano Base: {self.dano_base})\n"
            f"Percepção: {self.percepção} (Chance Percepção: {self.chance_percepção*100}%)"
        )
