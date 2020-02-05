<?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "school";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$name = "Junhong";

$sql = "UPDATE students SET age=18 WHERE name='$name' AND age=17";
$result = $conn->query($sql);

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
}
else {
    echo "Error: " . $sql . "\n" . $conn->error;
}
$conn->close();
?> 
