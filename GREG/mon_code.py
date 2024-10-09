
questions_melange =  #-> LISTE PRNG QUESTION CHARLES 

print("Le questionnaire est une liste de questions.")


reponse_player : []
for q in range(len(questions_melange)):
    print("\tQuestion " + str(q+1) + ": \"" + questions_melange[q][0] + "\"")

    for r in range(len(questions_melange[q][1])):
        print("\t\tReponses " + str(r+1) + ":" + questions_melange[q][1][r][0] + "\"")


    while True:
        reponse = input(str("Votre réponse (en chiffre(1, 2, 3,...)) ? "))
        if reponse.isdigit() and 0 <= reponse >= r:
            break
        else:
            print("Votre format de réponse est incorrect. Veuillez répondre à la question avec un chiffre correspondant à la réponse.")

    if questions_melange[q][1][r][1] == True:
        reponse_player.append([1])
    if questions_melange[q][1][r][1] == False:
        reponse_player.append([0]) 