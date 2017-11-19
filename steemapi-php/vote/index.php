<?php
header("Content-Type: text/plain");
$identifier = $_POST['i'];
$weight = $_POST['w'];
$voter = $_POST['v'];
$pk = $_POST['pk'];

setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
echo(exec("python3 ../../steemapi-python/votePost.py \"".$identifier."\" \"".$weight."\" \"".$voter."\" \"".$pk."\"" ));
?>