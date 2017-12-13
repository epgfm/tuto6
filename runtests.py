#! /usr/bin/env python

import sys, doctest, string, StringIO, dis
from colors import colorString
import argparse as ap
from snake import *


def check_usage(f, name):
    backup_stdout = sys.stdout
    fake_stdout = StringIO.StringIO()
    sys.stdout = fake_stdout
    dis.dis(f)
    sys.stdout = backup_stdout
    matchName = False
    lines = fake_stdout.getvalue().split("\n")
    lines = [l.split() for l in lines]
    for l in lines:
        i = l.index('LOAD_GLOBAL') if 'LOAD_GLOBAL' in l else -1 
        if i != -1:
            if l[i+2] == ('(%s)' % name):
                return True
    return False


def prompt_release_stdout(fakestdout):
    # Function that prompts the user to realease content of fakestdout, return True if the user decides to pass the current function
    while True:
        action = raw_input("Print failed tests? [F(irst)/a(ll)/o(ne by one)/n(one)/p(ass this function)] ")
        action = action.lower()
        if action.lower() == 'p':
            return True
        elif action == '' or action == 'f':
            print fakestdout.getvalue().split("*" * 70)[1]
            break
        elif action == 'a':
            print fakestdout.getvalue()
            break
        elif action == 'o':
            for s in fakestdout.getvalue().split("*" * 70)[1:-1]:
                print s                
                print
                action = raw_input("Next error? [Y(es)/n(o)] ")
                action = action.lower()
                if action == 'n':
                        break
            break
        elif action.lower() == 'n':
            break

    return False





if __name__ == '__main__':

    p = ap.ArgumentParser()
    p.add_argument("-f", "--function", default = '', help = "indicates a function's name to check only this function")
    p.add_argument("-a", "--all", action='store_true', help = "checks all functions without details")
    args = p.parse_args()

    fakestdout = StringIO.StringIO() # Fake file object for Stdout interception
    stdout = sys.stdout # Backup stdout


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


    # Override function name from cmd line argument
    if args.function != "":
        findtarget = [t for t in targets if t[0] == args.function]
        if len(findtarget) == 0:
            print "Error: Target function [%s] not found." % args.function
            sys.exit(1)
        else:
            print "Override: testing only [%s]" % args.function
            targets = findtarget


    print "=" * 79
    __test__ = {} # Functions mapped in __test__ are actually tested by doctest
    for fname, f in targets:
        __test__[fname] = f

        # Intercept Stdout
        sys.stdout = fakestdout
        res = doctest.testmod()
        # Restore Stdout
        sys.stdout = stdout
        test = string.ljust("{}".format(fname), 24, ' ') + " {}"

        if res.failed == 0:
            print colorString("green", test.format(res))
        else:
            if not args.all:
                print "=" * 79

            color = "yellow" if res.failed < res.attempted else "red"
            print colorString(color, test.format(res))

            if not args.all:
                print
                notPassing = prompt_release_stdout(fakestdout)
                if not notPassing:
                    break


        fakestdout.close()
        fakestdout = StringIO.StringIO()
        del __test__[fname]

        if fname == "updateGrid":
            print "-> You can now test main_v1.py"
        elif fname == "doCmd":
            print "-> You can now write main_v2.py"
        elif fname == "updateGrids":
            print "-> You can now write main_v3.py"


    print "=" * 79



