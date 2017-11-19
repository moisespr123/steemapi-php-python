<?php
require_once '../Michelf/MarkdownExtra.inc.php';
$body = $_POST['body'];
setlocale(LC_ALL, 'en_US.utf8');
putenv('LC_ALL=en_US.utf8');
echo \Michelf\MarkdownExtra::defaultTransform("$body");
?>