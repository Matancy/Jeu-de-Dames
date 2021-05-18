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


# Fonction pour vérifier si on respecte les indications
def respect_indications(xo, xd, yo, yd, prevision):
    # Si la prévision est vide
    if prevision == []:
        return "ok"
    # Boucle pour regarder si le déplacement est dans la prévision
    for i in range(len(prevision)):
        if prevision[i] == f"D{xd}{yd}":
            if prevision[i-1] == f"S{xo}{yo}":
                return "ok"
    else:
        return "doitmanger"



# Fonction pour calculer les coordonées du mileu d'un déplacement
def middle_coords(yo, yd):
    if yo + 2 == yd:
        return yd - 1
    elif yd + 2 == yo:
        return yd + 1
    elif yd + 1 == yo or yd - 1 == yo:
        return "nointention"
    else:
        return "nointention"  # Aucune volonté de manger