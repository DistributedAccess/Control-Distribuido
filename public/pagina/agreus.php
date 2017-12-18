<?php

$servername = "localhost";
$username = "root";
$pasw = "2010020726Ev";
$dbname = "CONTROL_DISTRIBUIDO";

// Create connection
$conn = new mysqli($servername, $username, $pasw, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$nombre = $_POST['nombre'];
$jerarquia = $_POST['jerarquia'];
$password = $_POST['password'];
echo $nombre;

if($nombre!="") {

    $sql = "INSERT INTO USUARIOS (Nombre, Password, Jerarquia)
VALUES ('$_POST[nombre]', '$_POST[password]', '$_POST[jerarquia]');";

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




    <form action="agreus.php" method="post">
        <label>Nombre:</label> <input type="text" name="nombre"><br/>  <br/>
        <label>Jerarquia:</label><input type="text" name="jerarquia"><br/> <br/>
        <label>Password:</label><input type="text" name="password"><br/> <br/>

        <input type="submit" value="Insertar datos">
    </form>


</body>
</html>

