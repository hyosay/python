# TURN GAME
a = 10
b = 50


# 스킬 리스트
# q,일격 피살, 데미지 = 100, 마나 = 50
# w,회복,

class Human:
    def __init__(self, name, skill, dmg, mana):
        self.name = name
        self.skill = skill
        self.dmg = dmg
        self.mana = mana

    def IN(self):
        print("커맨드 :", self.name, "/스킬이름 :", self.skill, "/사용마나 :", self.mana, "/대미지 :", self.dmg)

    def attack(self):
        print(self.name, "가 ", self.skill, "사용 [사용 마나 :", self.mana, "] 타격 대미지 :", self.dmg)


class Monster(Human):
    def __init__(self, name, HP, skill, dmg, mana):
        self.name = name
        self.HP = HP
        self.skill = skill
        self.dmg = dmg
        self. mana = mana

    def show_info(self):
        print(self.name, "의 체력이", self.HP, "남앗습니다.")

class Play(Human):
    def  __init__(self,name, HP, skill, dmg, mana):
        self.name = name
        self.HP = HP
        self.skill = skill
        self.dmg = dmg
        self.mana = mana
    def turn(self):
        for i in range(1, 100):
            eval(input())
            if self.HP < 100:
                self.HP = self.HP - self.dmg

Q = Human("q", "일격피살", 50, 100)
W = Human("w", "참격", 70, 40)
E = Human("e", "매혹", 30, 30)
R = Human("r", "최후의 만찬", 100, 200)

monster = Monster("슬라임", 1000, None, None, None)
monster.show_info()
user = Play("슬라임", 1000, 0, 0, 0)
for i in range(1,10):
    print(eval(input()).turn())
