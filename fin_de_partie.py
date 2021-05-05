from game_data import *


# On regarde si le jeu est terminé
def is_game_finished():
  """
    fonction nous  informe quand la partie est finie et quel est le gagnant
    renvoie "Rond Gagnant" si le jouer O à gagné
    renvoie "Croix Gagnante" si le jouer X à gagné
    renvoie "partie-en-cours" si la partie n'est pas terminé 
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