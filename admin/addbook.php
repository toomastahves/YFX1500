<?php
if(isset($_POST['title'])) {
    $title = addslashes(trim($_POST['title']));
    $author = addslashes(trim($_POST['author']));
    if(!$title || !$author) {
        echo 'All fields required';
        echo "<a href='index.html'>Back</a>";
        exit();
    }

    try {
        $db = new PDO('mysql:host=localhost;dbname=library', 'librarian', 'librarian');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $stmt = $db->prepare("insert into books (title, author) values (?, ?)");
        $stmt->execute(array("$title", "$author"));
        echo "Book added.";
        echo "<a href='index.html'>Back</a>";
        exit;
    } catch(PDOException $e) {
        echo "DB Error " . $e->getMessage();
    }
}
?>
<html>
    <head>
        <title>Add book</title>
    </head>
    <body>
        <form action='addbook.php' method='post'>
            <div>
                <label>Title:</label>
                <input type='text' name='title' />
            </div>
            <div>
                <label>Author:</label>
                <input type='text' name='author' />
            </div>
            <div>
                <button type='submit'>Save</button>
            </div>
        </form>
    </body>
</html>