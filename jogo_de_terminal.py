jogador = input("digite o nome do jogador:")
print("Bem-vindo", jogador)

inicio = input("começar o jogo? (S/N) : ")
if inicio == "S":
    print("história : você é um guerreiro de uma vila chamada Quata, mas em um dia lhe parece melhor sair um pouco. Então você vai")
    ajudar = input("pouco tempo depois de sua partida, você avista um ladrão roubando um camponês. Ajudar (S/N)? :")
    if ajudar == "S":
        agradecimento = input("você pega o que o ladrão roubou e devolve para a pessoa, ela agradeça oferecendo um pouco de dinheiro. Aceitar (S/N)? :")
    else:
        print ("O ladrão foge como os pertences daquela pessoa, e ainda reclama com você.")
        print("após isso, você segues seu caminho")
        
    if agradecimento == "S":
        print("você ganha 10 moedas de presente e segue seu caminho")
    else:
        print("Após recusar, você segue caminho")   
    
else:
    print("Ok, quando quiser")