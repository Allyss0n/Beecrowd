SELECT name, CAST(DATEPART(day, payday) AS INTEGER) AS day
FROM loan