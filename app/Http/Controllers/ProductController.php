<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Product;
use App\Http\Requests;

class ProductController extends Controller
{
    public function index() 
    {
    	return Product::paginate();
    }
    public function store(Request $request) 
    {
        $this->validate($request, [
            'name' => 'required|unique:products|productQuality'
        ]);

        $product = Product::create([
            'name' => $request->input('name')
        ]);
    	return $product;
    }
    public function update(Request $request, $id) 
    {
    	$product = Product::findOrFail($id);
        $product->update([
            'name' => $request->input('name')
        ]);
    }
}
