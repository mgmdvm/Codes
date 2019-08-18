import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "pi",
	passwd = "11235813m",
	database = "PHPSampledb"
)

mycursor= mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for row in myresult:
	print(row)
