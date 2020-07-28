import random
import pygame
import tkinter as tk
from tkinter import messagebox
import sys
import time

pygame.display.set_caption('SNAKE GAME BOT!')

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
        for i, c in enumerate(self.body):
                if c.dirnx == -1 and c.pos[0] <=0:
                    self.direction = 'right'
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    self.direction = 'down'
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    self.direction = 'left'
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif c.dirny == -1 and c.pos[1] <= c.rows -1:
                    self.direction = 'up'
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                else:
                    c.move(c.dirnx, c.dirny)

                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body) - 1:
                        self.turns.pop(p)

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
    score_surface = score_font.render('BOTS SCORE : ' + str(score), True, color)
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
        clock.tick(10)

        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(255, 0, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                show_score(0, red, 'times', 80, len(s.body))
                print('BOTS SCORE: ', len(s.body))
                time.sleep(1)
                s.reset((1, 10))
                break

        redrawWindow(win)


main()