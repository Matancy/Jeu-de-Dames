#
# Fichier regroupant les fonctions de gestion de données
#
from data import *


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