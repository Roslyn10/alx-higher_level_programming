-- lists all records of the table second_table of the database hbtn_0c_0
-- doesnt list rows without a name value
-- should display the score and the name
-- should be listed by descending score
-- mysql will be passed as an argument
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
GROUP BY score, name
ORDER BY score DESC;
