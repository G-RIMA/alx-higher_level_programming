-- Lists all the cities in the database hbtn_0d_usa
-- sorted in ascending order
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.id_id;
ORDER BY id ASC;

