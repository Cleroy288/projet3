
from qcm import build_questionnaire # la fonction 
import random # pour le prng

# ici on vas demandr au user combien de questions il veut , sur base de cela on vas tronquer la liste de questions pour en avoir une nouvelle contennat le nombre de questions que le user veut
def getListSizeAndMakeNewSizeList(lst):
	print("\n--------------Bonjour, bienvenue dans le qcm du groupe B07--------------\n")
	print(f"Combien de questions voulez-vous avoir ? Réponse entre 1 et {len(lst)}")# print un message explicatif

	while (True):# boucle while infni
		rep = input("Entrez une réponse en chiffre : ")# on demande au user comb de questions il veut
		if not rep.isdigit():
			print("Veuillez ne rentrer que des chiffres.")# pas que des chiffres == erreur
		else:
			rep = int(rep)
			if rep <= 0 or rep > len(lst):# un chiffre en dessous de zéro ou plus que de questions disponible == erreur
				print("Veuillez rentrer une valeur valide.")
			else:
				lst = lst[0:rep]
				return lst# après avoir géré les cas d'erreur on renvoi la liste

# fonction Charles 
def getListAndShuffle(filename):
	lst = build_questionnaire(filename)

	if not lst:
		print("Erreur, le fichier fourni n'est pas valide ou ne nous a renvoyé aucune questions.")
		exit(0)# il y as eu une erreur on quitte le programme 

	random.shuffle(lst) # on mélange la liste pour donner une liste aléatoire 
	
	lst = getListSizeAndMakeNewSizeList(lst) # on prend la bonne taille de liste

	return lst # on renvoi la liste
		
# fonction de greg 
def printQuestionsAndGetAnswers(questions_melange):
	
	print("\n------------ Nous allons passer à la partie QCM -------------\n")

	liste_reponse_player = []# liste dans la quel on vas stocker 1 ou 0 en fonction de si la réponse du user est juste ou non
	#liste_index_rep_player = []# liste dans la quel on vas stocker les index de réponses du joueur

	for q in range(len(questions_melange)):
		# print la question
		print(f"\tQuestion {q+1}: \"{questions_melange[q][0]}\"")

		# print les réponses 
		for r in range(len(questions_melange[q][1])):
			print(f"\t\tRéponse {r+1}: \"{questions_melange[q][1][r][0]}\"")

		# récupérer la réponse du user 
		while True:
			reponse = input("Votre réponse (en chiffre(1, 2, 3,...)) ? ")
			print(f"Réponse entrée : {reponse}")
			
			# vérification de la validité de la réponse du user 
			if reponse.isdigit():
				reponse = int(reponse)
				if 1 <= reponse <= len(questions_melange[q][1]):
					break
				else:
					print(f"Votre réponse doit être un chiffre entre 1 et {len(questions_melange[q][1])}.")
			else:
				print("Votre format de réponse est incorrect. Veuillez entrer un chiffre.")

		# déterminer l'indexe de la réponse sélectionné
		indexRep = reponse - 1
		#liste_index_rep_player.append(indexRep)

		# vérifier si la réponse est juste ou pas , si juste on ajoute un 1 si il à faux on ajoute 0
		if questions_melange[q][1][indexRep][1]:  # réponse correcte
			liste_reponse_player.append([1, indexRep])
		else:  # réponse fausse
			liste_reponse_player.append([0, indexRep])

	return liste_reponse_player#, liste_index_rep_player

def correctionOfUserReponses(listQuestions, listPlayerAnswers):
	print("\n--------- Nous allons passer à la partie correction --------\n")
	#print(listPlayerAnswers)
	points = 0 # on crée un compteur pour les points du USER
	for i in listPlayerAnswers:
		#print(f"i == {i}")
		#print(f"i[0] == {i[0]}")
		if i[0] == 1: # à chaque bonne réponse
			points += 1 # on ajoute un point

	print("Quel type niveau de difficulté voulez vous pour votre correction? ")# on demande le type de correction 
	while True: # on crée une boucle infi pour demander l'input du user
		correction_method = int(input("1 - Sympa, 2 - Méchante, 3 - Floue et tordue : ")) # on prend l'inupt qu'on change en int
		if correction_method != 1 and correction_method != 2 and correction_method != 3:# petite vérif de la validité de l'input
			print("Veuillez rentrer une valeur entre 1 et 3")
		else:
			break # si on à bien reçu une valeur entre 1 et 3 on sort de la boucle 
	# ici on gère les différent type de correction
	# il faut implémenter la logique pour ça 
	if correction_method == 1:
		print("Vous avez choisis la méthode de correction numéro 1")
		print("Ce mode de correction est assez facile et le plus utilisé, il met juste votre nombre de réponse juste sur le nombre de questions totales et ensuite remis sur 20.\n")
		print(f"Vous avez répondu à {points} bonne question sur {len(listQuestions)}")
		print(f"Votre note est de {(points/len(listQuestions))*20} sur 20")
	elif correction_method == 2:
		print("Vous avez choisis la méthode de correction numéro 2")
		print("Ce mode de correction est difficle, si vous avez juste, vous gagnez un point, mais si vous répondez faux, vous en perdez un. Tout ça sur le nombre de question totale, et ensuite remis sur 20.\n")
		points = 0
		for i in listPlayerAnswers:
				#print(f"i == {i}")
				#print(f"i[0] == {i[0]}")
				if i[0] == 1: # à chaque bonne réponse
					points += 1 # on ajoute un point
				else:
					points -= 1 # on enlève un point

		if points < 0:
			points = 0

		print(f"Vous avez répondu à {points} bonne question sur {len(listQuestions)}")
		print(f"Votre note est de {(points/len(listQuestions))*20} sur 20")
	elif correction_method == 3:
		print("Vous avez choisis la méthode de correction numéro 3")
		print("Ce mode de correction est très ardu")
		print("On vérifie si les réponses données ne sont pas des réponses mises au hasard")
		#PAS FAIT

def showQCMExplainations(newQuestions, listRepPlayer):

	# on passe à travers chaque réponse 
	if all(rep[0] == 1 for rep in listRepPlayer):  # si toute les rep sont juste
		print("\nWAOW vous n'avez pas fait d'erreurs, vous êtes trop fort !")
		print("Il n'y a donc pas de correction pour vous !\n")
		return True  # rien à corriger

	# print de rappel et instructions
	print("\n--------- Nous allons passer à la partie explications ----------\n")
	print("Souhaitez-vous avoir une correction de vos erreurs ?")
	rep = input("Répondez : oui ou non : ")
	
	# on récupère l'input du user, oui ou non
	while True:
		if rep != "oui" and rep != "non":
			print("Veuillez taper oui ou non")
			rep = input("Répondez : oui ou non : ")
		else:
			break

	# si le user veut des explications
	if rep == "oui":
		print("\n------------Vous avez choisi oui, nous allons donc procéder à la correction.------------")

		for i in range(len(newQuestions)): # in passer à travers chaque question 
			if listRepPlayer[i][0] == 0:  # si la réponse est fausse
				print(f"\nQuestion {i + 1} : {newQuestions[i][0]}")  # print la question
				indexRepPlayer = listRepPlayer[i][1]  # index de la rep du user
				playerRep = newQuestions[i][1][indexRepPlayer][0]  # test de la réponse du user
				print(f"Vous avez répondu : {playerRep}")	# print la réponse qu'on a donné du joueur

				# init les variables pour stocker les bonne réponse et les explications
				correctAnswer = None  
				explaination = None  

				# passer à travers les réponses pour trouver la bonne réponse
				for answer in newQuestions[i][1]:
					if answer[1]:  # bonne réponse
						correctAnswer = answer[0]  # stocker la bonne réponse
						break  # on sort de la boucle

				# print la bonne réponse et son explication si disponible
				print(f"La bonne réponse était : {correctAnswer}")

				explaination = newQuestions[i][1][indexRepPlayer][2]  # Explication associée à la réponse du joueur

				if explaination:  # si on à trouvé une explication pour la réponse du user on l'affiche
					print(f"Explications pour votre réponse : {explaination}")
				else:
					# si on n'a pas trouvé d'explications, on passe à travers l'élément de la liste pour voir si il n'y en à pas un autre , ceci est une sécurité
					explanation_found = False  # flag pour savoir si une explication a été trouvée
					for answer in newQuestions[i][1]:
						if answer[2]:  # si on trouve une réponse
							print(f"Explication pour la réponse {answer[0]} : {answer[2]}") # on la print
							explanation_found = True # on met le flag à true
							break  # on break / sort de la boucle

					# si il n'y à pas de bonne rep trouvé
					if not explanation_found:
						print("Il n'y a pas d'explication disponible pour cette question.") # on print un message

			else:
				# si la rép était correcte on le précise simplement
				print(f"\nVous aviez juste à la question {i + 1}.\n")
			print("\n")
	else:
		# si le USER choisit de ne pas voir les explications on quitte la fonction
		return True
	return True

def endMessage():
	print("Merci à vous d'avoir particpé à notre QCM, nous espérons que vous vous êtes follement amusés :J")
	print("\nCe QCM vous à été proposé par Charles, Jeremy, Gregoire, Yohan")
	
#def mandatory():
#	print("BONOUR pour pouvoir utiliser notre programme il y à 2 lib prérecquise")
#	print("La librairie python [colorama] et [pyfiglet], veuillez les installer avant de continuer")
#	rep = input("Avez vous installé ses librairies ? (oui / non) : ")
#	if rep == "oui":
#		print("Super bonne continuation")
#	else:
#		print("Veuillez les installer avant de continuer")
#		exit()

if __name__ == '__main__':
	filename = "QCM.txt"
	# verifier que le user à bien tout les prérequis de insatllé 
	#mandatory()
	# 1 ) on récupère la liste, on demande au USER combien de questions il veut, on les mélange et on renvoi une nouvelle liste
	newQuestions = getListAndShuffle(filename)
	# 2 ) on pose les questions QCM au USER	
	listRepPlayer = printQuestionsAndGetAnswers(newQuestions)
	# 3 ) correction 
	correctionOfUserReponses(newQuestions, listRepPlayer)
	# 3 demander si le user veut des explications par rapport à ces erreurs
	showQCMExplainations(newQuestions, listRepPlayer)
	# 4 ) message de fin 
	endMessage()

	

	

