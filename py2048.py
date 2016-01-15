# Author : Rakesh Gariganti 15/Jan/2016
from random import choice
from os import system
from string import center
class New2048:
	def __init__(self,size):
		self.grid = [[' ']*size for i in range(size)]
		self.size = size
		self.score = 0
		self.cellwidth = 6
		self.rowsize = 2*size+1+(size*self.cellwidth)
	def printGrid(self):
		system("clear")
		print "_"*self.rowsize
		for i in range(self.size):
			print "|",
			for j in range(self.size):
				print center(str(self.grid[i][j]),self.cellwidth)+"|",
			print "\n"+"_"*self.rowsize
		print "Score: ",self.score
	def isOver(self):
		if self.getRandomEmptyCell() != None:return False
		for i in self.grid:
			for j in xrange(1,self.size):
				if i[j] == i[j-1]:
					return False
		for i in xrange(1,self.size):
			for j in xrange(self.size):
				if self.grid[i][j] == self.grid[i-1][j]:
					return False
		return True
	def getRandomEmptyCell(self):
		empty_cells = []
		for i in range(0, self.size):
			for y in range(0, self.size):
				if self.grid[i][y] == ' ':empty_cells.append((i,y))
		if len(empty_cells) > 0:return choice(empty_cells)
		else:return None
	def addNewNumber(self):
		new_cell = self.getRandomEmptyCell()
		if new_cell == None:return False
		else:
			i,j = new_cell
			self.grid[i][j] = 2
			return True
	def settleDown(self, op):
		if op in "aaaAAA":
			for i in range(0, self.size):
				row = self.grid[i]
				temp = []
				for j in row:
					if j != " ":
						temp.append(j)
				if len(temp)>1:
					t = 1
					while t < len(temp):
						if temp[t] == temp[t-1]:
							temp[t] = 2*temp[t]
							self.score += temp[t]
							temp.pop(t-1)
							t += 2
						else:t += 1
				temp.extend([" "]*(self.size-len(temp)))
				self.grid[i] = temp
		elif op in "dddDDD":
			for i in range(0, self.size):
				row = self.grid[i]
				temp = []
				for j in row:
					if j != " ":
						temp.append(j)
				if len(temp)>1:
					t = len(temp)-2
					while t >= 0:
						if temp[t] == temp[t+1]:
							temp[t] = 2*temp[t]
							self.score += temp[t]
							temp.pop(t+1)
							t -= 2
						else:t -= 1
				temp2 = [" "]*(self.size-len(temp))
				temp2.extend(temp)
				self.grid[i] = temp2
		elif op in "wwwWWW":
			for i in xrange(self.size):
				column = []
				for j in xrange(self.size):
					column.append(self.grid[j][i])
				temp = []
				for j in column:
					if j != " ":
						temp.append(j)
				if len(temp)>1:
					t = 1
					while t < len(temp):
						if temp[t] == temp[t-1]:
							temp[t] = 2*temp[t]
							self.score += temp[t]
							temp.pop(t-1)
							t += 2
						else:t += 1
				temp.extend([" "]*(self.size-len(temp)))
				for j in xrange(self.size):
					self.grid[j][i] = temp[j]
		elif op in "sssSSS":
			for i in xrange(self.size):
				column = []
				for j in xrange(self.size):
					column.append(self.grid[j][i])
				temp = []
				for j in column:
					if j != " ":
						temp.append(j)
				if len(temp)>1:
					t = len(temp)-2
					while t >= 0:
						if temp[t] == temp[t+1]:
							temp[t] = 2*temp[t]
							self.score += temp[t]
							temp.pop(t+1)
							t -= 2
						else:t -= 1
				temp2 = [" "]*(self.size-len(temp))
				temp2.extend(temp)
				for j in xrange(self.size):
					self.grid[j][i] = temp2[j]
		else:
			if raw_input("Do you want to quit the game?(y/n):") in ['y','Y']:exit()
			else:self.settleDown(raw_input("Move: "))
	def start(self):
		self.addNewNumber()
		self.addNewNumber()
		while True:
			self.printGrid()
			op = raw_input("Move: ")
			if op != "" and op != None:
				self.settleDown(op)
				self.addNewNumber()
			if self.isOver():
				self.printGrid()
				print "Game Over, your Score: ",self.score
				exit()
def Main():
	print "Starting the game engine...\n\t\t	 Press 'a' to move the Grid Left\n\t\t	 Press 's' to move the Grid Down\n\t\t	 Press 'd' to move the Grid Right\n\t\t	 Press 'w' to move the Grid Up\n\t\t	 At anytime press 'Ctrl+c' to exit"
	size = -1
	while size<2:size = int(raw_input("Enter the size of the grid(greater than 1 please): "))
	New2048(size).start()
if __name__ == '__main__':
	try:Main()
	except KeyboardInterrupt:print "\nExiting.."