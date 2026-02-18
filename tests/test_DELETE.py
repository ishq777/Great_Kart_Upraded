import requests

for i in range(22, 25):
    url = f"http://127.0.0.1:8000/api/v1/products/{i}/"
    
    response = requests.delete(url)
    print(i, response.status_code)




# import requests

# url = f"http://127.0.0.1:8000/api/v1/products/?/"
    
# response = requests.delete(url)
# print(response.status_code)

