
# AmazonTop50ProductsReview

This component retrieves the top 50 products from Amazon based on user reviews and saves the product names in a spreadsheet. The component takes a product name as input, searches for the top 50 products related to the input, and writes the product names to a spreadsheet file with the specified output path.

## Initial generation prompt
description: "IOs - InputModel:\n  product_name: str\nOutputModel:\n  spreadsheet_path:\
  \ str\n"
name: AmazonTop50ProductsReview


## Transformer breakdown
- Fetch the top 50 products related to the input 'product_name' from Amazon based on user reviews
- Create a new spreadsheet file or open an existing one at the specified 'spreadsheet_path'
- Write the retrieved top 50 product names in the spreadsheet
- Save and close the spreadsheet

## Parameters
[]

        