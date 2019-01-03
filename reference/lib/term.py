#!/usr/bin/env python
# -*- coding: utf-8 -*-
# THIS IS THE SOURCE FILE TO CONVERT
"""
Copyright (c) 2015-2016, René Tanczos <gravmatt@gmail.com> (Twitter @gravmatt)
The MIT License (MIT)

pyterm helps positioning the cursor and styling output inside the terminal.

Project on github https://github.com/gravmatt/pyterm
"""

__author__ = 'Rene Tanczos'
__version__ = '0.4'
__license__ = 'MIT'

import sys
import re
from subprocess import Popen, PIPE


OFF = '\033[0m\033[27m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERSCORE = '\033[4m'
BLINK = '\033[5m'
REVERSE = ' \033[7m'
HIDE = '\033[8m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

BGBLACK = '\033[40m'
BGRED = '\033[41m'
BGGREEN = '\033[42m'
BGYELLOW = '\033[43m'
BGBLUE = '\033[44m'
BGMAGENTA = '\033[45m'
BGCYAN = '\033[46m'
BGWHITE = '\033[47m'


def send(cmd):
    sys.stdout.write(cmd)
    sys.stdout.flush()


def pos(line, column):
    send('\033[%s;%sf' % (line, column))


def homePos():
    send('\033[H')


def up(value=1):
    send('\033[%sA' % value)


def down(value=1):
    send('\033[%sB' % value)


def right(value=1):
    send('\033[%sC' % value)


def left(value=1):
    send('\033[%sD' % value)


def saveCursor():
    send('\0337')
    # send('\033[s')


def restoreCursor():
    send('\0338')
    # send('\033[u')


def clear():
    send('\033[2J')


def clearLineFromPos():
    send('\033[K')


def clearLineToPos():
    send('\033[1K')


def clearLine():
    send('\033[2K')


def write(text='', *style):
    send(format(text, *style))


def writeLine(text='', *style):
    write(str(text) + '\n', *style)


def strip(text):
    return re.sub('\x1b\[[0-9]{1,2}m', '', text)


def center(text):
    return ' ' * (int(getSize()[1] / 2) - int(len(strip(text)) / 2)) + text


def right(text):
    return ' ' * (getSize()[1] - len(strip(text))) + text


def getSize():
    p = Popen('stty size', shell=True, stdout=PIPE, stderr=PIPE)
    err = p.stderr.read().strip()
    if(err):
        return (0, 0)
    else:
        out = p.stdout.read().decode('ascii').strip().split(' ')
        return int(out[0]), int(out[1])


def format(text, *style):
    if(style):
        return '%s%s%s' % (''.join(style), text, OFF)
    else:
        return text


def highlight(pattern, text, func):
    output = ''
    idx = 0
    matches = [(m.start(), m.end()) for m in re.finditer(pattern, text)]
    for p in matches:
        output += text[idx:p[0]]
        output += func(text[p[0]:p[1]])
        idx = p[1]
    output += text[idx:]
    return (output, len(matches), matches)
