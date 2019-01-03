import os
import sys
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../")))

import pryzm

def test_red_fg():
    pz = pryzm.Pryzm()
    assert pz.fg_red("blah") == '\x1b[31mblah\x1b[0m'

