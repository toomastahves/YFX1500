# Before trigger
DELIMITER //
CREATE TRIGGER language_before_insert
BEFORE INSERT on language
FOR EACH ROW
BEGIN
	SET NEW.name = concat(UPPER(SUBSTRING(NEW.name, 1, 1)), LOWER(SUBSTRING(NEW.name FROM 2)));
END//
DELIMITER ;

insert into language (name) values ('test');
select * from language;
drop trigger language_before_insert;

# After trigger
CREATE TABLE audit_language (language_id TINYINT(3), name CHAR(20), last_update TIMESTAMP, rowvalue char(20));

DELIMITER //
CREATE TRIGGER language_after_insert
AFTER UPDATE on language
FOR EACH ROW
BEGIN
	INSERT INTO audit_language (language_id, name, last_update, rowvalue)
	VALUES (OLD.language_id, OLD.name, OLD.last_update, 'before update');
	INSERT INTO audit_language (language_id, name, last_update, rowvalue)
	VALUES (NEW.language_id, NEW.name, NEW.last_update, 'after update');
END//
DELIMITER ;

DROP TRIGGER language_after_insert;

UPDATE language SET name = 'test2' WHERE name = 'test';
