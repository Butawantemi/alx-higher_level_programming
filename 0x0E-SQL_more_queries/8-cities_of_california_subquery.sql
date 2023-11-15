-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- states table conatins only one record where name= california, id can be difffrent
-- not allowed to use the JOIN keyword

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'california'
)
ORDER BY id ASC;
