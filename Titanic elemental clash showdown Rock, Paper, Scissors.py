import random

class Personnage:
    def __init__(self, nom, vies=3):
        self.nom = nom
        self.vies = vies

def choix_coup():
    coup = input("Choisissez votre coup (pierre/feuille/ciseaux): ").lower()
    while coup not in ['pierre', 'feuille', 'ciseaux']:
        print("Coup invalide. Veuillez choisir parmi pierre, feuille, ou ciseaux.")
        coup = input("Choisissez votre coup (pierre/feuille/ciseaux): ").lower()
    return coup

def choix_coup_adversaire():
    return random.choice(['pierre', 'feuille', 'ciseaux'])

def combat(personnage1, personnage2):
    coup_personnage1 = choix_coup()
    coup_personnage2 = choix_coup_adversaire()

    print(f"{personnage1.nom} attaque avec {coup_personnage1}")
    print(f"{personnage2.nom} attaque avec {coup_personnage2}")

    if coup_personnage1 == coup_personnage2:
        print("Égalité!")
    else:
        if (coup_personnage1 == 'pierre' and coup_personnage2 == 'ciseaux') or \
           (coup_personnage1 == 'feuille' and coup_personnage2 == 'pierre') or \
           (coup_personnage1 == 'ciseaux' and coup_personnage2 == 'feuille'):
            print(f"{personnage1.nom} gagne! {personnage2.nom} perd une vie.")
            personnage2.vies -= 1
        else:
            print(f"{personnage2.nom} gagne! {personnage1.nom} perd une vie.")
            personnage1.vies -= 1

    print(f"{personnage1.nom} a {personnage1.vies} vie(s) restante(s).")
    print(f"{personnage2.nom} a {personnage2.vies} vie(s) restante(s).")

# Fonction pour la séquence de combats contre les boss
def sequence_combats(personnage, boss_list):
    for boss in boss_list:
        personnage.vies = 3  # Réinitialisation des vies de Billy à 3 avant chaque combat
        print(f"{personnage.nom} se prépare à affronter {boss.nom}!")
        while personnage.vies > 0 and boss.vies > 0:
            combat(personnage, boss)
        if boss.vies <= 0:
            print(f"{boss.nom} a été vaincu! {personnage.nom} passe au boss suivant.")
        else:
            print(f"{personnage.nom} a été vaincu par {boss.nom}. La quête est terminée.")
            break

# Création des personnages
billy = Personnage("Billy")
djilsi = Personnage("Djilsi")
gmk = Personnage("GMK")
squeezie = Personnage("Squeezie")
dark_billy = Personnage("Dark Billy")

# Séquence de combats contre les boss
boss_list = [djilsi, gmk, squeezie, dark_billy]
sequence_combats(billy, boss_list)

# Affichage du résultat final
if billy.vies > 0:
    print(f"{billy.nom} a vaincu tous les boss et remporte la victoire!")
else:
    print(f"{billy.nom} a échoué dans sa quête. Mieux chance la prochaine fois.")
