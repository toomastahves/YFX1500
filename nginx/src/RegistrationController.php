<?php

class RegistrationController {

  public function UpdateSummaryCount($registration) {
    try {
        $db = new PDO('mysql:host=localhost;dbname=test', 'user', 'pass');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $query = 'insert into registration (first_name, last_name, date_of_birth, email, ip_address) values (?, ?, ?, ?, ?)';
        $stmt = $db->prepare($query);
        $stmt->execute(array(
          $registration->FirstName,
          $registration->LastName,
          $registration->DateOfBirth,
          $registration->EmailAddress,
          $registration->IpAddress
        ));
    } catch(PDOException $e) {
        echo "DB Error " . $e->getMessage();
    }
  }

}

?>
