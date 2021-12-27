class Animal:
    def __init__(self, birth_year, is_male):
        self.birth_year = birth_year
        self.is_male = is_male
        
    def run(self):
        print('동물이 뛰어다닙니다.')