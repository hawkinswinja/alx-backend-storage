-- create trigger event to validate email
DELIMITER $$
CREATE TRIGGER valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF
		OLD.email != NEW.email THEN SET NEW.valid_email = 0;
	END IF;
END;
$$
DELIMITER ;
