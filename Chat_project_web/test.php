<?php
    $index = $_GET['index'];

    $desc = ['Best Friend', 'Favorite Language', 'Best Musician'];
    $name = ['Aram Kim', 'Python', 'IU'];

    $json = json_encode(array('desc' => $desc[$index], 'name' => $name[$index]));

    echo($json);
?>