import pygame, random, sys
pygame.init()

width = 768
height = 480
size = 3
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virus Transmission")

class human:
    def __init__(self):
        self.x = random.randrange(3, width-3)
        self.y = random.randrange(3, height-3)

    def drawimage(self):
        pygame.draw.rect(window, (0, 128, 0), (self.x, self.y, size, size), 0)

humans = []
for i in range(200):
    Human = human()
    humans.append(Human)

def movement():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill((0, 0, 0))
        for i in humans:
            i.drawimage()
        pygame.display.update()

movement()