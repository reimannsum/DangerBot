import pytest


test_html_files = [
    (
        'clough-towers',
        {
            'location': {
                'name': 'Clough Towers',
                'coords': (89, 97),
                'barricade': 'VERY_HEAVY',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 47,
                'hp': 50,
                'xp': 0,
            },
        }
    ),
    (
        'clough-towers-bino-n',
        {
            'location': {
                'name': 'Clough Towers',
                'coords': (89, 97),
                'barricade': 'VERY_HEAVY',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 41,
                'hp': 50,
                'xp': 0,
            },
        }
    ),
    (
        'clough-towers-bino-ne',
        {
            'location': {
                'name': 'Clough Towers',
                'coords': (89, 97),
                'barricade': 'VERY_HEAVY',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 43,
                'hp': 50,
                'xp': 0,
            },
        }
    ),
    (
        'fricker-crescent-police-dept-low-ap',
        {
            'location': {
                'name': 'Fricker Crescent Police Dept',
                'coords': (90, 94),
                'barricade': 'EXTREMELY_HEAVY',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 7,
                'hp': 50,
                'xp': 1,
            },
        }
    ),
    (
        'glyde-bank',
        {
            'location': {
                'name': 'Glyde Bank',
                'coords': (90, 91),
                'barricade': 'VERY_STRONG',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 2,
                'hp': 50,
                'xp': 1,
            }
        }
    ),
    (
        'hanham-way',
        {
            'location': {
                'name': 'Hanham Way',
                'coords': (90, 93),
                'barricade': None,
                'dead': 1,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 6,
                'hp': 50,
                'xp': 1,
            }
        }
    ),
    (
        'kingham-drive',
        {
            'location': {
                'name': 'Kingham Drive',
                'coords': (99, 82),
                'barricade': None,
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 11,
                'hp': 50,
                'xp': 1,
            }
        }
    ),
    (
        'sprackling-square-police-dept-ext',
        {
            'location': {
                'name': 'Sprackling Square Police Dept',
                'coords': (88, 97),
                'barricade': 'VERY_STRONG',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 50,
                'hp': 50,
                'xp': 0,
            },
        }
    ),
    (
        'st-francis-hospital',
        {
            'location': {
                'name': "St Francis's Hospital",
                'coords': (90, 96),
                'barricade': 'OPEN',
                'dead': 0,
                'zombies': 1,
            },
            'player': {
                'name': 'GMClaystyle',
                'ap': 40,
                'hp': 50,
                'xp': 0,
            },
        }
    ),
    (
        'swansborough-park',
        {
            'location': {
                'name': 'Swansborough Park',
                'coords': (68, 53),
                'barricade': None,
                'dead': 3,
                'zombies': 4,
            },
            'player': {
                'name': 'MaltonMapper1',
                'ap': 37,
                'hp': 0,
                'xp': 12,
            },
        }
    ),
    (
        'warehouse',
        {
            'location': {
                'name': 'a warehouse',
                'coords': (60, 63),
                'barricade': 'VERY_STRONG',
                'dead': 0,
                'zombies': 0,
            },
            'player': {
                'name': 'MaltonMapper1',
                'ap': 33,
                'hp': 7,
                'xp': 23,
            },
        }
    ),
]


@pytest.fixture(params=range(len(test_html_files)), ids=lambda i:  test_html_files[i][0])
def example_file(request):
    return test_html_files[request.param]
