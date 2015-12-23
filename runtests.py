#! /usr/bin/env python

import doctest, string
from snake import *

targets = [
    ("genGrid", genGrid),
    ("displayGrid", displayGrid),
    ("pointInsideGrid", pointInsideGrid),
    ("placeObject", placeObject),
    ("dropBlock", dropBlock),
    ("dropFood", dropFood),
    ("genSnake", genSnake),
    ("isAlive", isAlive),
    ("killSnake", killSnake),
    ("getNextPosition", getNextPosition),
    ("turnRight", turnRight),
    ("turnLeft", turnLeft),
    ("updateSnake", updateSnake),
    ("updateGrid", updateGrid),
    ("cmdFromString", cmdFromString),
    ("doCmd", doCmd),
    ("genIntGrid", genIntGrid),
    ("decrIntGrid", decrIntGrid),
    ("updateGrids", updateGrids)
]

__test__ = {}
for fname, f in targets:
    __test__[fname] = f
    res = doctest.testmod()
    test = string.ljust("{}".format(fname), 20, ' ') + " {}"
    print test.format(res)
    del __test__[fname]
    if res.failed != 0:
        break
    if fname == "updateGrid":
        print "-> You can now test main_v1.py"
    elif fname == "doCmd":
        print "-> You can now write main_v2.py"
    elif fname == "updateGrids":
        print "-> You can now write main_v3.py"



