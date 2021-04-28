from affichage_damier import *
from jeu import *
from game_data import *
from fin_de_partie import *
from dame import *
from pygame_code import *

# Variable de déplacement évitant de bloquer le jeu par la prévision
deplacement_simple = 0

while partie != 5:

  # Vérification si on doit manger
  prevision = indication_doit_manger(joueur, deplacement_simple)
  print(joueur)
  print(prevision)

  # Réinitialisation du type de déplacement
  deplacement_simple = 0

  # Si on ne peut pas manger, on change de joueur
  if prevision == []:
   joueur = not joueur

  # On affiche la grille de jeu
  affichage_damier(damier)  

  # On demande quel déplacement le joueur veut faire
  player_name = quel_joueur(joueur)
  print(f"{bcolors.UNDERLINE}Joueur :{bcolors.ENDC} {player_name}")
  source = str(input("Emplacement source : "))
  destination = str(input("Emplacement destination : "))

  # On déplace le joueur
  result = quel_deplacement(source, destination, joueur, prevision)

  # On fait rejouer le joueur
  if result == False:
    if prevision == []:
      joueur = not joueur

  # Si le joueur fait un déplacement simple, pour pas le bloquer
  elif result == 1:
    deplacement_simple = 1

  # On regarde si une dame est crée
  #is_new_dame()
  
  # On regarde si la partie est terminée
  result = is_game_finished()
  if result != "partie-en-cours":
    print(result)
    partie = 5



