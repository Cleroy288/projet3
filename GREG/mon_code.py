def greg(questions_melange):
    
    print(questions_melange)
    print("------------------------------------------")

    liste_reponse_player = []
    for q in range(len(questions_melange)):
        # au dessus 
        print("\tQuestion " + str(q+1) + ": \"" + questions_melange[q][0] + "\"")                   #Print la question
    
        for r in range(len(questions_melange[q][1])):
            print("\t\tReponses " + str(r+1) + ":" + questions_melange[q][1][r][0] + "\"")           #Print les réponses
    
        while True:
            reponse = input(str("Votre réponse (en chiffre(1, 2, 3,...)) ? "))
            print(f"reponse : {reponse}")
            if reponse.isdigit() and reponse <= str(r) and reponse > str(0):                         #Demande sa réponse
                break
            else:
                print("Votre format de réponse est incorrect. Veuillez répondre à la question avec un chiffre correspondant à la réponse que vous souhaitez transmettre.")
    
        indexRep = int(reponse) - 1
        print(f"indexrep == {indexRep}")
		# retourner une
        if questions_melange[q][1][indexRep][1] == True:
            liste_reponse_player.append([1])             #Le joueur à juste, on ajoute 1 à la liste reponse player
    
        if questions_melange[q][1][indexRep][1] == False:
            liste_reponse_player.append([0, reponse])             #Le joueur a faux, on ajoute 0 à la liste reponse player
	
    print(f"liste reponse player {liste_reponse_player}")
    return liste_reponse_player