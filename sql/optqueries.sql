# Distinct
explain select distinct customer.first_name, staff.first_name
from customer
inner join rental on customer.customer_id = rental.customer_id
inner join store on customer.store_id = store.store_id
inner join staff on staff.staff_id = rental.staff_id;

# Currently executing commands
show full processlist;
show warnings;

alter table sakila.film add key ix_length (length);
# Does not use index, when using *, optimizer does full table scan
explain select * from sakila.film use index (ix_length) where length < 100;
# Uses index, when selecting specific column
explain select length from sakila.film use index (ix_length) where length < 100;

# Example 2
# Complex query vs many queries
select * from film f
inner join film_actor fa on f.film_id = fa.film_id
inner join film_category fc on fc.film_id = fa.film_id
where f.film_id = 10;
show status like 'last_query_cost'; # 10.799

select * from film where film_id = 10; # 1.000
select * from film_actor where film_id = 10; # 9.599
select * from film_category where film_id = 10; # 1.199

# Table order does not matter for inner join
# Table order matters for left join and affects last query cost

# Example 3
# For min/max, order by is more efficient because of index on primary key
explain select min(film_id) from sakila.film where length = 100;
explain select film_id from sakila.film where length = 100 order by film_id limit 1;

# Example 4
# group by optimization by using indexed column film_id
explain select title, length, count(*) from film where length < 100 group by title, length;
explain select title, length, count(*) from film where length < 100 group by film_id;

# Example 5 paging
# start at 396 and limit to 5
select * from customer order by customer_id limit 395, 5;

# Example 6
# <> does not use indexes
explain select * from customer where store_id <> 2;
# better solution:
select distinct store_id from customer;
select * from customer where store_id = 1;
