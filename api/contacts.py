import requests


def get_contacts():
    url = "https://wineoclockglobal.com/api/list_contact"
    response = requests.get(url)
    return response.json().get("data", [])
