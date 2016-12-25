#! /usr/bin/env python

import sys, doctest, string, StringIO
from colors import colorString
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

def ask_release_stdout(fakestdout):
    # Function that prompts the user to realease content of fakestdout
    while True:
        action = raw_input("Print failed tests? [F(irst)/a(ll)/n(one)] ")
        action = action.lower()
        if action == '' or action == 'f':
            print fakestdout.getvalue().split("*" * 70)[1]
            break
        elif action == 'a':
            print fakestdout.getvalue()
            break
        elif action.lower() == 'n':
            break


fakestdout = StringIO.StringIO() # Fake file object for Stdout interception
stdout = sys.stdout # Backup stdout

__test__ = {}
for fname, f in targets:
    __test__[fname] = f

    # Intercept Stdout
    sys.stdout = fakestdout
    res = doctest.testmod()
    # Restore Stdout
    sys.stdout = stdout
    test = string.ljust("{}".format(fname), 20, ' ') + " {}"

    print "=" * 79
    if res.failed == 0:
        print colorString("green", test.format(res))
    else:
        print colorString("red", test.format(res))
        print
        ask_release_stdout(fakestdout)
        break

    del __test__[fname]
    if fname == "updateGrid":
        print "-> You can now test main_v1.py"
    elif fname == "doCmd":
        print "-> You can now write main_v2.py"
    elif fname == "updateGrids":
        print "-> You can now write main_v3.py"



