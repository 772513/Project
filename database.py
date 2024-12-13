import sqlite3

#creates connection to database with cursor to perform SQL code
#variable made global to be accessed within other functions
def openConnection():
    global conn, cursor
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

#saves changes to database
#closes connection to database
def closeConnection():
    conn.commit()
    conn.close()

#creates database tables if they don't already exist
def createTables():
    openConnection()

    #users table stores iformation about users
    #usertype defines who can add and edit scores 
    cursor.execute("""  CREATE TABLE IF NOT EXISTS Users (
                        username CHAR NOT NULL PRIMARY KEY,
                        forename CHAR,
                        surname CHAR,
                        pw CHAR,
                        email CHAR,
                        userType BIT
                        )
                   """)
    
    #matches table stores data entered when the match is created like date and location
    cursor.execute("""  CREATE TABLE IF NOT EXISTS Matches (
                        matchID INT AUTO_INCREMENT PRIMARY KEY,
                        matchLocation CHAR,
                        matchDate DATE,
                        weekNum INT
                        )
                   """)
    
    #scores table stores scores each turn with a composite primary key
    #the composite primary key is used to determine which match it took place in and the player
    cursor.execute("""  CREATE TABLE IF NOT EXISTS Scores (
                        matchID INT,
                        username CHAR,
                        turn1 CHAR,
                        turn2 CHAR,
                        turn3 CHAR,
                        turn4 CHAR,
                        turn5 CHAR,
                        turn6 CHAR,
                        turn7 CHAR,
                        turn8 CHAR,
                        turn9 CHAR,
                        turn10 CHAR,
                        PRIMARY KEY(matchID, username),
                        FOREIGN KEY(matchID) REFERENCES Matches(matchID),
                        FOREIGN KEY(username) REFERENCES Users(username)
                        )
                   """)
    closeConnection()

def createUser(username, forename, surname, password, email, type):
    openConnection()
    cursor.execute('''  INSERT INTO Users (username, forename, surname, pw, email, userType)
                        VALUES (?, ?, ?, ?, ?, ?)''', 
                        (username, forename, surname, password, email, type))
    closeConnection()

# def createMatch():
#     openConnection()
#     cursor.execute('''  INSERT INTO matches (date, venue, teamName, teamLocation, fixture, teamScore)
#                         VALUES (?, ?, ?, ?, ?, ?)''')

# print(rows)