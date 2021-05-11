from affichage_damier import *
from jeu import *
from config import *
from data import *
from fin_de_partie import *
from verification_dame import *
import pygame

# Variable de déplacement évitant de bloquer le jeu par la prévision
deplacement_simple = False

while partie != 5:

    # Système de fermeture de l'interface graphique
    if game_display_type == "graphical":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                partie = 5

    # On regarde si le joueur précédent peut encore manger
    prevision = indication_doit_manger(joueur, deplacement_simple)

    # Si on ne peut pas manger, on change de joueur
    if prevision == []:

        # Réinitialisation du type de déplacement et inversion du joueur
        deplacement_simple = False
        joueur = not joueur

        # On refais les indications de déplacement avec le nouveau joueur
        prevision = indication_doit_manger(joueur, deplacement_simple)

    # Affichage du plateau de jeu en fonction de la configuration
    if game_display_type == "console":
        affichage_damier_console(damier)
    #else:
        # affichage_damier_graphique(damier)
        # Ne pas oublier de gérer cette zone pour ne pas afficher plusieurs fois le damier


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
