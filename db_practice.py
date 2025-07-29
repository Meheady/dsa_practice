import mysql.connector

print("Script started...")


print("✅ Connected to database.",mysql.connector.connect(
        host="127.0.0.1",        # use IP instead of 'localhost'
        user="root",
        password='' ,
        database="bishworang",
        connection_timeout=5
    ))
