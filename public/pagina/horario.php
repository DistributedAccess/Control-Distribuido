<?php
// Datos de la base de datos
$usuario = "root";
$password = "2010020726Ev";
$servidor = "localhost";
$basededatos = "CONTROL_DISTRIBUIDO";

// creación de la conexión a la base de datos con mysql_connect()
$conexion = mysqli_connect( $servidor, $usuario,$password,$basededatos ) or die ("No se ha podido conectar al servidor de Base de datos");

// Selección del a base de datos a utilizar
$db = mysqli_select_db( $conexion, $basededatos ) or die ( "Upps! no se ha podido conectar a la base de datos" );
// establecer y realizar consulta. guardamos en variable.
$consulta = "SELECT * FROM HORARIO";
$resultado = mysqli_query( $conexion, $consulta ) or die ( " mal en la consulta a la base de datos");





?>

<!doctype html>
<html lang="es">
<head>
    <form action="agreus.php" method="post">
        <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
                <button class="btn btn-primary btn-lg" type="submit"> Agregar Usuario</button>
            </div>
        </div>
    </form>

    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>

    <link  rel="stylesheet" href="css/base.css">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>


</head>


<div>
    <div class="container">
        <nav class="navbar navbar-default">
            <a class="navbar-header">
                <a href="login.php" class="navbar-brand"></a>
                <img id="img-brand" src="img/ipn.png" alt="logo" >
                <span>Control de Acceso / Horarios</span>
                <img id="img-brand" src="img/logoesime.png" alt="logozac">
            </a>
    </div>
</div>
</nav>



<br/><br/><br/><br/><br/>

<body>


<div class="container">
    <table class="table table-bordered table-hover">


 <tr>
     <th>Laboratorio</th>
     <th>Grupo</th>
     <th>Dia</th>
     <th>Hora</th>
     <th>Profesor</th>
</tr>

<?php while ($columna = mysqli_fetch_array( $resultado ))
{
    echo "<tr>";
    echo "<td>" . $columna['laboratorio'] . "</td><td>" . $columna['grupo'] . "</td>";
    echo "<td>" . $columna['dia'] . "</td><td>" . $columna['hora'] . "</td>";
    echo "<td>" . $columna['profesor'] . "</td>";
    echo "</tr>";
}


echo "</div>"; "</table>";

// Fin de la tabla
// cerrar conexión de base de datos
mysqli_close( $conexion );


?>




        <form action="agregar.php" method="post">
            <div class="form-group">
                    <div class="col-sm-offset-3 col-sm-9">
                        <button class="btn btn-primary btn-lg" type="submit">Agregar Horario</button>
                    </div>
                </div>



        </body>



</html>






