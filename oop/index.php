<?php
  include 'src/Form.php';
  include 'src/InputText.php';
  include 'src/StringLengthValidator.php';

$usernameInput = new InputText();
$usernameInput->setLabel('username')->setRequired();

$passwordInput = new InputText();
$passwordInput->setLabel('password')->setType('password')->setRequired();

$submitInput = new InputText();
$submitInput->setType('submit');

StringLengthValidator::setMaximum(10);
StringLengthValidator::setMinimum(3);

$fields = [
  'username' => $usernameInput,
  'password' => $passwordInput,
  'submit' => $submitInput
];

$form = new Form('form', 'id123', $fields);

if(isset($_POST['username']) && isset($_POST['password'])) {
  if(StringLengthValidator::validate($_POST['username']) && StringLengthValidator::validate($_POST['password'])) {
    echo 'thank you for logging in';
    exit;
  } else {
    echo 'validation failed<br />';
  }
}

echo 'please login';
echo $form->getStartTag(array('action'=>'index.php', 'method'=>'post'));
foreach($form->getFields() as $field) {
  if($field->label) echo $field->label . ': ';
  echo $field->getInput() . '<br />';
}
echo $form->getEndTag();

?>
