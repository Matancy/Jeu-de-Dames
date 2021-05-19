import pygame
import affichage_damier
from data import *



def plateau(size, couleur1, couleur2):
    for y in range(5):
        for i in range(5):
            pygame.draw.rect(surf, couleur1, (0 + (size/5 * i), 0 + (size/5 * y), size/10, size/10))
            pygame.draw.rect(surf, couleur2, (size/10 + (size/5 * i), 0 + (size/5 * y), size/10, size/10))
        for i in range(5):
            pygame.draw.rect(surf, couleur2, (0 + (size/5 * i), size/10 + (size/5 * y), size/10, size/10))
            pygame.draw.rect(surf, couleur1, (size/10 + (size/5 * i), size/10 + (size/5 * y), size/10, size/10))


def pion(size, couleur, x, y):
    pygame.draw.circle(surf, couleur, (x, y), int(size/22))
def x(case):
    return int((size/20)+(2*case*size/20))
def y(case):
    return int((size/20)+(2*case*size/20))


def dessiner_tableau (size, couleurO, couleurX):
  for i in range (10):
    for j in range (10):
      if damier[i][j] == 'O':
        pion(size, couleurO, x(j), y(i))
      elif damier[i][j] == 'X':
        pion(size, couleurX, x(j), y(i))

def Xvaleur(X):
  return X//(int(size/10))
def Yvaleur(Y):
  return Y//(int(size/10))




pygame.init()


size = 600
surf = pygame.display.set_mode((size, size))


beige1 = pygame.Color(226, 188, 116)
marron1 = pygame.Color(88, 41, 0)
beige2 = pygame.Color(230, 200, 150)
marron2 = pygame.Color(45, 30, 11)
orange = pygame.Color(152, 87, 23)
gris = pygame.Color(105, 105, 105)
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
      xOgraphique, yOgraphique  = Xvaleur(Xo), Yvaleur(Yo)
      print("depart :",xOgraphique, yOgraphique)
  if event.type == pygame.MOUSEBUTTONDOWN:
    if pygame.mouse.get_pressed() == (0, 0, 1):        
      Yd, Xd = pygame.mouse.get_pos()
      xDgraphique, yDgraphique  = Xvaleur(Xd), Yvaleur(Yd)
      print("arriver :",xDgraphique, yDgraphique)
  
  dessiner_tableau(size, gris, orange)


  """
  pion(size, gris, x(1), y(0))
  pion(size, orange, x(0), y(9))
  """


  


  pygame.display.flip()




pygame.quit()