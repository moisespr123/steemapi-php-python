<?php
header("Content-Type: text/plain");
$account = $_GET['a'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
echo(exec("python3 ../../steemapi-python/getCreatedDate.py $account"));
?>