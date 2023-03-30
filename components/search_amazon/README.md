
# SearchAmazon

A Component that searches Amazon for products matching the input product name and retrieves their URLs. Takes as input the product name and an optional limit for the number of results (defaults to 50). Outputs a list of product URLs.

## Initial generation prompt
description: 'A Component that searches Amazon for products matching the input product
  name and retrieves their URLs. Takes as input the product name and an optional limit
  for the number of results (defaults to 50). Outputs a list of product URLs.

  '
external_inputs:
- product_name
- limit
name: SearchAmazon


## Transformer breakdown
- Read the 'product_name' and 'limit' input
- Call Amazon's API to search for products with the provided 'product_name'
- Filter the search results based on the 'limit' parameter
- Extract the product URLs from the search results
- Return the list of 'product_urls' as output

## Parameters
[{'default_value': 50, 'description': 'The maximum number of product URLs to retrieve (this parameter is loaded from the configuration file)', 'name': 'result_limit', 'type': 'int'}]

        