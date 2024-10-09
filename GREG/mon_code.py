
questions_melange =  #-> LISTE PRNG QUESTION CHARLES 

print("Le questionnaire est une liste de questions.")






liste_reponse : []
liste_reponse_player : []
for q in range(len(questions_melange)):
    print("\tQuestion " + str(q+1) + ": \"" + questions_melange[q][0] + "\"")                   #Print la question

    for r in range(len(questions_melange[q][1])):
        print("\t\tReponses " + str(r+1) + ":" + questions_melange[q][1][r][0] + "\"")           #Print les réponses

    while True:
        reponse = input(str("Votre réponse (en chiffre(1, 2, 3,...)) ? "))
        if reponse.isdigit() and reponse <= str(r) and reponse > str(0):                         #Demande sa réponse
            break
        else:
            print("Votre format de réponse est incorrect. Veuillez répondre à la question avec un chiffre correspondant à la réponse.")

    

    if questions_melange[q][1][reponse-1][1] == True:
        liste_reponse_player.append([1])             #Le joueur à juste, on ajoute 1 à la liste reponse player

    if questions_melange[q][1][reponse-1][1] == False:
        liste_reponse_player.append([0])             #Le joueur a faux, on ajoute 0 à la liste reponse player
