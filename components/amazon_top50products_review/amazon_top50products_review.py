
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class AmazonTop50ProductsReviewIn(BaseModel):
    product_name: str


class AmazonTop50ProductsReviewOut(BaseModel):
    spreadsheet_path: str


class AmazonTop50ProductsReview(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: AmazonTop50ProductsReviewIn, callbacks: typing.Any
    ) -> AmazonTop50ProductsReviewOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Fetch the top 50 products related to the input 'product_name' from Amazon based on user reviews
        top_50_products = results_dict[0].top_50_products

        # Create a new spreadsheet file or open an existing one at the specified 'spreadsheet_path'
        spreadsheet_path = results_dict[1].spreadsheet_path

        # Write the retrieved top 50 product names in the spreadsheet
        # Save and close the spreadsheet
        # Assuming the results_dict[2] already contains the updated 'spreadsheet_path'
        updated_spreadsheet_path = results_dict[2].spreadsheet_path

        out = AmazonTop50ProductsReviewOut(spreadsheet_path=updated_spreadsheet_path)     
        return out


load_dotenv()
amazon_top_50_products_review_app = FastAPI()


@amazon_top_50_products_review_app.post("/transform/")
async def transform(
    args: AmazonTop50ProductsReviewIn,
) -> AmazonTop50ProductsReviewOut:
    amazon_top_50_products_review = AmazonTop50ProductsReview()
    return await amazon_top_50_products_review.transform(args, callbacks=None)

