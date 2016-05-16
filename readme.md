php artisan make:migration create_products_table --create=products
php artisan make:migration create_descriptions_table --create=descriptions
php artisan migrate
php artisan migrate:rollback # one at a time
php artisan migrate:reset # everything
php artisan migrate:refresh

php artisan make:seeder ProductTableSeeder
php artisan make:seeder DecriptionTableSeeder
php artisan db:seed --class=ProductTableSeeder
php artisan db:seed --class=DecriptionTableSeeder

php artisan make:model Product
php artisan make:model Description

php artisan serve --host=127.0.0.1:81
phpunit

php artisan make:controller ProductController
php artisan make:controller ProductDescriptionController

php artisan route:list


GET 127.0.0.1:81/api/products/1/descriptions
GET 127.0.0.1:81/api/products/
