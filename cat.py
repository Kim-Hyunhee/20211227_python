from animal import Animal

class Cat(Animal):

    # 동물 : 출생 년도 / 성별  +  달리기(메쏘드)
    
    # 기능 추가 - 고양이만의 별도 기능
    def play_with_human(self, owner_name):
        print(f'고양이가 {owner_name}과 놀아줍니다.')