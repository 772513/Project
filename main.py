import database

database.createTables()
database.createUser('tester', 'first', 'last', 'test123', 'tester@gmail.com', 'scorer')
database.createMatch('cheltenham')