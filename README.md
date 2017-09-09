Tournament Project for Udacity course Intro to Relational Databases
version 1.0 09/08/2017

The following flies are for the Tournament Project for the Udacity course Intro to Relational Databases.  This is my proposed solution for completing the project for a Swiss-style game tournament.  The program allows users to register players, delete players and matches, report match outcomes, view standings, and see a possible match up of opponents for the next round of matches.  This is in no way the only way to solve the problem, it only represents my approach to solving it.

To setup Tournament database, use tournament.sql file to create the database and create the appropriate Tables & Views.

Import the tournament.py file into a python file and use the associated functions to do the following actions:
-connect(): connect to the tournament database and create a cursor
-deleteMatches(): delete all matches from the database
-deletePlayers(): delete all players form the database
-countPlayers(): count the number of registered players
-registerPlayer(name): register a player for the name provided
-reportMatch(winner,loser): report the Winner and Loser for a match, with associated player_ids
-playerStandings(): see the standings for all players ranked from most wins to least
-swissPairings(): see a list of pairings for the next round of matches

Contact information:
Michael O'Brien
michael@mpobrien.co
