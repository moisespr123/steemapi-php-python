<?php
header("Content-Type: text/plain");
$identifier = $_POST['i'];
$body = $_POST['b'];
$body = str_replace("\"", "\\\"", $body);
$body = str_replace("`", "\`", $body);
$account = $_POST['a'];
$pk = $_POST['pk'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
$output = exec("python3 ../../steemapi-python/postReply.py '$identifier' '$body' '$account' '$pk'");
echo "$output";
?>