from game_data import *


# On regarde si le jeu est terminé
def is_game_finished():
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