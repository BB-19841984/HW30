import mysql.connector

db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database = 'MyFirstDB'
    )
my_database = db_connection.cursor()
sql_statemnt = "Select * FROM Employees"
my_database.execute(sql_statemnt)
output = my_database.fetchall()
print (output[8-1])

db_connection.commit()
db_connection.close()