# import requests

# for i in range(22, 32):
#     url = f"http://127.0.0.1:8000/api/v1/products/{i}/"

#     data = {
#         "price": 10,
#         "stock": 5
#     }

#     response = requests.put(url, data=data)
#     print(response.status_code, response.json())




import requests


url = f"http://127.0.0.1:8000/api/v1/products/31/"

data = {
    "price": 400,
    "stock": 50,
    "category": 1,
    "product_name": "DUMMY1",
    "slug": "dummy",
    "description": "dummy",
}

response = requests.put(url, data=data)
print(response.status_code, response.json())