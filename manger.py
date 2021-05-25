from gestion_data import *
#
# Fichier regroupant les fonctions relatives à l'action de manger
#


# Vérification si le joueur doit manger
def indication_doit_manger(joueur, deplacement_simple):
  """
    Fonction qui nous indique si le joueur doit manger

    Input (bool): Joueur, type de déplacement
    Return (list): Quel pions on doit manger
  """
  prevision = []
  joueur_inverse = quel_joueur(not joueur)
  joueur = quel_joueur(joueur)

  if deplacement_simple == True:
    return []

  for x in range(10):
    for y in range(10):
      tableau = [
          [[x-2], [y-2], [x-1], [y-1]],
          [[x+2], [y-2], [x+1], [y-1]],
          [[x-2], [y+2], [x-1], [y+1]],
          [[x+2], [y+2], [x+1], [y+1]]
      ]

      if joueur == damier[x][y]:
        for el in tableau:
          if 0 <= int(el[0][0]) <= 9 and 0 <= int(el[1][0]) <= 9:
            if damier[el[0][0]][el[1][0]] == "-" and damier[el[2][0]][el[3][0]] == joueur_inverse:
              print(f"{bcolors.WARNING}{x}{y} doit manger en {el[0][0]}{el[1][0]}{bcolors.ENDC}")
              prevision.append(f"S{x}{y}")
              prevision.append(f"D{el[0][0]}{el[1][0]}")

  return prevision


# Fonction pour regarder si on peut manger
def manger(xo, xd, yo, yd, joueur, prevision):
  """
    Fonction qui permet de regarder si on peut manger

    Input (int) x4, (bool), (list): Coordonnées xo, xd, yo, yd, joueur, prévision
    Return (bool): True / False

  """
  # On vérifie que la personne respecte bien les indications
  result = respect_indications(xo, xd, yo, yd, prevision)
  if result == "doitmanger":
    return "doitmanger"

  # On calcule les coordonnées du point au milieu
  result = middle_coords(yo, yd)
  if result == "nointention":
    return "nointention"
  else:
    ymilieu = result

  xmilieu = [
    ["O", xd+1, xo-2, "X"],
    ["O", xd-1, xo+2, "X"],
    ["X", xd+1, xo-2, "O"],
    ["X", xd-1, xo+2, "O"]
  ]
  for el in xmilieu:
    # On regarde si on a le bon joueur => appliquer les bonnes situations
    if joueur == el[0]:
      # On regarde si le joueur à manger est bien entre la source et destination, et si la destination est la bonne
      if damier[int(str(el[1]))][ymilieu] == el[3] and el[2] == xd:
        # On enregistre les déplacements
        sauvegarde(f"{el[1]}{ymilieu}", "-")
        return "mange"
  return "pasmange"