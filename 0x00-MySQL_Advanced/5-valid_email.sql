-- Script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.
DELIMITER //

CREATE TRIGGER Email_valid
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
		IF OLD.email <> NEW.email AND NEW.valid_email = 1 THEN
			SET NEW.valid_email = 0;
		END IF;
END //

DELIMITER ;
