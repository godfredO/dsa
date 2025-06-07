"""Brute Force Approach. For every city as starting city, traverse all other cities
until a valid starting city from which we can traverse other cities without ever
getting a negative gas mileage"""
#O(n^2) time | O(1) space
def validStartingCity(distances,fuel,mpg):
    numberOfCities = len(distances)

    for startCityIdx in range(numberOfCities):
        milesRemaining = 0

        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):#it is essential to get back to starting spot
            if milesRemaining < 0: #check if miles remaining is invalid
                continue
            currentCityIdx = currentCityIdx % numberOfCities #generate a valid circular index up to back to starting city

            fuelFromCurrentCity = fuel[currentCityIdx]
            distanceToNextCity = distances[currentCityIdx]
            milesRemaining += fuelFromCurrentCity*mpg - distanceToNextCity

        if milesRemaining >= 0: #if you get back to starting city with 0 or more miles
            return startCityIdx
    
    return -1

"""Optimal solution based on the facts that we are assured only one valid starting city, the total fuel mileage equals the total distances 
to be traversed. This means if we start at the valid starting city, we return with 0 gallons. If we start anywhere else, we arrive with
the minimum amount of gallons (negative). If we start at any invalid city, because we only have enough gallons of fuel to go round, we
will always arrive to the valid starting city with a lowest mileage. In fact, depending on the starting city we may have arrive to 
many other cities with negative mileage but of these, we arrive at the valid starting city with the most negative value. Thus we first
rephrase the original question as a question of how much mileage we arrive at any city wit by adding the gas from the previous city minus
the distance from the previous city and we keep track of the city that we arrive at with the lowest, most negative mileage. Thus by
realising that we will arrive to the valid starting city with the minimum mileage possible we are able to solve this question in pass
through the array. And we are able to initialize the miles remaining to 0 because we know that we will arrive at the first city with 0
and since we expect our valid city to have the most negative value, we can loop from the second city and use the first city's distance
and fuel in our calculations. Again, if we start at any other city other than the one valid city, we arrive at the valid city with the 
most minimum mileage possible. If we start at the one valid city, we arrive at every other city with a mileage greater than 0 and only
drop to zero when we get back to the valid city. So we intialize or assume the valid city is the first city and if it is, we will arrive
back there with 0. From there we calculate the mileage we arrive at each city with and compare this with the 0 mileage for the lowest
mileage and keep track of the index if we make an update. If our initial assumption is right, the first city's 0 mileage will still be
the lowest mileage arriving at any city and the lowest mileage arriving city will still be index 0. If we are wrong, we will still update
the lowest mileage arriving city to the valid city and we will store the most minimum value too. At the end we just return the index
of the lowest mileage arriving city, possibly updated irrespective of the mileage because we are assured a valid starting city."""
#O(n) time | O(1) space
def validStartingCityI(distances,fuel,mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1,numberOfCities):
        distanceFromPreviousCity = distances[cityIdx-1]
        fuelFromFromPreviousCity = fuel[cityIdx -1]
        milesRemaining += fuelFromFromPreviousCity *mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate


distances= [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

print(validStartingCity(distances,fuel,mpg))