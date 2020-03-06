<?php
// User credentials
$servername = "192.168.0.205";
$username = "humid";
$password = "password";
$dbname = "sensor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connectionmysqli
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Select the most recent time, temperature, and humidity
$sql = "SELECT * FROM weather ORDER BY time DESC LIMIT 1";
$result = $conn->query($sql);

// Order data according to temperature in descending order and select the first data point. 
$highestTemp = "SELECT * FROM weather ORDER BY temperature DESC LIMIT 1";
$result2 = $conn->query($highestTemp);

// Order data according to temperature in ascending order and select the first data point. 
$lowestTemp = "SELECT * FROM weather ORDER BY temperature ASC LIMIT 1";
$result3 = $conn->query($lowestTemp);

// Order data according to humidity in descending order and select the first data point. 
$highestHumi = "SELECT * FROM weather ORDER BY humidity DESC LIMIT 1";
$result4 = $conn->query($highestHumi);

// Order data according to humidity in ascending order and select the first data point. 
$lowestHumi = "SELECT * FROM weather ORDER BY humidity ASC LIMIT 1";
$result5 = $conn->query($lowestHumi);

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        // Echo most recent temperature and humidity, and the datetime stamp
        echo "Temperature: " . $row["temperature"]. "°C - Humidity: " . $row["humidity"]."%" . " - Last updated: " . $row["time"];
        
        // Compare current time to the datetime stamp of most recent data point
        $lastPt = new DateTime($row['time']);
        $currentTime = new DateTime();
        $interval = $currentTime->diff($format);
        
        // If the difference between the current time and time of lastpoint 
        // is greater than 5 minutes, output a warning in red.
        if (($currentTime->getTimestamp() - $lastPt->getTimestamp()) > 60*5){
            echo nl2br("\n <p> <font color=red> NO DATA COLLECTED IN LAST 5 MIN </font></p>");
        }
    }   
} 
else {
    echo "0 results";
}

if ($result2->num_rows > 0) {
    // Output highest temperature recorded and its date in human readable format
    while($row = $result2->fetch_assoc()) {
        echo nl2br("\n Highest temperature recorded: " . $row["temperature"]. "°C on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

if ($result3->num_rows > 0) {
    // Output lowest temperature recorded and its date in human readable format
    while($row = $result3->fetch_assoc()) {
        echo nl2br("\n Lowest temperature recorded: " . $row["temperature"]. "°C on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

if ($result4->num_rows > 0) {
    // Output highest humidity recorded and its date in human readable format
    while($row = $result4->fetch_assoc()) {
        echo nl2br("\n Highest humidity recorded: " . $row["humidity"]. "% on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

if ($result5->num_rows > 0) {
    // Output lowest humidity recorded and its date in human readable format
    while($row = $result5->fetch_assoc()) {
        echo nl2br("\n Lowest humidity recorded: " . $row["humidity"]. "% on ". date('F jS, Y h:i', strtotime($row["time"])));
    }
}

// Close database connection
$conn->close();

// Show graph on php page
echo "<img src='graph.png' >";


?>
