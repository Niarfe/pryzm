#!/usr/bin/env python
import time
import sys
from subprocess import Popen, PIPE
class Pryzm(object):
    _cap27 = '\033[27m'
    _text_attributes = {
        'at_off':       0,
        'at_bold':      1,
        'at_dim':       2,
        'at_italic':    3,
        'at_under':     4,
        'at_blink':     5,
        'at_reverse':   6,
        'at_hide':      8,

        'fg_black':     30,
        'fg_red':       31,
        'fg_green':     32,
        'fg_yellow':    33,
        'fg_blue':      34,
        'fg_magenta':   35,
        'fg_cyan':      36,
        'fg_white':     37,

        'bg_black':     40,
        'bg_red':       41,
        'bg_green':     42,
        'bg_yellow':    43,
        'bg_blue':      44,
        'bg_magenta':   45,
        'bg_cyan':      46,
        'bg_white':     47,
    }

    _clear = {
            'clear_screen': '2J',
            'clear_screen_to_end': '0J',
            'clear_screen_to_start': '1J',
            'clear_line': '2K',
            'clear_line_to_end': '0K',
            'clear_line_to_start': '1K',
            }

    _cursor = {
            'move_up': 'A',
            'move_down': 'B',
            'move_right': 'C',
            'move_left': 'D',
            'move_next_line': 'E',
            'move_prev_line': 'F',
            'move_column': 'G'
            }

    def set_position(self, x, y):
        sys.stdout.write(u"\u001b[{0};{1}H".format(str(x), str(y)))

    def _add_color(self, color, value):
        """Add dynamic function to insert color code.
           color: string, the name of the functio to add
           value: integer, the code value to insert
           return: function, adds a function named 'color' wrapping test with ascii code.
        """
        def fn(self, text):
            return u"\u001b[{0}m{1}\u001b[0m".format(value, text)

        setattr(Pryzm, color, fn)

        fn.__name__ = color
        fn.__doc__ = "Apply {0} to text".format(color)

    def _add_clear(self, function_name, code):
        def fn(self):
            sys.stdout.write(u"\u001b[{0}".format(code))

        setattr(Pryzm, function_name, fn)

        fn.__name__ = function_name
        fn.__doc__ = "Use code {0} to maneuver screen clears".format(code)

    def _add_cursor(self, function_name, code):
        def fn(self, num):
            sys.stdout.write(u"\u001b[{0}{1}".format(str(num), code))

        setattr(Pryzm, function_name, fn)

        fn.__name__ = function_name
        fn.__doc__ = "Use code {0} to maneuver screen cursor".format(code)


    def __init__(self):
        for key, val in self._text_attributes.items():
            self._add_color(key, val)
        for key, val in self._clear.items():
            self._add_clear(key, val)
        for key, val in self._cursor.items():
            self._add_cursor(key, val)

    def encode(self, codes, display_text):
        """Convenience method, format codes into ascii wrapper around text.
            This does NO checking, it simply formats.
            codes: list of codes, for example [31, 47] # 31 red text, 47 white bg
            return: string of formated text, for example u"\u001b[31;47 \u001b[0m"
        """
        codec = ";".join([str(idx) for idx in codes])
        return u"\u001b[{0}m{1}\u001b[0m".format(codec, display_text)

    def sleep(self, t):
        time.sleep(t)

    def write(self, st):
        sys.stdout.write(st)
        sys.stdout.flush()

    def get_screen_size(self):
        p = Popen('stty size', shell=True, stdout=PIPE, stderr=PIPE)
        out = p.stdout.read().decode('ascii').strip().split(' ')
        return int(out[0]), int(out[1])

if __name__ == "__main__":
    pryzm = Pryzm()
    test_string = pryzm.fg_red("Test String") 
    assert u"\u001b[31mTest String\u001b[0m" ==  test_string, "Simple red background"
    print(test_string)

    test_string = pryzm.bg_white(pryzm.fg_red("Test String"))
    assert u"\u001b[47m\u001b[31mTest String\u001b[0m\u001b[0m" ==  test_string, test_string
    print(test_string)

    test_string = pryzm.encode([31,47], "Test String")
    assert u"\u001b[31;47mTest String\u001b[0m" ==  test_string, test_string
    print(test_string)


    pryzm.clear_screen()
    pryzm.set_position(0,0)
    pryzm.write(pryzm.bg_red("Efrain"))
    pryzm.move_down(4)
    pryzm.write(pryzm.bg_blue("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
    for dt in range(2):
        pryzm.move_right(1)
        pryzm.sleep(1)
        pryzm.write( pryzm.bg_cyan("yay"))
    pryzm.set_position(0,10)
    for dt in range(2):
        pryzm.move_down(1)
        pryzm.sleep(0.5)
        pryzm.write(pryzm.bg_red("wow"))
    saystuff = ["Wow", "This", "Is", "Going", "to", "GREAT!"]
    for word in saystuff:
        pryzm.set_position(30,10)
        pryzm.write(pryzm.bg_red(word))
        pryzm.sleep(0.5)        
        pryzm.clear_line()





