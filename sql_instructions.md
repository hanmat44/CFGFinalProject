To use the database functionality of the  game you must first:

1. Create a config.py python that includes the following:

````python
USER = 'root'
HOST = 'localhost'
PASSWORD = 'your password for my_sql'
````

2. Then run the following code in MySQL:

````sql
CREATE database toptrumps;
USE toptrumps;

CREATE table TotalScores(
	player varchar(255),
    score int
    );

INSERT INTO TotalScores
(player, score)
VALUES
('person',0),
('computer',0);
````
You are now ready to run the  sql component of the game.

After you have played as many rounds as you would like, please run
check_scores to see your final score. The scores will then be reset.