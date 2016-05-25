<?php

require '../Models/City.php';
require '../Views/cities.php';

class CityController {
  function getCities() {
    $city = new City();
    $city->Name = 'tallinn';
    $citiesView = new CitiesView();
    return $citiesView->output($city);
  }
}

$cc = new CityController();
$cc->getCities();

?>
