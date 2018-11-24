# Alex Laubscher

import random

class Necklace:

	def __init__(self, length, jewels):
		self.length  = length
		self.num_jewels = len(jewels)
		self.jewels = jewels
		self.dict = {}
		self.necklace = []

	def getNecklace(self):
		for i in range(self.num_jewels):
			self.necklace.append(self.jewels[i])
			self.necklace.append(self.jewels[i])
		while(len(self.necklace) != self.length):
			temp = random.choice(self.jewels)
			self.necklace.append(temp)
			self.necklace.append(temp)
		return self.necklace

	def getLength(self):
		return self.length



