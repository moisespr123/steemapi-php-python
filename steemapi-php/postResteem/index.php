<?php
header("Content-Type: text/plain");
$identifier = $_POST['i'];
$account = $_POST['a'];
$pk = $_POST['pk'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
echo(exec("python3 ../../steemapi-python/postResteem.py \"".$identifier."\" \"".$account."\" \"".$pk."\"" ));
?>