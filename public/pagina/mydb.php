<?php
/**
 * Created by PhpStorm.
 * User: ana
 * Date: 29/11/17
 * Time: 12:30 PM
 */

function get_result_user($query)


{
            //variable de conexion
    $db = new mysqli('localhost', 'root', '2010020726Ev', 'CONTROL_DISTRIBUIDO');

    if ($db->connect_errno > 0) {
        die('No se puede conectar con la base de datos [' . $db->connect_error . ']');
    }


    if (!$result = $db->query($query)) {
        echo "sin resultados";
        exit;
    }

    $res = array();

    while ($row = $result->fetch_assoc()) {

        array_push($res, array(
            'Nombre' => $row['Nombre'],
            'Jerarquia' => $row['Jerarquia'],
            'Password' => $row['Password']
        ));

    }

    $db->close();

    return $res;

}

