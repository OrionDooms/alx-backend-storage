SELECT band_name, 
IF(split IS NULL, 2022 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style = 'GLAM ROCK'
ORDER BY lifespan DESC;
