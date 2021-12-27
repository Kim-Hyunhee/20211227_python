from dog import Dog


dog1 = Dog('해피', 2016, '푸들')  # 변수를 만들어줘야 객체를 불러올 수 있음.

dog2 = Dog('바둑이', 2014, '믹스견')

dog1 = dog2

dog1.name = '아롱이'

print(f'dog1의 이름 : {dog1.name}')
print(f'dog2의 이름 : {dog2.name}')

# 함수 예시
def print_main_info():
    # 함수 : 특정 객체가 실행하는 코드가 아님 => 단순 기능 수행
    # 어느 객체인지 알 필요가 없다. => self 변수를 파라미터로 만들지 않는다.
    print('이 함수는 main.py에서 실행됩니다.')
    
    # 함수 / 메쏘드 공통점 => 정의만 해서는 사용되지 않는다. => 사용하는 코드를 별도로 추가 작성해야함
    
# 함수 호출 예시  
# 특징 : 함수 이름을 곧바로 불러낸다.  
print_main_info()

# 메쏘드 호출 예시
# 특징 : 변수이름.메쏘드() 형태로 사용함.
dog1.print_dog_info()