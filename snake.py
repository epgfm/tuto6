#! /usr/bin/env python

def genGrid(nRows, nCols):
    ''' (int, int) -> list of list of chars {{grid}}

    Generates and returns a grid of nRows by nCols. Every element on the inner
    lists is a whitespace character.

    >>> genGrid(2, 3)
    [[' ', ' ', ' '], [' ', ' ', ' ']]
    >>> genGrid(1, 4)
    [[' ', ' ', ' ', ' ']]
    >>> s = genGrid(3, 4) ; s[0][0] = '*' ; s
    [['*', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    '''



def displayGrid(grid):
    ''' (grid) -> NoneType

    Display the grid to standard output. The grid must be surrounded by '+ '
    symbols. (Be careful: there's a space after the '+' sign)

    >>> s = [['8', ' ', ' '], [' ', ' ', '*']] ; displayGrid(s)
    + + + + + 
    + 8     + 
    +     * + 
    + + + + + 
    >>> s.append(['#', ' ', '#']) ; displayGrid(s)
    + + + + + 
    + 8     + 
    +     * + 
    + #   # + 
    + + + + + 
    >>> displayGrid(genGrid(3, 6))
    + + + + + + + + 
    +             + 
    +             + 
    +             + 
    + + + + + + + + 
    '''




def pointInsideGrid(grid, point):
    ''' (grid, (int, int)) -> Boolean

    Check if the point is somewhere inside the grid.

    >>> pointInsideGrid(genGrid(4, 5), (4, 5))
    False
    >>> pointInsideGrid(genGrid(4, 5), (3, 4))
    False
    >>> pointInsideGrid(genGrid(4, 5), (5, 3))
    False
    >>> pointInsideGrid(genGrid(6, 5), (4, 5))
    True
    >>> pointInsideGrid(genGrid(4, 5), (3, 3))
    True
    >>> pointInsideGrid(genGrid(4, 5), (0, 0))
    True
    >>> pointInsideGrid(genGrid(4, 5), (-1, 0))
    False
    '''



def placeObject(grid, x, y, o):
    ''' (grid, int, int, char) -> NoneType

    Place a character (the object o) at the given coordinates (x, y) on the
    grid. You can assume that (x, y) are valid coordinates inside the grid.

    >>> g = [[' ', ' '], [' ', ' ']] ; placeObject(g, 0, 0, 'o') ; g
    [['o', ' '], [' ', ' ']]
    >>> g = [[' ', ' '], [' ', ' ']] ; placeObject(g, 1, 0, 'o') ; g
    [[' ', 'o'], [' ', ' ']]
    '''



def dropBlock(grid, x, y):
    ''' (grid, int, int) -> NoneType

    Place a roadblock type object on the grid at the given (x, y) coordinates.
    A roadblock is identified by the character "#".

    >>> l = [[' ', ' '], [' ', ' ']] ; dropBlock(l, 1, 0) ; l
    [[' ', '#'], [' ', ' ']]
    >>> dropBlock(l, 1, 1) ; l
    [[' ', '#'], [' ', '#']]
    '''




def dropFood(grid, x, y):
    ''' (grid, int, int) -> NoneType

    Place a snakefood type object on the grid at the given (x, y) coordinates.
    A snakefood is identified by the character "o".

    >>> l = [[' ', ' '], [' ', ' ']] ; dropFood(l, 0, 1) ; l
    [[' ', ' '], ['o', ' ']]
    >>> dropFood(l, 1, 1) ; l
    [[' ', ' '], ['o', 'o']]
    '''




def genSnake(position, speed, color):
    ''' (tuple, tuple, str) -> [[int, int], [int, int], str, Boolean, int]
                                                {{snake}}

    Generates a new snake.

    A snake is represented by a list of 5 Values:

    - A list [x, y] representing the current position of the snake's head.
    - A list [vx, vy] representing the speed vector of the snake's head.
    - A string identifying the snake by a color.
    - A Boolean that is True if the snake is alive and False otherwise.
    - An integer representing the size of the snake (starts at 1)

    >>> genSnake((1, 1), (1, 0), 'red')
    [[1, 1], [1, 0], 'red', True, 1]
    >>> genSnake((0, 1), (-1, 0), 'green')
    [[0, 1], [-1, 0], 'green', True, 1]
    '''




def isAlive(snake):
    ''' (snake) -> Boolean

    Returns True if the snake is marked as being alive

    >>> isAlive([[0, 0], [1, 0], 'red', True, 1])
    True
    >>> isAlive([[0, 0], [1, 6], 'green', False, 1])
    False
    '''




def killSnake(snake):
    ''' (snake) -> NoneType

    Kills the snake (set alive status)

    >>> s = genSnake((0, 0), (1, 0), 'red') ; killSnake(s) ; s
    [[0, 0], [1, 0], 'red', False, 1]
    '''




def getNextPosition(snake):
    ''' (snake) -> (int, int)

    Returns the next position the (head of the) snake will move to.

    >>> getNextPosition([[0, 0], [1, 0], 'red', True, 1])
    (1, 0)
    >>> getNextPosition([[0, 0], [0, 1], 'red', True, 1])
    (0, 1)
    >>> getNextPosition([[4, 0], [-1, 1], 'red', True, 1])
    (3, 1)
    >>> s = genSnake((1, 2), (0, 1), "red") ; pos = getNextPosition(s) ; s
    [[1, 2], [0, 1], 'red', True, 1]
    '''




def turnRight(snake):
    ''' (snake) -> NoneType

    Change the speed vector of the snake to make it turn right.

    >>> s = genSnake((0, 0), (1, 0), 'red') ; s
    [[0, 0], [1, 0], 'red', True, 1]
    >>> turnRight(s) ; s
    [[0, 0], [0, 1], 'red', True, 1]
    >>> turnRight(s) ; s
    [[0, 0], [-1, 0], 'red', True, 1]
    >>> turnRight(s) ; s
    [[0, 0], [0, -1], 'red', True, 1]
    >>> turnRight(s) ; s
    [[0, 0], [1, 0], 'red', True, 1]
    '''




def turnLeft(snake):
    ''' (snake) -> NoneType

    Change the speed vector of the snake to make it turn left.

    >>> s = genSnake((0, 0), (1, 0), 'red') ; s
    [[0, 0], [1, 0], 'red', True, 1]
    >>> turnLeft(s) ; s
    [[0, 0], [0, -1], 'red', True, 1]
    >>> turnLeft(s) ; s
    [[0, 0], [-1, 0], 'red', True, 1]
    >>> turnLeft(s) ; s
    [[0, 0], [0, 1], 'red', True, 1]
    >>> turnLeft(s) ; s
    [[0, 0], [1, 0], 'red', True, 1]
    '''




def updateSnake(grid, snake):
    ''' (grid, snake) -> NoneType

    Update the given snake, relative to the grid.
        - If the snake steps over one side of the grid, its position switches
          to the other side of the grid.
        - If the snake's next position on the grid is occupied by a roadblock
          or a snake, the snake should be killed.
        - Else, Update the snake's position.
        - If the new position has snakefood, increase size element of the snake

    >>> s = genSnake((1, 0), (-1, 0), 'red') ; g = genGrid(3, 5) ; s
    [[1, 0], [-1, 0], 'red', True, 1]
    >>> updateSnake(g, s) ; s
    [[0, 0], [-1, 0], 'red', True, 1]
    >>> updateSnake(g, s) ; s
    [[4, 0], [-1, 0], 'red', True, 1]
    >>> updateSnake(g, s) ; s
    [[3, 0], [-1, 0], 'red', True, 1]
    >>> dropFood(g, 2, 0) ; updateSnake(g, s) ; s
    [[2, 0], [-1, 0], 'red', True, 2]
    >>> dropBlock(g, 1, 0) ; updateSnake(g, s) ; s
    [[2, 0], [-1, 0], 'red', False, 2]
    >>> s = genSnake((0, 0), (-1, 0), 'red') ; dropBlock(g, 4, 0) ; s
    [[0, 0], [-1, 0], 'red', True, 1]
    >>> updateSnake(g, s) ; s
    [[0, 0], [-1, 0], 'red', False, 1]
    >>> s = genSnake((0, 0), (-1, 0), 'red') ; placeObject(g, 4, 0, '*') ; updateSnake(g, s) ; s
    [[0, 0], [-1, 0], 'red', False, 1]
    '''




def updateGrid(grid, snake):
    ''' (grid, snake) -> NoneType

    Update the given grid, relative to the snake.
        - Wipe any snake symbol off the grid.
        - If the snake is not dead, repaint it on the grid

    >>> s = genSnake((2, 2), (-1, 0), 'red') ; g = genGrid(3, 3)
    >>> placeObject(g, 2, 2, '*') ; displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    +     * + 
    + + + + + 
    >>> updateSnake(g, s) ; updateGrid(g, s) ; displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    +   *   + 
    + + + + + 
    >>> turnRight(s) ; updateSnake(g, s) ; updateGrid(g, s) ; displayGrid(g)
    + + + + + 
    +       + 
    +   *   + 
    +       + 
    + + + + + 
    >>> killSnake(s); updateGrid(g, s) ; displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    +       + 
    + + + + + 
    '''




def cmdFromString(string, cmd_chars):
    ''' (str, str) -> int

    Gets a command from a string.
    A command consists of a single char.
    The cmd_chars parameters is a string of two chars, each char corresponds to
    a single command: "Turn Left" or "Turn Right". The first char is left, the
    second is right.

    Return the last command contained in the string, from left to right, as
    an int:
        -1 -> Turn Left
         0 -> No command found in string
         1 -> Turn Right

    >>> cmdFromString("ahpauyozdhgapzeaz", "op")
    1
    >>> cmdFromString("ahpauyozdhgapzoeaz", "op")
    -1
    >>> cmdFromString("ahauyzdhgazeaz", "op")
    0
    '''




def doCmd(s, cmd):
    ''' (snake, int) -> None

    Apply cmd on the snake s.
    If cmd is -1, turn the snake to the left. If it's 1, to the right.
    Do nothing if the command is 0.

    >>> s = genSnake((1, 2), (-1, 0), 'red') ; doCmd(s, -1) ; s
    [[1, 2], [0, 1], 'red', True, 1]
    >>> doCmd(s, -1) ; s
    [[1, 2], [1, 0], 'red', True, 1]
    >>> doCmd(s, 0) ; s
    [[1, 2], [1, 0], 'red', True, 1]
    >>> doCmd(s, 1) ; s
    [[1, 2], [0, 1], 'red', True, 1]
    '''




def genIntGrid(grid):
    ''' (grid) -> list of list of int {{intgrid}}


    Given a grid, returns an integer grid of the same dimentions, where every
    element is initialized at 0.

    >>> genIntGrid(genGrid(2, 3))
    [[0, 0, 0], [0, 0, 0]]
    >>> genIntGrid(genGrid(3, 4))
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''




def decrIntGrid(intgrid):
    ''' (intgrid) -> NoneType

    Decrement every value in intgrid by one if it is bigger than 0.

    >>> ig = genIntGrid(genGrid(2, 3)) ; ig[0][1] = 2 ; ig[1][2] = 9
    >>> decrIntGrid(ig) ; ig
    [[0, 1, 0], [0, 0, 8]]
    >>> ig[0][0] = 4 ; decrIntGrid(ig) ; ig
    [[3, 0, 0], [0, 0, 7]]
    >>> decrIntGrid(ig) ; ig
    [[2, 0, 0], [0, 0, 6]]
    '''




def updateGrids(grid, intgrid, snake):
    ''' (grid, , intgrid, snake) -> NoneType

    Update the given grids, relative to the snake.
        - Wipe any snake symbol off the grid if the corresponding counter in
          the intgrid has reached zero.
        - If the snake is not dead, repaint it on the grid and reset the
          counter for the snake's position.

    >>> s = genSnake((2, 2), (-1, 0), 'red') ; g = genGrid(3, 3)
    >>> placeObject(g, 2, 2, '*') ; dropFood(g, 1, 2) ; displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    +   o * + 
    + + + + + 
    >>> ig = genIntGrid(g) ; updateSnake(g, s) ; updateGrids(g, ig, s)
    >>> displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    +   *   + 
    + + + + + 
    >>> updateSnake(g, s) ; updateGrids(g, ig, s) ; displayGrid(g)
    + + + + + 
    +       + 
    +       + 
    + * *   + 
    + + + + + 
    '''






if __name__ == '__main__':
    import doctest, sys, os, time
    res = doctest.testmod()
    print(res)





