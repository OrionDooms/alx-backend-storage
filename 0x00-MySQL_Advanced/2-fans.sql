-- This SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans.
-- Requirements: Import the table dump metal_bands.sql.
SELECT origin, nb_fans
FROM (SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin)
AS subquery ORDER BY nb_fans DESC;
