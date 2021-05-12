from gestion_data import *
#
# Fichier regroupant les fonctions relatives à l'action de manger
#


# Vérification si le joueur doit manger
def indication_doit_manger(joueur, deplacement_simple):
  """
    Fonction qui nous indique si le joueur doit manger

    input (bool): le joueur qui joue
    input (bool): évite que la prédiction bloque le déplacement dans le cas d'un déplacment simple
    return (list): nous indique quel pion manger
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