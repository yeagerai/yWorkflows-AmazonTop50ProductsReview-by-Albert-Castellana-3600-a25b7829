
import pytest
import typing
from fastapi.testclient import TestClient
from pydantic import BaseModel
from amazon_top_50_products_review import (
    AmazonTop50ProductsReviewIn,
    AmazonTop50ProductsReviewOut,
    amazon_top_50_products_review_app,
    AmazonTop50ProductsReview,
)

client = TestClient(amazon_top_50_products_review_app)

# Define test cases
test_cases = [
    {
        "input": AmazonTop50ProductsReviewIn(product_name="laptop"),
        "expected_output": AmazonTop50ProductsReviewOut(
            spreadsheet_path="laptop_top_50_products.xlsx"
        ),
    },
    {
        "input": AmazonTop50ProductsReviewIn(product_name="smartphone"),
        "expected_output": AmazonTop50ProductsReviewOut(
            spreadsheet_path="smartphone_top_50_products.xlsx"
        ),
    },
]

# Use the test_cases dictionary to set the mocked input and expected output
@pytest.mark.parametrize(
    "mocked_input, expected_output",
    [(case["input"], case["expected_output"]) for case in test_cases],
)
async def test_amazon_top_50_products_review(mocked_input, expected_output):
    component = AmazonTop50ProductsReview()

    result = await component.transform(args=mocked_input, callbacks=None)

    assert result == expected_output

# Test an edge case with an empty product_name input
@pytest.mark.asyncio
async def test_amazon_top_50_products_review_empty_product_name():
    mocked_input = AmazonTop50ProductsReviewIn(product_name="")
    component = AmazonTop50ProductsReview()

    with pytest.raises(ValueError):
        await component.transform(args=mocked_input, callbacks=None)

# Test FastAPI app using TestClient
@pytest.mark.parametrize(
    "mocked_input, expected_output",
    [(case["input"].dict(), case["expected_output"].dict()) for case in test_cases],
)
def test_amazon_top_50_products_review_app(mocked_input, expected_output):
    response = client.post("/transform/", json=mocked_input)

    assert response.status_code == 200
    assert response.json() == expected_output
