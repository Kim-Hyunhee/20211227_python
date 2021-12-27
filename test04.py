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