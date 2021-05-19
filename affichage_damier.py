from data import *
from config import *
from gestion_data import *
import pygame
import pygame_code
#
# Fichier regroupant les fonctions relatives à l'affichage du damier
#



# Affichage du damier en mode console
def affichage_damier_console(damier):
  """
  Cette fonction permet d'afficher un damier, elle reçoit une liste et affiche le damier. Elle peut prendre le damier ou la grille de Manoury.
  Input (list): damier
  Return (print): Affichage de la liste
  """
  print(esp,end="")
  for i in range(10):
    print(i,end=esp)
  print("\n")
  for i in range(10):
    print(i,end=esp)
    for e in range(0, 10):
      print (damier[i][e],end=esp)
    print("\n")



# Affichage du damier en mode graphique
#def affichage_damier_graphique(damier):
  
  #Cette fonction affiche le damier en interface graphique
  #Input (list): damier
  #Return (display): Affichage du damier

  for i in range(10):
    for j in range(10):
      if damier[i][j] == 'O':
        pion(game_display_size, gris, convert_case_x(j), convert_case_y(i))
      elif damier[i][j] == 'X':
        pion(game_display_size, orange, convert_case_x(j), convert_case_y(i))
  

# Création du damier en mode graphique
def creation_plateau():
  return pygame.display.set_mode((game_display_size, game_display_size))


plateau = creation_plateau() # Variable de plateau


# Affichage d'un pion
def pion(size, couleur, x, y):
  pygame.draw.circle(plateau, couleur, (x, y), int(size / 22))


def init_plateau():
  pygame.init()