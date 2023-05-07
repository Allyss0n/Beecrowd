SELECT products.name
FROM products, providers
WHERE providers.id = products.id_providers
AND products.amount >=10
AND products.amount <=20
AND providers.name LIKE 'P%'