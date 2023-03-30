
# AmazonReviewScraper

A Component that takes a list of product URLs as input and retrieves the reviews for each product. Outputs a list of dictionaries where the key is the URL and the value is the associated reviews.

## Initial generation prompt
description: 'A Component that takes a list of product URLs as input and retrieves
  the reviews for each product. Outputs a list of dictionaries where the key is the
  URL and the value is the associated reviews.

  '
external_inputs:
- product_urls
name: AmazonReviewScrapper


## Transformer breakdown
- Initialize an empty dictionary for storing output
- Iterate through the input 'product_urls'
- For each URL, call the external API to scrape the reviews
- Store the list of reviews in the output dictionary with the URL as the key
- Return the output dictionary containing URL and associated reviews

## Parameters
[]

        