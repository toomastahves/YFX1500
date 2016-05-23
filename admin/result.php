<?php

$title = trim($_POST['title']);
$title = addslashes($title);

if(!$title) {
    echo 'Title required';
    exit();
}

try {
    $db = new PDO('mysql:host=localhost;dbname=library', 'assistant', 'assistant');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $stmt = $db->prepare("select * from books where title like ?");
    $stmt->execute(array("%$title%"));
    
    echo "<div style='background-color: " . $_COOKIE['color'] . "'>";
    while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<div>";
        echo htmlentities($row['title']);
        echo "</div>";
    }
    echo "</div>";
    echo "<a href='index.html'>Back</a>";
}
catch(PDOException $e) {
    echo "DB Error " . $e->getMessage();
}
