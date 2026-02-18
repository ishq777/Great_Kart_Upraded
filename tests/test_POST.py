import requests

url = "http://127.0.0.1:8000/api/v1/products/"

for i in range(10):
    with open("dummy.png", "rb") as img:
        files = {"image": img}

        data = {
            "category": 1,
            "product_name": f"pc{i}",
            "slug": f"p{i}",
            "description": "test",
            "price": 200,
            "stock": 10,
            "is_available": True
        }

        response = requests.post(url, data=data, files=files)
        print(response.status_code, response.json())
