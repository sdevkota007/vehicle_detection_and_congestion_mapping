<?php

// $db_host = "localhost";
// $db_username = "root";
// $db_pass = "";
// $db_name = "test_database";

// @mysql_connect("$db_host","$db_username","$db_pass") or die ("Could not collect to Mysql");
// @mysql_select_db("$db_name") or die ("No connecton");

// echo"Successful Connection";

$file = 'sample.csv';
if($handle = fopen($file, 'r')){
	$content = fgetcsv($handle, filesize($file));
	fclose($handle);

} else {
	echo "couldn't open file";
}

// echo filesize($file);

// echo $content; 
// echo nl2br($content)."<hr/>";
?>

<script>
    var myvar = <?php echo json_encode($content); ?>;
	if(myvar[0] == 1){
		myvar[0] = "RED";
	}
	else{
		myvar[0] = "GREEN";
	}
	if(myvar[1] == 1){
		myvar[1] = "RED";
	}
	else{
		myvar[1] = "GREEN";
	}
	alert(myvar[0]);
	alert(myvar[1]);
</script>

