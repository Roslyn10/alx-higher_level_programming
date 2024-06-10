-- Displays the average tempreture by city
-- ordered by tempreature

USE tempreature
SELECT city, AVG(value) as avg_temp
FROM tempreatures
GROUP BY city
ORDER BY avg_temp DESC;
