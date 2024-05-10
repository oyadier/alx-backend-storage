-- Sort by number of fans.
SELECT origin, SUM(fans) AS nb_fans 
FROM metal_bands
ORDER BY nb_fans DESC
GROUP BY origin;