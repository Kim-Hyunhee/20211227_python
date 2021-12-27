# 오버로딩의 개념에 대한 설명을 위한 클래스
# 라이브러리를 활용해 동작하도록

class OverloadingTest:
    
    # 두 개의 숫자를 더할 때 사용
    def add_num(self, num1, num2):
        print('두 개의 숫자 더하기')
        return num1 + num2
    
    # 세 개의 숫자를 더할 때 사용
    def add_num(self, num1, num2, num3):
        print('세 개의 숫자 더하기')
        return num1 + num2 + num3