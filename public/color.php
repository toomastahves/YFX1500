<?php
$colors = array("Green"=>"a8efab", "Blue"=>"a8c1ef");
if(isset($_GET['color'])) {
    $color = $_GET['color'];
    setcookie('color', $color, time() + 24*3600, '/', 'localhost');
}
?>
<html>
    <head>
        <title>Colors</title>
    </head>
    <body>
        <?php
        if(isset($_GET['color'])) {
            echo "Chosen color: " . $_GET['color'];
            echo "<a href='index.html'>Go back</a>";
            exit;
        }
        ?>
        <form action='color.php' method='GET'>
            <select name='color'>
                <?php
                    foreach($colors as $key=>$value) {
                        echo "<option value='".$value."'>".$key."</option>";
                    }
                ?>
            </select>
            <button type='submit'>Save</button>
        </form>
    </body>
</html>