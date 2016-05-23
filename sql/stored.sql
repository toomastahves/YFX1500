# Example 1
DELIMITER //
CREATE PROCEDURE GetLanguage()
BEGIN
	select * from language;
END//
DELIMITER ;

CALL GetLanguage();
DROP PROCEDURE GetLanguage;

# Example 2
DELIMITER //
CREATE PROCEDURE WhileLoop()
BEGIN
	DECLARE i INT DEFAULT 1;
	WHILE i < 6 DO
		SELECT POW(i, i);
		SET i = i + 1;
	END WHILE;
END//
DELIMITER ;

CALL WhileLoop();
DROP PROCEDURE WhileLoop;

# Example 3
DELIMITER //
CREATE PROCEDURE ConcatName(firstname VARCHAR(100), lastname VARCHAR(100))
BEGIN
	DECLARE fullname varchar(200);
	SET fullname = CONCAT(firstname, ' ', lastname);
	SELECT fullname;
END//
DELIMITER ;

CALL concatname('t', 'a');
DROP PROCEDURE concatname;

# Example 4
DELIMITER //
CREATE PROCEDURE InsertValue(NameOfLang VARCHAR(100))
BEGIN
	INSERT INTO language(name, last_update) VALUES (NameOfLang, NOW());
	SELECT LAST_INSERT_ID();
END//
DELIMITER ;

CALL insertvalue('hindi');
select * from language;
DROP PROCEDURE insertvalue;

# Example 5
DROP PROCEDURE IF EXISTS insertlanguage;
DELIMITER //
CREATE PROCEDURE insertlanguage(IN NameOfLang VARCHAR(100), OUT LangID INT)
BEGIN
	INSERT INTo language (name, last_update) VALUES (NameOfLang, NOW());
	SET LangID = last_insert_id();
END//
DELIMITER ;

CALL insertlanguage('est', @langid);
select concat('last language id: ', @langid);
select * from language;
DROP PROCEDURE insertlanguage;

# Example 6
DELIMITER //
CREATE FUNCTION getlanguage(lang_id INT)
RETURNS VARCHAR(100)
BEGIN
DECLARE langname VARCHAR(100);
SELECT name INTO langname FROM language WHERE language_id = lang_id;
RETURN(langname);
END//
DELIMITER ;

select getlanguage(1);
drop function getlanguage;

