# Import required modules
import sys
import Adafruit_DHT
from time import sleep
import pymysql
import datetime

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]

else:
    while True:
        # Try to grab a sensor reading. Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(11, 18)

        # Save current datetime stamp in variable
        currentDT = datetime.datetime.now()
        
        # Stringify the datetime stamp
        a = currentDT.strftime("%Y-%m-%d-%H:%M:%S")
        
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            
            # Open database connection
            db = pymysql.connect("192.168.0.205","humid","password","sensor")

            # Prepare a cursor object using cursor() method
            cur = db.cursor(pymysql.cursors.DictCursor)
            
            # Insert temperature, humidity, and datetime stamp into database
            sql = "INSERT INTO weather (temperature, humidity, time) VALUES (%f, %f, '%s')" %(temperature, humidity, a)
            
            # Execute SQL query using execute() method.
            cur.execute(sql)
            
            # Commit changes to database
            db.commit()
                    
            # Disconnect from server
            cur.close()
            db.close()
        
        else:
            print('Failed to get reading. Try again!')
            sys.exit(1)
        
        # Delay for 5 sec
        sleep(5)
        
    


