import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), "../")))
import pryzm

pz = pryzm.Pryzm()
test_string = pz.fg_red("Test String")
assert u"\u001b[31mTest String\u001b[0m" ==  test_string, "Simple red background"
print(test_string)

test_string = pz.bg_white(pz.fg_red("Test String"))
assert u"\u001b[47m\u001b[31mTest String\u001b[0m\u001b[0m" ==  test_string, test_string
print(test_string)

test_string = pz.encode([31,47], "Test String")
assert u"\u001b[31;47mTest String\u001b[0m" ==  test_string, test_string
print(test_string)


pz.clear_screen()
pz.set_position(0,0)
pz.write(pz.bg_red("Efrain"))
pz.move_down(4)
pz.write(pz.bg_blue("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
for dt in range(2):
    pz.move_right(1)
    pz.sleep(1)
    pz.write( pz.bg_cyan("yay"))
pz.set_position(0,10)
for dt in range(2):
    pz.move_down(1)
    pz.sleep(0.5)
    pz.write(pz.bg_red("wow"))
saystuff = ["Wow", "This", "Is", "Going", "to", "GREAT!"]
for word in saystuff:
    pz.set_position(30,10)
    pz.write(pz.bg_red(word))
    pz.sleep(0.5)
    pz.clear_line()
