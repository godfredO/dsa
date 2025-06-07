"""The question gives two input lists, redShirtHeights and blueShirtHeights, which represent the heights of students in a class wearing
a specific color. The students in the class are to take a class photo and they are to be arranged in two rows, a front row and a back
row. All the students in each row must have the same shirt color, meaning if the front row is all red shirts, the back row must be all
blue shirts. The next constraint is whichever color goes in which row, the student in the back row must be strictly taller than the 
corresponding student in the front row. And we are tasked with writing a function that returns a boolean representing a class photo that 
satisfies these constraints can be taken given the input. So if you are the photographer the obvious way to meet these constraints to to 
pair the shortest student in the front row with the shortest student in the back row, then the second shortest student in the front row with 
the second shortest student in the back row etc. Thus you first have to sort the heights of students for each color and then pair them.
And to determine which color goes in the front/back row, we just compare the heights of shortest students for the two colors, which will
be the first student in each sorted list. Therefore if the shortest red color student is shorter than the shortest blue color student then 
the red color students go in the front, the blue color students go in the back, and vice versa. Thus the greedy solution is to sort the two 
input arrays, choose which color goes in the front and then compare the corresponding heights in the sorted array. If for any pair of student
heights, the front row student height is found to be equal or taller than the back row student, we return False. If however we compare all 
height pairs and each student in the front row is strictly shorter than the corresponding student in the back row, we return True."""

def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()  #sort in-place
	blueShirtHeights.sort() #sort in-place
	
	firstrow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	
	for i in range(len(redShirtHeights)):
		# if first row is red, each red shirt must be shorter than corresponding blue
		if firstrow == "RED":
			if redShirtHeights[i] >= blueShirtHeights[i]:
				return False
		# if first row is blue, each blue shirt must be shorter than corresponding red
		else:
			if blueShirtHeights[i] >= redShirtHeights[i]:
				return False
	return True

def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	frontRow = redShirtHeights if redShirtHeights[0] < blueShirtHeights[0] else blueShirtHeights
	backRow = blueShirtHeights if frontRow == redShirtHeights else redShirtHeights

	for idx in range(len(frontRow)):
		if frontRow[idx] >= backRow[idx]:
			return False
	return True


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

redShirtHeights = [6, 9, 2, 4, 5, 1]
blueShirtHeights =  [5, 8, 1, 3, 4, 9]

print(classPhotos(redShirtHeights, blueShirtHeights))