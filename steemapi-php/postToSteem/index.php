<?php
header("Content-Type: text/plain");
$title = $_POST['title'];
$body = $_POST['body'];
$author = $_POST['author'];
$permlink = $_POST['permlink'];
$tags = $_POST['tags'];
$pk = $_POST['pk'];

setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
$title = str_replace("\"", "\\\"", $title);
$title = str_replace("`", "\`", $title);
$body = str_replace("\"", "\\\"", $body);
$body = str_replace("`", "\`", $body);
echo(exec("python3 ../../steemapi-python/postToSteem.py \"".$title."\" \"".$body."\" \"".$author."\" \"".$permlink."\" \"".$tags."\" \"".$pk."\"" , $output));
?>