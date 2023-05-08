SELECT c.name, round( ( ( (s.math*2) + (s.specific*3) + (s.project_plan*5) )/10),2) as avg
FROM candidate c, score  s
WHERE c.id = s.candidate_id
ORDER BY avg DESC