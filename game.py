#!/usr/bin/python

import cmd
from room import get_room
import textwrap
import shutil
import tempfile

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile)

        self.loc = get_room(1, self.dbfile)
        self.look()

    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("You can't go that way")
        else:
            self.loc = get_room(newroom, self.dbfile)
            self.look()

    def look(self):
        print("self.loc.name")
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_up(self, args):
        """Go up"""
        self.move('up')

    def do_down(self, args):
        """Go down"""
        self.move('down')

    def do_north(self, args):
        """Go North"""
        self.move('north')

    def do_south(self, args):
        """Go South"""
        self.move('south')

    def do_east(self, args):
        """Go East"""
        self.move('east')

    def do_west(self, args):
        """Go West"""
        self.move('west')

    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing!")
        return True

    def do_exit(self, args):
        """Leaves the game"""
        print("Thank you for playing!")
        return True


if __name__ == "__main__":
    game = Game()
    game.cmdloop()
