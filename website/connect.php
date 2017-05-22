<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = '';
$dbname = "traffic_record";

$connection=mysqli_connect ($dbhost, $dbuser, $dbpass, $dbname);
if (!$connection) {
  die("Not connected : " . mysqli_connect_error());
  echo("Not connected");
}
?>



