<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" type="text/css" href="/static/custom.css" />
    <link
      href="https://fonts.googleapis.com/css?family=Poppins&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" type="text/css" href="/static/viewer.css">
    <script type="text/javascript" src="/static/viewer.js"></script>
    <script type="text/javascript" src="/static/custom.js"></script>
    <title>Little paw</title>
  </head>

  <body class="pocetna">
    <div class="container">
    <div class="header">
        <div class="naslov">
            <button class="btnSU" onClick="parent.location='/signUp'">Sign up</button>
            <button class="btnSU" onClick="parent.location='/logIn'">Log in</button>
        </div>
<div class="guestDiv">
    <button class="guest" onclick="parent.location='/index_guest'">Continue <br>as guest</button>
</div>
<div>
  <img id="image" src="static/pravapocetna.png" alt="Picture">
</div>

<div>
  <ul id="images">
    <li><img src="static/prva.jpg" alt="Picture 1"></li>
    <li><img src="static/druga.jpg" alt="Picture 2"></li>
    <li><img src="static/treca.jpg" alt="Picture 3"></li>
    <li><img src="static/cetvrta.jpg" alt="Picture 4"></li>
    <li><img src="static/peta.jpg" alt="Picture 5"></li>
  </ul>
</div>
</div>
  </body>
</html>