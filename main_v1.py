#! /usr/bin/env python

import os, time
from snake import *

def run_test():

    g = genGrid(10, 20)
    s = genSnake((0, 0), (1, 0), 'red')

    dropFood(g, 4, 5)
    dropFood(g, 4, 6)
    dropFood(g, 4, 7)
    dropFood(g, 4, 8)
    dropFood(g, 5, 8)
    dropFood(g, 6, 8)
    dropFood(g, 7, 8)
    dropBlock(g, 8, 8)

    i = 0
    while isAlive(s):
        time.sleep(1)
        os.system("clear")
        if i == 3:
            turnRight(s)
        if i == 11:
            turnLeft(s)
        if i == 14:
            turnLeft(s)
        if i == 16:
            turnLeft(s)
        if i == 18:
            turnLeft(s)
        if i == 20:
            turnRight(s)
        if i == 22:
            turnRight(s)
        if i == 24:
            turnRight(s)
        if i == 26:
            turnRight(s)
        if i == 28:
            turnLeft(s)
        updateSnake(g, s)
        updateGrid(g, s)
        displayGrid(g)
        i += 1
    print "Snake score: {}".format(s[-1])



if __name__ == '__main__':
    run_test()








