-- Lists all cities contained in database
SELECT cities.id, cities.name, states.name 
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
