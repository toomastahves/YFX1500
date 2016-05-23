<?php

try {
    $db = new PDO('mysql:host=localhost;dbname=library', 'library', 'library');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $stmt = $db->prepare("select count_overdue_books(?)");
    $stmt->execute(array(2));

    echo $stmt->fetchColumn();
}
catch(PDOException $e) {
    echo "DB Error " . $e->getMessage();
}
