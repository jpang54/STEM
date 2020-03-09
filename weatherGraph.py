# Import the required modules
import matplotlib.pyplot as plt 
import pymysql
import os

# Create empty lists for time, humidity, temperature
timeList = []
humidityList = []
temperatureList = []

# Open database connection
db = pymysql.connect("192.168.0.205","humid","password","sensor")

# Prepare a cursor object using cursor() method
cur = db.cursor(pymysql.cursors.DictCursor)
  
# Select all data points              
sql = "SELECT * FROM weather";

# Execute SQL query using execute() method.
cur.execute(sql)
rows = cur.fetchall()
  
# Append data of each row in respective lists
for row in rows:
  temperatureList.append(row['temperature'])
  humidityList.append(row['humidity'])
  timeList.append(str(row['time']))

# Reference: https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/two_scales.html
fig, ax1 = plt.subplots(figsize=(10,5))
# Change temperature line graph to red
color = 'tab:red'
# Set x and y axis labels. Change temperature y axis to red
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature', color=color)
# Plot data points
ax1.plot(timeList, temperatureList, color=color)
# Change y axis tick marks to red
ax1.tick_params(axis='y', labelcolor=color)

# Rotate time on x-axis by 30 degrees so they don't overlap
plt.xticks(timeList, timeList, rotation=30)

# Instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()  

# Set humidity graph to blue
color = 'tab:blue'
# We already handled the x-label with ax1 so we only need to change y-label
ax2.set_ylabel('Humidity', color=color)  
ax2.plot(timeList, humidityList, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Otherwise the right y-label is slightly clipped
fig.tight_layout()

# If the file already exists, replace the file
if os.path.exists('/var/www/html/graph.png'):
  os.remove('/var/www/html/graph.png')
  plt.savefig('/var/www/html/graph.png')
else:
  plt.savefig('/var/www/html/graph.png')

# Show the graph
plt.show()

# Disconnect from server
cur.close()
db.close()
