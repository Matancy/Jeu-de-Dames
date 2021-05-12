from data import *
from gestion_data import *
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
    [["O"], [xd+1], [xo-2], ["X"]],
    [["O"], [xd-1], [xo+2], ["X"]],
    [["X"], [xd+1], [xo-2], ["O"]],
    [["X"], [xd-1], [xo+2], ["O"]]
  ]
  for el in xmilieu:
    # On regarde si on a le bon joueur => appliquer les bonnes situations
    if joueur == el[0][0]:
      # On regarde si le joueur à manger est bien entre la source et destination, et si la destination est la bonne
      if damier[el[0][1]][ymilieu] == el[0][3] and el[0][2] == xd:
        # On enregistre les déplacements
        sauvegarde(f"{el[0][1]}{ymilieu}", "-")
    return "mange"
  return "pasmange"
