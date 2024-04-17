-- Updates the score of Bob to 10 in the table
-- don't use Bob's id value, only name field
-- mysql will be passed as an argument
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
