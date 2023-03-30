
import pytest
from typing import List, Dict
from fastapi.testclient import TestClient
from pydantic import BaseModel
from your_module_path import AmazonReviewScraper, ProductURLsInputDict, ReviewsOutputDict

test_cases = [
    (
        # Mocked input data
        ["https://www.amazon.com/dp/abcdefghijk"],
        # Mocked external_api_client.scrape_amazon_reviews() response
        {"https://www.amazon.com/dp/abcdefghijk": [{"review_title": "Great product!", "review_text": "Loved it."}]},
        # Expected output data
        {"reviews": {"https://www.amazon.com/dp/abcdefghijk": [{"review_title": "Great product!", "review_text": "Loved it."}]}}
    ),
    (
        # Mocked input data
        ["https://www.amazon.com/dp/abcdefghijk", "https://www.amazon.com/dp/zyxwvutsrq"],
        # Mocked external_api_client.scrape_amazon_reviews() responses
        {
            "https://www.amazon.com/dp/abcdefghijk": [{"review_title": "Great product!", "review_text": "Loved it."}],
            "https://www.amazon.com/dp/zyxwvutsrq": [{"review_title": "Not good", "review_text": "Disappointed."}]
        },
        # Expected output data
        {
            "reviews": {
                "https://www.amazon.com/dp/abcdefghijk": [{"review_title": "Great product!", "review_text": "Loved it."}],
                "https://www.amazon.com/dp/zyxwvutsrq": [{"review_title": "Not good", "review_text": "Disappointed."}]
            }
        }
    )
]

@pytest.mark.parametrize("input_data, mocked_external_api_response, expected_output", test_cases)
def test_amazon_review_scraper(input_data: List[str], mocked_external_api_response: Dict, expected_output: BaseModel) -> None:
    # Replace the original external_api_client.scrape_amazon_reviews with a mock function
    def mock_scrape_amazon_reviews(url: str) -> Dict[str, List[str]]:
        return mocked_external_api_response.get(url, [])

    component = AmazonReviewScraper()
    component.external_api_client.scrape_amazon_reviews = mock_scrape_amazon_reviews

    # Call the component's transform() method with the mocked input data
    input_base_model = ProductURLsInputDict(product_urls=input_data)
    result = component.transform(input_base_model)

    # Assert that the output matches the expected output
    assert result == ReviewsOutputDict(**expected_output)

    # Alternatively, use FastAPI's TestClient to test the endpoint:
    # client = TestClient(component.amazon_review_scraper_app)
    # response = client.post("/transform/", json=input_base_model)
    # assert response.status_code == 200
    # assert response.json() == expected_output

