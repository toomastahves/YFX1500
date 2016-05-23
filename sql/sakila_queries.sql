USE sakila;

# Customers who watch Action movies
# Subqueries
SELECT cust.customer_id, cust.first_name, cust.last_name
FROM customer cust
WHERE cust.customer_ID IN (
	SELECT ren.customer_id
	FROM rental ren
	WHERE ren.inventory_id IN (
		SELECT inv.inventory_id
		FROM inventory inv
		WHERE inv.film_id IN (
			SELECT fl.film_id
			FROM film fl
			WHERE fl.film_id IN (
				SELECT fc.film_id
				FROM film_category fc
				WHERE fc.category_id IN (
					SELECT cat.category_id
					FROM category cat
					WHERE cat.name = 'Action'
				)
			)
		)
	)
);

# Same with INNER JOIN
SELECT DISTINCT cust.customer_id, cust.first_name, cust.last_name
FROM customer cust
INNER JOIN rental ren ON ren.customer_id = cust.customer_id
INNER JOIN inventory inv ON inv.inventory_id = ren.inventory_id
INNER JOIN film fl ON fl.film_id = inv.film_id
INNER JOIN film_category fc ON fc.film_id = fl.film_id
INNER JOIN category cat ON cat.category_id = fc.category_id
WHERE cat.name = 'Action'
ORDER BY cust.customer_id, cust.first_name, cust.last_name;

# Subquery with aggregation
SELECT fm.title, cat.name, dt.CountOfCategory
FROM film fm
INNER JOIN film_category fc ON fc.film_id = fm.film_id
INNER JOIN category cat ON cat.category_id = fc.category_id
INNER JOIN (
	SELECT COUNT(*) AS CountOfCategory, fc.category_id
	FROM film_category fc
	GROUP BY fc.category_id
) dt ON dt.category_id = fc.category_id;

# Find customer payments that are over their average payment
SELECT payment_id, cust.first_name, cust.last_name, amount
FROM payment pt
INNER JOIN customer cust ON cust.customer_ID = pt.customer_id
WHERE amount > (
	SELECT AVG(amount)
	FROM payment pt1
	WHERE pt1.customer_id = pt.customer_id
) ORDER BY cust.customer_id;

# Average amount per customer
SELECT AVG(amount), cust.first_name, cust.last_name
FROM payment pt
INNER JOIN customer cust ON cust.customer_id = pt.customer_id
GROUP BY cust.first_name, cust.last_name
ORDER BY cust.customer_id;

# Over average payments count
SELECT cust.first_name, cust.last_name, COUNT(payment_id) CountofPayment
FROM payment pt
INNER JOIN customer cust ON cust.customer_id = pt.customer_id
WHERE amount > (
	SELECT AVG(amount)
	FROM payment pt1
	WHERE pt1.customer_id = pt.customer_id
) GROUP BY cust.first_name, cust.last_name
ORDER BY cust.customer_id;
