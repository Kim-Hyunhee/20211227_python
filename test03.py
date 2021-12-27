from datas import OverloadingTest
from multipledispatch import dispatch 

ot = OverloadingTest()

# 정수 3개는 사용 가능
print(f'정수 3개 더하기 : {ot.add_num(4, 5, 6)}')

# 정수 2개만 더하기? 사용 불가
print(f'정수 2개 더하기 : {ot.add_num(5,6)}')