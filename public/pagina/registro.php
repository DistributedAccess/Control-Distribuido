<?php
/**
 * Created by PhpStorm.
 * User: ana
 * Date: 27/11/17
 * Time: 03:58 PM
 */
$nombre = $_POST['nombre'];
$password = $_POST['password'];

if (isset($nombre,$password) && !empty($nombre) && !empty($password)){

    require "mydb.php";

    $query = "select * from USUARIOS where Nombre = '" . $nombre . "' and Password = '" . $password . "';";
    $res = get_result_user($query);
    if (!empty($res)) {
        header("location:Horario.php?Nombre=" . urldecode($_GET['nombre']));
    }else  {
        header("location: login.php?nouser=1");
    }
}
