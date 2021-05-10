#
# Fichier regroupant les vérifications relatives à la dame
#
from data import *
from jeu import *


# On regarde si une dame est créée
def is_new_dame():
  for i in range(len(damier[0])):
    if damier[0][i] == "X":
      # On la sauvegarde en couleur
      sauvegarde(f"0{i}", f"{bcolors.OKBLUE}X{bcolors.ENDC}")
  
    if damier[9][i] == "O":
      # On la sauvegarde en couleur
      sauvegarde(f"9{i}", f"{bcolors.OKBLUE}O{bcolors.ENDC}")


# On regarde si le déplacement de la dame est possible
#def deplacement_dame(xo, xd, yo, yd):
#  pass



#def manger_dame():
#  pass
