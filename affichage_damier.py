from data import *
from config import *
import pygame
#
# Fichier regroupant les fonctions relatives à l'affichage du damier
#

plateau = pygame.display.set_mode((game_display_size, game_display_size)) # Variable du plateau


# Affichage du damier en mode console
def affichage_damier_console(liste):
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


# Affichage du damier en mode graphique
def creation_plateau(size, couleur1, couleur2):

  for y in range(5):
    for i in range(5):
      pygame.draw.rect(plateau, couleur1, (0 + (size / 5 * i), 0 + (size / 5 * y), size / 10, size / 10))
      pygame.draw.rect(plateau, couleur2, (size / 10 + (size / 5 * i), 0 + (size / 5 * y), size / 10, size / 10))
    for i in range(5):
      pygame.draw.rect(plateau, couleur2, (0 + (size / 5 * i), size / 10 + (size / 5 * y), size / 10, size / 10))
      pygame.draw.rect(plateau, couleur1, (size / 10 + (size / 5 * i), size / 10 + (size / 5 * y), size / 10, size / 10))


# Affichage d'un pion
def affichage_pion(size, couleur, x, y):
  pygame.draw.circle(plateau, couleur, (x, y), int(size / 22))