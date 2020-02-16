<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Bottle web project template" />
    <meta name="author" content="datamate" />

    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/custom.css" />
    <script type="text/javascript" src="/static/jquery.js"></script>
    <script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script>
  </head>

  <body>
    <a href="index"><button  class = "home">Back to<br>home</button></a>

    <table>
      <tr>
        <th>Animal</th>
        <th>Name</th>
        <th>E-mail</th>
        <th>Reason for adopting</th>
        <th></th>
        <th></th>
      </tr>
      %for dat in data:
      %if dat[6] == 0:
      <tr>
        <td><label for="">{{dat[5]}}</label></td>     
        <td><label for="">{{dat[1]}}</label></td>
        <td><label for=""> {{dat[2]}}</label></td>
        <td><label for="">{{dat[3]}} </label></td>
        <td><a href="prihvati{{ dat[0] }}"><button name ="prihvati" class = "DeUp">Accept</button></a></td>
        <td><a href="deleteU{{ dat[0] }}"><button class="DeUp">Decline</button></a></td>
        <br>
        
        
    </tr>
      
      %end
      
      
      %end
  </table>
  </body>
</html>
