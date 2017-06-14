<?php

	$file = 'sample.csv';
	if($handle = fopen($file, 'r')){
		$content = fgetcsv($handle, filesize($file));
		fclose($handle);

	} else {
		echo "couldn't open file";
	}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Major Project</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <link href='https://fonts.googleapis.com/css?family=Oxygen:400,300,700' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Lora' rel='stylesheet' type='text/css'>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
  </head>
  <body>
    <header>
      <nav id="header-nav" class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <a href="index.php" class="pull-left visible-md visible-lg">
              <div id="logo-img" alt="Logo image"></div>
            </a>
            <div class="navbar-brand">
              <a href="index.php"><h1>Traffic Congestion Detection System</h1></a>
            </div>
            <!-- <div class="navbar navbar-right">
            <a class="material-icons md-36">info</a>
            </div> -->
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#collapsable-nav" aria-expanded="false">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
          </div>
          <div id="collapsable-nav" class="collapse navbar-collapse">
           <ul id="nav-list" class="nav navbar-nav navbar-right">
            <li>
              <a href=data.php><i class="material-icons md-36 color">info</i></a>
            </li>
            <!-- <li>
              <a href=index.html><i class="material-icons md-36 color">info</i></a>
            </li> -->
            <li>
              <a href=index.php><i class="material-icons md-36 color">help</i></a>
            </li>
          </ul> 
        </div>
      </nav>
        <!-- <div class="row">
        <div class="input-group">
          <span class="input-group-addon" id="bassic-addon1">From</span>
          <input type="text" class="form-control" placeholder="Where you are" aria-describedly="basic-addon1">
      </div> -->
      <div class="row">
        <div class="col-lg-1"></div>
        <div class="col-lg-4">
          <div class="input-group">
            <span class="input-group-addon">From</span>
            <input id="pac-input1" class="form-control" type="text" placeholder="Where you are" aria-describedly="basic-addon1">
          </div>
        </div>
        <div class="col-lg-1"></div>
        <div class="col-lg-4">
          <div class="input-group">
            <span class="input-group-addon">GoTo</span>
            <input id="pac-input2" class="form-control" type="text" placeholder="Your Destination">
          </div>
        </div>
        <div class="col-lg-1">
          <span class="input-group" "input-group-btn">
            <button class="btn btn-default" type="button">Search</button>
          </span>
        </div>
      </div>
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
	  <script src="js/script.js"></script>
      <div id="googleMap"></div>
  </body>


  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBCdtjIHGN7ej7ZxKOQsqCBgrBQbBmywg0&libraries=places&callback=initialize"
        async defer></script>
  <script src="js/jquery-2.1.4.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
</html>
