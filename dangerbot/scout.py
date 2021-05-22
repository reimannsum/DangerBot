from http_wrapper import Http
from patrol import CompletePatrol
from page.map import Map


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
        password = "foo"  # fetch this from a file
        self.map = Map(self.driver.get(MAP_URL, {'username': name, 'password': password}))

    def move_to(self, pos):
        # use self.driver to load the next map location
        pass

    def report_on_position(self):
        # build the report output on the current location
        report = {}
        self.reporter.report(report)

    def scout(self):
        while (self.map.getAP() > 0):
            self.make_report()
            self.move_to(self.patrol.get_next_pos())
