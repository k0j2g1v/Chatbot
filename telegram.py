"""
python으로 telegram message 보내기
"""
import requests

base_url= 'https://api.telegram.org'
token = 'Bot Token Code'

# (1) getUpdate을 통해 chat_id를 가져옴
url = f'{base_url}/bot{token}/getUpdates'
print(url)
res = requests.get(url)
res_dic = res.json()

chat_id = res_dic['result'][0]['message']['chat']['id']

# (2)
text = '와 자동화!'
url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
print(url)
requests.get(url)