import requests

url =  'https://dummyjson.com/products'

def get_products():
    base = requests.get(url)

    return base.json()
