-- Sort by number of fans.
SELECT origin, nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;