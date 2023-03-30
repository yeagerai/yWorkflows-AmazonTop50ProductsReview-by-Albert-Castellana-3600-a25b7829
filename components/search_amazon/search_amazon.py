
import os
import openai
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import yaml

from core.abstract_component import AbstractComponent


class SearchAmazonInputDict(BaseModel):
    product_name: str
    limit: Optional[int] = None


class SearchAmazonOutputDict(BaseModel):
    product_urls: List[str]


class SearchAmazon(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.result_limit: int = yaml_data["parameters"]["result_limit"]

    def search_amazon_api(self, product_name: str, limit: int) -> List[str]:
        api_url = "https://amazon-api.example.com/search"
        response = requests.get(api_url, params={"q": product_name, "limit": limit})
        product_urls = response.json()["urls"]
        return product_urls

    def transform(
        self, args: SearchAmazonInputDict
    ) -> SearchAmazonOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        limit = args.limit if args.limit is not None else self.result_limit
        product_urls = self.search_amazon_api(args.product_name, limit)

        return SearchAmazonOutputDict(product_urls=product_urls)


search_amazon_app = FastAPI()


@search_amazon_app.post("/transform/")
async def transform(
    args: SearchAmazonInputDict,
) -> SearchAmazonOutputDict:
    search_amazon = SearchAmazon()
    return search_amazon.transform(args)
