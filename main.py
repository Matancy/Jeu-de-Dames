from affichage_damier import *
from jeu import *
from game_data import *
from fin_de_partie import *
from dame import *
from pygame_code import *

# On définie la variable de déplacement
deplacement_simple = False

while partie != 5:

  # Vérification si on doit manger
  prevision = indication_doit_manger(joueur, deplacement_simple)
  if prevision == []:
   joueur = not joueur

  # On affiche la grille de jeu
  affichage_damier(damier)  

  # On demande quel déplacement le joueur veut faire
  player_name = quel_joueur(joueur)
  print(f"{bcolors.UNDERLINE}Joueur :{bcolors.ENDC} {player_name}")
  source = str(input("Emplacement source : "))
  destination = str(input("Emplacement destination : "))
  if quel_deplacement(source, destination, joueur, prevision) == False:
    if prevision == []:
      joueur = not joueur

  # On regarde si un dame est crée
  #is_new_dame()
  
  # On regarde si la partie est terminée
  result = is_game_finished()
  if result != "partie-en-cours":
    print(result)
    partie = 5



