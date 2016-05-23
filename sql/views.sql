CREATE VIEW my_AllActors AS SELECT * FROM actor;

SELECT * FROM my_AllActors WHERE first_name LIKE '%jenn%';

DROP VIEW my_AllActors;

# DML Operation
CREATE VIEW DMLOperation
AS
SELECT language_id, name, last_update FROM sakila.language WITH CHECK OPTION;

SELECT * FROM DMLOperation;
SELECT * FROM sakila.language;

INSERT INTO DMLOperation (name, last_update) VALUES ('hindi', NOW());
UPDATE DMLOperation SET name = 'est' WHERE name = 'hindi';
DELETE FROM DMLOperation WHERE name = 'est';

DROP VIEW DMLOperation;
