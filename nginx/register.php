<?php

include('src/Registration.php');
include('src/RegistrationController.php');
include('../vendor/autoload.php');

$registration = new Registration();

if(isset($_POST['FirstName'])) {
  $registration->FirstName = $_POST['FirstName'];
  $registration->LastName = $_POST['LastName'];
  $registration->DateOfBirth = $_POST['DateOfBirth'];
  $registration->EmailAddress = $_POST['EmailAddress'];
  $registration->IpAddress = $_SERVER['REMOTE_ADDR'];

  if($registration->IsValid()) {
    try {
      $controller = new RegistrationController();
      $controller->UpdateSummaryCount($registration);
      Logger::configure('../log4php.properties');
      $logger = Logger::getRootLogger();
      $logger->info("Registration success.");
      include('thankyou.php');
      exit();
    } catch(Exception $e) {
      $logger->error('Registration error.');
    }
  }
}

?>

<!DOCTYPE html>
<html>
  <?php require('head.php'); ?>
<body>
  <div class='container'>
    <div>
      <?php
        if(count($registration->ValidationErrors) > 0) {
          foreach($registration->ValidationErrors as $value) {
            echo "<div>$value</div>";
          }
        }
      ?>
    </div>
    <form action='register.php' method='post'>
      <div>
        FirstName: <input type='text' name='FirstName' value="<?php echo $registration->FirstName; ?>" />
      </div>
      <div>
        LastName: <input type='text' name='LastName' value="<?php echo $registration->LastName; ?>" />
      </div>
      <div>
        DateOfBirth: <input type='text' name='DateOfBirth' value="<?php echo $registration->DateOfBirth; ?>" />
      </div>
      <div>
        EmailAddress: <input type='text' name='EmailAddress' value="<?php echo $registration->EmailAddress; ?>" />
      </div>
      <div>
        <button type='submit'>Register</button>
      </div>
    </form>
  </div>
</body>
</html>
