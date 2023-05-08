SELECT products.name, categories.name
FROM products, categories
WHERE products.id_categories = categories.id 
AND products.amount > 100 
AND categories.id in (1,2,3,6,9)
ORDER BY categories.id asc