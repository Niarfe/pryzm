#!/usr/bin/env python
import time
import sys
from subprocess import Popen, PIPE
from pryzm.codes import cap27, text_attributes
class Pryzm(object):
    _cap27 = cap27
    _text_attributes = text_attributes
    def __init__(self, subject=None):
        self.subject = subject if subject else ''
        for key, val in self._text_attributes.items():
            self._add_color(key, val)
        # for key, val in self._clear.items():
        #     self._add_clear(key, val)
        # for key, val in self._cursor.items():
        #     self._add_cursor(key, val)

    def _add_color(self, color, code):
        """Add dynamic function to insert color code.
            color: string, the name of the function to add
            value: integer, the code value to insert
            return: function, adds a function named 'color' wrapping test with ascii code.
        """
        def fn(self, text=None):
            self.subject = text if text else self.subject
            self.subject =  u"\u001b[{0}m{1}".format(code, self.subject)
            return self

        setattr(Pryzm, color, fn)

        fn.__name__ = color
        fn.__doc__ = "Apply {0} to text".format(color)

    def set_position(self, x, y):
        sys.stdout.write(u"\u001b[{0};{1}H".format(str(x), str(y)))

    def show(self):
        return self.subject+u"\u001b[0m"

    def print(self):
        print(self.subject+u"\u001b[0m")

    def __str__(self):
        return self.subject

    def encode(self, codes, display_text):
        """Convenience method, format codes into ascii wrapper around text.
            This does NO checking, it simply formats.
            codes: list of codes, for example [31, 47] # 31 red text, 47 white bg
            return: string of formated text, for example u"\u001b[31;47 \u001b[0m"
        """
        codec = ";".join([str(idx) for idx in codes])
        return u"\u001b[{0}m{1}\u001b[0m".format(codec, display_text)








