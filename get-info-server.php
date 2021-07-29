<?php
header('Content-Type: application/json;charset=utf-8');  
session_start();
error_reporting(0);
$json->ip=$_SERVER['REMOTE_ADDR'];
$json->useragent=$_SERVER ['HTTP_USER_AGENT'];
echo json_encode($json);
?>
