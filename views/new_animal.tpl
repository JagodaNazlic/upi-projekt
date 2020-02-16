<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="HandheldFriendly" content = "true">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <script type="text/javascript" src="/static/jquery.js"></script>
	<script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 
</head>
<body>
	<div class = "cntn1">
	<div class="btnNZD">
		<button class="btnNZ" onClick="parent.location='/index'">Home</button>
	</div>
	<form action="/newA" method="POST" class = "formAnimal">
		
	
		<div class="labels">
			<input type="text" name="ime"  placeholder="Name..." />

		<fieldset data-role="controlgroup" data-type="horizontal">
			
			<input type="radio" name="vrsta" id="cat" value="Cat">
			<label for="cat">Cat</label>
			<input type="radio" name="vrsta" id="dog" value="Dog">
			<label for="dog">Dog</label>
			</fieldset>

			<fieldset data-role="controlgroup" data-type="horizontal">
				<input type="radio" name="spol" id="M" value="Male">
				<label for="M">Male</label>
				<input type="radio" name="spol" id="F" value="Female">
				<label for="F">Female</label>
			</fieldset>
		
			

				<input type="number" name="dob"  placeholder="Age..." />

				<input type="text" name="datOdlaska" placeholder="Leaving date... "/>
	
				<input type="number" name="fin" placeholder="Finance..." />
	
				<input type="text" name="zdrst" placeholder="Health condition..." />
			</div>
			
<div class = "btnnnn">
					<button type="submit" onClick="parent.location='/index'" class="btnNZ" value="Save" name="unesi">Save</button>
				</div>
			
	</form>
	
</div>
<div class = "aaaaa">

	</div>
	<div class="footer">
	</div>


</body>	


</html>