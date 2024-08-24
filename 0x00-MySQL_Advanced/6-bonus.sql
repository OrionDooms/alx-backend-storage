-- This SQL script that creates a stored procedure AddBonus that adds
-- a new correction for a student.
DELIMITER //

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)

BEGIN
	DECLARE project_id INT DEFAULT NULL;

	INSERT INTO project(name) VALUES (project_name);
	SET project_id = LAST_INSERT_ID(id);

	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END //

DELIMITER ;
