<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="/static/custom.css" />
    <link
      href="https://fonts.googleapis.com/css?family=Poppins&display=swap"
      rel="stylesheet"
    />
    <title>Little paw</title>
  </head>

  <body class = "udomib">
    <div class="ud">
<p>
  <h1>READ THIS!</h1>
  Be aware that by clicking 'I agree' you are giving us permition to check up on you and your adopted animal anytime we feel the need.<br>
  We can also take your new pet if we feel that you are not taking good care!
  It is in our best inetrest to make sure that 
  both you and your new pet have a nice life!
  <br>
  Also, have in mind that providing for animal is not easy so think twice before adopting.
   
</p>

    </div>


    <form action="/udomi{{idd}}" method="POST" class="udomi">
        
        <input type="text" name="imeU"  placeholder="Name..." /><br>
        <input type="text" name="adresa"  placeholder="Adress..." /><br>
        <input type="email" name="mejl" placeholder="E-mail... "/><br>

        <td><button type="submit" onClick="parent.location='/'" class="btnUdomi" value="Save" name="moze">I agree</button></td>
        
	</form>
  </body>
  </html>