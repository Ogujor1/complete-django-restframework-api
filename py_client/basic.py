import requests

endpoint = "http://localhost:8000/api/"

response_post = requests.post(endpoint, json={'title':'My here Product', 'content': 'This product is classic'})
print(response_post.json())
