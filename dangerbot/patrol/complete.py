from paths.complete import SUBURB_PATHS


class CompletePatrol(object):
    """A patrol route that covers every square in the game"""
    def __init__(self, coords=(0, 0)):
        self.coords = coords

    def set_pos(self, coords):
        self.coords = coords

    def get_suburb_coords(self):
        pass

    def get_next_pos(self, arg):
        pass
