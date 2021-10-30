# 상속

# 메딕 : 의무병. 치유사. 공격을 하지 않으므로 damage 매개변수를 삭제.
class Unit:
    def __init__(self, name, hp): # __init__는 생성자이다. 자동으로 호출되는 부분.
        self.name = name
        self.hp = hp
        

# 공격 유닛
class AttackUnit(Unit): # 클래스에 다른 클래스인 Unit을 매개변수로 넣고
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # Unit의 __init__를 사용하고 그곳에서 사용된 매개변수를 포함시킨다.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# Unit 클래스에 damage(공격력)를 지웠으나
# 상속에 의해 이전과 그대로 출력되는 것을 확인할 수 있다.