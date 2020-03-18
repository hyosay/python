class Unit:  #Unit class를 작성
    def __init__(self, name, power):  #이름과 전투력을 정의
        self.name = name
        self.power = power

    def attack(self):      #공격을 하는 함수
        print(self.name, "이(가) 공격을 수행합니다. [전투력 :", self.power, "]")


unit = Unit("전효성", 285)
unit.attack()


class Monster(Unit):  # Unit을 상속
    def __init__(self, name, power, type):  #이름,전투력, 종류를 정의
        self.name = name
        self.power = power
        self.type = type

    def show_info(self):
        print("몬스터 이름 :", self.name, "/ 몬스터 종류 :", self.type)


monster = Monster(" 슬라임", 10, "초급 ")
monster.attack()

# class와 class 상속을 공부하고있었습니다.
# 저는 25번쨰 행에 monster.attack()라는 소스코드 작성 후 스크립트를 싱행시켜 "슬라임 이(가) 공격을 수행합니다. [전투력 : 10 ]" 라는 출력값을 받았습니다.
# 하지만 저는 25번쨰 행에 있는 monster.attack() 소스코드를 지운 후 스크립트를 싱행시켜 콘솔을 통해 monster.attack() 함수를 호출하고싶습니다.
# 저는 input()을 통해 monster.attack()실행을 시켜보려고 시도하였지만
# input()을 통해 monster.attack()을 입력하면 결과값으로 문자열인"monster.attack()"이 그대로 출력되었습니다.
#스크립트에 25행과 같은 함수실행 소스 코드를 작성하지 않은 채로 스크립트를 실행 시켜 출력 결과값(콘솔) 창에서 함수를 호출 할 수 있는 방법이 있는지 궁금합니다.
