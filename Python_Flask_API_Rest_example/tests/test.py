import requests

BASE = 'http://127.0.0.1:5000/'

# 500 – Internal Server Error
# 200 - Success Status Response

# response_get = requests.get(BASE + 'helloworld')
# print(response_get.status_code)
# print(response_get.json())

# response_post = requests.post(BASE + 'helloworld')
# print(response_post.status_code)
# print(response_post.json())

response_get2 = requests.get(BASE + 'helloworld/bill')
print(response_get2.status_code)
print(response_get2.json())
