import random
import pygame
import tkinter as tk
from tkinter import messagebox
import sys
import time

pygame.display.set_caption('SNAKE GAME!!! HAVE FUN PLAYING')

class cube(object):
    rows = 20
    w = 800

    def __init__(self, start, dirnx=1, dirny=0, color=(30,144,255)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0,128,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,128,0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.direction = direction

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for i, c in enumerate(self.body):
            if c.pos in [(1,1),(2,19),(3,1),(4,19),(5,1),(6,19),(7,1),(8,19),(9,1),(10,19),(11,1),(12,19),(13,1),(14,19),(15,1),(16,19),(17,1),(18,19),(0,19)]:
                print("right")
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif c.pos in [(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(2,15),(2,16),(2,17),(2,18),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(4,16),(4,17),(4,18),(6,1),(6,2),(6,3),(6,4),(6,5),(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12),(6,13),(6,14),(6,15),(6,16),(6,17),(6,18),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(8,15),(8,16),(8,17),(8,18),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10),(10,11),(10,12),(10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(12,15),(12,16),(12,17),(12,18),(14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,14),(14,15),(14,16),(14,17),(14,18),(16,1),(16,2),(16,3),(16,4),(16,5),(16,6),(16,7),(16,8),(16,9),(16,10),(16,11),(16,12),(16,13),(16,14),(16,15),(16,16),(16,17),(16,18),(18,1),(18,2),(18,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,15),(18,16),(18,17),(18,18),(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18)]:
                print("down")
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif c.pos in [(19,0),(18,0),(17,0),(16,0),(15,0),(14,0),(13,0),(12,0),(11,0),(10,0),(9,0),(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0)]:
                print("left")
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif c.pos in [(1,10),(1,9), (1,8), (1,7), (1,6), (1,5), (1,4), (1,3), (1,2), (1,19),(3,19),(3,18),(3,17),(3,16),(3,15),(3,14),(3,13),(3,12),(3,11),(3,10),(3,9),(3,8),(3,7),(3,6),(3,5),(3,4),(3,3),(3,2),(5,19),(5,18),(5,17),(5,16),(5,15),(5,14),(5,13),(5,12),(5,11),(5,10),(5,9),(5,8),(5,7),(5,6),(5,5),(5,4),(5,3),(5,2),(7,19),(7,18),(7,17),(7,16),(7,15),(7,15),(7,14),(7,13),(7,12),(7,11),(7,10),(7,9),(7,8),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(9,19),(9,18),(9,17),(9,16),(9,15),(9,14),(9,13),(9,12),(9,11),(9,10),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(11,19),(11,18),(11,17),(11,16),(11,15),(11,14),(11,13),(11,12),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(11,5),(11,4),(11,3),(11,2),(13,19),(13,18),(13,17),(13,16),(13,15),(13,14),(13,13),(13,12),(13,11),(13,10),(13,9),(13,8),(13,7),(13,6),(13,5),(13,4),(13,3),(13,2),(15,19),(15,18),(15,17),(15,16),(15,15),(15,14),(15,13),(15,12),(15,11),(15,10),(15,9),(15,8),(15,7),(15,6),(15,5),(15,4),(15,3),(15,2),(17,19),(17,18),(17,17),(17,16),(17,15),(17,14),(17,13),(17,12),(17,12),(17,11),(17,10),(17,9),(17,8),(17,7),(17,6),(17,5),(17,4),(17,3),(17,2),(19,19),(19,18),(19,17),(19,16),(19,15),(19,14),(19,13),(19,12),(19,11),(19,10),(19,11),(19,10),(19,9),(19,8),(19,7),(19,6),(19,5),(19,4),(19,3),(19,2),(19,1),(1,19),(1,18),(1,17),(1,16),(1,15),(1,14),(1,13),(1,12),(1,11)]:
                print("up")
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else:
                reset = (1, 10)
                if c.dirnx == -1 and c.pos[0] <= 0:
                    show_score(0, red, 'times', 75, len(s.body))
                    time.sleep(1)
                    s.reset(reset)
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    show_score(0, red, 'times', 75, len(s.body))
                    time.sleep(1)
                    s.reset(reset)
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    show_score(0, red, 'times', 75, len(s.body))
                    time.sleep(1)
                    s.reset(reset)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    show_score(0, red, 'times', 75, len(s.body))
                    time.sleep(1)
                    s.reset(reset)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((154,205,50))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def show_score(choice, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('YOU LOST!!! Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (60, 60)
    else:
        score_rect.midtop = (400, 400)
    win.blit(score_surface, score_rect)
    pygame.display.flip()

def main():
    global width, rows, s, snack, win, direction, red
    direction = 'right'
    width = 800
    rows = 20
    red = pygame.Color(255, 0, 0)
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initializing game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialized')

    win = pygame.display.set_mode((width, width))
    s = snake((30,144,255), (1, 10))
    snack = cube(randomSnack(rows, s), color=(255, 0, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(1)
        clock.tick(1000)

        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                show_score(0, red, 'times', 80, len(s.body))
                print('YOU LOST!!! Score: ', len(s.body))
                time.sleep(1)
                s.reset((1, 10))
                break

        redrawWindow(win)


main()