
# AmazonTop50ProductsReview

A Yeager Workflow that takes as input a product name, searches Amazon for the top 50 products with that name, retrieves the product link and reviews for each product, and creates a spreadsheet with this information. The Workflow is comprised of the following steps: 1. Accept the product name as input and pass it to the SearchAmazon API. 2. Use the SearchAmazon API to find the top 50 products matching the search criteria
   and retrieve their URLs.
3. For each product URL, retrieve the reviews using the AmazonReviewScrapper Component. 4. For each product, create a data entry with the URL and its reviews. 5. Compile all the data entries and format them into a spreadsheet using
   the SpreadsheetBuilder Component.
6. Save the spreadsheet to a desired location.

## Initial generation prompt
a workflow that takes in a product name, scans amazon for the top 50 products with that name and creates a spreadsheet with the link and the reviews for each product

## Authors: 
- yWorkflows
- Albert Castellana#3600
        