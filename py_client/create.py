import requests

endpoint = "http://localhost:8000/api/products/"

headers = {
  'Authorization': f"Bearer 51da949b1a3529c47b5ef90ba610b960df0f5946"
}

data = {
  'title': input('Enter Title:\n'),
  'content': input('Enter Content:\n'),
  'price': float(input('Enter the price in 2 decimal places:\n'))
}
response_post = requests.post(endpoint, json=data, headers=headers)
print(response_post.json())