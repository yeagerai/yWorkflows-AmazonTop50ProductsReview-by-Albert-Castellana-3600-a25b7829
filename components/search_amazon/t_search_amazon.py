
import os
import pytest
import requests
import json
from pydantic import ValidationError
from typing import List, Tuple
from unittest.mock import MagicMock

from components.search_amazon import SearchAmazon, SearchAmazonInputDict, SearchAmazonOutputDict

# Mocked API response
api_response = {
    "urls": [
        "https://amazon.example.com/product/12345",
        "https://amazon.example.com/product/67890",
    ]
}

# Test cases with mocked input and expected output data
test_cases: List[Tuple[SearchAmazonInputDict, SearchAmazonOutputDict]] = [
    (
        SearchAmazonInputDict(product_name="laptop", limit=None),
        SearchAmazonOutputDict(product_urls=[
            "https://amazon.example.com/product/12345",
            "https://amazon.example.com/product/67890",
        ]),
    ),
    (
        SearchAmazonInputDict(product_name="laptop", limit=1),
        SearchAmazonOutputDict(product_urls=[
            "https://amazon.example.com/product/12345",
        ]),
    ),
]

# Test scenarios using @pytest.mark.parametrize
@pytest.mark.parametrize("input_data,expected_output_data", test_cases)
def test_search_amazon_component(input_data: SearchAmazonInputDict, expected_output_data: SearchAmazonOutputDict):
    # Mock the request to the API
    requests.get = MagicMock(return_value=MagicMock(httpretty.Response, json=lambda: api_response))

    # Instantiate the component
    search_amazon = SearchAmazon()

    # Execute the component's transform() method
    output_data = search_amazon.transform(input_data)

    # Assert the output matches the expected output
    assert output_data == expected_output_data

# Test handling of invalid input data
def test_invalid_input_data():
    with pytest.raises(ValidationError):
        input_data = {"product_name": 123, "limit": "invalid"}

        # Attempt to create an instance of SearchAmazonInputDict using the invalid input data
        search_amazon_input = SearchAmazonInputDict(**input_data)

    # Assert the appropriate ValidationError is raised

# Test handling of empty input data
def test_empty_input_data():
    with pytest.raises(ValidationError):
        input_data = {"product_name": "", "limit": None}

        # Attempt to create an instance of SearchAmazonInputDict using the empty input data
        search_amazon_input = SearchAmazonInputDict(**input_data)

    # Assert the appropriate ValidationError is raised
