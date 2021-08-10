<?php

$addr = "localhost";
$id = "root";
$pw = "";
$db = "chatproject";

$conn = mysqli_connect($addr, $id, $pw, $db, 3306) or die("connect err");
$sql = "select * from chat_table";
$result = mysqli_query($conn, $sql);

while( $rows = mysqli_fetch_array( $result )  ) {

  echo '<tr><td>' , $rows[ 'time_log' ]  , ' </td>' , 
  '<td>' , $rows[ 'user_addr' ]  , "</td> ",
  '<td>', $rows[ 'message' ] , '</td></tr>';

}

?>


