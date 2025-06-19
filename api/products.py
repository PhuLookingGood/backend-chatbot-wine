import requests


def get_products():
    url = "https://wineoclockglobal.com/api/products"
    response = requests.get(url)
    return response.json().get("data", [])
