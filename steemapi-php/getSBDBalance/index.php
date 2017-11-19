<?php
header("Content-Type: text/plain");
$account = $_GET['a'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
$output = exec("python3 ../../steemapi-python/getSBDBalance.py $account");
echo "$output";
?>