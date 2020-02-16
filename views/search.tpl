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
        <th>Name</th>
                <th>Cat/Dog</th>
                <th>Age</th>
                <th>Gender</th>
                <th>Health condition</th>
                <th>Leaving date</th>
                <th>Arrival date</th>
                <th>Finance</th>
                <th>Interes</th>
                <th></th>
                <th></th>
      </tr>
      %for dat in data:
      <tr>
          <td><label for="">{{dat[1]}}</label></td>     
          <td><label for="">{{dat[2]}}</label></td>
          <td><label for=""> {{dat[3]}}</label></td>
          <td><label for="">{{dat[4]}} </label></td>
          <td><label for="">{{dat[5]}}</label></td>
          <td><label for="">{{dat[6]}}</label></td>
          <td><label for="">{{dat[7]}}</label></td>
          <td><label for="">{{dat[8]}} kn</label></td>
          <td><label for="">{{ dat[9] }} </label></td>
          <td><a href="delete{{ dat[0] }}"><button class = "DeUp">Delete</button></a></td>
          <td><a href="upd{{ dat[0] }}"><button class="DeUp">Update</button></a></td>
          <br>
          
          
      </tr>
      
      
      
      
      %end
  </table>
  </body>
</html>
