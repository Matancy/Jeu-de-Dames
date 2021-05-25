from data import *
#
# Fichier regroupant les fonctions relatives à la fin de partie
#


# On regarde si le jeu est terminé
def is_game_finished():
  """
    Fonction nous  informe quand la partie est finie et quel est le gagnant
    Input : Void
    Return (str) : texte indiquant le gagnant de la partie / partie en cours
  """
  rond = 0
  croix = 0
  for i in range(10):
    for e in range(len(damier[i])):
      if damier[i][e] == "O":
        rond += 1
      elif damier[i][e] == "X":
        croix += 1
  
  if croix == 0 and rond >= 1:
    return "Rond Gagnant"
  elif croix >= 1 and rond == 0:
    return "Croix Gagnante"
  else:
    return "partie-en-cours"