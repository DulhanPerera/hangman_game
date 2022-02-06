def insertFunc(all_data):
    import mysql.connector
    #import random

    # Open database connection
    conDict = {'host':'localhost',
               'database':'hangman_data',
               'user':'root',
               'password':''}
    
    db = mysql.connector.connect(**conDict)

    # Prepare a cursor object
    cursor = db.cursor()

    #execute SQL query
    text = "INSERT INTO game_records(user_name, Win_Count, Lost_Count, TotalPlay_Count) VALUES (%s, %s, %s, %s)"
    myValues = (all_data[0], all_data[1], all_data[2], all_data[3])
    cursor.execute(text, myValues)

    # Commit Changes
    db.commit()
    print(cursor.rowcount, "Record Added")

    # Disconnect the server
    db.close()
    return
