#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2, bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    # conn = psycopg2.connect('dbname=tournament')
    # return conn
    return psycopg2.connect('dbname=tournament')


def deleteMatches():
    # Remove all the match records from the database.
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM matches;")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM players;")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT count(name) as num FROM players;")
    players = cur.fetchone()
    db.close()
    return players[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT a.player_id, a.name, b.wins, c.matches FROM players a LEFT JOIN wins_record b ON a.player_id = b.player_id LEFT JOIN matches_played c ON a.player_id = c.player_id GROUP BY a.player_id, a.name, b.wins, c.matches ORDER BY b.wins DESC;")
    standings = cur.fetchall()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT INTO matches (winner,loser) VALUES (%s,%s);", (winner,loser,))
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players = []
    standings = playerStandings()
    for row in standings:
        players.append(row[0])
        players.append(row[1])
    pairings = []
    k = 0; j = 1; x = 2; y = 3
    for i in range(0,len(players)/4):
        pairings.append([players[k],players[j],players[x],players[y]])
        k += 4; j += 4; x += 4; y += 4
    return pairings

