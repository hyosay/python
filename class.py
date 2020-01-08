#클래스(class): 반복되는 불필요한 소스코드를 최소화 하면서
# 현실 세계의 사물을 컴퓨터 프호그래밍 상에서
# 쉽게 표현할 수 있도록 해주는 프로그래밍 기술

# 인스턴스: 클래스호 정의된 객체를 ㅠㅡ호그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수, 메소드라고 부릅니다.

#  실수형 문자열형 같이 자동차형이라는 하나의 자료형을 만들었다고 보면 됨
'''
class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name #  클래스의 멤버
        self.color = color # 클래스의 멤버
    # 클래스 소멸자
    def __del__(self):
        print("삭제합니다")
    # 클래스의 메소드
    def show_info(self):
        print("name :", self.name, "/ color : " ,self.color)
    # Setter 메소드 (바꾸는 메소드)
    def set_name(self, name):
        self.name = name

Car1 = Car("소나타", "Red")
Car1.set_name("그랜저")

Car1.show_info()
Car2 = Car("아반뗴", "blue")
Car2.show_info()
print(Car1.name, "을 구매했습니다!")
del Car1

'''

# 클래스 상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부ㅗ와 자식 관계가 존재합니다.
class Unit:
    def __init__(self, name ,power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [전투력 :",self.power, "]")
unit = Unit("전효성", 285)
unit.attack()
class Monster(Unit):
    def __init__(self,name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름 :", self.name, "/ 몬스터 종류 :", self.type)
monster = Monster(" 슬라임", 10, "초금 ")
monster.attack()
monster.show_info()