class Dog:
    # 각 객체의 변수를 클래스단에 적지 않는다. => 함수 / 생성자의 객체에서 달아준다.
    def __init__(self, name, birth_year, type):
        self.name = name
        self.birth_year = birth_year
        self.type = type
        
        
    # 메쏘드 예시
    def print_dog_info(self):
        # 메쏘드 : 어떤 객체가 수행하는 그 객체의 기능
        # 어느 객체 (self 변수에 담아두자)가 수행하는지? 알아낸 상태로 코드를 작성해야함
        
        print(f'강아지 이름 : {self.name}')