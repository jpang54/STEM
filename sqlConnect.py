import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "password", "school")

# prepare a cursor object using cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * from students"

# execute SQL query using execute() method.
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
	print("Name: " + row['name'] + " Age: " + str(row['age']) + " Grade level: " + str(row['gradeLevel'])) 

# disconnect from server
cur.close()
db.close()

