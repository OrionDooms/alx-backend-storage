SELECT
	band_name,
	CASE
		WHEN split IS NULL 2022 - formed
		ELSE split - formed
	END AS lifespan
FROM
	metal_bands
WHERE
	Style = 'GLAM ROCK'
ORDER BY
	lifespan DESC;
