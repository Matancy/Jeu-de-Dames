import pygame




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


def depart(size, couleur1, couleur2):
    for i in range(5):
        pion(size, couleur1, x(1+i*2), y(0))
        pion(size, couleur1, x(0+i*2), y(1))
        pion(size, couleur1, x(1+i*2), y(2))
        pion(size, couleur1, x(0+i*2), y(3))

    for i in range(5):
        pion(size, couleur2, x(1+i*2), y(6))
        pion(size, couleur2, x(0+i*2), y(7))
        pion(size, couleur2, x(1+i*2), y(8))
        pion(size, couleur2, x(0+i*2), y(9))




pygame.init()


size = 800
surf = pygame.display.set_mode((size, size))


beige1 = pygame.Color(226, 188, 116)
marron1 = pygame.Color(88, 41, 0)
beige2 = pygame.Color(230, 200, 150)
marron2 = pygame.Color(45, 30, 11)
orange = pygame.Color(152, 87, 23)


test = pygame.Color(105, 105, 105)

blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)
run = True



while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    plateau(size, beige1, marron2)


    depart(size, test, orange)

    """
    pion(size, beige2, x(1), y(0))
    pion(size, orange, x(0), y(9))


    """


    pygame.display.flip()




pygame.quit()