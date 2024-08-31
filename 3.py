import mysql.connector

db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database = 'MyFirstDB'
    )
my_database = db_connection.cursor()
insertQuery = """
                INSERT INTO Employees(name, position, salary)
                VALUES('Jon', 'Layer', '55000')"""
my_database.execute(insertQuery)
print(f"Вставлено {my_database.rowcount} строка")
sql_statemnt = "Select * FROM Employees"
my_database.execute(sql_statemnt)
output = my_database.fetchall()
for x in output:
    print (x)

db_connection.commit()
db_connection.close()

