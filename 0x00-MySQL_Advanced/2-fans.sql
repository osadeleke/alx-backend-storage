-- sort list of band by country and fans

-- select countries, sum fans and sort by fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;