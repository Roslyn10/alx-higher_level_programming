-- Lists all cities contained in the database hbtn_0d_usa
-- Should be displayed in ascending order by city.id
SELECT cities.id, city.name, states.name
FROM citites
INNER JOIN states
ON cities.sate_id = states.id;
