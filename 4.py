import mysql.connector

db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database = 'MyFirstDB'
    )
my_database = db_connection.cursor()
deleteQuery = "DELETE FROM MyFirstDB WHERE name='Bob'"
               
my_database.execute(deleteQuery)
db_connection.commit()
print("Строки удалены")


