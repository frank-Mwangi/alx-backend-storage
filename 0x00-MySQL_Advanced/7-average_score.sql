-- Procedure to compute average score for
-- a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score DECIMAL(10, 2);
	SELECT AVG(score) AS avg_score
	FROM corrections
	WHERE user_id = user_id;

	INSERT INTO average_scores (user_id, score)
	VALUES (user_id, avg_score)
	ON DUPLICATE KEY UPDATE score = avg_score;
END;
//
DELIMITER ;
