-- check for style

SELECT band_name,
CASE WHEN split IS NULL THEN 2020 - formed ELSE split - formed END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
