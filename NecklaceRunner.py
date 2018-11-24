# Alex Laubscher
import random
from necklace import Necklace

def main():
	n = Necklace(20, ["D","S"])
	necklace = n.getNecklace()
	random.shuffle(necklace)
	print(necklace)

	cut_list = []
	while True:
		cut_list.append(n.getLength() / 2)
		result = testValid(necklace, cut_list)
		if result:
			print(cut_list)
			break
		
		for i in range(1, n.getLength() / 2):
			cut_list = []
			cut_list.append(i)
			cut_list.append(n.getLength() / 2 + i)
			result = testValid(necklace, cut_list)
			if result:
				print(cut_list)
				break
		break


def testValid(necklace, cut_list):
	one_list = []
	two_list = []
	counter = True
	start = 0

	cut_list.append(len(necklace))
	for index in cut_list:
		if counter:
			one_list += necklace[start:index]
			start = index
			counter = False
		else:
			two_list += necklace[start:index]
			start = index
			counter = True

	one_list.sort()
	two_list.sort()

	if one_list == two_list:
		print(one_list)
		print(two_list)
		return True
	else:
		return False

main()