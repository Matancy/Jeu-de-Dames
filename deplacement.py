from data import *
from gestion_data import *
from verification_dame import *
from verification_deplacement import *
from verification_damier import *
from manger import *


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

  # On récupère la variable du joueur
  joueur = quel_joueur(joueur)

  # Conversion des coordonnées
  xo = int(source[:1])
  yo = int(source[1:])
  xd = int(destination[:1])
  yd = int(destination[1:])

  # On regarde si c'est le bon joueur qui joue
  if joueur in damier[xo][yo]:

    # Vérification si c'est un déplacement simple
    result = is_deplacement_simple(xo, xd, yo, yd)
    global deplacement_simple
    if result == True:
      deplacement_simple = "deplacement_simple"
    else:
      deplacement_simple = "deplacement_complexe"

    # Vérification si la case est existante
    result = case_existante(xd, yd)
    if result != True:
      print (f"{bcolors.FAIL}Case incorrecte{bcolors.ENDC}")
      return "Erreur"
  
    # Vérification si la case est prise
    result = case_vide(xd, yd)
    if result != True:
      print (f"{bcolors.FAIL}Case prise{bcolors.ENDC}")
      return "Erreur"

    # Vérification que le déplacement ne se fasse pas en arrière
    result = deplacement_arriere(xo, xd, joueur)
    if result != True:
      print(f"{bcolors.FAIL}Déplacement impossible{bcolors.ENDC}")
      return "Erreur"

    # Vérification si le déplacement est possible
    result = deplacement_possible(xo, xd, yo, yd)
    if result != True:
      print(f"{bcolors.FAIL}Déplacement impossible{bcolors.ENDC}")
      return "Erreur"

    # Vérification si on a affaire à une dame ou un pion
    if joueur == "\033[94mX\033[0m" or joueur == "\033[94mO\033[0m":
      pass
    else:  

      # Vérification si on doit manger
      result = manger(xo, xd, yo, yd, joueur, prevision)
      if result == "mange":
        print(f'{bcolors.OKGREEN}Joueur mangé{bcolors.ENDC}')
      elif result == "pasmange":
        print(f"{bcolors.FAIL}Déplacement impossible{bcolors.ENDC}")
        return "Erreur"
      elif result == "doitmanger":
        print(f"{bcolors.FAIL}Vous devez manger{bcolors.ENDC}")
        return "Erreur"

    # Sauvegarde
    sauvegarde(destination, joueur) # Déplacement joueur
    sauvegarde(source, "-") # Vider la case précédente

    # On retourne le type de déplacement effectué
    return deplacement_simple
  else:
    print(f'{bcolors.WARNING}Mauvais joueur{bcolors.ENDC}')
    return "Erreur"

