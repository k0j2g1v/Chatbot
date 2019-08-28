import requests

# 1. requests 통해 요청 보내기
# requests.get('주소')
url = 'https://api.bithumb.com/public/ticker'
response = requests.get(url)
res_dic = response.json()
print(res_dic['data']['opening_price'])