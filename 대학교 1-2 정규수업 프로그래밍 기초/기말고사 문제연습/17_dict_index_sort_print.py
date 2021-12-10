# 딕셔너리 항목 정렬하여 출력

animal = {'고양이': 'NyanNyan', '강아지': 'MungMung'}

for key in sorted(animal.keys()):
    print(key, animal[key])
    
# 강아지 MungMung
# 고양이 NyanNyan