<?php

class Registration {
    public $FirstName = '';
    public $LastName = '';
    public $DateOfBirth;
    public $EmailAddress = '';
    public $IpAddress = '';

    public $ValidationErrors;
    public function IsValid() {
      $this->ValidationErrors = array();
      if($this->IsNullOrEmpty($this->FirstName)) {
        array_push($this->ValidationErrors, 'First name is required');
      }
      if($this->IsNullOrEmpty($this->LastName)) {
        array_push($this->ValidationErrors, 'Last name is required');
      }
      if($this->IsNullOrEmpty($this->EmailAddress)) {
        array_push($this->ValidationErrors, 'Email is required');
      }
      if($this->IsNullOrEmpty($this->DateOfBirth)) {
        array_push($this->ValidationErrors, 'Date of birth is required');
      } else {
        $date = DateTime::createFromFormat('Y-m-d', $this->DateOfBirth);
        if($date === false) {
          array_push($this->ValidationErrors, 'Date of birth must be valid');
        } else {
          $this->DateOfBirth = $date->format('Y-m-d');
        }
      }
      return count($this->ValidationErrors) === 0;
    }
    private function IsNullOrEmpty($string) {
      return (!isset($string) || trim($string === ''));
    }
}

?>
