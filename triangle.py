from graphics import *

def main():
	# Make the graphical windows to view the triangles
	pascal = GraphWin("Pascal's Triangle", 1000, 600)
	necklace = GraphWin("Necklace Triangle", 1200, 600)
	quotient = GraphWin("Quotient Triangle", 1200, 600)

	# Length can be as long as you want
	length = 20

	# Generates the three triangle that we want
	pascal_list = genPascal(length)
	necklace_list = genNecklace(length)
	quotient_list = getQuotient(pascal_list, necklace_list, length)

	# Moves all of the contents to the graphical window
	for i in range(len(pascal_list)):
		Text(Point(500, 25 + 25 * i), str(pascal_list[i])).draw(pascal)
		Text(Point(600, 25 + 25 * i), necklace_list[i]).draw(necklace)
		Text(Point(600, 25 + 25 * i), quotient_list[i]).draw(quotient)

	# Waits for click so the window stays open
	pascal.getMouse()
	necklace.getMouse()
	quotient.getMouse()

def genPascal(length):
	triangle = []
	for i in range(0,length):
		sub_tri = []
		for k in range(0,i):
			if k == 0 or k == i-1:
				sub_tri.append(1)
			else:
				sub_tri.append(triangle[i-1][k] + triangle[i-1][k-1])
		triangle.append(sub_tri)
	del triangle[0]
	return triangle 

def genNecklace(length):
	triangle = ["1/1"]
	for i in range(1,length):
		sub_tri = []
		num = i
		den = 1
		pause = False
		for k in range(i):
			inp = str(num) + "/" + str(den)
			sub_tri.append(inp)
			if k == 0:
				ratio = 1.1
			else:
				ratio = float(i)/2/float(k+1)
			if ratio > 1:
				if float(i)/2/float(k+1) < 0:
					pause = True
				if not pause:
					num = num - 1
					den = den + 1
			elif ratio < 1:
				num = num + 1
				den = den - 1
		triangle.append(sub_tri)
	del triangle[0]
	return triangle

def getQuotient(pascal, necklace, length):
	triangle = []
	new_list = []
	for line in necklace:
		sub_new = []
		for item in line:
			sub_new.append(item.split("/"))
		new_list.append(sub_new)

	triangle = []
	for i in range(length-1):
		sub_list = []
		for k in range(i+1):
			new_list[i][k][1] = int(new_list[i][k][1]) * int(pascal[i][k])
			sub_list.append(str(new_list[i][k][0])+"/"+str(new_list[i][k][1]))
		triangle.append(sub_list)

	return triangle

main()