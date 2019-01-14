import requests
import word2number as w2n
from bs4 import BeautifulSoup as Soup
#using BeautifulSoup4 to parse page data this might change if selenium proves to be easier to get this info from
s = requests.session()


def get_soup(request):
    return Soup(request.text, 'html.parser')



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
    plan = []
    ## This is the Dictionary that will convert move directions into coodinates
    dirs = {'U': [0, -1], 'U-R': [1, -1], 'U-L': [-1, -1], 'R': [1, 0], 'L': [-1, 0], 'D': [0, 1]}

    def set_plan(self, moves_list):
        self.plan = moves_list

    def get_move(self, position):
        return self.plan [position[0]][position[1]]


class Walker():
    #   online flag to allow for playing even when bot can't connect to the wiki (before wiki access is built)
    online = False
    #name of current character
    name = ''
    #   is the character currently dead
    is_dead = False
    #   GPS position
    pos = [0,0]
    #   Character AP
    AP = 0
    #   Place name, building name, to identify which DangerReport page to update
    loc = ""
    #   suburb name, some locations names are used more than once. in those cases the suburb is needed to properly create the
    sub = ""


    #number of walking or resting corpses
    zed = 0
    ded = 0
    ## This is the dictionary that i will check against the building description string.
    b = {"doors secured": 0, 'loosely barricaded': 1, 'lightly barricaded': 2, 'quite strongly barricaded': 3,
         'very strongly barricaded': 4, 'heavily barricaded': 5, 'very heavily barricaded': 6,
         'extremely heavily barricaded': 7, 'wide open': -1}
    cade = -1
    burb_path = getPaths()
    soup = Soup()

    def get_events(self):
        events = self.soup.ul.get_text().split('\n')
        relevent_events = []
        for event in events:
            if 'The lights went' in event:
                relevent_events.append(event)
        return relevent_events

    def get_position(self):
        # find the value of the first input in the page, which is the move to the N-E
        not_pos = self.soup.input['value']
        not_pos = not_pos.split('-')
        for index in range(2):
            self.pos[index] = int(not_pos[index])


    # TODO: update()     this will do the updating of the walker
    def update(self, list_of_info):
        #   find suburb
        self.sub = self.soup.find(class_='sb').get_text()
        #   Find all the text boxes
        text = self.soup.find_all(class_='gt')
        #   get AP of character
        self.AP = int(text[0].find_all('b')[-1].get_text())
        #   record the name of the current location
        self.loc = text[1].find('b').get_text()
        #   find the character's position
        self.get_position()


    #TODO: read()       this will read the web page and record the surroundings
    def read(self):
        text = self.soup.find_all(class_='gt')
        info_box = text[1]
        for level,val in self.b.items():
            if level in info_box.get_text():
                self.cade = val
        # Not sure that I need to process the events that happen between days
        #get_events()
        self.update()
        return

    #TODO:  write_log()     this will write all info to a log file
    def write_log(self):
        log_string = f"Log of {self.name} at {self.pos}\nLocation: {self.loc} in {self.sub}\n"
        log_string = f"AP: {self.ap}   Dead? {self.is_dead}\n"
        log_string += f"Ccndition: {list(self.b[self.cade])}\nZombies:\nZed: {self.zed}  Ded:{self.ded}"

        return

    #TODO:  write_wiki()    this will write the info to the wiki, thisa must include generating the correcr text for the DRs
    def write_wiki(self):

        #   Also write to log file, until I know no problems exist
        self.write_log()
        return



    #TODO: write()      this will write the info found into a log that can be transitioned into writing into the wiki
    def write(self):
        if self.online:
            self.write_wiki()
        else:
            self.write_log()
        return

    #TODO: move()        write this for real
    def move(self):
        #   determine move to make based on current suburb
        # pos % 10 = suburb_index
        #   determine exact move based on current square
        # malton[suburb_index] = suburb_index
        # move_vals = burb_path[suburb_index].get_move(posR10)
        # test/check to see if pos + move_vals are still valid positions within the suburb

        # make move call and read new page data




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