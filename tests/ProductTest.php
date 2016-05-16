<?php

use Illuminate\Foundation\Testing\WithoutMiddleware;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class ProductTest extends TestCase
{
    use DatabaseTransactions;
    protected $jsonHeaders = ['Content-Type' => 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept' => 'application/json'];

    public function testProductsList()
    {
        $products = factory(\App\Product::class, 3)->create();

        $this->get(route('api.products.index'))
             ->assertResponseOk();

        array_map(function($product) {
            $this->seeJson($product->jsonSerialize());
        }, $products->all());
    }

    public function testProductDescriptionsList()
    {
        $product = factory(\App\Product::class)->create();
        $product->descriptions()->saveMany(factory(\App\Description::class, 3)->make());

        $this->get(route('api.products.descriptions.index', ['products' => $product->id]))
             ->assertResponseOk();

        array_map(function($description) {
            $this->seeJson($description->jsonSerialize());
        }, $product->descriptions->all());
    }

    public function testProductCreation()
    {
        $product = factory(\App\Product::class)->make(['name' => 'pets']);

        $this->post(route('api.products.store'), $product->jsonSerialize(), $this->jsonHeaders)
            ->seeInDatabase('products', ['name' => $product->name])
            ->assertResponseOk();
    }

    public function testProductDescriptionCreation()
    {
        $product = factory(\App\Product::class)->create(['name' => 'pets']);
        $description = factory(\App\Description::class)->make();
        
        $this->post(route('api.products.descriptions.store', ['products' => $product->id]), $description->jsonSerialize())
            ->seeInDatabase('descriptions', ['body' => $description->body])
            ->assertResponseOk();
    }

    public function testProductUpdate()
    {
        $product = factory(\App\Product::class)->create(['name' => 'pets']);
        $product->name = 'pets2';

        $this->put(route('api.products.update', ['products' => $product->id]), $product->jsonSerialize(), $this->jsonHeaders)
            ->seeInDatabase('products', ['name' => $product->name])
            ->assertResponseOk();
    }

    public function testProductCreationFailsWhenNameNotProvided() 
    {
        $product = factory(\App\Product::class)->create(['name' => '']);

        $this->post(route('api.products.store'), $product->jsonSerialize(), $this->jsonHeaders)
            ->seeJson(['name' => ['The name field is required.']])
            ->assertResponseStatus(422);
    }

    public function testProductCreationFailsWhenNameTaken() 
    {
        $name = 'pets';
        $product1 = factory(\App\Product::class)->create(['name' => $name]);
        $product2 = factory(\App\Product::class)->make(['name' => $name]);

        $this->post(route('api.products.store'), $product2->jsonSerialize(), $this->jsonHeaders)
            ->seeJson(['name' => ['The name has already been taken.']])
            ->assertResponseStatus(422);
    }

    public function testProductDescriptionCreationFailsWhenBodyNotProvided() 
    {
        $product = factory(\App\Product::class)->create(['name' => 'pets']);
        $description = factory(\App\Description::class)->make(['body' => '']);

        $this->post(route('api.products.descriptions.store', ['products' => $product->id]), $product->jsonSerialize(), $this->jsonHeaders)
            ->seeJson(['body' => ['The body field is required.']])
            ->assertResponseStatus(422);
    }

        public function testProductCreationFailsWhenNameBadQuality() 
    {
        $product = factory(\App\Product::class)->make(['name' => '123']);

        $this->post(route('api.products.store'), $product->jsonSerialize(), $this->jsonHeaders)
            ->seeJson(['name' => ['Poor quality']])
            ->assertResponseStatus(422);
    }
}
