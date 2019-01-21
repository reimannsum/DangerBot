from helpers import get_html_from_file
from dangerbot.page.map import Map


######################
# Environment
######################


def test_map_location(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.location() == data['location']['name']


def test_map_coords(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.coordinates() == data['location']['coords']


def test_map_baracade_level(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.barricade_level() == data['location']['barricade']


def test_map_dead_count(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.count_dead() == data['location']['dead']

def test_map_zed_count(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.count_zombies() == data['location']['zombies']


######################
# Player Status
######################

def test_player_name(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.player() == data['player']['name']


def test_player_ap(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.getAP() == data['player']['ap']


def test_player_hp(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.getHP() == data['player']['hp']


def test_player_xp(example_file):
    file, data = example_file
    page = Map(get_html_from_file(file), raise_exceptions=True)
    assert page.getXP() == data['player']['xp']
