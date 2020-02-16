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
        <th></th>
      </tr>
      %for dat in data:
      %if dat[6] == 1:
      <tr>
        <td><label for="">{{dat[1]}} adopted {{dat[5]}}</label></td>     
        <br>
        
    </tr>
      
      %end
      
      
      %end
  </table>
  </body>
</html>
