"""This question gives two input lists, redShirtSpeeds, blueShirtSpeeds, representing the speeds of tandem bike riders wearing a specific
shirt color and a boolean named fastest. If fastest is true our function should maximize the total tandem bike speed after pairing up 
riders to form a team. Thus a team consists of one red shirt and one blue shirt and the speed of a tandem bicycle is determined by the
team rider with the higher speed for. Thus if fastest is true, we maximize the total tandem bike speed by maximizing the tandem bike 
speed for each team. If fastest is False, we minimize the total tandem bike speed by minimizing the tandem bike spped for each team. Let's
handle the case where fastest is True. Since each team has to have a red shirt rider and a blue shirt rider, in order to maximize the speed
of each team, we need to ensure that the fastest red/blue team riders determine the speeds of their teams. This means we need to sort the
arrays in opposite directions so that the fastest red team rider is on the same team with the slowest blue team rider, thus ensuring that
all the fastest riders determine the speed of their bicycles. Conversely, if fastest is False, we minimize the speed of each team by 
ensuring that the slowest riders determine the speed of their tandem bicycles and we achieve this by pairing up the slowest riders from
each team so that one of them determines the speed of their bicycles and we do this by sorting both arrays in the same direction and 
pairing up the corresponding riders. Thus if fastest is true, we sort in opposite directions before pairing up, determining the speed of
each bicycle and adding up all the speeds. If fastest is false, we sort in the same direction before pairing up, determining the speed of
each bicycle and adding up all the speeds."""

#O(nlog(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	if fastest:
		blueShirtSpeeds.sort(reverse=True)
	else:
		blueShirtSpeeds.sort()
	
	totalSpeed = 0
	for i in range(len(redShirtSpeeds)):
		totalSpeed += max(redShirtSpeeds[i],blueShirtSpeeds[i])
		
	return totalSpeed


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True
print(tandemBicycle(redShirtSpeeds,blueShirtSpeeds,fastest))