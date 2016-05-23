<?php
if(isset($_POST['name'])) {
    $name = addslashes(trim($_POST['name']));
    $address = addslashes(trim($_POST['address']));
    if(!$name || !$address) {
        echo 'All fields required';
        echo "<a href='index.html'>Back</a>";
        exit();
    }

    try {
        $db = new PDO('mysql:host=localhost;dbname=library', 'librarian', 'librarian');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $stmt = $db->prepare("insert into borrowers (name, address) values (?, ?)");
        $stmt->execute(array("$name", "$address"));
        echo "Borrower added.";
        echo "<a href='index.html'>Back</a>";
        exit;
    } catch(PDOException $e) {
        echo "DB Error " . $e->getMessage();
    }
}
?>
<html>
    <head>
        <title>Add borrower</title>
    </head>
    <body>
        <form action='addborrower.php' method='post'>
            <div>
                <label>Name:</label>
                <input type='text' name='name' />
            </div>
            <div>
                <label>Address:</label>
                <input type='text' name='address' />
            </div>
            <div>
                <button type='submit'>Save</button>
            </div>
        </form>
    </body>
</html>