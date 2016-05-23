SET GLOBAL event_scheduler = ON;

CREATE TABLE event_audit (id INT NOT NULL AUTO_INCREMENT, last_update TIMESTAMP, PRIMARY KEY(ID));

# Example 1
DELIMITER //
CREATE EVENT one_time_event
ON SCHEDULE AT NOW() + INTERVAL 1 MINUTE
DO BEGIN
	INSERT INTO event_audit(last_update) VALUES (NOW());
END//
DELIMITER ;

select * from event_audit;

drop event one_time_event;

# Example 2
DELIMITER //
CREATE EVENT recurring_time_event
ON SCHEDULE EVERY 2 SECOND
STARTS NOW()
DO BEGIN
	INSERT INTO event_audit(last_update) VALUES (NOW());
END//
DELIMITER ;

drop event recurring_time_event;