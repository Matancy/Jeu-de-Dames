from game_data import *

# Affichage du damier
def affichage_damier(liste):
  """
  Cette fonction permet d'afficher un damier, elle reçoit une liste et affiche le damier. Elle peut prendre le damier ou la grille de Manoury.
  In : liste
  Out : Print de la liste
  """
  print(esp,end="")
  for i in range(10):
    print(i,end=esp)
  print("\n")
  for i in range(10):
    print(i,end=esp)
    for e in range(0, 10):
      print (liste[i][e],end=esp)
    print("\n")

