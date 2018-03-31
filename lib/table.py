#!/usr/bin/env python
import sys
width = 16 
for i in range(0, width):
    for j in range(0, width):
        code = str(i * width + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print u"\u001b[0m"

for i in range(0, width):
    for j in range(0, width):
        code = str(i * width + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print u"\u001b[0m"
