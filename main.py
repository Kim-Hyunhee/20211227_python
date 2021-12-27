from dog import Dog


dog1 = Dog('해피', 2016, '푸들')  # 변수를 만들어줘야 객체를 불러올 수 있음.

dog2 = Dog('바둑이', 2014, '믹스견')

dog1 = dog2

dog1.name = '아롱이'

print(f'dog1의 이름 : {dog1.name}')
print(f'dog2의 이름 : {dog2.name}')