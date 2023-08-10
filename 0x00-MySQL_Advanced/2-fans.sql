--Rank bands by number of fans
SELECT origin, SUM(fans) as nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC

