-- Lists all cities in california found
SELECT id, state_id, name  FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California') 
ORDER BY cities.id DESC;
