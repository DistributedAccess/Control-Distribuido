<?php
/**
 * Created by PhpStorm.
 * User: root
 * Date: 27/11/17
 * Time: 03:57 PM
 */



?>

<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>

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

<center>
<div class="panel panel-default">
    <div class="panel-body">
        <form name="registro" action="registro.php" method="post">
            <div class="form-group">
                <div class="col-sm-offset-6 col-sm-6">
                    <img id="userimg" src="img/usuario.png" alt="" class="img-rounded">
                </div>
            </div>
            <div class="form-group">
                <label for="nombre" class="col-sm-3 control-label">Nombre</label>
                <input class="col-sm-9" type="Nombre" name="Nombre" placeholder="Nombre">
            </div>
            <div class="form-group">
                <label for="password" class="col-sm-3 control-label">Password</label>
                <input class="col-sm-9" type="password" name="Password" placeholder="Password">
            </div>
            <div class="form-group">
                <div class="col-sm-offset-3 col-sm-9">
                    <button class="btn btn-primary btn-lg" type="submit">Enviar</button>
                </div>
            </div>

</center>
        </form>
    </div>
</div>

<div align="center">
    <span><i>Academia de Computacion de ICE ESIME Zacatenco</i></span>
</div>
</div>

</body>
</html>