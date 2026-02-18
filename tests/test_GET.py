import requests

url = "http://127.0.0.1:8000/api/v1/products/"

response = requests.get(url)
print(response.status_code)
print(response.json())




# # use for specific products 

# import requests

# for i in range(1, 6):
#     url = f"http://127.0.0.1:8000/api/v1/products/{i}/"
    
#     response = requests.get(url)
#     print(i, response.status_code, response.json())
