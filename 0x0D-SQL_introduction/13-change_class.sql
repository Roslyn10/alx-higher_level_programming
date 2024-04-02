-- Removes all records with a score <= 5
-- in the second_table in hbtn_0c_0 
-- mysql will be passed as an argument
DELETE score, name 
FROM second_table
WHERE score <5;
