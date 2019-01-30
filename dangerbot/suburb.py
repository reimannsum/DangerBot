from dangerbot.paths import PATHS


class Suburb:
	# This is the index of the burb-path that will be taken in each suburb
	malton = """7,0,5,0,5,0,5,0,5,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,10,11,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,0,4,0,4,0,4,0,4,0
1,2,9,2,9,2,9,2,12,0
8,3,3,3,3,3,3,3,13,6""".split('\n')
	for sub in range(10):
		malton[sub] = malton[sub].split(',')
	for i in range(10):
		for j in range(10):
			malton[i][j] = int(malton[i][j])

	plan = []
	# This is the Dictionary that will convert move directions into coodinates
	dirs = {'U': [-1, 0], 'U-R': [-1, 1], 'U-L': [-1, -1], 'R': [0, 1], 'L': [0, -1], 'D': [1, 0], 'D-R': [1, 1], 'D-L': [1, -1]}

	def set_plan(self, moves_list):
		self.plan = moves_list
		return self

	def get_move(self, position):
		if position[0] < 0 or position[1] < 0:
			return
		return self.dirs[self.plan[position[0]][position[1]]]


def get_paths():
	lists = PATHS.split(',,,,,,,,,')
	paths = []
	for x in range(len(lists)):
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