import random
from inimigos import Froglin

def combate(jogador, inimigo):
    while jogador.vida > 0 and inimigo.vida > 0:
        print("Escolha sua ação (atacar/bloquear): ")
        print("1. Atacar")
        print("2. Bloquear")
        acao_jogador = input("").lower()
        #ação de ataque
        if acao_jogador == '1':
            
            if random.random() < jogador.atributos.chance_critico:
                dano = jogador.dano * 3
                print("Ataque crítico!")
                
            else:
                dano = jogador.dano
            inimigo.vida -= dano
            print(f"Você causou {dano} de dano ao {inimigo.nome}.\n")
        #acão de bloqueio
        elif acao_jogador == '2':
            jogador.bloqueando = True
            print("Você se prepara para bloquear o próximo ataque.\n")

        if inimigo.vida <= 0:
            print("Você venceu o combate!")
            break

        acao_inimigo = inimigo.acao()
        if acao_inimigo == 'ataque':
            dano = inimigo.dano
        elif acao_inimigo == 'ataque poderoso':
            dano = inimigo.dano * 2
            print(f"{inimigo.nome} está carregando um ataque poderoso!")
            continue

        if jogador.bloqueando:
            dano = inimigo.dano
            dano /= 2
            jogador.bloqueando = False
            print("Você bloqueou parte do dano!\n")
        dano = inimigo.dano
        jogador.vida -= dano
        print(f"{inimigo.nome} causou {dano} de dano a você.\n")

    if jogador.vida <= 0:
        print("Você foi derrotado.")
    