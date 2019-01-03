import pryzm

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