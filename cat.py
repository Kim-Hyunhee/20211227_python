from animal import Animal

class Cat(Animal):

    # 동물 : 출생 년도 / 성별  +  달리기(메쏘드)
    
    # 기능 추가 - 고양이만의 별도 기능
    def play_with_human(self, owner_name=None):
        
        if owner_name != None:
            print(f'고양이가 {owner_name}과 놀아줍니다.')
        else:
            print('고양이가 사람과 놀아줍니다.')
        
    
    # 물려받은 기능 수정 - 고양이가 뛰어다니는 기능
    def run(self):
        # 원래 동물로써 뛰어다니는 기능도 같이 실행
        super().run()
        print('고양이가 뛰어다닙니다')
    