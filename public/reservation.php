<?php

$bookid = $_GET['bookid'];

session_start();
if(!isset($_SESSION['books'])) {
    $books = [];
} else {
    $books = $_SESSION['books'];
}
array_push($books, $bookid);
$_SESSION['books'] = $books;
echo "Book reserved: " . $bookid;
echo "<br/>Reserved books: ";
foreach($books as $bookid) {
    echo $bookid . " ";
}
echo "<br /><a href='index.html'>Back</a>";