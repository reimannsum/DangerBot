import re
from bs4 import BeautifulSoup as BeautifulSoup
from word2number.w2n import word_to_num

from dangerbot.logger import logger

BARRICADE_CAPTURE = (
                        r'(?P<open>wide open)|'
                        r'(?P<secured>doors secured)|'
                        r'(?P<loose>loosely barricaded)|'
                        r'(?P<light>lightly barricaded)|'
                        r'(?P<quite_strong>quite strongly barricaded)|'
                        r'(?P<very_strong>very strongly barricaded)|'
                        r'(?P<heavy>heavily barricaded)|'
                        r'(?P<very_heavy>very heavily barricaded)|'
                        r'(?P<extremely_heavy>extremely heavily barricaded)'
                    )
HP_CAPTURE = r'(\d+) Hit Points?'
AP_CAPTURE = r'(\d+) Action Points?'
XP_CAPTURE = r'(\d+) Experience Points?'
ZOMBIES_CAPTURE = r'There (is|are) (?P<count>[^.]+) zombies?'
BODIES_CAPTURE = r'There (is|are) (?P<count>[^.]+) dead (body|bodies)'

## A map object should to all computation on initialization, any calls to it should be only pulling values it holds


class mMap(object):
    def __init__(self, html="", raise_exceptions=False):
        super(mMap, self).__init__()
        self._html = BeautifulSoup(html, 'html.parser')
        self._player_node = None
        self._environment_node = None
        self._raise = raise_exceptions

    def __repr__(self):
        return "mMap[{}]".format(self.location())

    def _raise_or_log(self, msg, node):
        text = "{} Node[{}]".format(msg, node.get_text())
        if self._raise:
            raise Exception(text)
        else:
            logger.warn(text)

    def _element(self, selector):
        """Return an HTML node by css selector. The selector must be present and should describe a unique element"""
        return self._html.select(selector)[0]

    def _player(self):
        if self._player_node is None:
            self._player_node = self._element('.cp .gt')
        return self._player_node

    def _environment(self):
        if self._environment_node is None:
            self._environment_node = self._element('.gp .gt')
        return self._environment_node

    def _match_text(self, node, regex, force_match=True):
        m = re.search(regex, node.get_text())
        if force_match and m is None:
            self._raise_or_log('Pattern not found for "{}"'.format(regex), node)
        return m

    def player(self):
        return self._player().a.string

    def getHP(self):
        hp = self._match_text(self._player(), HP_CAPTURE)
        return int(hp.group(1))

    def getAP(self):
        ap = self._match_text(self._player(), AP_CAPTURE)
        return int(ap.group(1))

    def getXP(self):
        xp = self._match_text(self._player(), XP_CAPTURE)
        return int(xp.group(1))

    def location(self):
        return self._environment().b.string


    def suburb(self):
        suburb_name = self._element('table.c td.sb').string
        return suburb_name

    def coordinates(self):
        current_td = self._element('table.c td > input[type="submit"]').parent
        value = '999-999'
        offset = (0, 0)
        for e in current_td.next_siblings:
            if e.name == 'td':
                value = e.form.input['value']
                offset = (-1, 0)
                break
        if offset == (0, 0):
            for e in current_td.previous_siblings:
                if e.name == 'td':
                    value = e.form.input['value']
                    offset = (1, 0)
        if offset == (0, 0):
            self._raise_or_log('Cannot determine location', current_td)
        coords = tuple(map(int, value.split('-')))
        return (coords[0] + offset[0], coords[1])

    def barricade_level(self):
        level = self._match_text(self._environment(), BARRICADE_CAPTURE, force_match=False)
        if level is None:
            return None
        else:
            groups = level.groupdict().items()
            for lvl, match in groups:
                if match is not None:
                    return lvl.upper()
        self._raise_or_log('Unable to determine barricade level', self._environment())

    def count_dead(self):
        match = self._match_text(self._environment(), BODIES_CAPTURE, force_match=False)
        count = -1
        if match is None:
            count = 0
        elif match.group('count') == 'a':
            count = 1
        elif match.group('count') is not None:
            count = word_to_num(match.group('count'))

        if count == -1 or count is None:
            count = None
            self._raise_or_log('Unable to determine body count', self._environment())
        return count

    def count_zombies(self):
        match = self._match_text(self._environment(), ZOMBIES_CAPTURE, force_match=False)
        count = -1
        if match is None:
            count = 0
        elif match.group('count') == 'a lone':
            count = 1
        elif match.group('count') is not None:
            count = word_to_num(match.group('count'))

        if count == -1 or count is None:
            count = None
            self._raise_or_log('Unable to determine body count', self._environment())
        return count
