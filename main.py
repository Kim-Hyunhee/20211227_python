from datas.cat import Cat
from datas.dog import Dog
from datas.cow import Cow
from datas.horse import Horse
from datas.test.test import Mytest
from datas.test.test_module import test01, test02


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

# dog2를 비워두자

dog2 = None
print(dog2)

# del(dog2)
# print(dog2)

num1 = 10

if num1 ==10:
    num2 = 20
    print(num2)

print(num2)


# 고양이 한 마리 생성

# Cat 클래스는 Animal 클래스로부터 생성자도 물려받은 상태
# 출생년도, 성별을 넣어야 하는 이유
cat1 = Cat(2014, True)

# Cat은 동물의 일종 => 동물이 하는 기능은 전부 수행 가능
cat1.run()

cow1 = Cow(2020, False)
cow1.run()

horse1 = Horse(2019, True)
horse1.run()

cat1.play_with_human()
cat1.run()



test01()
test02()