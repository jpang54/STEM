import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "password", "school")

# prepare a cursor object using cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)

sql = "UPDATE students SET age=20 WHERE name='Junhong'"

# execute SQL query using execute() method.
cur.execute(sql)

# commit changes in database
db.commit()

# disconnect from server
cur.close()
db.close()

