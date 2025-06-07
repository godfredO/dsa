
"""This question is about a round robin tournament, a tournament where each competitor plays in turn against every other. In this 
tournament only two teams compeate against each other at a time. For each competition one team is the home team, the other the 
away team, there is only one winner, one loser, no ties and a team receives 3 points if it wins, 0 points if it loses. The winner
of the tournament is the team with the most amount of points. The input consists of array of pairs representing the teams for
each competition and an array of results for each competition. The pairs in the competitions array is of form [homeTeam, awayTeam], 
eachteam is represented by at most 30 letter name of the team. In the results array, results[i] denotes the winner of competitions[i]
where a 1 denotes that the home team won and a 0 means that the away team won. It is guaranteed one team will win the tournament, and
the tournament will have at least two teams. The question wants us to return the winning team. 
The solution to this question utilizes the constant time access afforded by a hashtable and the fact that in Python variable names 
are references that point to data. So we initialize a reference for the tournament winner and have it point to an empty array. We
then create a league table hashtable and set the tournament winner reference as a key with 0 value. This means if there are 6 teams
in this tournament the hashtable will have 6 keys, one for each team and one for the tournament winner. This allows us to simplify
comparisons and also update the team pointed to by the tournament winner variable. So thats what we do. We loop through the results
away with indices, because we know that results[i] corresponds to competitions[i]. And based on the results[i] ;1 means hometeam,
which is the first name in the competions[i] pair won , if 0 the away team won; we set the winning team, and add 3 points to the
value of the winning team. We then compare the points of the current winning team to the points of the  team referenced by the 
tournament winner and if the current team's updated point haulage exceeds the points of the reference team, we update the string
referenced by the tournament winner. Thus the team_on_top:0 key in the hashtable serves as a placeholder for the first comparsion
because after that whenever we reference leagueTable[team_on_top], we will be referring to one of the other key, value pairs.This
solution is linear time and linear space. """

#O(n) time | O(n) space
def tournamentWinner(competitions,results):
    team_on_top = "" #initialize an empty string with a team_on_top reference pointing to it

    leagueTable = {team_on_top:0} #add the team of top key with a point of zero
    
    for i in range(len(results)):
        if results[i] == 1:  #read the result of competition i, if its is 1, home team won
            winning_team = competitions[i][0]     #set winning_team variable to home team name
        else:
            winning_team = competitions[i][1]    #set winning+_team variable to away team name

        winningTeamInTable(winning_team, leagueTable)  #add three points to  winning team tally
        if leagueTable[winning_team] > leagueTable[team_on_top]: #compare to tournament winner each time a winner is recorded
            team_on_top = winning_team      #update the string referenced by team_on_top variable
        
    return team_on_top  #return the string pointed to by team_on_top reference

def winningTeamInTable(winning_team, leagueTable):
    if winning_team in leagueTable:
        leagueTable[winning_team] += 3  #increment winning team points if team name already in
    else:
        leagueTable[winning_team] = 3



def tournamentWinner(competitions, results):
	tournamentWinner = ""
	leagueTable = {tournamentWinner:0}
	for i in range(len(results)):
		winningTeam = competitions[i][0] if results[i] == 1 else competitions[i][1]

		updateLeaguePoints(leagueTable, winningTeam)

		if leagueTable[winningTeam] > leagueTable[tournamentWinner]:
			tournamentWinner = winningTeam
	return tournamentWinner


def updateLeaguePoints(leagueTable, winningTeam):
	if winningTeam not in leagueTable:
		leagueTable[winningTeam] = 0
	leagueTable[winningTeam] += 3





competitions = [
    ["HTML","C#"],
    ["C#", "Python"],
    ["Python","HTML"],
]

results = [0,0,1]

print(tournamentWinner(competitions,results))

