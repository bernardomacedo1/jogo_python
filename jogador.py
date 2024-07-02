from atributos import atributos 
from utils import printl, printll

class jogador:

    def __init__(self, nome):
        self.nome = nome
        self.atributos = atributos()
        self.vida = self.atributos.vida_base
        self.dano = self.atributos.dano_base
        self.critico = self.atributos.chance_critico
        self.esquiva = self.atributos.chance_esquiva
        self.bloqueando = False
        self.ataque_primeiro = False
        self.inventario = []

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Vida: {self.vida}\n"
                f"Dano: {self.dano}\n"
                f"Atributos:\n{self.atributos}\n"
                f"Inventário: {', '.join(self.inventario)}")

    def configurar_jogador(self):
        print(" - Destreza: Aumenta a chance de ataques críticos e de desviar de ataques\n")
        print(" - Força: Aumenta a vida base e o dano base\n")
        print(" - Percepção: Aumenta a chance de encontrar itens")
        print("   Além de ajudar a atacar inimigos de surpresa.\n")
        input("Pressione enter para continuar\n")
        printll("DICA: não deixe nenhum atributo vazio!\n")

        pontos = 10
        while pontos > 0:
            print(f"Pontos restantes: {pontos}\n")

            destreza = int(input("Quantos pontos deseja adicionar em Destreza? "))
            if 0 <= destreza <= pontos:
                self.atributos.adicionar_destreza(destreza)
                pontos -= destreza
            else:
                print("Valor inválido. Tente novamente.")

            if pontos == 0:
                break

            força = int(input("Quantos pontos deseja adicionar em Força? "))
            if 0 <= força <= pontos:  
                self.atributos.adicionar_força(força)
                pontos -= força
            else:
                print("Valor inválido. Tente novamente.")

            if pontos == 0:
                break

            percepção = int(input("Quantos pontos deseja adicionar em Percepção? "))
            if 0 <= percepção <= pontos:  
                self.atributos.adicionar_percepção(percepção)
                pontos -= percepção
            else:
                print("Valor inválido. Tente novamente.")


            self.vida = self.atributos.vida_base
        self.dano = self.atributos.dano_base
        

        self.critico = self.atributos.chance_critico
        self.esquiva = self.atributos.chance_esquiva
        
        printll("\nAtributos atualizados:")
        print(self)
        printl("\n")

    def recompensa_pontos(self, pontos):
        while pontos > 0:
            print(f"Pontos restantes: {pontos}")
            print("1. Destreza")
            print("2. Força")
            print("3. Percepção")
            escolha = input("Escolha o atributo para aumentar: ")

            if escolha == '1':
                self.atributos.adicionar_destreza(1)
            elif escolha == '2':
                self.atributos.adicionar_força(1)
            elif escolha == '3':
                self.atributos.adicionar_percepção(1)
            else:
                print("Escolha inválida.")
                continue

            pontos -= 1
        printll("\nAtributos atualizados:")
        print(self)
        printl("\n")
        
    def ArmaduraEscamas(self):
        self.atributos.adicionar_força(1)
        
    def ColarPresas(self):
        self.atributos.adicionar_destreza(1)
        self.atributos.adicionar_percepção(1)
