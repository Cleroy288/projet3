# Il vous est demandé d'implémenter une fonction permettant de tester si une implémentation d'un PRNG est correcte ou non. INGInious va utiliser votre fonction avec plusieurs implémentations d'un PRNG, certaines sont erronées, d'autres non.
# 
# Cette tâche sera comptabilisée dans votre note de participation. Il vous faut réussir la tâche entièrement. Cette tâche ne doit être validée que par un seul membre de votre équipe pour obtenir la participation, mais tous les étudiant·es peuvent l'utiliser pour leurs tests.
# 
# def is_correct(PRNG):
#     # Cette fonction doit retourner un booléen, indiquant si le PRNG est correct.
#     # Son unique paramêtre vous permet de créer un PRNG.
#     # Si vous souhaitez créer un PRNG avec une seed de 33 et un interval de 0 à 10,
#     # faites comme ceci:
#     # prng = PRNG(33, 11)
#     #
#     # Pour obtenir le prochain nombre aléatoire de ce PRNG:
#     # prng.next_int()
# 
#     return True
# Validation des PRNGs
# Utiliser le code fourni pour commencer. La signature de la fonction is_correct doit rester inchangée. Vous êtes libre d'ajouter d'autres fonctions dans cet encadré et de les utiliser dans is_correct.
# 
# def is_correct(PRNG):
#     return True
# 1
"""""
PRNG1: Ces nombres ne sont pas très aléatoires, les avez-vous vérifiés ?
PRNG2: Certains nombres dans l'interval limite sont omis.
PRNG3: Avez-vous vérifié la limite supérieure ?
PRNG4: Avez-vous verifié le signe des nombres générés ?
PRNG5: Êtes-vous sur que ce PRNG génère tout les nombres ?
PRNG6: Une seed de 3 ne produit pas de nombres très aléatoires.
PRNG7: Une nouvelle seed devrait produire une nouvelle séquence. Est-ce le cas ?
PRNG8: Il semblerait qu'une seed valant 10 ne produit pas des nombres très aléatoires.
PRNG9: Ces nombres semblent prédictible, comme si ils formaient un cycle. Ce n'est pas très aléatoire.
PRNG10: Ces nombres semblent prédictible, comme si ils formaient un cycle. Ce n'est pas très aléatoire.


PRNG1: Certains nombres dans l'interval limite sont omis.
PRNG2: Êtes-vous sur que ce PRNG génère tout les nombres ?
PRNG3: Il semblerait qu'une seed valant 10 ne produit pas des nombres très aléatoires.
PRNG4: Avez-vous vérifié la limite supérieure ?
PRNG5: Ces nombres ne sont pas très aléatoires, les avez-vous vérifiés ?
PRNG6: Une seed de 3 ne produit pas de nombres très aléatoires.
PRNG8: Une nouvelle seed devrait produire une nouvelle séquence. Est-ce le cas ?
PRNG10: Avez-vous verifié le signe des nombres générés ?

"""""
#################################################################################
#################################################################################

## Vérifier si les nombres générés couvrent tout l'intervalle
#def test_full_coverage(PRNG, upperLimit):
#    prng = PRNG(33, upperLimit)  # initialiser le PRNG avec seed 33
#    generated_numbers = set()  # ensemble pour stocker les nombres uniques
#    
#    for _ in range(1000):  # générer 1000 nombres
#        num = prng.next_int()
#        
#        if num < 0:  # vérifier si un nombre est négatif
#            return False  # si un nombre est négatif, c'est faux
#        
#        generated_numbers.add(num)  # ajouter le nombre généré
#
#    # vérifier si on a bien généré tous les nombres de 0 à upperLimit - 1
#    if len(generated_numbers) == upperLimit:
#        return True  # si oui, c'est bon
#    else:
#        return False  # sinon, renvoie faux
#
## Vérifier que chaque graine donne une séquence différente
#def test_different_seeds(PRNG, upperLimit):
#    for i in range(1, 101):  # boucle de 1 à 100 pour les graines
#        prng1 = PRNG(i, upperLimit)     # première séquence avec graine i
#        prng2 = PRNG(i + 1, upperLimit) # deuxième séquence avec graine i+1
#
#        seq1 = [prng1.next_int() for _ in range(100)]
#        seq2 = [prng2.next_int() for _ in range(100)]
#
#        if seq1 == seq2:
#            return False  # retourne faux si les séquences sont identiques
#
#    return True  # si toutes les séquences sont différentes, c'est bon
#
## Vérifier s'il y a un cycle évident
#def test_no_cycles(PRNG, upperLimit):
#    prng = PRNG(33, upperLimit)  # initialiser PRNG avec seed 33
#    seq = [prng.next_int() for _ in range(100)]  # générer 100 nombres
#    
#    # vérifier si les 50 premiers nombres sont identiques aux 50 suivants
#    if seq[:50] == seq[50:]:
#        return False  # renvoie faux si un cycle est détecté
#    
#    return True  # sinon, c'est bon
#
## Vérifier les graines spécifiques pour voir si elles sont correctes
#def test_specific_seeds(PRNG, upperLimit):
#    seeds_to_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]  # tester les graines 3 et 10
#
#    for seed in seeds_to_test:
#        prng = PRNG(seed, upperLimit)  # initialiser PRNG avec la graine spécifique
#        seq = [prng.next_int() for _ in range(100)]  # générer 100 nombres
#        
#        # vérifier si une sous-séquence de 50 nombres se répète
#        if seq[:50] == seq[50:]:
#            return False  # si répétition, renvoyer faux
#
#    return True  # si pas de problème, c'est bon
#
#def is_correct(PRNG):
#    upperLimit = 11
#
#    if not test_full_coverage(PRNG, upperLimit):
#        return False
#    if not test_different_seeds(PRNG, upperLimit):
#        return False
#    if not test_no_cycles(PRNG, upperLimit):
#        return False
#    if not test_specific_seeds(PRNG, upperLimit):
#        return False
#
#    return True 

#################################################################################
#################################################################################
## cette version ci réussi une fois sur 2 elle n'est pas fiable 
#def isOlyOneNum(number):
#    numberStr = str(number) # changer 
#
#    val = numberStr[0]
#    for char in numberStr:
#        if char != val:
#            return False
#    return True
#
## fonction pour vérifier si il n'y à pas de séquece au sien du nombre donnée 
#def verifySeq(prng):
#    count = 100 # nombre de tours
#    previous_val = [] # liste contenant les ancienne valeurs
#    for _ in range(count):
#        value = prng.next_int()
#        if value in previous_val: # on vérifie si la valeur actuelle est dans la liste de valeur qu'on à déjà 
#            return False
#        previous_val.append(value) # on met la nouvelle val dans la liste
#    return True
#
## renvoi true si le nombre est négatif ce qui n'est pas autorisé 
#def isNeg(nbr):
#    if nbr < 0:
#        return True
#    return False
#
## renvoi True si la longueur du nombre est de 1 == nombre trop court 
#def isLen1(nbr):
#    if len(str(nbr)) > 1:
#        return False
#    return True
#
## on vas générer plusieurs nombres et les stcoker dans les listes pr1 et pr2 et puis vérifier si ils sont identique
## le but de cette fonction est de vérifier que les nombres généré changeant en fonction des params données 
#def isNotAlwaysSameVal(PRNG, upperLimit):
#
#    for i in range(100):
#        pr1 = PRNG(i, upperLimit)
#        pr2 = PRNG(i+1, upperLimit)
#        for j in range(50):
#            seq_1 = [pr1.next_int() for _ in range(100)]
#            seq_2 = [pr2.next_int() for _ in range(100)]
#
#        if seq_1 == seq_2: # si identique 
#            return False  # renvoi False car la liste est mauvaise 
#
#    return True # return True
#
#def verify_full_range(prng, upperLimit):
#
#    count = 1000
#    generated_numbers = []
#
#    for _ in range(count):
#        num = prng.next_int()
#        if num not in generated_numbers:
#            generated_numbers.append(num)
#    
#    if len(generated_numbers) < upperLimit:
#        return False
#    return True
#
#
#def test_no_cycles(PRNG, upperLimit):
#    prng = PRNG(33, upperLimit)
#    seq = [prng.next_int() for _ in range(100)]
#    # vérification d'une sous séquence de 50 
#    return seq[:50] != seq[50:]  # si une séquences de 50 nombres se suit alors , il y à une erreur 
#
#def is_correct(PRNG):
#
#    upperLimit = 11 # je ne suis pas sur que ce soit nécessaire ... 
#    prng = PRNG(33, upperLimit) # j'ai aucune idée de si il faut faire ça ou pas 
#    
#    # premiers test de base , pos, neg, oneNum, pour 300 nombres 
#    for i in range(300):
#        val = prng.next_int()
#        # verification si le nombre est négatif ou pas 
#        if isNeg( val ) == True:
#            return False # if neg return False
#        if isLen1( val ) == True: # Si la len n'est pas sup à 1 
#            return False # retrun False
#        if isOlyOneNum( val ) == False:
#            return False
#
#    prng = PRNG(33, upperLimit) # on re génère le prng 
#
#    # verification des séquences 
#    #if not verifySeq(prng):
#    #    return False
#    #if not test_no_cycles(PRNG, upperLimit):
#    #	return False
#
#    # les séquences génré sont toujours de la meme valeur 
#    if not isNotAlwaysSameVal(PRNG, upperLimit):
#        return False
#
#    prng = PRNG(33, upperLimit)
#    if not verify_full_range(prng, upperLimit):
#        return False
#
#    return True

#
##print(is_correct(input('vasy ')))
#################################################################################
#################################################################################

#def isOlyOneNum(PRNG):
#    prng = PRNG(3, upperLimit)
#    lst = []
#
#    for i in range(100):
#        number = prng.next_int()
#        lst.append(number)
#
#    val = lst[0]
#    for i in lst:
#        if i != val:
#            return False
#    
#    return True
#
#
## renvoi true si le nombre est négatif ce qui n'est pas autorisé 
#def isNeg(nbr):
#    if nbr < 0:
#        return True
#    return False
#
## renvoi True si la longueur du nombre est de 1 == nombre trop court 
#def isLen1(nbr):
#    if len(str(nbr)) > 1:
#        return False
#    return True
#
## on vas générer plusieurs nombres et les stcoker dans les listes pr1 et pr2 et puis vérifier si ils sont identique
## le but de cette fonction est de vérifier que les nombres généré changeant en fonction des params données 
#def isNotAlwaysSameVal(PRNG, upperLimit):
#    for i in range(100):
#        pr1 = PRNG(i, upperLimit)
#        pr2 = PRNG(i+1, upperLimit)
#        for j in range(50):
#            seq_1 = [pr1.next_int() for _ in range(100)]
#            seq_2 = [pr2.next_int() for _ in range(100)]
#
#        if seq_1 == seq_2: # si identique 
#            return False  # renvoi False car la liste est mauvaise 
#
#    return True # return True
#
#def allNbrMade(PRNG, upperLimit):
#    lst = []
#    prng = PRNG(3, upperLimit)
#
#    for nbr in range(100):
#        val = prng.next_int()
#        lst.append(val)
#    for i in range(0, upperLimit - 1):
#        if lst.count(i) == 0:
#            return False
#    return True
#
#def is_correct(PRNG):
#    upperLimit = 11 # je ne suis pas sur que ce soit nécessaire ... 
#    prng = PRNG(33, upperLimit) # j'ai aucune idée de si il faut faire ça ou pas 
#    
#    # on crée la liste 
#    lst = []
#    for i in range(100):
#        val = prng.next_int()
#        lst.append(val)
#    
#    # test 
#
#    if not allNbrMade(PRNG, upperLimit):
#        return False
#    
#    # premiers test de base , pos, neg, oneNum, pour 300 nombres 
#    for i in range(300):
#        val = prng.next_int()
#        if val > upperLimit - 1:
#            return False
#        # verification si le nombre est négatif ou pas 
#        if isNeg( val ) == True:
#            return False # if neg return False
#        #if isLen1( val ) == True: # Si la len n'est pas sup à 1 
#        #	return False # retrun False
#        if isOlyOneNum( val ) == False:
#            return False
#
#    return True

#################################################################################
#################################################################################

#################################################################################
# version 1 qui fonctionne 
#################################################################################

def is_correct(PRNG):
    upperLimit = 11
    num_samples = 1000

    # Test 1 ) vérif que les nb sont val
    prng = PRNG(33, upperLimit)
    numbers = [prng.next_int() for _ in range(num_samples)]
    for n in numbers:
        if n < 0:
            return False 
        if n >= upperLimit:
            return False

    # Test 2: verif que tt les nombres sont gen , dans 0 à upperLimit
    counts = [0] * upperLimit
    for n in numbers:
        counts[n] += 1
    if min(counts) == 0:# si le plus petit nombre est 0 c'est que jen à un qui manque 
        return False

    # nécessaire , présent dans la version originale mais pas nécéssaire 
    # Test 3 vérifier que des seed diff produisent des res différents
    prng1 = PRNG(33, upperLimit)
    prng2 = PRNG(34, upperLimit)
    seq1 = [prng1.next_int() for _ in range(100)]
    seq2 = [prng2.next_int() for _ in range(100)]
    if seq1 == seq2:
        return False

    # test 4 pas nécessaire 
    # test 4 , vérifier que la meme seed génère les meme nombres
    #prng1 = PRNG(33, upperLimit)
    #prng2 = PRNG(33, upperLimit)
    #seq1 = [prng1.next_int() for _ in range(100)]
    #seq2 = [prng2.next_int() for _ in range(100)]
    #if seq1 != seq2:
    #    return False

    # nécessaire 
    # Test 5: tes pour seed 3 et 10 
    for seed in [3, 10]:
        prng = PRNG(seed, upperLimit)
        numbers = [prng.next_int() for _ in range(num_samples)]
        counts = [0] * upperLimit
        for n in numbers:
            counts[n] += 1
        if min(counts) == 0:
            return False

    # Test 6: vérifier l'absence de cycles courts
    prng = PRNG(33, upperLimit)
    sequence_length = 1000
    numbers = [prng.next_int() for _ in range(sequence_length)]
    max_cycle_length = sequence_length // 2 # random , peut etre changer plus tard 

    for cycle_length in range(2, max_cycle_length):
        pattern = numbers[:cycle_length]
        repeats = True
        for i in range(cycle_length, sequence_length, cycle_length):
            # not sure ... 
            if i + cycle_length > sequence_length:
                break
            if numbers[i:i+cycle_length] != pattern:
                repeats = False
                break
        if repeats:
            return False

    # pas nécessaire présent dans la version originale mais pas nécessaire 
    # Test 7; vérifier période 2 
    #prng = PRNG(33, upperLimit)
    #sequence_length = 2000
    #numbers = [prng.next_int() for _ in range(sequence_length)]
    #for offset in range(1, sequence_length // 2):
    #    if numbers[:sequence_length - offset] == numbers[offset:]:
    #        return False  # La séquence se répète, période détectée

    return True

#################################################################################
#################################################################################

#################################################################################
# version 2 , fonctionne 
#################################################################################

# j'ai remarqué une similitude dans le test 2 et le test4
# je vais donc essayer de les fusionner 
def test1_and_2(PRNG, upperLimit, num_samples):

    # nous allons tester avec 3 seed , on augemntera si nécessaire , mais pour l'instant c'est suffisant 
    for seed in [3, 10, 33]:
        prng = PRNG(seed, upperLimit)
        numbers = [prng.next_int() for _ in range(num_samples)] # on crée une liste avce les nombres générés

        # vérifier les nombres valides, donc [0 , upperLimits - 1]
        for n in numbers:
            if n < 0 or n >= upperLimit:
                return False
        
        # vérification que tt les nombres dans la plage soient générés
        counts = [0] * upperLimit # on crée une liste de [0] avec le nombre upperLimits 
        for n in numbers:
            counts[n] += 1 # à chaque fois qu'on croise un nombre dans la liste number on incrémente son indice dans la liste counts,
            # ainsi nous ne aurons qu'a vérifier quel indice est à 0 dans la liste pour savoir quel nombre n'a pas été généré 

        # ici on vérifie si l'indice le plus petit dans la liste est 0 , si c'est le cas c'est que un nombre n'a pas été généré 
        if min(counts) == 0:
            return False
    return True

    # version 1 
    # Test 1 ) vérif que les nb sont val
    #prng = PRNG(33, upperLimit)
    #numbers = [prng.next_int() for _ in range(num_samples)]
    #for n in numbers:
    #    if n < 0:
    #        return False 
    #    if n >= upperLimit:
    #        return False
    ## Test 2: verif que tt les nombres sont gen , dans 0 à upperLimit
    #counts = [0] * upperLimit
    #for n in numbers:
    #    counts[n] += 1
    #if min(counts) == 0:# si le plus petit nombre est 0 c'est que jen à un qui manque 
    #    return False
    #return True

def test3(PRNG, upperLimit):
    # nécessaire , présent dans la version originale mais pas nécéssaire 
    # Test 3 vérifier que des seed diff produisent des res différents
    prng1 = PRNG(33, upperLimit)
    prng2 = PRNG(34, upperLimit)
    seq1 = [prng1.next_int() for _ in range(100)]
    seq2 = [prng2.next_int() for _ in range(100)]
    if seq1 == seq2:
        return False
    return True

#def test4(PRNG, upperLimit, num_samples):
#    # Test 4: tes pour seed 3 et 10 
#    for seed in [3, 10]:
#        prng = PRNG(seed, upperLimit)
#        numbers = [prng.next_int() for _ in range(num_samples)]
#        counts = [0] * upperLimit
#        for n in numbers:
#            counts[n] += 1
#        if min(counts) == 0:
#            return False
#    return True

def test5(PRNG, upperLimit):
    # Test 5: vérifier l'absence de cycles courts
    prng = PRNG(33, upperLimit)
    sequence_length = 1000
    numbers = [prng.next_int() for _ in range(sequence_length)]
    max_cycle_length = sequence_length // 2 # random , peut etre changer plus tard 

    for cycle_length in range(2, max_cycle_length):
        pattern = numbers[:cycle_length]
        repeats = True
        for i in range(cycle_length, sequence_length, cycle_length):
            # not sure ... 
            if i + cycle_length > sequence_length:
                break
            if numbers[i:i+cycle_length] != pattern:
                repeats = False
                break
        if repeats:
            return False
    return True

def is_correct(PRNG):
    upperLimit = 11
    num_samples = 1000

    # test 1 & 2 
    if not test1_and_2(PRNG, upperLimit, num_samples):
        return False

    # test 3 
    if not test3(PRNG, upperLimit):
        return False

    # test 4 
    #if not test4(PRNG, upperLimit, num_samples):
    #    return False
    
    # test 5 
    if not test5(PRNG, upperLimit):
        return False

    return True


#################################################################################
#################################################################################

#################################################################################
# version 3 : Version FINALE test finale 
#################################################################################

# j'ai remarqué une similitude dans le test 2 et le test4
# je vais donc essayer de les fusionner 
def test1_and_2(PRNG, upperLimit):
    
    num_samples = 1000 # nombre d'éléments que on vas mettre dans la liste 

    # nous allons tester avec 3 seed , on augemntera si nécessaire , mais pour l'instant c'est suffisant 
    for seed in [3, 10, 33]:
        prng = PRNG(seed, upperLimit)
        numbers = [prng.next_int() for _ in range(num_samples)] # on crée une liste avce les nombres générés

        # vérifier les nombres valides, donc [0 , upperLimits - 1]
        for n in numbers:
            if n < 0 or n >= upperLimit:
                return False
        
        # vérification que tt les nombres dans la plage soient générés
        counts = [0] * upperLimit # on crée une liste de [0] avec le nombre upperLimits 
        for n in numbers:
            counts[n] += 1 # à chaque fois qu'on croise un nombre dans la liste number on incrémente son indice dans la liste counts,
            # ainsi nous ne aurons qu'a vérifier quel indice est à 0 dans la liste pour savoir quel nombre n'a pas été généré 

        # ici on vérifie si l'indice le plus petit dans la liste est 0 , si c'est le cas c'est que un nombre n'a pas été généré 
        if min(counts) == 0:
            return False
    return True

def test3(PRNG, upperLimit):
    # nécessaire , présent dans la version originale mais pas nécéssaire 
    # Test 3 vérifier que des seed diff produisent des res différents
    prng1 = PRNG(33, upperLimit)
    prng2 = PRNG(34, upperLimit)
    seq1 = [prng1.next_int() for _ in range(100)]# on crée 2 liste de 100 nombres avec chaque prng
    seq2 = [prng2.next_int() for _ in range(100)]
    if seq1 == seq2:# si les 2 séquences sont identiques, on renvoi false , car elel devraient etre différente ua vu que elle ne ont pas la meme seed
        return False
    return True # sinon on renvoi true car elle ne sont pas les memes 

# notes à savoir, 
# Slicing : permet de etraire une sous liste d'une liste en spécifiant les indices de départ et de fin(1 à 10, 1 : 10) , si il n'y à pas d'indice de départ (:10), l'indice de dpéart est 0 
# condition i + cycle_leght > sequence_lenght : utilisé pour éviter de sortir des limites de la liste
# condition numbers[i:i+cycle_lenght] != pattern : vérifie si la portion de la séquence courante correspond au patterne recherche ou pas
def test5(PRNG, upperLimit):
    # Test 5: vérifier l'absence de cycles courts
    prng = PRNG(33, upperLimit)
    sequence_length = 1000 # le nombre de nombres généré dans la liste
    numbers = [prng.next_int() for _ in range(sequence_length)] # liste contenant les nombres que nous allons vérifier
    max_cycle_length = sequence_length // 2 # la taille maximum de chaque cycle, on met la moitié de sequence_lenght car on doit pouvoir avoir au moins 2 séquences 

    # ! ATTENTION utilisation du Slicing ici , ne pas se perdre
    for cycle_length in range(2, max_cycle_length):
        pattern = numbers[:cycle_length]# donc on commence par crée une liste , contanant un certain nombre de chiffres, représentant le patterne que nous allons vérifier
        for i in range(cycle_length, sequence_length, cycle_length):# on commence à cycle l'enght, et on avance de la longueur du cycle a travers la liste de nombres 
            # i == indice actuelle dans la liste, cycle_lenght == longueur du cycle qu'on veut tester, seq_length == la longueur de la séquence (1000)
            if i + cycle_length > sequence_length:# vérifications de dépassement de liste
                return True # si on à dépasse on return True car aucun patterne n'a été retrouvé 
            # Alors ici il vas falloir se concentrer :
            # ici on utilise le sclicing pour vérifier si chaque portion de number correspond au patterne qu'on vérifie
            # donc si on est à i == 5 et que cycle_lenght est de 20, on vérifie la portion de numbers (liste) de l'indice 5 à 5 + 20 donc 25 , donc de 5 à 25 ou 5:25 ;) 
            if numbers[i:i+cycle_length] != pattern: # si une portion de la liste ne correspond pas au petterne c'est bon 
                break # on break pour sortir de la boucle et commencer à vérifier une nouvelle séquence 
            else:
                return False # sinon c'est que le patterne se répète sur toute la longueur , donc faux 
    return True

def is_correct(PRNG):
    upperLimit = 11

    # test 1 & 2 
    if not test1_and_2(PRNG, upperLimit):
        return False
    # test 3 
    if not test3(PRNG, upperLimit):
        return False
    # test 5 
    if not test5(PRNG, upperLimit):
        return False
    return True


#################################################################################
#################################################################################


# def verifySeq(prng, upperLimit):
#     count = 50 # nombre de tours, y aurais il trop de nombres vérifié ? 
#     previous_val = [] # liste contenant les ancienne valeurs
#     max_occurence = 3 # max 3 fois 
# 
#     for _ in range(count):
#         value = prng.next_int()
#         if value < 0 or value > upperLimit - 1:
#             return False
#         previous_val.append(value) # on met la nouvelle val dans la liste
# 
#     for value in previous_val:
#         if previous_val.count(value) > max_occurence:
#             return False
# 
#     return True
# 
# def verify_double(PRNG, upperLimit):
#     l1 = []
#     l2 = []
# 
#     pr1 = PRNG(33, upperLimit)
#     pr2 = PRNG(34, upperLimit)
# 
#     for i in range(30):
#         val1 = pr1.next_int()
#         val2 = pr2.next_int()
#         l1.append(val1)
#         l2.append(val2)
#     if l1 == l2:
#         return False
#     return True
# 
# def is_correct(PRNG):
#     upperLimit = 11
#     
#     if not verify_double(PRNG, upperLimit):
#         return False
# 
#     for i in range(1, 50):
#         prng = PRNG(i, upperLimit)
#         if not verifySeq(prng, upperLimit):
#             return False
#     return True 

#################################################################################
#################################################################################

# version plus simple ... 
# vérifier si les nombres généré respectent les intervalles 
#def test_full_coverage(PRNG, upperLimit):
#    prng = PRNG(33, upperLimit)
#    generated_numbers = set()
#    for _ in range(1000):  # gen 1000 nombres
#        generated_numbers.add(prng.next_int())
#
#    # verif
#    if len(generated_numbers) == upperLimit:
#        return True  # si tout les nombres sont présents 
#    else:
#        return False  # faux 
#
## vérifier que plusieurs graines donnent des res différents 
#def test_different_seeds(PRNG, upperLimit):
#    for i in range(1, 100):
#        prng1 = PRNG(i, upperLimit)
#        prng2 = PRNG(i + 1, upperLimit)
#
#		# génère 100 nombres pr chaque seed
#        seq1 = [prng1.next_int() for _ in range(100)]
#        seq2 = [prng2.next_int() for _ in range(100)]
#
#        if seq1 == seq2:
#            return False 
#
#    return True
#
#    #prng1 = PRNG(33, upperLimit)
#    #prng2 = PRNG(34, upperLimit)
#    #seq1 = [prng1.next_int() for _ in range(100)]
#    #seq2 = [prng2.next_int() for _ in range(100)]
#    #return seq1 != seq2
#
## vérifier les cycles évidents dans les 100 premiers nombres 
#def test_no_cycles(PRNG, upperLimit):
#    prng = PRNG(33, upperLimit)
#    seq = [prng.next_int() for _ in range(100)]
#    # vérification d'une sous séquence de 50 
#    return seq[:50] != seq[50:]  # si une séquences de 50 nombres se suit alors , il y à une erreur 
#
## Fonction principale qui vérifie si le PRNG est correct
#def is_correct(PRNG):
#    upperLimit = 11  
#
#    if not test_full_coverage(PRNG, upperLimit):
#        return False
#    if not test_different_seeds(PRNG, upperLimit):
#        return False
#    if not test_no_cycles(PRNG, upperLimit):
#        return False
#
#    return True

#################################################################################
#################################################################################


"""""
# Fonction qui vérifie si un nombre est constitué d'un seul chiffre
def isOlyOneNum(number):
    numberStr = str(number)
    val = numberStr[0]
    for char in numberStr:
        if char != val:
            return False
    return True

# Fonction qui vérifie si un nombre est négatif
def isNeg(nbr):
    return nbr < 0

# Fonction qui vérifie si la longueur du nombre est de 1 (peu de variété)
def isLen1(nbr):
    return len(str(nbr)) == 1

# Fonction pour tester si une nouvelle seed produit une nouvelle séquence
def test_new_seed(PRNG):
    prng1 = PRNG(33, 11)
    prng2 = PRNG(44, 11)
    seq1 = [prng1.next_int() for _ in range(10)]
    seq2 = [prng2.next_int() for _ in range(10)]
    return seq1 != seq2  # Les séquences doivent être différentes

# Fonction pour tester si tous les nombres de l'intervalle sont générés
def test_full_range(PRNG, seed, interval):
    prng = PRNG(seed, interval)
    generated = set(prng.next_int() for _ in range(interval * 10))  # On génère beaucoup de nombres
    return len(generated) == interval  # Tous les nombres doivent être générés

# Fonction principale pour vérifier le PRNG
def is_correct(PRNG):
    prng = PRNG(33, 11)  # On crée le PRNG avec une seed et un interval

    # Vérification 1: Vérifier si le PRNG génère des nombres répétitifs (tous identiques)
    for _ in range(10):  # On teste sur 10 nombres
        if isOlyOneNum(prng.next_int()):
            return False

    # Vérification 2: Vérifier si le PRNG génère des nombres négatifs (si cela n'est pas autorisé)
    for _ in range(10):
        if isNeg(prng.next_int()):
            return False

    # Vérification 3: Vérifier si une nouvelle seed produit une nouvelle séquence
    if not test_new_seed(PRNG):
        return False

    # Vérification 4: Vérifier que tous les nombres de l'intervalle sont générés au moins une fois
    if not test_full_range(PRNG, 33, 11):
        return False

    # Si toutes les vérifications sont passées, on retourne True
    return True

# Exemple d'utilisation
# Ici, tu pourrais tester différents PRNGs comme tu le faisais avec `input`, mais IngInious utilisera le sien.
"""""