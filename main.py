import random
from combate import combate
from inimigos import Froglin, Guarda, Monstro, Velho
from jogador import jogador
from utils import printl, printll

final = 0
escolha_caminho = 0
escolha_do_velho = 0
escolha_final = 0
def teste_habilidade(habilidade, dificuldade):
    return random.randint(1, 10) + habilidade >= dificuldade


def cena_cidade():
    printl("\nVocê enxerga ao longe uma vila, e se apressa") 
    printl("Você anceia por respostas, e comida...")
    printl("Chegando na vila, algo te assusta: é uma vila de Froglins!\n")
    printll("Mas...")
    printl("eles parecem não se importar com a sua presença")
    printl("Eles falam uma língua que você não entende.\n")
    printl("Na praça central, você vê uma lojinha à esquerda e um templo mais a frente.")
    printl("Parecem os únicos lugares abertos ao público")

    while final == 0:
        printl("\nO que você deseja fazer?\n")
        print("1. Ir para a lojinha")
        print("2. Ir para o templo")


        escolha_cidade = input("Digite o número da sua escolha: ")

        if escolha_cidade == "1":
            interacao_lojinha()
        elif escolha_cidade == "2":
            interacao_templo()
        else:
            printl("Escolha inválida. Digite um número de 1 a 3.")
            return

def interacao_lojinha():
    printl("\nVocê entra na lojinha dos Froglin. O lojista te observa com curiosidade, mas não diz nada.")
    if "Moeda Estranha" in jogador.inventario:
        printl("Sabendo que vocês não compartilham um idioma, você se lembra da moeda que conseguiu...")
        printl("Você mostra a Moeda Estranha para o lojista.")
        printl("Ele faz um gesto de entendimento e mostra dois itens sobre o balcão:\n")
        
        print("1. Armadura de Escamas")
        print("2. Colar de Presas")
        print("3. Voltar para a praça da cidade")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            printl("\nVocê troca a Moeda Estranha pela Armadura de Escamas.")
            jogador.inventario.append("Armadura de Escamas")
            jogador.inventario.remove("Moeda Estranha")
            jogador.ArmaduraEscamas()
        elif escolha == "2":
            printl("\nVocê troca a Moeda Estranha pelo Colar de Presas.")
            jogador.inventario.append("Colar de Presas")
            jogador.inventario.remove("Moeda Estranha")
            jogador.ColarPresas()
        elif escolha == "3":
            printl("\nVocê decide não trocar a Moeda Estranha por nada.")
        else:
            printl("\nEscolha inválida.")
    else:
        printl("Sem saber o que dizer, você sai da loja e retorna à praça")

def interacao_templo():
    global escolha_do_velho
    global final
    printl("\nVocê entra no templo dos Froglin. Há um sacerdote à frente, que te cumprimenta com respeito.")
    printl("Ele fala a sua língua, surpreendendo você.\n")
    printl("'O que houve jovem? tem algo te preocupando?'\n")

    printl("Você decide contar ao sacerdote o que aconteceu?\n")
    print("1. Sim, revelar a verdade")
    print("2. Não, manter segredo")
    print("3. Voltar para a praça\n")

    escolha = input("Digite o número da sua escolha: ")

    if escolha == "1":
        printl("\nVocê revela ao sacerdote que foi enjaulado por um Froglin.")
        printl("O sacerdote parece sério por um momento, então ele sorri gentilmente.")
        printl("Ele leva você até um espelho antigo no fundo do templo.")
        printl("Olhe no espelho, jovem.")
        printl("\nVocê olha no espelho e vê sua reflexão como um Froglin.")
        printl("O sacerdote fala com seriedade:")
        printl("'Você foi transformado em um de nós, agora está no caminho do Deus Sapo.'\n")
        printll("Um sentimento surge dentro de você, te impulsionando à... rezar...")
        rezar = input("Deseja rezar para o Deus Sapo? (s/n): ").lower()

        if rezar == "s":
            printl("\nVocê se ajoelha diante da estátua do Deus Sapo e começa a rezar.")
            printl("De repente, a estátua começa a tremer e se quebrar.")
            printl("De dentro da estátua emerge um monstro horrendo, você se prepara para se defender!")

            inimigo = Monstro()
            combate(jogador, inimigo)

            # Lógica após combate com o Monstro, se o jogador sobreviver
            if jogador.vida > 0:
                printl("\nOfegante, você se senta para recuperar o fôlego")
                printl("O sacerdote parece confuso, ele olha pra você com preocupação")
                printl("Você vê enquanto sua pele e rosto se transformam em um humano")
                printl("O que quer que seja esse templo, e esse bosque... Talvez o pesadelo tenha acabado.\n")
                printl("Fim!")
                final = 1

            else:
                printl("Você perde suas forças e cai no chão, o monstro olha dentro da sua alma")
                printl("Você escuta uma última vez uma voz familiar:\n")
                printl("'Seu destino é e sempre será dentro do bosque, jovem'")
                printl("A voz do velho caipira ecoa na sua cabeça. Você fecha os olhos.\n")
                printl("Fim!")
                final = 1
                
        else:
            printl("\nVocê decide não rezar. O sacerdote te observa com compreensão.")
            printl("Ele diz: 'Você tem um longo caminho pela frente. Que o Deus Sapo te guie.'")
            cena_ancião()

    elif escolha == "2":
        printl("\nVocê decide não revelar a verdade ao sacerdote.")
        printl("Ele olha para você com respeito, mas uma sombra de preocupação passa por seus olhos.")
        printl("'Eu sinto que você não está sendo sincero comigo, jovem.'")
        printll("Um sentimento surge dentro de você, te impulsionando à rezar...")
        rezar = input("Deseja rezar para o Deus Sapo? (s/n): ").lower()

        if rezar == "s":
            printl("\nVocê se ajoelha diante da estátua do Deus Sapo e começa a rezar.")
            printl("De repente, o sacerdote olha para a estátua com preocupação.")
            printl("Ele murmura algo e a estátua começa a tremer e se quebrar.")
            printl("De dentro da estátua emerge um monstro horrendo, você está em um combate contra o Monstro!")

            inimigo = Monstro()
            combate(jogador, inimigo)

            # Lógica após combate com o Monstro, se o jogador sobreviver
            if jogador.vida > 0:
                printl("\nOfegante, você se senta para recuperar o fôlego")
                printl("O sacerdote parece confuso, ele olha pra você com preocupação")
                printl("Você vê enquanto sua pele e rosto se transformam em um humano")
                printl("O que quer que seja esse templo, e esse bosque... Talvez o pesadelo tenha acabado.\n")
                printl("Fim!")
                final = 1
            else:
                printl("Você perde suas forças e cai no chão, o monstro olha dentro da sua alma")
                printl("Você escuta uma última vez uma voz familiar:\n")
                printl("'Seu destino é e sempre será dentro do bosque, jovem'")
                printl("A voz do velho caipira ecoa na sua cabeça. Você fecha os olhos.\n")
                printl("Fim!")
                final = 1
        else:
            printl("\nVocê decide não rezar. O sacerdote te observa com compreensão.\n")
            cena_ancião()
            

    elif escolha == "3":
        printl("\nVocê decide sair do templo.")
    else:
        printl("\nEscolha inválida.")

    # Verifica se o jogador escolheu não rezar

    if escolha == "1":
        pass 
    elif escolha == "2":
        pass
    elif escolha == "3":
        printl("\nVocê decide sair do templo.")
        
def cena_ancião():
    global final
    global escolha_do_velho
    printl("Ele diz: 'Você tem um longo caminho pela frente. Que o Deus Sapo te guie.'")
    printl("\n Um outro Froglin entra no templo, e o sacerdote o dá boas vindas")
    printl("Ele parece ser o ancião da vila, e o sacerdote está feliz em vê-lo")
    printl("Se tem alguém que vai lhe dar respostas concretas, é ele.")
    printl("\n Você espera eles entrarem no templo, e em silêncio se aproxima")
    printl("Os dois Froglins entram em uma sala, e você vê através da porta entreaberta:")
    printl("O ancião revela sua verdadeira forma, o velho caipira da prisão!")
    printl("Você não consegue se conter e se assusta, revelando sua localização")
    printl("Os seus olhares se encontram:")
    
    printl(f"'Ora, ora, se não é {nome}'")
    
    if escolha_do_velho == 1: 
        
        printl("\n'Vejo que você decidiu me soltar', diz o velho com um sorriso sardônico.")
        printl("'Você fez a escolha certa. Deixe-me explicar...'\n")
        printl("'Eu criei com sucesso uma raça superior, como você pode ver'")
        printl("'Eles não tem egoísmo,'")
        printl("\nEle oferece que você se junte a eles e viva em paz com os Froglin.")
        printl("Você decide:\n")
        print("1. Aceitar a oferta e viver com os Froglin")
        print("2. Rejeitar a oferta e confrontar o velho\n")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            printl("\nVocê decide aceitar a oferta do velho e viver com os Froglin.")
            printl("Ele te guia para dentro da sala onde revelou sua forma verdadeira.")
            printl("Você se junta a eles, esperando uma vida de paz no bosque.\n")
            printl("\nFim!")
            final = 1
        elif escolha == "2":
            printl("\nVocê decide rejeitar a oferta do velho e confrontá-lo.")
            combate(jogador, Velho())
            if jogador.vida > 0:
                printl("\nVocê derrota o velho, que cai derrotado no chão do templo.")
                printl("Você se sente aliviado, mas ainda confuso com tudo o que aconteceu.")
                printl("Talvez o bosque pode finalmente encontrar paz.")
                printl("\nFim!")
                final = 1
            else:
                printl("\nInfelizmente, o velho se mostra forte demais para você.")
                printl("Ele ri enquanto você cai derrotado no chão do templo.")
                printl("Seu destino permanece ligado ao bosque pútrido.")
                printl("\nFim!")
                final = 1
        else:
            printl("\nEscolha inválida. O velho ri da sua indecisão.")
            printl("Você percebe que suas escolhas são cruciais no bosque pútrido.")
            printl("\nFim!")
            final = 1

    elif escolha_do_velho == 2:
    
        printl("\n'O que é isso? É você? Eu vou garantir que pague por me deixar preso!'\n")
        printl("Você se prepara para se defender!\n")
        combate(jogador, Velho())

        if jogador.vida > 0:
            printl("\nVocê derrota o velho, que cai derrotado no chão do templo.")
            printl("Você se sente aliviado, mas ainda confuso com tudo o que aconteceu.")
            printl("Talvez o bosque pode finalmente encontrar paz.")
            printl("\nFim!")
            final = 1
        else:
            printl("\nInfelizmente, o velho se mostra forte demais para você.")
            printl("Ele ri enquanto você cai derrotado no chão do templo.")
            printl("Seu destino permanece ligado ao bosque pútrido.")
            printl("\nFim!")
            final = 1
        

    # Se perder a batalha contra o primeiro inimigo, o Froglin.
def cena_preso():
    global escolha_do_velho
    printl("\nVocê acorda em uma jaula, com gotas caindo no seu rosto\n")
    printl("Você descansou e recuperou suas forças\n")
    jogador.vida = jogador.atributos.vida_base
    printl("Você olha ao redor, e vê um guarda com chaves na cintura")
    printl("Ele patrulha sua jaula até o fim do corredor\n")
    
    if teste_habilidade(jogador.atributos.percepção, 7):
            printl("Percepção: você vê um baú no fim do corredor, talvez ele contém seus pertences\n")
    printl("Parece que existem duas maneiras de sair daqui:")
    printl("1. Desacordar o guarda (Teste de Força)")
    printl("2. Pegar as chaves (Teste de Destreza)\n")
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        printl("\nVocê tenta desacordar o guarda quando ele se aproxima")
        printll("...")
        if teste_habilidade(jogador.atributos.força, 7):
            printl("Sucesso! Você desacordou o guarda")
            printl("Você pega a chave do guarda desacordado e destranca sua jaula, e escuta a voz de um homem:\n")
        else:
            printl("\nO guarda é forte demais, e tenta revidar!")
            printl("Mas você escuta uma voz vindo de outra jaula")
            printl("\n'Toma seu vagabundo!!'\n")
            printl("Uma rocha atinge a cabeça do guarda e ele desmaia em frente a sua jaula")
            printl("O homem diz novamente:") 
             
    elif escolha == "2":
        printl("Você tenta pegar as chaves quando ele se aproxima")
        printll("...")
        if teste_habilidade(jogador.atributos.destreza, 7):
            printl("Sucesso! Você pegou as chaves")
            printl("Você destranca sua jaula sem o guarda perceber, e escuta a voz de um homem")
            printl("Ele diz o mais baixo possível para não chamar atenção do guarda:\n")
        else:
            printl("\nO guarda é forte demais, e tenta revidar!")
            printl("Mas você escuta uma voz vindo de outra jaula")
            printl("\n'Toma seu vagabundo!!'\n")
            printl("Uma rocha atinge a cabeça do guarda e ele desmaia em frente a sua jaula")
            printl("O homem diz novamente:") 
#escolha de soltar o velho ou não
    printl("\n'Pega essas chave e vamo da no pé daqui!!'\n")
    printl("Você vê um senhor de idade com chapéu de palha enjaulado\n")
    printl("Após você se libertar, o senhor diz:")
    printl("\n Destranca minha jaula! eu sei a saída!")
    printl("1. Soltar o velho")
    printl("2. Não soltar o velho\n")
    escolha = input("Digite o número da sua escolha: ")
    if escolha == "1":
        escolha_do_velho = 1
        escolha_final = 1
        printl("Você decide soltá-lo\n")
        printl("'Muito obrigado jovem, me siga e eu te mostro a saída'")
    elif escolha == "2":
        escolha_do_velho = 2
        escolha_final = 1
        printl("Você decide não soltá-lo...\n")
        printl("Eu te amaldiçoo jovem! Você não vai sair daqui!")
#Continuação antes do combate contra guarda, depois da escolha do velho
    printl("Você continua pelo corredor, a única saída visível.")
    printl("Apenas uma tocha no final de alguns lances de escada iluminam seu caminho")
    printl("Enquanto você sobe, você escuta passos em sua direção\n")
    printl("'Você não vai a lugar nenhum, criatura nojenta!'\n")
    printl("Um guarda aponta uma espada em sua direção, você se prepara para se defender\n")
    
def escolher_caminho():
    print("1. Passar pela ponte")
    print("2. Escalar a árvore")
    print("3. Nadar pelo rio")

    escolha_caminho = input("Digite o número da sua escolha: ")
    if escolha_caminho == "1":
        printl("Você pisa com cautela nas tábuas velhas da ponte")
        printl("Parece que algo está se emergindo da água, você se prepara para se defender")
        printl("Um humanóide sapo pula para a ponte, e aponta uma lança em sua direção!\n")
        
        if teste_habilidade(jogador.atributos.percepção, 7):
            printl("Percepção: Você percebe algo no bolso do Froglin. Se ganhar o combate, receberá Moeda Estranha")
            jogador.inventario.append("Moeda Estranha")
            
    elif escolha_caminho == "2":
        printl("Você começa a escalar a árvore mais próxima do rio")
        printl("A seiva da árvore parece brilhar, e é quente, você tenta não encostar\n")
        
        if teste_habilidade(jogador.atributos.percepção, 7):
            printl("Percepção: Você encontrou uma 'Moeda Estranha' durante a escalada.")
            jogador.inventario.append("Moeda Estranha")
            printl("Fruta Estranha foi adicionada ao seu inventário\n")
            
        printl("Ao chegar no topo, você consegue pular para outra árvore, do outro lado do rio")
        printl("Quando você começa a descer em segurança, algo se emerge da água")
        printl("Um humanóide sapo pula para a ponte, e aponta uma lança em sua direção!\n")
            
        if teste_habilidade(jogador.atributos.percepção, 7):
            printl("Percepção: Você ataca o inimigo primeiro!")
            jogador.ataque_primeiro = True
        else:
            printl("O inimigo ataca primeiro.")
            jogador.ataque_primeiro = False
            
    elif escolha_caminho == "3":
        printl("Por algum motivo, você acha que a escolha correta é nadar pelo rio esquisito")
        
        if teste_habilidade(jogador.atributos.percepção, 7):
            printl("Percepção: Você encontrou uma 'Moeda Estranha' durante a travessia.")
            jogador.inventario.append("Moeda Estranha")
            printl("Moeda Estranha foi adicionada ao seu inventário")
            
        printl("Você termina a natação e começa a se secar do outro lado, mas algo se emerge da água")
        printl("Um humanóide sapo pula para a ponte, e aponta uma lança em sua direção!\n")
            
        if teste_habilidade(jogador.atributos.percepção, 7):
            print("Percepção: Você ataca o inimigo primeiro!")
            jogador.ataque_primeiro = True
        else:
            print("O inimigo ataca primeiro.")
            jogador.ataque_primeiro = False
            
    # O JOGO COMEÇA AQUI


printl("Mistério do Bosque Pútrido\n")
nome = input("Digite o nome do seu personagem: ")
jogador = jogador(nome)

printl(f"Você não se lembra de nada... apenas seu nome, {nome}")
printl("Você abre os olhos e se encontra em um bosque escuro")
printl("Você se levanta...\n")
printl("As árvores têm formatos estranhos, e suas folhagens cobrem o céu")
printl("Um cheiro pútrido estranhamente forte invade seus pulmões")
printl("Tem algo de errado com esse bosque...\n")
printl("Você tenta se lembrar de quem você é...\n")

jogador.configurar_jogador()

printl("\nVocê enxerga uma luz bem distante, se ofuscando entre as árvores")
printl("Parece que é a única fonte de luz do bosque, como um farol, que substitui o sol")
printl("O único caminho para seguir parece ser em direção a luz...")
printll("")
printl("Você encontra um rio, mas a água é escura e parece correr bem lentamente")
printl("Parece que existem três maneiras de continuar")

escolher_caminho()

inimigo = Froglin()
combate(jogador, inimigo)

# Após vencer a luta

if jogador.vida > 0:
    printl("Você se torna mais experiente, e se lembra um pouco mais de seu passado...")
    printl("\nVocê recebeu 2 pontos de atributo")
    
    if escolha_caminho == '1':
        printl("Você recebe uma 'Moeda Estranha'.")
        jogador.inventario.append("Moeda Estranha")
        
    jogador.recompensa_pontos(2)
    printl("Você descansa e recupera suas forças\n")
    jogador.vida = jogador.atributos.vida_base
    printl("\n Enquanto descansa, você sente que algo está te observando...")
    printl("Você decide continuar a sua jornada, passando pela trilha que tem na floresta.")

    cena_cidade()

# Quando o Jogador perde a luta

elif jogador.vida <= 0:
    cena_preso()
    inimigo= Guarda()
    combate(jogador, inimigo)
    jogador.vida = jogador.atributos.vida_base
    
if escolha_do_velho == 1:
    printl("Você e o senhor saem da prisão.")
    printl("O senhor te da direções para a vila mais próxima\n")
    printl("Enquanto vocês partem seus caminhos, ele diz: ")
    printl(f"Até mais, {nome}\n")
    printl("Assustado, você olha pra trás, mas não vê nada. 'Como ele sabe meu nome'?\n")
    printl("Você continua na direção apontada pelo estranho, uma estrada velha de terra\n")
    printll("...")
elif escolha_do_velho == 2:
    printl("...")
    printl("Você segue seu caminho, pensando nas suas ações\n")
    printl("Por quê ele estava preso? e como ele desacordou um guarda com uma pedra?\n")
    printl("Você segue o único caminho, uma estrada velha de terra")
    printll("...")
    
cena_cidade()