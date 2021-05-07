from game_data import *
#
# Fichier regroupant les fonctions de vérification du damier
#


# Vérifier si la case est existante
def case_existante(x, y):
  """
    Fonction qui nous informe si la case existe dans le deplacement_arriere

    input (int) x,y: coordonnées de la case
    return (bool): True / False
  """
  if damier[x][y] != '':
    return True
  else:
    return False


# Vérification si la case est vide
def case_vide(x, y):
  """
    Fonction qui regarde si la case est vide

    input (int) x,y: coordonnées de la case
    return (bool): True ou False
  """
  return damier[x][y] == '-'