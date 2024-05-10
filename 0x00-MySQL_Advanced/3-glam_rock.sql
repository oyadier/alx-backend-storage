-- Old school band.
SELECT band_name, (split - formed) AS lifespan
WHERE style='Glam rock'
GROUP BY band_name
ORDER BY lifespan
