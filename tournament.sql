-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE IF NOT EXISTS players ( player_id serial PRIMARY KEY,
									 name text,
									 UNIQUE (player_id));

CREATE TABLE IF NOT EXISTS matches ( match_id serial PRIMARY KEY,
									 winner integer NOT NULL REFERENCES players(player_id),
									 loser integer NOT NULL REFERENCES players(player_id));

CREATE VIEW wins_record AS 
	SELECT a.player_id, count(b.match_id) as wins
	FROM players a LEFT JOIN matches b ON a.player_id = b.winner
	GROUP BY a.player_id;

CREATE VIEW matches_played AS
	SELECT a.player_id, count(b.match_id) as matches
	FROM players a LEFT JOIN matches b ON a.player_id = b.winner or a.player_id = b.loser
	GROUP BY a.player_id