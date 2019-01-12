import requests
from bs4 import BeautifulSoup as Soup
#using BeautifulSoup4 to parse page data this might change if selenium proves to be easier to get this info from
s = requests.session()
r = s.get('http://www.urbandead.com/map.cgi?username=MaltonMapper1&password=urbandead')

soup = Soup(r.text, 'html.parser')


def getPage(soup):
    r = s.get('http://www.urbandead.com/map.cgi?username=MaltonMapper1&password=urbandead')
    soup = Soup(r.text, 'html.parser')
    return soup






def getPaths():
    lists: List[str] = """R,R,R,R,R,R,R,R,R,D
    D,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,D
    D,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,D
    D,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,D
    D,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,D
    D,L,L,L,L,L,L,L,L,L
    ,,,,,,,,,
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    ,,,,,,,,,
    D,R,D,R,D,R,D,R,D,R
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    D,U,D,U,D,U,D,U,D,U
    R,U,R,U,R,U,R,U,R,U
    ,,,,,,,,,
    L,D,L,D,L,D,L,D,L,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,L,U,L,U,L,U,L,U,L
    ,,,,,,,,,
    R,R,R,R,R,R,R,R,R,U
    U,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,U
    U,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,U
    U,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,U
    U,L,L,L,L,L,L,L,L,L
    R,R,R,R,R,R,R,R,R,U
    U,L,L,L,L,L,L,L,L,L
    ,,,,,,,,,
    R,R,R,R,R,R,R,R,R,D
    U-L,D,L,D,L,D,L,D,L,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,D,U,D,U,D,U,D,U,D
    U,L,U,L,U,L,U,L,U,D
    ,,,,,,,,,
    R,D,R,D,R,D,R,D,R,D
    U,R,U,R,U,R,U,R,U,U-R
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U
    U,R,R,R,R,R,R,R,R,R
    L,L,L,L,L,L,L,L,L,U""".split(',,,,,,,,,')
    paths = []
    for x in range(7):
        paths.append([])
    for item in lists:
        paths[lists.index(item)] = item.lstrip().split('\n')
    for item in paths:
        for sub in range(10):
            item[sub] = item[sub].split(',')
    return lists

class Suburb():
    plan = [[]]
    ## This is the Dictionary that will convert move directions into coodinates
    dirs = {'U': [0, -1], 'U-R': [1, -1], 'U-L': [-1, -1], 'R': [1, 0], 'L': [-1, 0], 'D': [0, 1]}

    def set_plan(self, moves_list):
        plan = moves_list

    def get_move(self, right, down):
        return plan[right][down]


class Walker():
    #   online flag to allow for playing even when bot can't connect to the wiki (before wiki access is built)
    online = False

    #   GPS position
    pos = [0,0]
    #   Character AP
    AP = 0

    #   Place name, building name, to identify which DangerReport page to update
    loc = ""
    #   suburb name, some locations names are used more than once. in those cases the suburb is needed to properly create the
    sub = ""
    cade = ""
    burb_path = getPaths()

    #TODO: read()       this will read the web page and update all local variables (pos, loc, AP, ...)
    def read(self, URL):
        return

    #TODO: update()     this will probably exist and actually do the updating of the walker
    def update(self, list_of_info):
        return

    #TODO: write()      this will write the info found into a log that can be transitioned into writing into the wiki
    def write(self):
        return

    #TODO: move()        write this for real
    def move(self):
        # get_pos()
        # pos % 10 = suburb_index
        # malton[suburb_index] = suburb_index
        # move_vals = burb_path[suburb_index].get_move(posR10)
        # test/check to see if pos + move_vals are still valid positions within the suburb

    ## This is the dictionary that i will check against the building description string.
    b = {"doors secured":0, 'loosely barricaded':1, 'lightly barricaded':2, 'quite strongly barricaded':3,
         'very strongly barricaded':4, 'heavily barricaded':5, 'very heavily barricaded':6,
         'extremely heavily barricaded':7, 'wide open': -1}


    ## This is the index of the burb-path that will be taken in each suburb
    malton = """6,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,2,2,2,2,2,2,2,2,0
3,3,3,3,3,3,3,3,3,5""".split('\n')
    for sub in range(10):
        malton[sub] = malton[sub].split(',')