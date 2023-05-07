SELECT name
FROM customers
WHERE customers.id IN (SELECT id_customers FROM legal_person )