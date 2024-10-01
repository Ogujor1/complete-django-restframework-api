import requests

product_id = input('Enter a whole number\n')
try:
  product_id = int(product_id)
except:
  product_id = None
  print(f"{product_id} is not valid!!")

endpoint = f"http://localhost:8000/api/products/{product_id}/update"

response_put = requests.put(endpoint, json={'title':'I love you Baby', 'content': 'I sincerely miss you, My white Soup', 'price':125})
print(response_put.json())
 
