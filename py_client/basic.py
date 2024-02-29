import requests
import json

endpoint = "http://127.0.0.1:8000/products/"


# response = requests.post(endpoint, json={
#             'title':"Mouse", 
#             'content':"This is content", 
#             # 'price':20.5
#             })
data = {
    "title": "keyboard"
}
response = requests.post(endpoint, json=data)
print(response.json())
