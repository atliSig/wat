#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

FIELD_W = 6
FIELD_H = 6

import random
from termcolor import colored

class Board:
    def __init__(self, H, W, randomize=True):
        self.cells = []
        self.H = H
        self.W = W
        for i in range(H):
            self.cells.append([Cell(i, j, randomize=randomize) for j in range(W)])

    def splash(self, i, j):
        num_splashes = 0
        did_splashback = self.cells[i][j].splash(selected=True)
        if did_splashback:
            num_splashes += 1
            for s in self.get_splashable(i, j):
                num_splashes += self.splash(s[0], s[1])
        return num_splashes

    def get_splashable(self, c_i, c_j):
        '''
        Returns the cells that get splashed in each direction
        from the originally splashed cell
        '''
        splashable = []
        # check left
        for j in reversed(range(0, c_j)):
            if self.cells[c_i][j].is_splashable():
                splashable.append([c_i, j])
                break

        # check right
        for j in range(c_j+1, self.W):
            if self.cells[c_i][j].is_splashable():
                splashable.append([c_i, j])
                break

        # check up
        for i in reversed(range(0, c_i)):
            if self.cells[i][c_j].is_splashable():
                splashable.append([i, c_j])
                break

        # check up
        for i in range(c_i+1, self.H):
            if self.cells[i][c_j].is_splashable():
                splashable.append([i, c_j])
                break

        return splashable

    def is_clear(self):
        for i in range(self.H):
            for j in range(self.W):
                if not self.cells[i][j].is_clear():
                    return False
        return True

    def __str__(self):
        horizontal = '   -{}'.format(''.join('----' for _ in range(self.W )))
        out = '    {}\n'.format(''.join(' {}  '.format((j+1)%10) for j in range(self.W)))
        out += '{}\n'.format(horizontal)
        for i in range(self.H):
            out += ' {} '.format((i+1)%10)
            for j in range(self.W):
                out += '| {} '.format(self.cells[i][j])
            out += '|\n{}\n'.format(horizontal)
        return out

class Cell:
    num_states = 5
    displays = [' ', '.', '°', 'o', 'O']

    def __init__(self, i, j, randomize=True):
        self.i = i
        self.j = j

        self.state = 0
        self.just_selected = False
        self.just_splashed = False

        if randomize:
            self.state = random.randint(0, 4)

    def splash(self, selected=False):
        self.increment()
        if selected:
            self.just_selected = True
        else:
            self.just_splashed = True
        return self.state == 0

    def increment(self):
        self.state =  (self.state + 1) % self.num_states

    def is_splashable(self):
        return self.state != 0

    def is_clear(self):
        return self.state == 0

    def get_coords(self):
        return self.i, self.j

    def __str__(self):
        color = 'green'
        if self.just_selected:
            color = 'yellow'
        if self.just_splashed:
            print('just splashed')
            color = 'red'
        self.just_selected = False
        self.just_splashed = False
        return colored(self.displays[self.state], color)


def safe_input(prompt, r):
    out = -1
    while out not in r:
        out = int(input(prompt))
    return out - 1


if __name__ == '__main__':
    b = Board(FIELD_W, FIELD_H, randomize=True)
    lives = 10
    live_color = 'white'
    level = 1


    while lives > 0:
        print(b)
        print('***************************')
        print(" LIVES : {}".format(colored(lives, live_color)))
        print(" LEVEL : {}".format(level))
        print('***************************\n')

        i = safe_input("Enter row (1-{}): ".format(b.H), range(1, b.H+1))
        j = safe_input("Enter column (1-{}): ".format(b.W), range(1, b.W+1))
        print('\n')

        num_splashes = b.splash(i, j)

        live_color = 'white'
        if num_splashes < 2:
            lives -= 1
            live_color = 'red'
        elif num_splashes > 2:
            lives += num_splashes - 2
            live_color = 'green'

        if b.is_clear():
            print(colored("******** LEVEL {} CLEARED ********".format(level), "green"))
            print('\n')

            b = Board(FIELD_W, FIELD_H, randomize=True)
            lives += 2
            level += 1

