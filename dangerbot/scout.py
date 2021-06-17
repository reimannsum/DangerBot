from http_wrapper import Http
from patrol import CompletePatrol
from page.mmap import mMap


MAP_URL = 'http://urbandead.com/map.cgi'


class Reporter(object):
    def report(self, report):
        # log the report somewhere. Probably using python's logging system
        # output probably wants to be a json object for easy parsing by the wiki editor
        pass


class Scout(object):
    """Scout is a glue class that knows how to make http requests"""
    def __init__(self, name, patrol=CompletePatrol, http=Http, reporter=Reporter):
        self.driver = http()
        self.load_initial_page(name)
        self.patrol = patrol(self.map.coordinates())
        self.reporter = reporter()

    def load_initial_page(self, name):
        """Load the credentials from the config file and performs a login"""
        # this is just a rough outline
        password = "urbandead"  # fetch this from a file
        self.map = mMap(self.driver.get(MAP_URL, {'username': name, 'password': password}))

    def move_to(self, pos):
        # use self.driver to load the next map location
        # remember coords will be reversed for the patrol class
        move = self.patrol.get_next_pos()
        xy = self.map.coordinates()
        coords = "" + (xy[1] + move[1]) + "-" + (xy[0] + move[0])
        self.map = mMap(self.driver.get(MAP_URL, {'v': coords}))
        pass

    def make_report(self):
        # build the report output on the current location
        report = ""
        suburb = self.map.suburb()
        location = self.map.location()
        coords = self.map.coordinates()
        real_coords = (coords[1], coords[0])
        report = "{}"

        self.reporter.report(report)

    def scout(self):
        while self.map.getAP() > 0:
            self.make_report()
            self.move_to(self.patrol.get_next_pos())
        return 1
