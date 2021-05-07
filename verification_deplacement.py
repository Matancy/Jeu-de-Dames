#
# Fichier regroupant toutes les fonctions relatives à la vérification de déplacement
#


# Regarder si il s'agit d'un déplacement simple
def is_deplacement_simple(xo, xd, yo, yd):
  """
    Fonction qui nous informe si c'est un déplacement simple

    input (int) xo, xd, yo, yd: coordonnées des cases de départ et de destination du pion
    return (bool): True / False
  """
  if xd + 1 == xo or xd - 1 == xo and yd + 1 == yo or yd - 1 == yo:
    return True


# Vérifier si le déplacement est possible
def deplacement_possible(xo, xd, yo, yd):
  """
    Fonction qui vérifie que le déplacement est possible

    input (int) xo, xd, yo, yd: coordonnées des cases de départ et de destination du pion
    return (bool): True / False
  """
  return yo != yd


# Vérifier si on ne va pas en arrière
def deplacement_arriere(xo, xd, joueur):
  """
    Fonction qui vérifie qu'on aille pas en arrière

    input (int) xo, xd: coordonnée x de la cases de départ et de la case de destination du pion
    return (bool): False
  """
  if joueur == "X" and xo + 1 == xd:
    return False
  elif joueur == "O" and xo - 1 == xd:
    return False