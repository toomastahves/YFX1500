# Example 1
SHOW INDEX FROM film from SAKILA;
SHOW INDEX FROM film;
SELECT * FROM information_schema.statistics WHERE table_name = 'film';

# ASC index by default
CREATE INDEX idx_film_length ON film (length);
# Does not support DESC indexes
CREATE INDEX idx_film_length_desc ON film (length DESC);

SELECT film_id, length FROM film WHERE length = 100;

EXPLAIN SELECT film_id, length FROM film WHERE length = 100;

DROP INDEX idx_film_length ON film;
DROP INDEX idx_film_length_desc ON film;

# Example 2
# Slow query without index
EXPLAIN SELECT title, rental_duration, length FROM film WHERE rental_duration = 6 OR length = 100;

# One index not optimal, need two for performance
CREATE INDEX idx_film_rental_duration ON film (rental_duration);
CREATE INDEX idx_film_length ON film (length);

# Not necessary, MySQL engine still finds index_merge optimal
CREATE INDEX idx_film_rental_duration_length ON film (rental_duration, length);
CREATE INDEX idx_film_length_rental_duration ON film (length, rental_duration);

DROP INDEX idx_film_rental_duration ON film;
DROP INDEX idx_film_length ON film;
DROP INDEX idx_film_rental_duration_length ON film;
DROP INDEX idx_film_length_rental_duration ON film;

# Example 3
# Same query, but MySQL engine works differently. Creates temporary table for union and uses indexes differently
EXPLAIN SELECT title, rental_duration, length FROM film WHERE length = 100
UNION
SELECT title, rental_duration, length FROM film WHERE rental_duration = 6;

# Example 4
# AND operator uses index that has multiple columns. Order does not matter.
EXPLAIN SELECT title, rental_duration, length FROM film WHERE rental_duration = 6 AND length = 100;

# Example 5
# Cover index
CREATE INDEX idx_film_length_rental_duration_title ON film (length, rental_duration, title);

EXPLAIN SELECT title, rental_duration, length FROM film WHERE rental_duration = 6
UNION
SELECT title, rental_duration, length FROM film WHERE length = 100;

EXPLAIN SELECT * FROM film WHERE rental_duration = 6 AND length = 100;

# Example 6
# Clustered index
CREATE TABLE TestTable (
ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
FirstName VARCHAR(64) NOT NULL DEFAULT '',
LastName VARCHAR(64) NOT NULL DEFAULT '',
FullName VARCHAR(64) NOT NULL DEFAULT '',
PRIMARY KEY (ID),
KEY ix_TestTable_FN_LN (FirstName, LastName)
);

INSERT INTO TestTable (FirstName, LastName, FullName) SELECT First_Name, Last_name, CONCAT(First_Name, ' ', Last_Name) FROM actor;

# Uses Primary key as index
EXPLAIN SELECT FirstName, LastName FROM TestTable ORDER BY ID;
# Uses Secondary key as index
EXPLAIN SELECT FirstName, LastName FROM TestTable ORDER BY FirstName;
EXPLAIN SELECT FirstName, LastName FROM TestTable ORDER BY LastName;
# No index for FullName, need to scan entire table
EXPLAIN SELECT FirstName, LastName FROM TestTable ORDER BY FullName;
# Uses primary key as index
EXPLAIN SELECT FirstName, LastName FROM TestTable WHERE ID = 100 ORDER BY FullName;
# Uses secondary key as index
EXPLAIN SELECT FirstName, LastName FROM TestTable WHERE FirstName = 'ALBERT' ORDER BY ID;
# Tricky part: Uses primary key as index, because seconday index had FirstName as first parameter ix_TestTable_FN_LN (FirstName, LastName)
EXPLAIN SELECT FirstName, LastName FROM TestTable WHERE LastName = 'GRANT' ORDER BY ID;
# No index, full table scan
EXPLAIN SELECT FirstName, LastName FROM TestTable WHERE LastName = 'GRANT' ORDER BY FullName;

DROP TABLE TestTable;

EXPLAIN TestTable;

# Example 7
EXPLAIN SELECT title, rental_duration, length 
FROM film FORCE INDEX (idx_film_length_rental_duration)
WHERE rental_duration = 6 AND length = 100;

EXPLAIN SELECT title, rental_duration, length 
FROM film USE INDEX (idx_film_rental_duration_length, idx_film_length_rental_duration)
WHERE rental_duration = 6 AND length = 100;

EXPLAIN SELECT title, rental_duration, length 
FROM film IGNORE INDEX (idx_film_rental_duration_length, idx_film_length_rental_duration)
WHERE rental_duration = 6 AND length = 100;

# Example 8
ANALYZE TABLE TestTable;
OPTIMIZE TABLE TestTable;
ALTER TABLE TestTable; # Recreate table
SHOW TABLE STATUS;