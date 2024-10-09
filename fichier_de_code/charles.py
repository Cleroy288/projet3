from qcm import build_questionnaire # la fonction 
import random # pour le prng

def function1(filename):
	lst = build_questionnaire(filename)

	random.shuffle(lst) # on mélange la liste pour donner une liste aléatoire 

	return lst # on renvoi la liste 