-- Lists all cities in california found
SELECT * FROM cities
WHERE state.id = (
	SELECT id
	FROM states
	WHERE name = 'California');
