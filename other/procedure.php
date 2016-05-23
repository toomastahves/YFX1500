<?php

try {
    $db = new PDO('mysql:host=localhost;dbname=library', 'library', 'library');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $stmt = $db->query("call overdue_books()");

    while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo htmlentities($row['title']);
    }
}
catch(PDOException $e) {
    echo "DB Error " . $e->getMessage();
}
