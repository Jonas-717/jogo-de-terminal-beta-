jogador = input("digite o nome do jogador : ")
classe = input("Escolha sua classe (guerreiro/mago) : ")
print("Bem-vindo", jogador, ". Você é um ", classe)

if classe == "mago":
    item = "feitiço novo"
else:
    item = "escudo"


inicio = input("começar o jogo? (S/N) : ")
if inicio == "S":
    print("história : você é um ", classe, "em uma vila chamada Quata, mas em um dia lhe parece melhor sair um pouco. Então você vai.")
    ajudar = input("Narração : Pouco tempo depois de sua partida, você avista um ladrão roubando uma camponês. Ajudar (S/N) ? : ")
    if ajudar == "S":
        agradecimento = input("Narração : você pega o que o ladrão roubou e devolve para a pessoa, ela agradeça oferecendo um pouco de dinheiro. Aceitar (S/N) ? : ")
    else:
        print ("Decisão : O ladrão foge como os pertences daquela pessoa, e ainda reclama com você.")
        print("após isso, você segues seu caminho")
        
    if agradecimento == "S":
        print("Decisão : você ganha 10 moedas de presente e segue seu caminho")
    else:
        print("Decisão : Após recusar, você segue caminho")

    visita = input("Narração : Após caminhar alguns minutos você percebe em sua frente uma grande cidade (você acha que nela mora um rei chamado Lion). Visitar (S/N) ? : ")

    if visita == "S":
        print("Narração : depois de passar pelo portão da cidade, você olha ao redor e percebe vários comércios e camponeses.")
        print("Andando um pouco mais, um comerciante lhe oferece um", item,"por 10 moedas.")
        compra = input("Comprar (S/N) ? : ")
        if compra == "S":
            print("Decisão : Parabéns, agora você tem um", item,".")
            conversa = input("Narração : Seguindo seu caminho, um homem vem e te pergunta de onde veio. Conversar (S/N) ? : ")
            if conversa == "S":
                print("Fala do jogador : Eu me chamo", jogador, "e sou um", classe, ". Vim de uma vila chamada Quata.")
                print("NPC : Entedi, mas o veio fazer aqui?")
                print("Fala do jogador : Decide sair um pouco de minha vila e acabei parando aqui.")
                print("NPC : Que legal, mas aonde você vai dormir aqui? Já ta escurecendo.")
                print("Fala do jogador : Eu também não sei...")
                dormir_na_casa = input("NPC : Se quiser pode vir comigo e domir em minha casa, lá tem um quarto vazio. Aceitar (S/N) ? ")
                if dormir_na_casa == "S":
                    print("Narração : Você acompanha aquele homem até sua casa, e é bem recibido em sua casa. Você dorme bem naquela noite.")
                else:
                    print("Decisão : Você recusa a oferta de forma educada, mas não sabe onde dormir.")
            else:
                print("Decisão : Você ignora aquela pessoa e segue.")
        else:
            print("Decisão : Você recusa o", item, "mesmo ele incistindo.")
            conversa = input("Narração : Seguido seu caminho, um homem vem e te pergunta de onde veio. Conversar (S/N) ? : ")
            if conversa == "S":
                print("Fala do jogador : Eu me chamo", jogador, "e sou um", classe, ". Vim de uma vila chamada Quata.")
                print("NPC : Entedi, mas o veio fazer aqui?")
                print("Fala do jogador : Decide sair um pouco de minha vila e acabei parando aqui.")
                print("NPC : Que legal, mas aonde você vai dormir aqui? Já ta escurecendo.")
                print("Fala do jogador : Eu também não sei...")
                dormir_na_casa = ("NPC : Se quiser pode vir comigo e domir em minha casa, lá tem um quarto vazio. Aceitar (S/N) ? ")
                if dormir_na_casa == "S":
                    print("Narração : Você acompanha aquele homem até sua casa, e é bem recibido em sua casa. Você dorme bem naquela noite.")
                else:
                    print("Decisão : Você recusa a oferta de forma educada, mas não sabe onde dormir.")
                # Falta a sequência de quando o jogador RECUSAR A DORMINADA NA CASA DO HOMEM
            else:
                print("Decisão : Você ignora aquela pessoa e segue.")
            # Falta a sequência de quando o jogador IGNORAR O HOMEM
    else:
        luta = input("Decisão : você não visita a cidade e continua sua jornada. Mas derrepente aparece um lobo selvagem em sua frente. Lutar (S/N) ?")
        if luta == "S":
            if item == "feitiço novo":

                print("Narração : você luta contra o lobo usando um feitiço, e acaba ganhando")
            # Falta a sequência de quando jogador NÃO VISITAR A CIDADE (e vencer do lobo)
            else:
                print("Narração : você luta contra o lobo usando sua espada, e acaba ganhando")
            # Falta a sequência de quando jogador NÃO VISITAR A CIDADE (e vencer do lobo)
        else: 
            print("Decisão : Você tenta fugir do lobo, mas não consegue e acaba morrendo para ele (FIM DE JOGO).")

else:
    print("Ok, quando quiser")
