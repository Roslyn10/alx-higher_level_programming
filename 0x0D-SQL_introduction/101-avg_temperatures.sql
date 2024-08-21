-- Displays the average temperature by city
-- ordered by temperature

USE temperature;
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
