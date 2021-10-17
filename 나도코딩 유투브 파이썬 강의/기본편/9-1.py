# 클래스

class Unit:
    def __init__(self, name, hp, damage): # __init__는 생성자이다. 자동으로 호출되는 부분.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("채력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린1", 40, 5)
marine2 = Unit("마린2", 40, 5)
tank = Unit("탱크", 150, 35)