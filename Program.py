import pygame, random, sys
pygame.init()

width = 768
height = 480
size = 3
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virus Transmission")
fps = 60
offset = random.random()
if offset > .65 or offset < .25:
    offset = random.random()

class disease:
    def __init__(self):
        self.x = random.randrange(3, width-3)
        self.y = random.randrange(3, height-3)
        self.speed = random.randrange(2, 5)  # cell speed
        self.move = [None, None]  # realtive x and y coordinates to move to
        self.direction = None  # movement direction

    def drawimage(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, size, size), 0)

    def run(self):
        directions = {"S": ((-1, 2), (1, self.speed)), "SW": ((-self.speed, -1), (1, self.speed)),
                      "W": ((-self.speed, -1), (-1, 2)), "NW": ((-self.speed, -1), (-self.speed, -1)),
                      "N": ((-1, 2), (-self.speed, -1)), "NE": ((1, self.speed), (-self.speed, -1)),
                      "E": ((1, self.speed), (-1, 2)),
                      "SE": ((1, self.speed), (1, self.speed))}  # ((min x, max x)(min y, max y))
        directionsName = ("S", "SW", "W", "NW", "N", "NE", "E", "SE")  # possible directions
        if random.randrange(0, 5) == 2:  # move about once every 5 frames
            if self.direction == None:  # if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction)  # get the index of direction in directions list
                b = random.randrange(a - 1,
                                     a + 2)  # set the direction to be the same, or one next to the current direction
                if b > len(directionsName) - 1:  # if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][
                1]) + offset  # change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][
                1]) + offset  # change relative y to a random number between min y and max y
        if self.x < 5 or self.x > width - 5 or self.y < 5 or self.y > height - 5:  # if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > width - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > height - 5:
                self.direction = "N"
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][
                1]) + offset  # change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][
                1]) + offset  # change relative x to a random number between min x and max x
        if self.move[0] != None:  # add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]

class human():
    def __init__(self):
        self.x = random.randrange(3, width-3)
        self.y = random.randrange(3, height-3)
        self.speed = random.randrange(2, 5)  # cell speed
        self.move = [None, None]  # realtive x and y coordinates to move to
        self.direction = None  # movement direction

    def drawimage(self):
        pygame.draw.rect(window, (0, 128, 0), (self.x, self.y, size, size), 0)

    def run(self):
        directions = {"S": ((-1, 2), (1, self.speed)), "SW": ((-self.speed, -1), (1, self.speed)),
                      "W": ((-self.speed, -1), (-1, 2)), "NW": ((-self.speed, -1), (-self.speed, -1)),
                      "N": ((-1, 2), (-self.speed, -1)), "NE": ((1, self.speed), (-self.speed, -1)),
                      "E": ((1, self.speed), (-1, 2)),
                      "SE": ((1, self.speed), (1, self.speed))}  # ((min x, max x)(min y, max y))
        directionsName = ("S", "SW", "W", "NW", "N", "NE", "E", "SE")  # possible directions
        if random.randrange(0, 5) == 2:  # move about once every 5 frames
            if self.direction == None:  # if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction)  # get the index of direction in directions list
                b = random.randrange(a - 1,
                                     a + 2)  # set the direction to be the same, or one next to the current direction
                if b > len(directionsName) - 1:  # if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][
                1]) + offset  # change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][
                1]) + offset  # change relative y to a random number between min y and max y
        if self.x < 5 or self.x > width - 5 or self.y < 5 or self.y > height - 5:  # if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > width - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > height - 5:
                self.direction = "N"
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][
                1]) + offset  # change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][
                1]) + offset  # change relative x to a random number between min x and max x
        if self.move[0] != None:  # add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]

diseases = []
for i in range(1):
    Disease = disease()
    diseases.append(Disease)

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
        for i in diseases:
            i.drawimage()
            i.run()
        for i in humans:
            i.drawimage()
            i.run()
        pygame.display.update()
        pygame.time.Clock().tick(fps)

movement()