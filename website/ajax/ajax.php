

		
// <?php
// $db_host = 'localhost';
// $db_user = 'root';
// $db_pwd = '';

// $database = 'traffic_record';
// $table = 'roada';

// if (!mysql_connect($db_host, $db_user, $db_pwd))
    // die("Can't connect to database");

// if (!mysql_select_db($database))
    // die("Can't select database");

// $search = $_POST['Id'];

// // sending query ".$_POST['Id']."'
// $result = mysql_query("SELECT * FROM {$table} WHERE `Day`='5'");
// if (!$result) {
    // die("Query to show fields from table failed");
// }

// $fields_num = mysql_num_fields($result);

// echo "<h1>Table: {$table}</h1>";
// echo "<table border='1'><tr>";
// // printing table headers
// for($i=0; $i<$fields_num; $i++)
// {
    // $field = mysql_fetch_field($result);
    // echo "<td>{$field->name}</td>";
// }
// echo "</tr>\n";
// // printing table rows
// while($row = mysql_fetch_row($result))
// {
    // echo "<tr>";

    // // $row is array... foreach( .. ) puts every element
    // // of $row to $cell variable
    // foreach($row as $cell)
        // echo "<td>$cell</td>";

    // echo "</tr>\n";
// }
// mysql_free_result($result);
// ?>

<?php
	if(isset($_POST['Id']) === true && empty($_POST['Id']) === false){
		require '../connect.php';
		
		$table = "roada";

		$query ="SELECT * FROM roada WHERE `Day`='.$POST['Id'].'

		";



		$result = mysqli_query($connection, $query);
		


		if(!' result'){
			die("Database query failed.");
		}

		while($row = mysqli_fetch_assoc($result)){
			
			if($row === ''){
				echo("Id not found");
			}
			else {
				
					$fields_num = mysql_num_fields($result);
					//echo $fields_num; die();
					echo "<h1>Table: {$table}</h1>";
					echo "<table border='1'><tr>";
					// printing table headers
					for($i=0; $i<$fields_num; $i++)
					{
						$field = mysql_fetch_field($result);
						echo "<td>{$field->name}</td>";
					}
					echo "</tr>\n";
					// printing table rows
					while($row = mysql_fetch_row($result))
					{
						echo "<tr>";

						// $row is array... foreach( .. ) puts every element
						// of $row to $cell variable
						foreach($row as $cell)
							echo "<td>$cell</td>";

						echo "</tr>\n";
					}
			}echo($row["10:00-10:15"]);
			//var_dump '$row';
		}
		// ". mysql_real_escape_string(trim($_POST['Id'])) ."
		
	}


?>


