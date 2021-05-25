import pygame
import affichage_damier
from data import *
from gestion_data import *




joueur = quel_joueur(joueur)





size = 600
plateau = pygame.display.set_mode((size, size))



marron1 = pygame.Color(88, 41, 0)
beige2 = pygame.Color(230, 200, 150)
marron2 = pygame.Color(45, 30, 11)


blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)
run = True



while run :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  plateau(size, beige1, marron2)
  dessiner_tableau(size, gris, orange)
  if event.type == pygame.MOUSEBUTTONDOWN:
    if pygame.mouse.get_pressed() == (1, 0, 0):
      Yo, Xo = pygame.mouse.get_pos()
      xOgraphique, yOgraphique  = str(Xvaleur(Xo)), str(Yvaleur(Yo))
      print("depart :",xOgraphique, yOgraphique)
  if event.type == pygame.MOUSEBUTTONDOWN:
    if pygame.mouse.get_pressed() == (0, 0, 1):        
      Yd, Xd = pygame.mouse.get_pos()
      xDgraphique, yDgraphique  = str(Xvaleur(Xd)), str(Yvaleur(Yd))
      print("arriver :",xDgraphique, yDgraphique)
  
    dessiner_tableau(size, gris, orange)



  


  pygame.display.flip()




pygame.quit()