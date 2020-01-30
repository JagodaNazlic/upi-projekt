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

    <script type="text/javascript" src="/static/custom.js"></script>
    <title>Little paw</title>
  </head>

  <body class="signin">
    <div class="loginBox">
      <form action="/logIn" method="POST">
        <input type="text" name="username" placeholder="Username.." />

        <input type="password" name="password" id="" placeholder="Password.." />

        <input type="submit" name="login" value="Login" />

        <div class="links">
          <a href="signUp">Don't have an account?</a>
        </div>
      </form>
    </div>
  </body>
</html>
