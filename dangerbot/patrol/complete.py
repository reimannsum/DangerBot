from .paths.complete import *


class CompletePatrol(object):
    """A patrol route that covers every square in the game"""
    def __init__(self, coords=(0, 0)):
        self.coords = coords

    def set_pos(self, coords):
        self.coords = coords

    def get_suburb_number(self):
        return MALTON[self.coords[0]//10][self.coords[1]//10]

    def get_next_pos(self):
        suburb_coords = (self.coords[0] % 10, self.coords[1] % 10)
        return SUBURB_PATHS[self.get_suburb_number()][suburb_coords[0]][suburb_coords[1]]
