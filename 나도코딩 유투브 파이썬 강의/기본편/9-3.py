# 멤버변수

class Unit:
    def __init__(self, name, hp, damage): # __init__는 생성자이다. 자동으로 호출되는 부분.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("채력 {0}, 공격력 {1}".format(self.hp, self.damage))

wraith1 = Unit("레이스1", 80, 5)
print("유닛 이름:{0}, 공격력:{1}".format(wraith1.name, wraith1.damage)) # 멤버변수를 사용하여 출력하기

wraith2 = Unit("레이스2", 80, 5)
wraith2.clocking = True # 외부에서 wraith2에 clocking이라는 변수를 추가로 할당하였다

if wraith2.clocking == True: # wraith2에는 clocking 변수가 있지만, wraith1에는 없다. wraith1에 따로 변수를 선언하지 않았기 때문이다.
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))