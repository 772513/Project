#datetime is used to calculate the week number for each match
import sqlite3, datetime
from datetime import datetime

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

def calculateWeekNumber():
    openConnection()
    #obtaining current date
    cursor.execute('''  SELECT DATE("NOW") DATE''')
    currentDate = cursor.fetchone()[0]

    #checking whether a match exists in the Matches table
    #if it doesn't exist, it returns a week number of 1 and currentDate
    cursor.execute('''  SELECT COUNT(*) FROM Matches''')
    firstMatchCheck = cursor.fetchone()
    if firstMatchCheck[0] == 0:
        weekNum = 1
        return currentDate, weekNum

    #retrieves the date of the first match
    cursor.execute('''  SELECT matchDate FROM Matches''')
    firstMatchDate = cursor.fetchone()[0]
    closeConnection()

    #calculates the difference between the first match date and current date
    firstMatchDate = datetime.strptime(firstMatchDate, '%Y-%m-%d').date()
    currentDate = datetime.strptime(currentDate, '%Y-%m-%d').date()
    dateDiff = abs(firstMatchDate - currentDate).days
    weekNum = int(dateDiff / 7) + (dateDiff % 7 > 0) + 1
    return currentDate, weekNum

def createMatch(location):
    currentDate, weekNum = calculateWeekNumber()
    openConnection()
    cursor.execute('''  INSERT INTO Matches (matchLocation, matchDate, weekNum)
                        VALUES (?, ?, ?)''',
                        (location, currentDate, weekNum)
                        )
    closeConnection()

# print(rows)