#! /usr/bin/env python

import select, termios, sys, time, tty

def inputWithTimeout(timeout):
    ''' (float) -> NoneType

    Gets input from standard input, for 'timeout' seconds.
    '''
    fd = sys.stdin.fileno()         # Get file descriptor for stdin.
    old = termios.tcgetattr(fd)     # Backup old terminal input mode.
    tty.setraw(fd, termios.TCSANOW) # Set the terminal to reactive mode.
    string = ""
    t_start = t_now = time.time()
    over = False
    while not over:
        # Select call returns when one char is available or timeout reached.
        r, w, x = select.select([sys.stdin], [], [], timeout - t_now + t_start)
        # Depending on the char, issue command to the snake.
        if sys.stdin in r:
            string += sys.stdin.read(1)
        # update time counters
        t_now = time.time()
        # Check if allocated time for the function to complete is spent.
        over = (t_now - t_start) > timeout
    # Restore old terminal input mode.
    termios.tcsetattr(fd, termios.TCSANOW, old)
    return string


if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res


