<?php

class InputText {
  public $type = 'text';
  public $label;
  public $value;
  public $required;

  public function getInput() {
    return "<input type='$this->type' name='$this->label' label='$this->label' $this->required />";
  }

  public function setLabel($label) {
    $this->label = $label;
    return $this;
  }
  public function setValue($value) {
    $this->value = $value;
    return $this;
  }
  public function setType($type) {
    $this->type = $type;
    return $this;
  }
  public function setRequired() {
    $this->required = 'required';
    return $this;
  }
}

?>
