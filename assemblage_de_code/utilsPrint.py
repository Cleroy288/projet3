import pyfiglet

result = pyfiglet.figlet_format("QCM TIME!")
print(result)

def print_bordered_message(message):
    border = "+" + "-" * (len(message) + 2) + "+"
    print(border)
    print(f"| {message} |")
    print(border)

print_bordered_message("Bienvenue au QCM !")

from colorama import init, Fore, Style

init()  # Initialisation de colorama

print(Fore.GREEN + "C'est parti pour le QCM !" + Style.RESET_ALL)
print(Fore.RED + "Attention : réponse incorrecte !" + Style.RESET_ALL)

import time

def print_with_delay(message, delay=1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay / len(message))
    print()

print_with_delay("Chargement du QCM...", 2)

import pyfiglet
from colorama import init, Fore, Style
import time

# Initialisation de colorama pour les couleurs
init()

def print_bordered_message(message):
    border = "+" + "-" * (len(message) + 2) + "+"
    print(border)
    print(f"| {message} |")
    print(border)

def print_separator(char='*', length=50):
    print(char * length)

def print_with_delay(message, delay=1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay / len(message))
    print()

# Exemple de mise en forme
print(Fore.CYAN + pyfiglet.figlet_format("QCM TIME!") + Style.RESET_ALL)
print_bordered_message("Bienvenue à notre QCM !")

print_with_delay("Préparez-vous...", 2)
print_separator('-')

print(Fore.GREEN + "C'est parti pour la première question !" + Style.RESET_ALL)


import pyfiglet
from colorama import init, Fore, Style
import random

# Initialisation de colorama
init()

# Liste de couleurs possibles dans colorama
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Générer le texte en grand format avec pyfiglet
figlet_text = pyfiglet.figlet_format("ON VAS CHEZ QUICK WESH!")

# Fonction pour colorier chaque lettre de manière aléatoire
def colorize_figlet_text(text):
    for line in text.splitlines():  # Traiter chaque ligne du texte
        colored_line = ""
        for char in line:  # Boucle sur chaque caractère
            if char.strip():  # Appliquer une couleur seulement aux caractères visibles
                colored_line += random.choice(colors) + char + Style.RESET_ALL
            else:
                colored_line += char  # Ne rien faire pour les espaces
        print(colored_line)

# Appel de la fonction pour afficher le texte avec des couleurs
colorize_figlet_text(figlet_text)