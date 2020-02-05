import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "password", "school")

# prepare a cursor object using cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)

sql = "INSERT INTO students (name,age,gradeLevel) VALUES ('Stephen', 7, 11)"

# execute SQL query using execute() method.
cur.execute(sql)
db.commit()

sql2 = "SELECT * from students"
cur.execute(sql2)
rows = cur.fetchall()
for row in rows:
	print("Name: " + row['name'] + " Age: " + str(row['age']) + " Grade level: " + str(row['gradeLevel'])) 

# disconnect from server
cur.close()
db.close()
