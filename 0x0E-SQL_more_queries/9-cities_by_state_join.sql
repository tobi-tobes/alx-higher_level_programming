-- A script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities INNER JOIN hbtn_0d_usa.states
ON hbtn_0d_usa.cities.state_id = hbtn_0d_usa.states.id
ORDER BY cities.id;
