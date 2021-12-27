from geopy.distance import geodesic


# 학원의 위도 / 경도 를 tuple로 만들자
coord_nepplus = ( 37.5777919200324, 127.03365483134596 )   # 여러 개의 값을 넣으면 tuple 형태로 만들어짐 tuple : 내용 변경 불가능한 list

coord_home = ( 37.58922206585357, 127.0173636275008 )

print( geodesic(coord_nepplus, coord_home).km )