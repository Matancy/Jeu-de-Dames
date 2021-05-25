from data import *
from config import *
from pygame_code import*
#
# Fichier regroupant les fonctions de gestion de données
#


# Sauvegarde des informations de jeu
def sauvegarde(destination, joueur):
    """
    Fonction qui sauvegarde les déplacements des joueurs
    Input (int), (bool): Coordonnées, joueur
    Return : Void
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
def convert_case_x(case):
    """
    Fonction pour convertir les coordonnées de case permettant de créer les cases
    Input (int) : Case x
    Return (int) : Dimmensions de la case
    """
    return int((game_display_size/20)+(2*case*game_display_size/20))


# Fonction pour convertir les coordonnées y en coordonnées plateau
def convert_case_y(case):
    """
    Fonction pour convertir les coordonnées de case permettant de créer les cases
    Input (int) : Case y
    Return (int) : Dimmensions de la case
    """
    return int((game_display_size/20)+(2*case*game_display_size/20))


# Fonction pour convertir les coordonnées lorsque l'on clique sur une case
def convert_co_x(X):
  return X//(int(size/10))


# Fonction pour convertir les coordonnées lorsque l'on clique sur une case
def convert_co_y(Y):
  return Y//(int(size/10))

# Fonction pour vérifier si on respecte les indications
def respect_indications(xo, xd, yo, yd, prevision):
    """
    Fonction pour vérifier que la prédiction est respectée
    Input (int) x4, (list): Coordonnées xo, xd, yo, yd, prévision
    Return (str): Message de confirmation / refus
    """
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
    """
    Fonction qui permet de calculer les coordonnées du pion entre deux
    Input (int) x2: Coordonnées yo, yd
    Return (int), (str): coords, message
    """
    if yo + 2 == yd:
        return yd - 1
    elif yd + 2 == yo:
        return yd + 1
    elif yd + 1 == yo or yd - 1 == yo:
        return "nointention"
    else:
        return "nointention"  # Aucune volonté de manger