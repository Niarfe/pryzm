#!/usr/bin/env python

class Ansi(object):
    def __init__(self):
        self._attributes = {
                'reset': 0,
                'on_bright_red': 101
                }

        
    def is_foreground(self, code): 
        return (code in range(30, 37 + 1)) or (code in range(90, 97 + 1))

    def is_background(self, code):
        return (code in range(40, 47 + 1)) or (code in range(100, 107 + 1))

    def is_style(self, code):
        return (code in range(1, 9 +1))



# Test Cases

def setup_module(module):
    print module 
    module.ansi = Ansi()

def test_is_foreground():

    foreground_cases = {
        29: False,
        30: True,
        37: True,
        89: False,
        97: True,
    }

    for key in foreground_cases: 
        assert(ansi.is_foreground(key) == foreground_cases[key])

def test_is_background():
    background_cases = {
        39: False,
        40: True,
        47: True,
        99: False,
        107: True,
    }
    for key in background_cases: 
        assert(ansi.is_background(key) == background_cases[key])


def test_is_style():
    style_cases = {
        0: False,
        1: True,
        8: True,
        10: False,
        5: True,
    }
   
    for key in style_cases: 
       assert(ansi.is_style(key) == style_cases[key])

  
 
