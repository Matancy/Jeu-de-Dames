from game_data import *
from dame import *


# Gestion des déplacements du joueur
def quel_deplacement(source, destination, joueur, prevision):

  joueur = quel_joueur(joueur)

  # Conversion des coordonnées
  xo = int(source[:1])
  yo = int(source[1:])
  xd = int(destination[:1])
  yd = int(destination[1:])

  # On regarde si c'est le bon joueur qui joue
  if joueur in damier[xo][yo]:

    # On regarde si il s'agit d'un déplacement simple
    result = is_deplacement(xo, xd, yo, yd)
    global deplacement_simple
    if result == True:
      deplacement_simple = 1
    else:
      deplacement_simple = 0

    # Vérification si la case est existante
    result = case_existante(xd, yd)
    if result != True:
      print ("Case incorrecte (case_possible)")
      return False
  
    # Vérification si la case est prise
    result = case_vide(xd, yd)
    if result != True:
      print ("Case prise (case_vide)")
      return False

    # Vérification si le déplacement est possible
    result = deplacement_possible(xo, xd, yo, yd)
    if result != True:
      print("Déplacement impossible (deplacement_possible)")
      return False

    #Vérification si on a affaire à une dame ou un pion
    if joueur == "\033[94mX\033[0m" or joueur == "\033[94mO\033[0m":
      pass
    else:  

      # Vérification si on doit manger
      result = manger(xo, xd, yo, yd, joueur, prevision)
      if result == True:
        print(f'{bcolors.OKGREEN}Joueur mangé{bcolors.ENDC}')
      elif result == False:
        print("Déplacement impossible (manger)")
        return False
      elif result == "doitmanger":
        print("Vous devez manger")
        return False
      else:
        result = deplacement_arriere(xo, xd, joueur)
        if result == False:
          print('Déplacement impossible (deplacement_arriere)')
          return False

    # Sauvegarde
    sauvegarde(destination, joueur) # Déplacement joueur
    sauvegarde(source, "-") # Vider la case précédente

    # On retourne le type de déplacement effectué
    return deplacement_simple
  else:
    print(f'{bcolors.WARNING}Mauvais joueur{bcolors.ENDC}')
    return False


# Fonction pour voir si c'est un déplacement
def is_deplacement(xo, xd, yo, yd):
  if xd + 1 == xo or xd - 1 == xo and yd + 1 == yo or yd - 1 == yo:
    return True


# Vérification si le joueur doit manger
def indication_doit_manger(joueur, deplacement_simple):
  prevision = []
  joueur_inverse = quel_joueur(not joueur)
  joueur = quel_joueur(joueur)

  if deplacement_simple == 1:
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

# Sauvegarde des informations de jeu
def sauvegarde(destination, joueur):

  # Conversion des coordonnées
  xd = int(destination[:1])
  yd = int(destination[1:])
  
  # Modification dans les informations du jeu
  damier[xd][yd] = joueur
  

# Fonction pour savoir quel joueur joue
def quel_joueur(joueur):
  if isinstance(joueur, bool):
    if joueur: 
      joueur = 'O'
    elif joueur == False:
      joueur = 'X'
  else: 
    joueur = '-'
  return joueur


# Fonction pour savoir si la case existe
def case_existante(x, y):
  if damier[x][y] != '':
    return True
  else:
    return False
    

# Fonction pour vérifier que la case est vide
def case_vide(x, y):
  return damier[x][y] == '-'


# Fonction pour vérifier que le déplacement est possible
def deplacement_possible(xo, xd, yo, yd): 
  return yo != yd

  
# Vérification qu'on aille pas en arrière pour rien
def deplacement_arriere(xo, xd, joueur):
  if joueur == "X" and xo + 1 == xd:
    return False
  elif joueur == "O" and xo - 1 == xd:
    return False


# Fonction pour regarder si on peut manger
def manger(xo, xd, yo, yd, joueur, prevision):
  # On vérifie que la personne respecte bien les indications
  if prevision != [] and f"D{xd}{yd}" and f"S{xo}{yo}" not in prevision:
    return "doitmanger"

  # On calcule les coordonnées du point au milieu
  if yo + 2 == yd:
    ymilieu = yd - 1
  elif yd + 2 == yo:
    ymilieu = yd + 1
  elif yd + 1 == yo or yd - 1 == yo:
    return "nointention"
  else:
    return False # Aucune volonté de manger

  # On regarde si on a un déplacement pour manger (2 lignes)
  if joueur == "X":
      # Manger en avant pour X
      if damier[xd + 1][ymilieu] == "O" and xo-2 == xd:
        # On enregistre les déplacements
        xmilieu = xd + 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return True
      # Manger en arrière pour X
      elif damier[xd - 1][ymilieu] == "O" and xo+2 == xd:
        # On enregistre les déplacements
        xmilieu = xd - 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return True
      else:
        return False
  else:
      # Manger avant pour O
      if damier[xd - 1][ymilieu] == "X" and xo+2 == xd:
        # On enregistre les déplacements
        xmilieu = xd - 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return True
      # Manger arrière pour O
      elif damier[xd + 1][ymilieu] == "X" and xo-2 == xd:
        # On enregistre les déplacements
        xmilieu = xd + 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        print(xd+1, ymilieu)
        return True
      else:
        return False
  return False

