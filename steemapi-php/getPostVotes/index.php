<?php
header("Content-Type: text/plain");
$account = $_GET['i'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
$output = exec("python3 ../../steemapi-python/getPostVotes.py $account");
echo "$output";
?>