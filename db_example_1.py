import sqlite3
print(sqlite3.sqlite_version)

# 1 - Connect to a database/create a database
dbconn = sqlite3.connect('library_example')

# 2 - Create a cursor object to allow us to execute SQL statements
cursor = dbconn.cursor()

# 3 - SQL Statement - CREATE TABLE
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY, title TEXT, author TEXT, price TEXT, year TEXT)
''')

# 4 - SQL Statement - INSERT RECORDS
cursor.execute('''INSERT INTO books values(1, 'Pro Powershell', 'Bryan Cafferky', 35.00, 2015)''')
cursor.execute('''INSERT INTO books values(2, 'Hitchhikers Guide to the Galaxy', 'Douglas Adams', 12.00, 1999)''')

# 5 - Commit changes
dbconn.commit()

# 6 - SQL Statement - SELECT
lstbooks = cursor.execute('''SELECT * from books;''').fetchall() 
print(lstbooks)