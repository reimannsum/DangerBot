import requests
import word2number as w2n
from bs4 import BeautifulSoup as Soup
#using BeautifulSoup4 to parse page data this might change if selenium proves to be easier to get this info from
s = requests.session()


def get_soup(request):
    return Soup(request.text, 'html.parser')



def getPaths():
    lists = """R,R,R,R,R,R,R,R,R,D
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
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
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
R,R,R,R,R,R,R,R,R,R
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
U,L,U,L,U,L,U,L,U,L
,,,,,,,,,
R,D,R,D,R,D,R,D,R,D
U,R,U,R,U,R,U,R,U,U-R
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
U,L,L,L,L,L,L,L,L,L
R,R,R,R,R,R,R,R,R,U
,,,,,,,,,
U,D,L,D,L,D,L,D,L,D
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
D,R,D,R,D,R,D,R,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
D,U,D,U,D,U,D,U,D,U
R,U,R,U,R,U,R,U,R,U""".split(',,,,,,,,,')
    paths = []
    for x in range(10):
        paths.append([])
    for item in lists:
        paths[lists.index(item)] = item.strip().split('\n')
    for item in paths:
        for sub in range(10):
            item[sub] = item[sub].split(',')
    burbs = []
    for item in paths:
        new_burb = Suburb()
        burbs.append(new_burb.set_plan(item))
    return burbs

class Suburb:
    plan = []
    ## This is the Dictionary that will convert move directions into coodinates
    dirs = {'U': [-1, 0], 'U-R': [-1, 1], 'U-L': [-1, -1], 'R': [0, 1], 'L': [0, -1], 'D': [1, 0]}

    def set_plan(self, moves_list):
        self.plan = moves_list
        return self

    def get_move(self, position):
        if position[0] < 0 or position[1] < 0:
            return
        return self.dirs[self.plan[position[0]][position[1]]]


class Walker:

    def __init__(self):
        #   online flag to allow for playing even when bot can't connect to the wiki (before wiki access is built)
        self.online = False
        #name of current character
        self.name = ''
        #   is the character currently dead
        self.is_dead = False
        #   GPS position
        self.pos = [0,0]
        #   Character AP
        self.ap = 0
        #   Place name, building name, to identify which DangerReport page to update
        self.loc = ""
        #   building_flag   this identifies if this is a building, and so will need a report and can be caded
        self.building = False
        #   suburb name, some locations names are used more than once. in those cases the suburb is needed to properly create the
        self.sub = ""


        #number of walking or resting corpses
        self.zed = 0
        self.ded = 0
        ## This is the dictionary that i will check against the building description string.
        self.b = {'wide open': -1, "doors secured": 0, 'loosely barricaded': 1, 'lightly barricaded': 2, 'quite strongly barricaded': 3,
             'very strongly barricaded': 4, 'heavily barricaded': 5, 'very heavily barricaded': 6,
             'extremely heavily barricaded': 7}
        self.cade = -1
        self.burb_path = getPaths()
        # soup = Soup()

        ## This is the index of the burb-path that will be taken in each suburb
        self.malton = """7,0,5,0,5,0,5,0,5,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,2,9,2,9,2,9,2,9,0
8,3,3,3,3,3,3,3,3,6""".split('\n')
        for sub in range(10):
            self.malton[sub] = self.malton[sub].split(',')
        for i in range(10):
            for j in range(10):
                self.malton[i][j] = int(self.malton[i][j])


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
    def update(self):
        #   find suburb
        self.sub = self.soup.find(class_='sb').get_text()
        #   Find all the text boxes
        text = self.soup.find_all(class_='gt')
        #   get AP of character
        self.ap = int(text[0].find_all('b')[-1].get_text())
        #   record the name of the current location
        self.loc = text[1].find('b').get_text()
        if 'a ' in self.loc:
            self.loc += ' ' + str(self.pos)
        #   find the character's position
        self.get_position()


    #TODO: read()       this will read the web page and record the surroundings
    def read(self):
        text = self.soup.find_all(class_='gt')
        info_box = text[1]

        if 'The building' in info_box.get_text():
            self.building = True
            for level,val in self.b.items():
                if level in info_box.get_text():
                    self.cade = val

        # Not sure that I need to process the events that happen between days
        # get_events()
        self.update()
        return

    #TODO:  write_log()     this will write all info to a log file
    def write_log(self):
        log_string = f"Log of {self.name} at {self.pos}\nLocation: {self.loc} in {self.sub}\n"
        log_string += f"AP: {self.ap}   Dead? {self.is_dead}\n"
        if self.building:
            log_string += f'Condition: {list(self.b)[self.cade+1]}'
        log_string += f'Zombies:  Zed: {self.zed}  Ded:{self.ded}\n'

        print(log_string)
        print('----------\n')

        return log_string

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
        suburb = [self.pos[0]//10, self.pos[1]//10]
        moveplan = self.malton[suburb[0]][suburb[1]]
        sub = 10*suburb[0] + suburb[1]

        #   determine exact move based on current square
        square = [self.pos[0] % 10, self.pos[1] % 10]
        # move_vals = burb_path[suburb_index].get_move(posR10)
        moves = self.burb_path[moveplan].get_move(square)
        # test/check to see if pos + move_vals are still valid positions within the suburb
        for i in range(2):
            self.pos[i] += moves[i]
        # make move call and read new page data

    #TODO: move2() this is the testing function
    def move2(self):
        #   determine move to make based on current suburb
        suburb = [self.pos[0]//10, self.pos[1]//10]
        moveplan = self.malton[suburb[0]][suburb[1]]
        sub = 10*suburb[0] + suburb[1]

        #   determine exact move based on current square
        square = [self.pos[0]%10, self.pos[1]%10]
        # move_vals = burb_path[suburb_index].get_move(posR10)
        moves = self.burb_path[moveplan].get_move(square)
        # test/check to see if pos + move_vals are still valid positions within the suburb
        for i in range(2):
            self.pos[i] += moves[i]
        # make move call and read new page data
        print(f'location = {self.pos} sub = {sub},\t\tMove plan {moveplan}\tMove {moves}')
        return sub



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