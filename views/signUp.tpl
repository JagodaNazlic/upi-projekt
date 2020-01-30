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

  <body class="signin">
    <div class="registerBox">
      <img src="/static/userFinal.png" class="avatar" alt="" />
      <form action="/signUp" method="POST">
        <input type="text" name="ime_prezime" placeholder="Ime i prezime..." />
        <input type="text" name="username" placeholder="Username.." />

        <input
          type="password"
          name="password1"
          id=""
          placeholder="Password.."
        />

        <input
          type="password"
          name="password2"
          id=""
          placeholder="Confirm the password.."
        />

        <input type="submit" name="register" value="Register" />
      </form>
    </div>
  </body>
</html>
