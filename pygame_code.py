import pygame
from affichage_damier import *
from data import *
from gestion_data import *




joueur = quel_joueur(joueur)
run = True

while run :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  if event.type == pygame.MOUSEBUTTONDOWN:
    if pygame.mouse.get_pressed() == (1, 0, 0):
      Yo, Xo = pygame.mouse.get_pos()
      xOgraphique, yOgraphique  = str(convert_co_x(Xo)), str(convert_co_y(Yo))
      print("depart :",xOgraphique, yOgraphique)
  if event.type == pygame.MOUSEBUTTONDOWN:
    if pygame.mouse.get_pressed() == (0, 0, 1):        
      Yd, Xd = pygame.mouse.get_pos()
      xDgraphique, yDgraphique  = str(convert_co_x(Xd)), str(convert_co_y(Yd))
      print("arriver :",xDgraphique, yDgraphique)

  #pygame.display.flip()

pygame.quit()