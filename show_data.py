import mysql.connector

# Open database connection
conDict = {'host':'localhost',
           'user':'root',
           'database':'hangman_data',
           'password':''}

db = mysql.connector.connect(**conDict)

# Prepare a cursor object
cursor = db.cursor()

# Execute SQL Query
cursor.execute("SELECT * FROM game_records")

print("User_name\tWin Count\tLost Count\tTotal Play Count\n================================================================")

# Fetch result
data = cursor.fetchall()
for item in data:
    for val in item:
        print(val, end = "\t\t  ")
    print()
    
# Execute SQL Query
#cursor.execute("SELECT * FROM marks_records")
#print("\nRec No.\tMark1\tMark2\tMark3\tMark4\tMark5\n==============================================")

# Fetch result
#data = cursor.fetchall()
#for item in data:
    #for val in item:
        #print(val, end = "\t")
    #print()

db.close()
