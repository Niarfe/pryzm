#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This package contains utilities to 
* color text (in 10 different colors)
* color background (in 10 different colors)
* Get info about the screen
* Move cursor location on screen
"""

__author__  = 'Efrain Olivares'
__version__ = '0.0.1'
__license__ = 'MIT'

import sys
import re
from subprocess import Popen, PIPE

# Don't write out pyc files
# This can also be set via an environment variable
# export PYTHONDONTWRITEBYTECODE=1
sys.dont_write_bytecode = True

_OFF        = '\033[0m\033[27m'
_BOLD       = '\033[1m'
_DIM        = '\033[2m'
_UNDERSCORE = '\033[4m'
_BLINK      = '\033[5m'
_REVERSE    = '\033[7m'
_HIDE       = '\033[8m'

_BLACK      = '\033[30m'
_RED        = '\033[31m'
_GREEN      = '\033[32m'
_YELLOW     = '\033[33m'
_BLUE       = '\033[34m'
_MAGENTA    = '\033[35m'
_CYAN       = '\033[36m'
_WHITE      = '\033[37m'

_BGBLACK    = '\033[40m'
_BGRED      = '\033[41m'
_BGGREEN    = '\033[42m'
_BGYELLOW   = '\033[43m'
_BGBLUE     = '\033[44m'
_BGMAGENTA  = '\033[45m'
_BGCYAN     = '\033[46m'
_BGWHITE    = '\033[47m'

def off(txt):
    return '%s%s%s' % (_OFF, txt, _OFF)

def bold(txt):
    return '%s%s%s' % (_BOLD, txt, _OFF)

def dim(txt):
    return '%s%s%s' % (_DIM, txt, _OFF)

def underscore(txt):
    return '%s%s%s' % (_UNDERSCORE, txt, _OFF)

def blink(txt):
    return '%s%s%s' % (_BLINK, txt, _OFF)

def reverse(txt):
    return '%s%s%s' % (_REVERSE, txt, _OFF)

def hide(txt):
    return '%s%s%s' % (_HIDE, txt, _OFF)

def black(txt):
    return '%s%s%s' % (_BLACK, txt, _OFF)

def red(txt):
    return '%s%s%s' % (_RED, txt, _OFF)

def green(txt):
    return '%s%s%s' % (_GREEN, txt, _OFF)

def yellow(txt):
    return '%s%s%s' % (_YELLOW, txt, _OFF)

def blue(txt):
    return '%s%s%s' % (_BLUE, txt, _OFF)

def magenta(txt):
    return '%s%s%s' % (_MAGENTA, txt, _OFF)

def cyan(txt):
    return '%s%s%s' % (_CYAN, txt, _OFF)

def white(txt):
    return '%s%s%s' % (_WHITE, txt, _OFF)

def onBlack(txt):
    return '%s%s%s' % (_BGBLACK, txt, _OFF)

def onRed(txt):
    return '%s%s%s' % (_BGRED, txt, _OFF)

def onGreen(txt):
    return '%s%s%s' % (_BGGREEN, txt, _OFF)

def onYellow(txt):
    return '%s%s%s' % (_BGYELLOW, txt, _OFF)

def onBlue(txt):
    return '%s%s%s' % (_BGBLUE, txt, _OFF)

def onMagenta(txt):
    return '%s%s%s' % (_BGMAGENTA, txt, _OFF)

def onCyan(txt):
    return '%s%s%s' % (_BGCYAN, txt, _OFF)

def onWhite(txt):
    return '%s%s%s' % (_BGWHITE, txt, _OFF)

def clear():
    _send('\033[2J')

def home():
    _send('\033[H')

def _send(cmd):
    sys.stdout.write(cmd)
    sys.stdout.flush()

def put(cmd):
    _send(cmd)

def move(delx, dely):
    moves = []
    if (delx < 0):
        moves.append('\033[%sD' % abs(delx))
    elif (delx > 0):
        moves.append('\033[%sC' % delx)

    if (dely < 0):
        moves.append('\033[%sA' % abs(dely))
    elif (dely > 0):
        moves.append('\033[%sB' % dely)

    for move in moves:
        _send(move)


def moveTo(xpos, ypos):
    _send('\033[%s;%sf' % (ypos, xpos))


def getSize():
    p = Popen('stty size', shell=True, stdout=PIPE, stderr=PIPE)
    err = p.stderr.read().strip()
    if (err):
        return (0, 0)
    else:
        out = p.stdout.read().decode('ascii').strip().split(' ')
        return int(out[0]), int(out[1])
    

if __name__ == "__main__":
    clear()
    home()
    txt = "Hello World"
    print off(txt)
    print bold(txt)
    print dim(txt)
    print underscore(txt)
    print blink(txt)
    print reverse(txt)
    print hide(txt)


    print black(onWhite(txt))
    print red(onCyan(txt))
    print green(onMagenta(txt))
    print yellow(onBlue(txt))
    print blue(onYellow(txt))
    print magenta(onGreen(txt))
    print cyan(onRed(txt))
    print white(onBlack(txt))
    home()
    move(10, 10)
    print 'A'
    move(5,5)
    print 'B'
    for pos in range(20):
        moveTo(pos, pos)
        print 'Y'

    moveTo(20,20)
    print getSize()
    moveTo(12, 0)
    for pos in range(5):
        move(pos,pos)
        put(yellow(onBlue('#')))

