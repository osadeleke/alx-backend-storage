-- check email change

DELIMITER $$

-- drop trigger if it exists
DROP TRIGGER IF EXISTS email_validate;

-- create trigger
CREATE TRIGGER email_validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
