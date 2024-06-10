-- Displays the max tempreature of each state
-- ordered by State name

SELECT state, MAX(value) AS max_temp
FROM tempreatures
GROUP BY state
ORDER BY state;
