CREATE TABLE IF NOT EXISTS Scores (
                        matchID INT,
                        username CHAR,
                        turn1 INT,
                        turn2 INT,
                        turn3 INT,
                        turn4 INT,
                        turn5 INT,
                        turn6 INT,
                        turn7 INT,
                        turn8 INT,
                        turn9 INT,
                        turn10 INT,

                        PRIMARY KEY (matchID, username),
                        FOREIGN KEY matchID REFERENCES Matches matchID,
                        FOREIGN KEY username REFERENCES Users username
                        )