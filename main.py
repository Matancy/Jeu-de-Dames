from affichage_damier import *
from jeu import *
from game_data import *
from fin_de_partie import *
from dame import *
from pygame_code import *

# Variable de déplacement évitant de bloquer le jeu par la prévision
deplacement_simple = False

while partie != 5:

    # On regarde si le joueur précédent peut encore manger
    prevision = indication_doit_manger(joueur, deplacement_simple)

    # Si on ne peut pas manger, on change de joueur
    if prevision == []:

        # Réinitialisation du type de déplacement et inversion du joueur
        deplacement_simple = False
        joueur = not joueur

        # On refais les indications de déplacement avec le nouveau joueur
        prevision = indication_doit_manger(joueur, deplacement_simple)

    # On affiche la grille de jeu
    affichage_damier(damier)

    # On demande quel déplacement le joueur veut faire
    player_name = quel_joueur(joueur)
    print(f"{bcolors.UNDERLINE}Joueur :{bcolors.ENDC} {player_name}")
    source = str(input("Emplacement source : "))
    destination = str(input("Emplacement destination : "))

    # On déplace le joueur
    result = quel_deplacement(source, destination, joueur, prevision)

    # Si on a une erreur sur le fonctionnement, on fait rejouer le joueur
    if result == "Erreur":
        if prevision == []:
            joueur = not joueur

    # Si le joueur fait un déplacement simple, pour pas le bloquer
    elif result == "deplacement_simple":
        deplacement_simple = True

    # On regarde si une dame est crée
    #is_new_dame()

    # On regarde si la partie est terminée
    result = is_game_finished()
    if result != "partie-en-cours":
        print(result)
        partie = 5
