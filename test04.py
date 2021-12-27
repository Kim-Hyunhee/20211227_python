from datas.dog import Dog
# 파이썬 제공 내장 함수들 체험
# 내장 함수 : import 없이 진행

# 1. enumerate => for 문을 도는 list의 위치 / 데이터 동시 추출

student_names = ['김범준','김현희','이승훈','전은형']

# 수강생들의 이름을 뽑으면서 => '1번째 학생 : 김범준' , '2번째 학생 : 김현희' 양식으로 가공해서 출력

for i, name in enumerate(student_names):
    print(f'{i + 1}번째 학생 : {name}')
    
print('======================')

# 2. id / hex 체험

dog1 = Dog('바둑이', 2015, '믹스견')
dog2 = Dog('아롱이', 2010, '치와와')

# 변수와 객체가 나눠져있다. 체험

# dog1과 dog2가 같은 객체를 바라보게 된다.
dog1 = dog2

# dog1의 이름을 해피로 바꿈
dog1.name = '해피'

# 두 개의 변수가 연결된 주소? => 둘 다 같은 주소로 변경
print( hex(id(dog1)) )  # hex ( 숫자 )  => 16진수로는 어떻게 되는지 변환 : 메모리 주소를 컴퓨터가 다루는 양식으로 확인할 때
print( hex(id(dog2)) )

dog1.print_dog_info()
dog2.print_dog_info()


# 3. input / int 체험

birth_year = int( input('출생 년도 입력 : ') )

age = 2021 - birth_year + 1

print(f'나이 : {age}세')

# 4. float() 체험 / round() 체험

height = float(input('키 입력 : '))

# ex. 키 179.7 => 사실상 180임

print(f'당신의 키는 사실상 {round(height)}cm 입니다.')



result = 0
for i in range(1, 50):
    result += 0.1
    
print(result)


# user_info = []
# user_info.append('김현희')
# user_info.append(1995)
# user_info.append(True)

# user_info2 = []
# user_info2.append(2010)
# user_info2.append(False)
# user_info2.append('김학생')

# 두 사용자의 이름을 꺼내보자 => list / tuple 모두 넣어준 순서 (index) 가 자료를 꺼낼 때 중요한 기준
# user_info[0]
# user_info2[2]

# 'name' 이름표로 이름을 꺼낸다면? 순서에 관계없이 명확한 코딩

user_info1 = {}  # dictionary : 이름표 - 실제값 쌍으로 저장하는 자료구조 Key- Value

user_info1['name'] = '김현희'
user_info1['birth_year'] = 1995
user_info1['is_female'] = True

user_info2 = {}
user_info2['birth_year'] = 2010
user_info2['is_female'] = False
user_info2['name'] = '김학생'


# dictionary는 순서는 중요하지 않다. => 이름표가 어떤 게 붙어있느냐?

print(user_info1['name'])
print(user_info2['name'])           