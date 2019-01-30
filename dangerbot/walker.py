import requests
from os import path
from os import pardir
from dangerbot.suburb import Suburb
from dangerbot.suburb import get_paths
from bs4 import BeautifulSoup as Soup
# using BeautifulSoup4 to parse page data this might change if selenium proves to be easier to get this info from
s = requests.session()




class Walker:

	def __init__(self):
		#   online flag to allow for playing even when bot can't connect to the wiki (before wiki access is built)
		self.online = False
		# name of current character
		self.name = ''
		#   is the character currently dead
		self.is_dead = False
		#   Character position
		self.pos = [0, 0]
		#   Character AP
		self.ap = 0
		#   Place name, building name, to identify which DangerReport page to update
		self.loc = ""
		#   building_flag   this identifies if this is a building, and so will need a report and can be caded
		self.building = False
		#   the position to move to
		self.new_pos = [0, 0]
		#   suburb name, some locations names are used more than once. the suburb is needed to properly create the
		self.sub = ""
		self.page = requests.get('https://www.google.com')

		# number of walking or resting corpses
		self.zed = 0
		self.dead = 0
		# This is the dictionary that i will check against the building description string.
		self.b = {
			'wide open': -1,
			"doors secured": 0,
			'loosely barricaded': 1,
			'lightly barricaded': 2,
			'quite strongly barricaded': 3,
			'very strongly barricaded': 4,
			'heavily barricaded': 5,
			'very heavily barricaded': 6,
			'extremely heavily barricaded': 7
		}
		self.cade = -1
		self.is_lit = False
		self.burb_path = get_paths()

		self.file = open(path.abspath(path.join(pardir, path.join('logs', 'log.log'))), 'a')
		self.soup = Soup('', 'html.parser')

	def get_page(self, url):
		r = s.get(url)
		return Soup(r.text, 'html.parser')

	def get_position(self):
		# find the value of the first input in the page, which is the move to the N-E
		not_pos = self.soup.input['value']
		not_pos = not_pos.split('-')
		for index in range(2):
			self.pos[index] = int(not_pos[index]) + 1

	# TODO: update()     this will do the updating of the walker
	def update(self):
		#   find suburb
		self.sub = self.soup.find(class_='sb').get_text()
		#   find the character's position
		self.get_position()
		#   Find all the text boxes
		text = self.soup.find_all(class_='gt')
		#   get AP of character
		self.ap = int(text[0].find_all('b')[-1].get_text())
		#   record the name of the current location
		self.loc = text[1].find('b').get_text()
		if 'a ' in self.loc:
			self.loc += ' ' + str(self.pos)

	# TODO: read()       this will read the web page and record the surroundings
	def read(self):
		text = self.soup.find_all(class_='gt')
		info_box = text[1]

		if 'The building' in info_box.get_text():
			self.building = True
			for level, val in self.b.items():
				if level in info_box.get_text():
					self.cade = val

		# Not sure that I need to process the events that happen between days
		# get_events()
		self.update()
		return

	def write_log(self):
		log_string = "Log of %(location)s at %(position)s in %(suburb)s\n" % {'location':self.loc, 'position':self.pos,
		                                                                    'suburb':self.sub}
		if self.building:
			log_string += "Condition: %(condition)s , the lights are on: %(lights)s\n" % \
			              {'condition': list(self.b)[self.cade+1],'lights':self.is_lit}

		log_string += 'Zombies:  Zed: %(zombies)s  Dead:%(bodies)s\n----------\n' % \
		              {'zombies':self.zed ,'bodies':self.dead}
		return log_string

	def move(self):
		#   determine move to make based on current suburb
		suburb = [self.pos[0]//10, self.pos[1]//10]
		move_plan = Suburb.malton[suburb[0]][suburb[1]]

		#   determine exact move based on current square
		square = [self.pos[0] % 10, self.pos[1] % 10]
		moves = self.burb_path[move_plan].get_move(square)

		for i in range(2):
			self.new_pos[i] = self.pos[i] + moves[i]
		# make move call and read new page data
		self.soup = self.get_page('http://www.urbandead.com/map.cgi?v=' + str(self.new_pos[0]) + '-' + str(self.new_pos[1]))

	def walk(self):
		import datetime
		t = datetime.datetime.today()
		file_name = t.strftime('%d-%m-%y-walker1.txt')
		log_file = open(path.abspath(path.join('logs', file_name)), 'a')
		while self.ap > 0:
			self.read()
			log_file.write(self.write_log())
			self.move()
		return

	# TODO: move2() this is the testing function
	def move2(self):
		#   determine move to make based on current suburb
		suburb = [self.pos[0]//10, self.pos[1]//10]
		move_plan = Suburb.malton[suburb[0]][suburb[1]]
		sub = 10*suburb[0] + suburb[1]

		#   determine exact move based on current square
		square = [self.pos[0] % 10, self.pos[1] % 10]
		# move_vals = burb_path[suburb_index].get_move(posR10)
		moves = self.burb_path[move_plan].get_move(square)
		# test/check to see if pos + move_vals are still valid positions within the suburb
		for i in range(2):
			self.pos[i] += moves[i]
		# make move call and read new page data
		# print(f'location = {self.pos} sub = {sub},\t\tMove plan {move_plan}\tMove {moves}')
		return sub

	# TODO: login()
	def login(self, character):
		url_string = "http://www.urbandead.com/map.cgi?username=MaltonMapper" + character + "&password=urbandead"
		self.soup = self.get_page(url_string)
		self.name = self.soup.find_all(class_='gt')[0].b.contents[0]
		#   check to see if the walker is standing
		if self.soup.find_all(value='Stand up'):
			self.is_dead = True
		self.read()

		return

	#TODO: login2()  TESTING FUNCTION, REMOVE LATER
	def login2(self, files):
		file = open(files, 'r')
		self.soup = Soup(file.read(), 'html.parser')
		self.name = self.soup.find(class_='gt').b.contents[0]
		#   check to see if the walker is standing
		if self.soup.find_all(value='Stand up'):
			self.is_dead = True
		self.read()
		return


def _test_write():
	walker1 = Walker()
	walker1.login2(path.abspath(path.join(pardir, path.join('data', 'swansborough-park.html'))))
	print(walker1.write_log())
	walker1.login2(path.abspath(path.join(pardir, path.join('data', 'warehouse.html'))))
	print(walker1.write_log())


def _test_move():
	thing = []
	for i in range(10):
		thing.append([])
		for j in range(10):
			thing[i].append(0)
	walker1 = Walker()
	for i in range(10000):
		num = walker1.move2()
		thing[(num//10)][(num % 10)] += 1

	print('-------Turns in each square -------')
	print(thing[0])
	print(thing[1])
	print(thing[2])
	print(thing[3])
	print(thing[4])
	print(thing[5])
	print(thing[6])
	print(thing[7])
	print(thing[8])
	print(thing[9])


if __name__ == '__main__':
	_test_write()
	_test_move()
