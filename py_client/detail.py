import requests

product_id = input('Enter a whole number\n')
try:
  product_id = int(product_id)
except:
  product_id = None
  print(f"{product_id} is not valid!!")

endpoint = f"http://localhost:8000/api/products/{product_id}"

response_get = requests.get(endpoint)
print(response_get.json())
