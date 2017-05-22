<?php

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
  <!--</head>
  <body style="background-color:gray;">
    <header>
      <nav id="header-nav" class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <a href="index.php" class="pull-left visible-md visible-lg">
              <div id="logo-img" alt="Logo image"></div>
            </a>
            <div class="navbar-brand">
              <a href="index.php"><h1>Trafic Conjestion Detection System</h1></a>
            </div>
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
            
            <li>
              <a href=index.php><i class="material-icons md-36 color">help</i></a>
            </li>
          </ul> 
        </div>
      </nav> -->
      	<div class="col-lg-2">
	      	<div class="input-group">
	            <span class="input-group-addon">Day</span>
	            <input id="name" class="form-control" type="text" placeholder="eg.2">
	         </div>
	    </div>
	    <div class="col-lg-1">
          <span class="input-group" "input-group-btn">
            <input class="btn btn-default" type="submit" id="name-submit" value="Search" method="post"></input>
          </span>
	    </div>
		<div class="row" style="margin-top:50px;">
			<div id = "name-data">
			
			</div>
		</div>

      <!-- <div>
    	Name:
      	<input type= "text" id = "name" class="form-control" placeholder="Ram">
		<input type = "submit" id = "name-submit">
		<div id = "name-data"></div>
      </div> -->
  </body>
  <script src="js/jquery-2.1.4.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/global.js"></script>
</html>