# creating a Player class that will take two parameters name and score
class Player:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	# implementing a key method to use as a key in sorted function
	def key(self):
		return (-self.score, self.name)



n = int(input('Enter the no of instances to create : '))

data = []

for _ in range(n):
	name, score = input().split()
	score = int(score)
	player = Player(name, score)
	data.append(player)

data = sorted(data, key = Player.key, )

for i in data:
	print(i.name, i.score)