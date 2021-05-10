from data import *
from verification_dame import *
from verification_deplacement import *
from verification_damier import *


# Gestion des déplacements du joueur
def quel_deplacement(source, destination, joueur, prevision):
  """
    Fonction qui va gérer les déplacements des pions

    input source: coordonnées de la case de départ du pion à déplacer
    input destination: coordonnées de la case de destination du pion à déplacer
    input joueur: le joueur qui joue
    input prevision: stocke les indications pour manger

    return booléen: False (le déplacement est impossible)
    return booléen: True (le déplacement est possible)
  """

  joueur = quel_joueur(joueur)

  # Conversion des coordonnées
  xo = int(source[:1])
  yo = int(source[1:])
  xd = int(destination[:1])
  yd = int(destination[1:])

  # On regarde si c'est le bon joueur qui joue
  if joueur in damier[xo][yo]:

    # On regarde si il s'agit d'un déplacement simple
    result = is_deplacement_simple(xo, xd, yo, yd)
    global deplacement_simple
    if result == True:
      deplacement_simple = "deplacement_simple"
    else:
      deplacement_simple = "deplacement_complexe"

    # Vérification si la case est existante
    result = case_existante(xd, yd)
    if result != True:
      print ("Case incorrecte (case_possible)")
      return "Erreur"
  
    # Vérification si la case est prise
    result = case_vide(xd, yd)
    if result != True:
      print ("Case prise (case_vide)")
      return "Erreur"

    # Vérification si le déplacement est possible
    result = deplacement_possible(xo, xd, yo, yd)
    if result != True:
      print("Déplacement impossible (deplacement_possible)")
      return "Erreur"

    #Vérification si on a affaire à une dame ou un pion
    if joueur == "\033[94mX\033[0m" or joueur == "\033[94mO\033[0m":
      pass
    else:  

      # Vérification si on doit manger
      result = manger(xo, xd, yo, yd, joueur, prevision)
      if result == "mange":
        print(f'{bcolors.OKGREEN}Joueur mangé{bcolors.ENDC}')
      elif result == "pasmange":
        print("Déplacement impossible (manger)")
        return "Erreur"
      elif result == "doitmanger":
        print("Vous devez manger")
        return "Erreur"
      else:
        result = deplacement_arriere(xo, xd, joueur)
        if result == "pasmange":
          print('Déplacement impossible (deplacement_arriere)')
          return "Erreur"

    # Sauvegarde
    sauvegarde(destination, joueur) # Déplacement joueur
    sauvegarde(source, "-") # Vider la case précédente

    # On retourne le type de déplacement effectué
    return deplacement_simple
  else:
    print(f'{bcolors.WARNING}Mauvais joueur{bcolors.ENDC}')
    return "Erreur"


# Vérification si le joueur doit manger
def indication_doit_manger(joueur, deplacement_simple):
  """
    Fonction qui nous indique si le joueur doit manger

    input joueur: le joueur qui joue
    input deplacement_simple: évite que la prédiction bloque le déplacement dans le cas d'un déplacment simple

    return prevision: nous indique quel pion manger
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

# Sauvegarde des informations de jeu
def sauvegarde(destination, joueur):
  """
    Fonction qui sauvegarde les déplacements des joueurs

    input destination: coordonnées de la case de destination du pion
    input joueur: le joueur qui joue

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

    input joueur: le joueur qui joue

    return: joueur
  """
  if isinstance(joueur, bool):
    if joueur: 
      joueur = 'O'
    elif joueur == False:
      joueur = 'X'
  else: 
    joueur = '-'
  return joueur


# Fonction pour regarder si on peut manger
def manger(xo, xd, yo, yd, joueur, prevision):
  """
    Fonction qui permet de regarder si on peut manger

    input xo, xd, yo, yd: coordonnées des cases de départ et de destination du pion
    input joueur: le joueur qui joue
    input prevision: stocke les indications pour manger

    return booléen: True (on peut manger)
    return booléen: False (on ne peut pas manger)

  """
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
    return "nointention" # Aucune volonté de manger

  # On regarde si on a un déplacement pour manger (2 lignes)
  if joueur == "X":
      # Manger en avant pour X
      if damier[xd + 1][ymilieu] == "O" and xo-2 == xd:
        # On enregistre les déplacements
        xmilieu = xd + 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return "mange"
      # Manger en arrière pour X
      elif damier[xd - 1][ymilieu] == "O" and xo+2 == xd:
        # On enregistre les déplacements
        xmilieu = xd - 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return "mange"
      else:
        return "pasmange"
  else:
      # Manger avant pour O
      if damier[xd - 1][ymilieu] == "X" and xo+2 == xd:
        # On enregistre les déplacements
        xmilieu = xd - 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        return "mange"
      # Manger arrière pour O
      elif damier[xd + 1][ymilieu] == "X" and xo-2 == xd:
        # On enregistre les déplacements
        xmilieu = xd + 1
        sauvegarde(f"{xmilieu}{ymilieu}", "-")
        print(xd+1, ymilieu)
        return "mange"
      else:
        return "pasmange"
  return "pasmange"

