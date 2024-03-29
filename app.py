from flask import Flask
import random
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return 'hello'

# 1. 주문서를 만들고
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return "홍길동"

@app.route('/hello/<name>')
def hello(name):
    #return 'hello' + name
    #return 'hello {}'.format(name)
    return f'hello {name}'

@app.route('/square/<int:number>')
    # number를 제곱하여 변환
    # 1. 글자 number를 숫자로 변환
def square(number):    
    return str(number ** 2)
    
@app.route('/menu')
def menu():
    foods = ['바스버거','대우식당','진가와','고갯마루']
    food = random.choice(foods)
    return food

@app.route('/lotto')
def lotto():    

    # 1. requests 통해 요청 보내기
    # requests.get('주소')
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    #print(response.text)
    winner = response.json()
    result = random.sample(range(1,46),6) #비복원 무작위 추출    
    
    #random.sample(리스트/튜플, 뽑을갯수)
    #print(type(result)) 타입확인

    # 만약 6개가 모두 일치하면
    # -> 1등
    # 만약 5개가 모두 일치하면
    # -> 3등
    # 만약 4개가 일치하면
    # -> 4등
    # 만약 3개가 일치하면
    # -> 5등
    
    # => {3, 5, 12}
    num_list = []
    for  i in range(1,7):
        num_list.append(winner['drwtNo'+str(i)])
    print(num_list)

    count = len(set(winner) & set(result))
    # for num in result:
    #     if num in winner:
    #         count+=1

    rank = "다음 기회에"
    if count == 6:
        rank = '1등 입니다'
    elif count == 5:
        rank = '3등 입니다'
    elif count == 4:
        rank = '4등 입니다'
    elif count == 3:
        rank = '5등 입니다'
          
    return str(sorted(result)) + rank

    #sort는 원본 데이터를 바꾸지만 sorted는 원본데이터를 유지한다
