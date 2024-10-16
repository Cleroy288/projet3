
from qcm import build_questionnaire # la fonction 
import random # pour le prng
import pyfiglet
from colorama import init, Fore, Style
import questionary
import time

# VALEUR GLOBALES == ACESSIBLE PARTOUT DANS LE CODE !
# on défini des couleurs de base
COLOR_RED = Fore.RED
COLOR_GREEN = Fore.GREEN
COLOR_YELLOW = Fore.YELLOW
COLOR_WHITE = Fore.WHITE
COLOR_PURPLE = Fore.MAGENTA # mauve
COLOR_BLUE = Fore.BLUE 

############ utils ###########
# fonction simple pour print avec du délai
def printWithDelay(text):
	delay = 2 # on met un délai de 1 à 2 , je ne sais pas ce que ça représente j'ai test avec cette valeur la au début et ça à fonctionné direct 
	for char in text:
		print(char, end='', flush=True) # on affiche chaque caratère sans retour à la ligne
		time.sleep(delay / len(text) ) # pause entre chaque caratère
	print()# on print le retour à la ligne

# fonction pour print des message entouré de barres (caratères spéciaux en couleur)
def printWithBorder(text, color):
	border = '=' * (len(text) + 6)# cree la première ligne de la longueur du texte + 4
	#afficher le texte avec bordures
	print(color + f"+{border}+")
	printWithDelay(f"|   {text}   |")
	print(f"+{border}+" + Style.RESET_ALL) # on preint la barrière à nouveau + on reset les couleurs, sinon les autre messages serons de la meme couleur


################################

# ici on vas demandr au user combien de questions il veut , sur base de cela on vas tronquer la liste de questions pour en avoir une nouvelle contennat le nombre de questions que le user veut
def getListSizeAndMakeNewSizeList(lst):
	#print(f"Bonjour , combien de questions voulez-vous avoir ? Réponse entre 1 et {len(lst)}")# print un message explicatif
	printWithBorder(f"Bonjour , combien de questions voulez-vous avoir ? Réponse entre 1 et {len(lst)}", COLOR_YELLOW)
	while (True):# boucle while infni
		rep = questionary.text("Entrez une réponse en chiffre : ").ask() # on demande au user comb de questions il veut
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
	
	print("\n")
	printWithBorder(f"Nous allons passer à la partie QCM", COLOR_PURPLE) # on change le print par border with radius
	print("\n")
	#print("\n------------ Nous allons passer à la partie QCM -------------\n")

	liste_reponse_player = []# liste dans la quel on vas stocker 1 ou 0 en fonction de si la réponse du user est juste ou non
	#liste_index_rep_player = []# liste dans la quel on vas stocker les index de réponses du joueur

	for q in range(len(questions_melange)):
		# print la question
		printWithBorder(f"Question {q+1}: {questions_melange[q][0]}", COLOR_WHITE)

		choices = [] # liste de choix possibles 
		for r in range(len(questions_melange[q][1])):
			choix = f"{r + 1}: {questions_melange[q][1][r][0]}"
			choices.append(choix) # on ajoute le choix possible à la liste de choix
		
		# on utilise questionnary
		reponse = questionary.select(f"Choisissez une réponse pour la question {q + 1} :", choices=choices).ask() # on passe les choix à dictionnary et il le donnera au user
		# on récup l'index rep 
		indexRep = int(reponse.split(":")[0]) - 1 # on récupère l'index à la réponse choisie, meme chose que avant
		

		# !! ANCIENNE VERS CI DESSOUS
		## print les réponses 
		#for r in range(len(questions_melange[q][1])):
		#	print(f"\t\tRéponse {r+1}: \"{questions_melange[q][1][r][0]}\"")

		## récupérer la réponse du user 
		#while True:
		#	reponse = input("Votre réponse (en chiffre(1, 2, 3,...)) ? ")
		#	print(f"Réponse entrée : {reponse}")
		#	
		#	# vérification de la validité de la réponse du user 
		#	if reponse.isdigit():
		#		reponse = int(reponse)
		#		if 1 <= reponse <= len(questions_melange[q][1]):
		#			break
		#		else:
		#			print(f"Votre réponse doit être un chiffre entre 1 et {len(questions_melange[q][1])}.")
		#	else:
		#		print("Votre format de réponse est incorrect. Veuillez entrer un chiffre.")
		#
		# déterminer l'indexe de la réponse sélectionné
		#indexRep = reponse - 1

		# vérifier si la réponse est juste ou pas , si juste on ajoute un 1 si il à faux on ajoute 0
		if questions_melange[q][1][indexRep][1]:  # réponse correcte
			liste_reponse_player.append([1, indexRep])
		else:  # réponse fausse
			liste_reponse_player.append([0, indexRep])

	return liste_reponse_player

# fonction pour imprimer les résultats du user
def printResult(listQuestions, points):
	if points > (len(listQuestions) // 2): # plus que la moitié 
		printWithBorder(f"Votre note est de {points} sur {len(listQuestions)}", COLOR_GREEN)
	else:
		printWithBorder(f"Votre note est de {points} sur {len(listQuestions)}", COLOR_RED)

def correctionOfUserReponses(listQuestions, listPlayerAnswers):
	# print à changé 
	printWithBorder(" Nous allons passer à la partie correction", COLOR_BLUE)

	#print("\n--------- Nous allons passer à la partie correction --------\n")
	#print(listPlayerAnswers)
	points = 0 # on crée un compteur pour les points du USER
	for i in listPlayerAnswers:
		if i[0] == 1: # à chaque bonne réponse
			points += 1 # on ajoute un point

	printWithDelay("Quel type niveau de difficulté voulez vous pour votre correction?")
	correction_method = questionary.select(
		"Choisissez un niveau de difficulté : ",
		choices=[
			"1: Facile",
			"2: Moyen",
			"3: Difficile"
		]
	).ask()

	# on récupère la valeur réelle 
	correction_method = int(correction_method.split(":")[0])

	#print("Quel type niveau de difficulté voulez vous pour votre correction? ")# on demande le type de correction 
	#while True: # on crée une boucle infi pour demander l'input du user
	#	correction_method = int(input("1 facile, 2 moyen, 3 difficle : ")) # on prend l'inupt qu'on change en int
	#	if correction_method != 1 and correction_method != 2 and correction_method != 3:# petite vérif de la validité de l'input
	#		print("Veuillez rentrer une valeur entre 1 et 3")
	#	else:
	#		break # si on à bien reçu une valeur entre 1 et 3 on sort de la boucle 
	# ici on gère les différent type de correction
	# il faut implémenter la logique pour ça 
	if correction_method == 1:
		printWithDelay("Vous avez choisis la méthode de correction numéro 1")
		printWithDelay("Ce mode de correction est assez facile et le plus utilisé, il met juste votre nombre de réponse juste sur le nombre de questions totales.")
		#printResult(listQuestions, points)# on imprime le résultats 
		#if points > (len(listQuestions) // 2): # plus que la moitié 
		#	printWithBorder(f"Votre note est de {points} sur {len(listQuestions)}", COLOR_GREEN)
		#else:
		#	printWithBorder(f"Votre note est de {points} sur {len(listQuestions)}", COLOR_RED)
	elif correction_method == 2:
		printWithDelay("Vous avez choisis la méthode de correction numéro 2")
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

		#print(f"Vous avez {points} sur {len(listQuestions)}")
	elif correction_method == 3:# encore à faire je suppose
		printWithDelay("Vous avez choisis 3")
		points = 0
		#print("Vous avez choisis la méthode de correction numéro 0")

	printResult(listQuestions, points)

def showQCMExplainations(newQuestions, listRepPlayer):

	# on passe à travers chaque réponse 
	if all(rep[0] == 1 for rep in listRepPlayer):  # si toute les rep sont juste
		printWithBorder("WAOW vous n'avez pas fait d'erreurs, vous êtes trop fort !", COLOR_GREEN)
		printWithBorder("Il n'y a donc pas de correction pour vous !\n", COLOR_YELLOW)
		return True  # rien à corriger

	# print de rappel et instructions
	printWithBorder("Nous allons passer à la partie explications", COLOR_BLUE)
	#printWithDelay("Souhaitez-vous avoir une correction de vos erreurs ?")

	rep = questionary.select("Souhaitez vous avois une correction de vos erreurs ?",
		choices=["oui", "non"]	
	).ask()

	#rep = input("Répondez : oui ou non : ")
	#
	## on récupère l'input du user, oui ou non
	#while True:
	#	if rep != "oui" and rep != "non":
	#		print("Veuillez taper oui ou non")
	#		rep = input("Répondez : oui ou non : ")
	#	else:
	#		break

	# si le user veut des explications
	if rep == "oui":
		printWithBorder("Vous avez choisi oui, nous allons donc procéder à la correction.", COLOR_BLUE)
		#print("\n------------Vous avez choisi oui, nous allons donc procéder à la correction.------------")

		for i in range(len(newQuestions)): # in passer à travers chaque question 
			if listRepPlayer[i][0] == 0:  # si la réponse est fausse
				printWithBorder(f"Question {i + 1} : {newQuestions[i][0]}", COLOR_WHITE)  # print la question
				indexRepPlayer = listRepPlayer[i][1]  # index de la rep du user
				playerRep = newQuestions[i][1][indexRepPlayer][0]  # test de la réponse du user
				printWithDelay(COLOR_RED + f"Vous avez répondu : {playerRep}" + Style.RESET_ALL)# print la réponse qu'on a donné du joueur

				# init les variables pour stocker les bonne réponse et les explications
				correctAnswer = None  
				explaination = None  

				# passer à travers les réponses pour trouver la bonne réponse
				for answer in newQuestions[i][1]:
					if answer[1]:  # bonne réponse
						correctAnswer = answer[0]  # stocker la bonne réponse
						break  # on sort de la boucle

				# print la bonne réponse et son explication si disponible
				printWithDelay(COLOR_YELLOW + f"La bonne réponse était : {correctAnswer}" + Style.RESET_ALL)

				explaination = newQuestions[i][1][indexRepPlayer][2]  # Explication associée à la réponse du joueur

				if explaination:  # si on à trouvé une explication pour la réponse du user on l'affiche
					printWithDelay(f"Explications pour votre réponse : {explaination}")
				else:
					# si on n'a pas trouvé d'explications, on passe à travers l'élément de la liste pour voir si il n'y en à pas un autre , ceci est une sécurité
					explanation_found = False  # flag pour savoir si une explication a été trouvée
					for answer in newQuestions[i][1]:
						if answer[2]:  # si on trouve une réponse
							printWithDelay(f"Explication pour la réponse {answer[0]} : {answer[2]}") # on la print
							explanation_found = True # on met le flag à true
							break  # on break / sort de la boucle

					# si il n'y à pas de bonne rep trouvé
					if not explanation_found:
						printWithDelay("Il n'y a pas d'explication disponible pour cette question.") # on print un message

			else:
				# si la rép était correcte on le précise simplement
				printWithBorder(f"Question {i + 1} : {newQuestions[i][0]}", COLOR_WHITE)
				printWithDelay(COLOR_GREEN + f"Vous aviez juste à la question {i + 1}." + Style.RESET_ALL)
			print("\n")
	else:
		# si le USER choisit de ne pas voir les explications on quitte la fonction
		return True
	return True

def printInBIg(text, color):
	print(color + pyfiglet.figlet_format(text) + Style.RESET_ALL)

# message de fin 
def endMessage():
	printWithBorder("Merci à vous d'avoir particpé à notre QCM, nous espérons que vous vous êtes follement amusés :J",COLOR_PURPLE)
	printWithBorder("Ce QCM vous à été proposé par Charles, Jeremy, Gregoire, Yohan", COLOR_GREEN)
	printInBIg("BYE BYE ET BIZZ DE BO7 !", COLOR_BLUE)

# on imprime un message de 
def mandatory():
	print("BONOUR pour pouvoir utiliser notre programme il y à 3 lib prérecquise")
	print("La librairie python [colorama] et [pyfiglet] et [questionary], veuillez les installer avant de continuer")
	rep = input("Avez vous installé ses librairies ? (oui / non) : ")
	if rep == "oui":
		print("Super bonne continuation")
	else:
		print("Veuillez les installer avant de continuer ou utiliser l'exécutable que nous avonns laissé")
		exit()

# petit print sympa en  début de programme ...
def WelcomePrint():
	printInBIg("BIENVENUE AU QCM DU GROUPE B07!", Fore.CYAN) # le couleur c'est une sorte de bleu pas mal
	#print(Fore.CYAN + pyfiglet.figlet_format("BIENVENUE AU QCM DU GROUPE B07!") + Style.RESET_ALL)



if __name__ == '__main__':
	filename = "QCM.txt"
	# verifier que le user à bien tout les prérequis de insatllé 
	mandatory()

	# welcome print
	WelcomePrint()

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

	

	

