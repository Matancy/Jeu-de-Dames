import pygame

pygame.init()

size = 800

surf = pygame.display.set_mode((size, size))
marron_clair = pygame.Color(226, 188, 116)
marron_fonce = pygame.Color(88, 41, 0)
blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)
run = True

while run :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    for y in range(5):
        for i in range(5):
            pygame.draw.rect(surf,marron_clair,(0 + (size/5 * i), 0 + (size/5 * y), size/10, size/10))
            pygame.draw.rect(surf,marron_fonce,(size/10 + (size/5 * i), 0 + (size/5 * y), size/10, size/10))
        for i in range(5):
            pygame.draw.rect(surf,marron_fonce,(0 + (size/5 * i), size/10 + (size/5 * y), size/10, size/10))
            pygame.draw.rect(surf,marron_clair,(size/10 + (size/5 * i), size/10 + (size/5 * y), size/10, size/10))


  pygame.display.flip()




pygame.quit()