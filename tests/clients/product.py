import requests

from tests.configuration import url


class ProductClient:
    def __init__(self):
        self.url = url

    @staticmethod
    def print_result(response: requests.Response):
        print("REQUEST INFO")
        print("METHOD", response.request.method)
        print("URL", response.request.url)
        print("BODY", response.request.body)

        print("RESPONSE INFO")
        print("STATUS_CODE", response.status_code)
        print("TEXT", response.text)

    def get_products(self):
        endpoint = f"{self.url}/products"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def get_product_by_id(self, product_id: int):
        endpoint = f"{self.url}/product/{product_id}"
        response = requests.get(endpoint)
        self.print_result(response)
        return response

    def create_product(self, name, price, dimensions):
        endpoint = f"{self.url}/product"
        req_dict = {
            "name": name,
            "price": price,
            "dimensions": dimensions
        }

        response = requests.post(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def update_product(self, product_id: int, name: str = None, price: int = None, dimensions: dict = None):
        endpoint = f"{self.url}/product/{product_id}"
        req_dict = {
            "name": name,
            "price": price,
            "dimensions": dimensions
        }

        response = requests.put(endpoint, json=req_dict)
        self.print_result(response)
        return response

    def delete_product(self, product_id: int):
        endpoint = f"{self.url}/product/{product_id}"
        response = requests.delete(endpoint)
        self.print_result(response)
        return response
