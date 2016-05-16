<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Description extends Model
{
	public $fillable = ['product_id', 'body'];

	public function product()
	{
		$this->belongsTo(Product::class);
	}
	public function scopeOfProduct($query, $productId)
	{
		return $query->where('product_id', $productId);
	}
}
