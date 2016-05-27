<?php

  $curry= function ($val1) {
    return function($val2) use ($val1) {
      return function($val3) use ($val1, $val2) {
        return $val1 + $val2 + $val3;
      };
    };
  };
  $curry(1)(0)(3);

  class chain {
    public $firstname = '';
    public $lastname = '';
    public function setFirstname($value) {
      $this->firstname = $value;
      return $this;
    }
    public function setLastname($value) {
      $this->lastname = $value;
      return $this;
    }
  }
  $ch = new chain();
  $ch->setFirstname('a')->setLastname('b');
  $ch->firstname . ' ' . $ch->lastname;

 ?>
