<?php

$servername = "localhost";
$username = "root";
$password = "2010020726Ev";
$dbname = "CONTROL_DISTRIBUIDO";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$laboratorio = $_POST['laboratorio'];
$dia = $_POST['dia'];
$grupo = $_POST['grupo'];
$hora = $_POST['hora'];
$profesor = $_POST['profesor'];
/*echo $laboratorio;*/

if($laboratorio!="") {

    $sql = "INSERT INTO HORARIO (Nombre, Laboratorio, Grupo, Hora, Dia)
VALUES ('$_POST[nombre]', '$_POST[laboratorio]','$_POST[grupo]','$_POST[hora]','$_POST[dia]');";

   if ($conn->multi_query($sql) === TRUE) {
        echo "Se agrego correctamente";

    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
$conn->close();
?>


<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Agregar</title>

    <link  rel="stylesheet" href="css/base.css">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

</head>
<body>

<div>
    <div class="conteiner">
        <div class="container">
            <nav class="navbar navbar-default">
                <a class="navbar-header">
                    <a href="login.php" class="navbar-brand"></a>
                    <img id="img-brand" src="img/ipn.png" alt="logo" >
                    <span>Control de Acceso/ Inicio</span>
                    <img id="img-brand" src="img/logoesime.png" alt="logozac">
                </a>
        </div>

        </nav>


    </div> <br/><br/><br/>


<form action="agregar.php" method="post">
    <label>Laboratorio:</label> <input type="text" name="laboratorio"><br/>  <br/>
    <label>Dia:</label><input type="text" name="dia"><br/> <br/>
    <label>Grupo:</label><input type="text" name="grupo"><br/> <br/>
    <label>Hora:</label><input type="text" name="hora"><br/> <br/>
    <label>Profesor:</label><input type="text" name="profesor"><br/> <br/>


    <input type="submit" value="Insertar datos">

</form>


    <form action="agreus.php" method="post">
        <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
                <button class="btn btn-primary btn-lg" type="submit"> Agregar Usuario</button>
            </div>
        </div>
    </form>



</body>
</html>
