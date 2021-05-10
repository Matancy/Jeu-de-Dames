from data import *
from config import *
#
# Fichier regroupant les fonctions de gestion de données
#


# Sauvegarde des informations de jeu
def sauvegarde(destination, joueur):
    """
      Fonction qui sauvegarde les déplacements des joueurs

      input (int): coordonnées de la case de destination du pion
      input (bool): le joueur qui joue

    """

    # Conversion des coordonnées
    xd = int(destination[:1])
    yd = int(destination[1:])

    # Modification dans les informations du jeu
    damier[xd][yd] = joueur


# Fonction pour savoir quel joueur joue
def quel_joueur(joueur):
  """
    Fonction qui permet d convertir la valeur du joueur en son nom d'usage

    input (bool): le joueur qui joue
    return (str): joueur
  """
  if isinstance(joueur, bool):
    if joueur:
      joueur = 'O'
    elif joueur == False:
      joueur = 'X'
  else:
    joueur = '-'
  return joueur


# Fonction pour convertir les coordonnée x en coordonnés plateau
def convert_x(case):
    return int((game_display_size/20)+(2*case*game_display_size/20))

# Fonction pour convertir les coordonnées y en coordonnées plateau
def convert_y(case):
    return int((game_display_size/20)+(2*case*game_display_size/20))
