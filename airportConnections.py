"""
Tag: Graph; Hard

The question gives a list of airports, a list of routes and a starting airport. Each route is a list
or tuple with the source and destination airports of the route and each airport is representated by a
three letter string. The question is asking to find the minimum number of routes that need to be added
in order to be able to reach each airport from the starting airport either directly or withlayovers. The
most important thing to realize is that this question can be modelled as a graph where the nodes are
airports and the edges are routes which will be directed edges because the source, destination matters
in that order. The solution involves five distinct steps. First we need to iterate through the routes
given in order to generate a graph or some sort of data structure that models the question in a way that
makes it easy to work through. Second we conduct a dfs from the starting airport in order to determine
the airports that are unreachable from the starting airport. That is if a dfs with the starting airport
as source node doesn't find a particular airport in our list of airports, then that airport is unreachable
from the starting airport, thus filtering the unreachables. Third we conduct another dfs from each
unreachable airport in order to give a score for the number of unreachable airports that are themselves
reachable from the current unreachable airport. The score given includes all airports that can be reached
from a particular unreachable airport either directly or with layovers. This score is simply the number of
unreachable airports that are reachable from each unreachable airport. Fourth we sort all the unreachable
airports by this score in descending order. Finally, starting with the unreachable airport with the highest
score, we add a connection from the starting airport and then iterate through all the airports reachable
from the recently connected airport and then mark them as reachable. That is to say, the single connection
from the starting airport to a hitherto unreachable airport will also connect all the other airports in the
hitherto unreachable airport's network so whenever we add a connection we have to iterate through the
connected airports network and now mark those as reachable and then go back to adding a connection to the
next unreachable airport with the highest score, mark all other unreachable airports in its network
as reachable before going on. The idea is that if at most we need an additional connection between
the starting airport as each unreachable airport. Since the unreachable airports likely have connecting
routes among them, we may not need as many additonal connections as there are unreachable airports. Thus
we need to identify the unreachable airports that are reachable from other unreachable airports and also
make sure that additional connections are first added to the unreachable airport that connect to most
unreachable airport. Its possible that a single connection is all we need if one unreachable airport
could already be connected to the rest. This solution depends on the isReachable and unreachableConnections
attributes of the AirportNode class that was created. The first attribute, isReachable helps us identify
airports that are reachable from the starting point, either before or after the addition of a new route.
The second attribue, unreachableConnections, helps us with the order in which to add additional routes.
To find the unreachable airports we use the visited set after the initial dfs from starting airport.

"""
# O(a*(a+r) + a+r + alog(a)) time | O(a+r) space


class AirportNode:
    def __init__(self, airport):
        self.airport = airport  # name of airport, three letter string
        self.connections = []  # store a list of connections from airport ie directed edges from current
        # Boolean, airport reachable from starting airport? Initialize to True cos starting airport reachable from itself
        self.isReachable = True
        # unreachable airports in current airport's network ie reachable from current airport
        self.unreachableConnections = []


def airportConnections(airports, routes, startingAirport):
    # first create a graph representing the airports and routes
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(  # unreachable from the starting airport
        airportGraph, airports, startingAirport)  # get list of unreachable airports' nodes
    # mark unreachable airports as unreachable in graph
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    # helper function to return min number of new connections
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)

# O(a+r) time | O(a+r) space - iterate and add airport and then routes to graph data structure


def createAirportGraph(airports, routes):
    airportGraph = {}  # we will use a hashtable for graph representation

    for airport in airports:  # add an airport key and an airport node for each airport key
        # map airport key to a node containing all info we need about an airport
        airportGraph[airport] = AirportNode(airport)

    for route in routes:  # add the routes originating from an airport to its node
        airport, connection = route  # unpack the routes list
        # add connection to connections list of airport node in airport graph
        airportGraph[airport].connections.append(connection)

    return airportGraph  # return the populated graph

# O(a+r) time | O(a) space - O(v+e) time for dfs v=airports e=routes, O(v) space for dfs v=airports


def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    # airports that are reachable from starting airport ie were able to be visited in dfs from starting airport
    visitedAirports = {}
    # dfs starting from starting airport to populate visitedAirports
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
    unreachableAirportNodes = []  # array of nodes of airports unreachable from starting airport to be populated below
    for airport in airports:  # going through the airports and the visited airports
        if airport in visitedAirports:  # first check if the airport was already visited in dfs ie reachable from starting node
            continue  # if already visited, skip to next airport (isReachable = True)
        # access node object stored at airport key in airport graph(hashtable: airport>node)
        airportNode = airportGraph[airport]  # grab airport node to mark isReachable=False
        airportNode.isReachable = False  # mark airport as unreachable in the node attribute
        # add unreachable airport node to array of unreachable airports
        unreachableAirportNodes.append(airportNode)  # populating unreachable nodes (for loop aim)
    return unreachableAirportNodes


def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:  # dfs base case, if airport is already visited
        return
    # add airport to visited airports if previously unvisited, initially starting airport is added
    visitedAirports[airport] = True  # ideally add to visited after for loop; set will suffice
    connections = airportGraph[airport].connections  # access the just visited airport's connections
    for connection in connections:  # for each connection
        # dfs to connections as reachable from starting node
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)

# O(a*(a+r)) time | O(a) space - unreachable airports could be up to one less than total airports, dfs time and space


# to find all airports reachable from unreachable airport and score
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:  # access unreachable airport's node
        airport = airportNode.airport  # access airport's name from node object
        unreachableConnections = []  # initialize unreachable connections as empty array
        depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {
        })  # dfs from all unreachable from starting airport to populate unreachable connections
        # update airport node with starting point unreachable connections reachable from current airport
        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    # if the airport reachable from unreachable airport is actually reachable from starting airport
    if airportGraph[airport].isReachable:  # skip reachables (dfs fitted with new base case)
        return  # then return, doesnt count towards the unreachable connections score ie unreachable connection has to be unreachable first
    if airport in visitedAirports:  # dfs always needs a way to track nodes already visited to avoid repeated work, getting stuck in cyles
        return  # if unreachable connection was already visited via someother node or edge return, avoid getting stuck in cycles
    # if unreachable and unvisited then mark unreachable connection as visited
    visitedAirports[airport] = True
    # then add to unreachable connections array, first to be added is airport itself
    unreachableConnections.append(airport)  # unreachables only because of first base case
    # then access the just added unreachable connection's connections from graph
    connections = airportGraph[airport].connections
    for connection in connections:  # dfs of connections to be added to unreachable connections if unvisited and indeed unreachable
        depthFirstAddUnreachableConnections(
            airportGraph, connection, unreachableConnections, visitedAirports)  # dfs on connection

# O(alog(a)+a+r) time | O(1)  - sorting up to a unreachable airports, iterating through unreachable airports and their connections


def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    # sort list of nodes descending by num unreachable connections of nodes
    unreachableAirportNodes.sort(key=lambda airport: len(  # unreachableAirportNodes is a list type with a sort method
        airport.unreachableConnections), reverse=True)  # descending order by number of reachable unreachables (greedy)
    numberOfNewConnections = 0  # initialize output, number of new connectins needed to be 0
    for airportNode in unreachableAirportNodes:  # unreachables for loop since not necessarily connected
        if airportNode.isReachable:  # previously unreachable node made reachable if new connection added to another node to which its connected
            continue  # if airport was in the unreachable connections of a node that received a new connection, its reachable and so skip
        numberOfNewConnections += 1  # one connection to unreachable airport and all its unreachableConnections
        # go through unreachable connections of airport which includes airport itself
        for connection in airportNode.unreachableConnections:  # new connection added making connections reachable
            # set previous unreachable connections as reachable
            airportGraph[connection].isReachable = True   # unreachableConnections via connection
    return numberOfNewConnections


airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND",
            "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]
startingAirport = "LGA"

print(airportConnections(airports, routes, startingAirport))
