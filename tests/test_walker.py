from os import path
from dangerbot.walker import Walker


def test_write():
    walker1 = Walker()
    walker1.login2(path.abspath(path.join('data', 'swansborough-park.html')))
    assert walker1.write_log == """Log of MaltonMapper1 at [67, 52]
Location: Swansborough Park in Roftwood
AP: 37   Dead? True
Zombies:  Zed: 0  Ded:0
"""

    walker1.login2(path.abspath(path.join('data', 'warehouse.html')))
    assert walker1.write_log == """Log of MaltonMapper1 at [59, 62]
Location: a warehouse [59, 62] in Tollyton
AP: 33   Dead? True
Condition: very strongly barricaded
Zombies:  Zed: 0  Ded:0
"""


def test_move():
    pass
