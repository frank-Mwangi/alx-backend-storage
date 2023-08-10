--Rank bands by number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC

