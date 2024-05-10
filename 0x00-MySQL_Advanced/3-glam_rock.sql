SELECT band_name, (2022 - formed) AS lifespan
WHERE style=='Glam rock'
GROUP BY band_name
ORDER BY lifespan
