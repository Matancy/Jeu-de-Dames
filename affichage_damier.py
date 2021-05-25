from data import *
from config import *
from gestion_data import *
#
# Fichier regroupant les fonctions relatives à l'affichage du damier
#


# Affichage du damier en mode console
def affichage_damier_console(damier):
  """
  Cette fonction permet d'afficher un damier en console en lui fournissant une liste
  Input (list): damier
  Return : Void
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
def affichage_damier_graphique(damier):
  """
  Cette fonction affiche le damier en interface graphique en lui fournissant une liste
  Input (list): damier
  Return : Void
  """

  for i in range(10):
    for j in range(10):
      if damier[i][j] == 'O':
        pion(game_display_size, gris, convert_case_x(j), convert_case_y(i))
      elif damier[i][j] == 'X':
        pion(game_display_size, orange, convert_case_x(j), convert_case_y(i))


# Création de la variable du plateau
def variable_plateau():
  """
  Cette fonction s'occupe de créer la variable de plateau
  Input: void
  Return (pygame): plateau
  """
  return pygame.display.set_mode((game_display_size, game_display_size))


# Création du damier en mode graphique
def creation_plateau():
  """
  Cette fonction permet de créer la variable de plateau
  Input : Void
  Return : Variable du plateau
  """
  for y in range(5):
    for i in range(5):
      pygame.draw.rect(plateau, beige, (0 + (game_display_size / 5 * i), 0 + (game_display_size / 5 * y), game_display_size / 10, game_display_size / 10))
      pygame.draw.rect(plateau, marron, (game_display_size / 10 + (game_display_size / 5 * i), 0 + (game_display_size / 5 * y), game_display_size / 10, game_display_size / 10))
    for i in range(5):
      pygame.draw.rect(plateau, marron, (0 + (game_display_size / 5 * i), game_display_size / 10 + (game_display_size / 5 * y), game_display_size / 10, game_display_size / 10))
      pygame.draw.rect(plateau, beige, (game_display_size / 10 + (game_display_size / 5 * i), game_display_size / 10 + (game_display_size / 5 * y), game_display_size / 10, game_display_size / 10))
  return plateau


# Affichage d'un pion
def pion(size, couleur, x, y):
  """
  Fonction qui permet d'afficher un pion sur l'interface graphique
  Input (str) : Taille, couleur, position x et position y
  Return : Void
  """
  pygame.draw.circle(plateau, couleur, (x, y), int(size / 22))


def init_plateau():
  pygame.init()
