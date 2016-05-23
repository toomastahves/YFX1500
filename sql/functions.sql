USE sakila;

# String functions
SELECT ASCII('a');
SELECT CHAR(97);
SELECT LENGTH('asd');
SELECT CONCAT('a','s','d');
SELECT LCASE('ASD');
SELECT LEFT('asd', 1);
SELECT TRIM('  asd ');
SELECT STRCMP('asd', 'dsa');
SELECT REVERSE('asd');

SELECT CONCAT(first_name, ' ', last_name) AS full_name,
REVERSE(CONCAT(first_name, ' ', last_name)) AS reversed_full_name
FROM sakila.actor;

# Numeric functions
SELECT ABS(-123);
SELECT CEILING(123.34);
SELECT DEGREES(PI());
SELECT FLOOR(123.34);
SELECT PI() + 0.0000000000000000;
SELECT POW(2,3);
SELECT SQRT(25);
SELECT SIN(180);

SELECT amount, amount-0.5 AS discounted, ROUND(amount) AS rounded_amount FROM sakila.payment;

# DateTime functions
SELECT ADDDATE('2016-05-25', INTERVAL 5 DAY);
SELECT SUBDATE('2016-05-25', INTERVAL 5 DAY);
SELECT CURDATE();
SELECT CURTIME();
SELECT NOW();
SELECT WEEK(NOW());
SELECT DATE_FORMAT(NOW(), '%d %M');

SELECT rental_date, DATE_FORMAT(rental_date, '%M %Y') FROM sakila.rental;

# Control flow
SET @myVar = 1;
SELECT CASE @myVar
	WHEN 1 THEN 'one'
	WHEN 2 THEN 'two'
	ELSE 'more' END AS Result;

SELECT CASE 
	WHEN @myVar = 1 THEN 'one'
	WHEN @myVar = 2 THEN 'two'
	ELSE 'more' END AS Result;

SELECT IF(@myVar < 2, 'smaller', 'larger');

SELECT IFNULL(1, 10);
SELECT IFNULL(NULL, 10);
SELECT IFNULL(1/0, 'bad');

SELECT NULLIF(1, 10);
SELECT NULLIF(10, 10);

# Cast
SELECT 1-2;
SELECT CAST(1-2 AS UNSIGNED);
SELECT CAST(18446744073709551615 AS SIGNED);
SELECT CONVERT('120619', DATE) AS mydate;

# Information
SELECT CHARSET('asd');
SELECT COLLATION('asd');
SELECT CONNECTION_ID();
SELECT CURRENT_USER();
SELECT DATABASE();
SELECT SCHEMA();
SELECT USER();
SELECT VERSION();

# Misc
SELECT RAND();
SELECT LEFT(CEILING(RAND() * 10), 1);
SELECT SLEEP(5);
SELECT UUID();

# Aggregate
SELECT COUNT(*) norentals, customer_id FROM rental GROUP BY customer_id;
SELECT MAX(rental_date) lastrentaldate, customer_id FROM rental GROUP BY customer_id;
SELECT AVG(amount), SUM(amount), COUNT(rental_id), customer_id FROM payment GROUP BY customer_id; 
