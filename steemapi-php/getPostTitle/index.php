<?php
header("Content-Type: text/plain");
$post = $_GET['p'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
echo(exec("python3 ../../steemapi-python/postGetTitle.py $post"));
?>