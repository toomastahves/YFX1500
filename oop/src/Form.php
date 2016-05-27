<?php

class Form {
  public $id;
  public $name;
  public $fields = [];

  public function __construct($name, $id, array $fields = null) {
    $this->name = $name;
    $this->id = $id;
    $this->fields = $fields;
  }

  public function getStartTag($attributes = null) {
    if(!$attributes) return '<form>';
    $tag = '<form';
    foreach($attributes as $key => $value) {
      $tag .= " $key =\"$value\"";
    }
    $tag .= '>';
    return $tag;
  }

  public function getFields() {
    return $this->fields;
  }

  public function getEndTag() {
    return '</form>';
  }

}

?>
