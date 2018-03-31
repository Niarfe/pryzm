#!/usr/bin/env python
import prysm as pm

class Window(object):
    wlines = -1
    wcols = -1

    def __init__(self):
        self.pr = pm.Prysm()
        self.wlines, self.wcols = self.pr.get_screen_size()
        print "wcols: {0} wlines: {1}".format(str(self.wcols), str(self.wlines))
        self.pr.sleep(0.25)


    def clear_and_set_cursor(self, x, y):
        self.pr.clear_screen()
        self.pr.set_position(x, y)


    def fill_row_open_ends(self, row, char):
        if row == -1: row = self.wlines
        self.pr.set_position(row, 2)
        for col in range(self.wcols - 2):
            self.pr.write(char)
            

    def fill_col_open_ends(self, col, char):
        if col == -1: col = self.wcols

        self.pr.set_position(2, col)
        for line in range(self.wlines -1):
            self.pr.write(char)
            self.pr.set_position(line+2, col)


    def pause_and_wait_for_input(self, dt):
        self.pr.sleep(dt)


if __name__ == "__main__":
    win = Window()
    win.clear_and_set_cursor(0,0)
    win.fill_row_open_ends(0, "*")
    win.fill_row_open_ends(-1, "*")
    win.fill_col_open_ends(0, "|")
    win.fill_col_open_ends(-1, "|")
    win.pause_and_wait_for_input(10)
