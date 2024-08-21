-- Lists all cities contained in the database hbtn_0d_usa
-- Should be displayed in ascending order by city.id
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM citites
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
