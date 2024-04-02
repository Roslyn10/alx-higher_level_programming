-- lists the number of records with the same score in second_table
-- of the hbtn_0c_0
-- List should be sprted by number of records (descending)
-- mysql qill be passed as an argument
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
