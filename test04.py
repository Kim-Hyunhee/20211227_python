# 파이썬 제공 내장 함수들 체험
# 내장 함수 : import 없이 진행

# 1. enumerate => for 문을 도는 list의 위치 / 데이터 동시 추출

student_names = ['김범준','김현희','이승훈','전은형']

# 수강생들의 이름을 뽑으면서 => '1번째 학생 : 김범준' , '2번째 학생 : 김현희' 양식으로 가공해서 출력

for i, name in enumerate(student_names):
    print(f'{i + 1}번째 학생 : {name}')
    
print('======================')

