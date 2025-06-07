"""Amazon ships millions of packages regularly. There are a number of parcels that need to be shipped. Compute the minimum possible sum of
transportation costs incurred in the shipment of additional parcels in the following scenario. A fully loaded truck carries k parcels. The
number of parcels already on the truck is listed in parcels array. There are parcels with a uniqe id that ranges from 1 through infinity. 
The parcel id is also the cost to ship that parcel. Given the parcel ids which are already added in the shipment, find the minimum possible
cost of shipping the items added to complete the load."""

"""The question is clearly shouting for a hashset. We loop over the parcels array and we add all the unique parcel ids to the hashset. We 
also calculate the number of new parcels to be added as k - len(parcels). So with that said, we start looking for new parcels, starting 
from parcel id = 1 and incrementing each time in the while loop, initializing an added variable which will track how many parcels we added
up to k - len(parcels), and a minCost variable that tracks the cost of added parcels. So before we increment parcel id, we check if the 
current new parcel id is not in the hashset. If its not, we add it to the 'truck' by adding its value to minCost and then incrementing 
added variable. When the while loop breaks, we would have added, exactly the number of parcels needed to fill up the track. So we return
minCost. The while loop can run up to O(k) times, and the hashset is O(n) space. """

#O(k) time | O(n) space
def getMinimumCost(parcels, k):
    if k < len(parcels):
        return 0

    needed = k - len(parcels)

    shipment = set()
    for parcel in parcels: #O(n)
        shipment.add(parcel)
    
    added = 0
    minCost = 0
    parcelId = 1
    while added < needed: #O(k)
        if parcelId not in shipment:
            minCost += parcelId
            added += 1
        parcelId += 1
    
    return minCost





#parcels = [2,3,6,10,11]
#k = 9
parcels = [6,5,4,1,3]
k = 7
print(getMinimumCost(parcels, k))