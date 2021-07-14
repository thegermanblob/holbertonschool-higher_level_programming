-- lists all records of second table with name
SELECT `score`, `name`
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
