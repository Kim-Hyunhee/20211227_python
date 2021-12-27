class Dog:
    # 각 객체의 변수를 클래스단에 적지 않는다. => 함수 / 생성자의 객체에서 달아준다.
    def __init__(self, name, birth_year, type):
        self.name = name
        self.birth_year = birth_year
        self.type = type