#클래스(class): 반복되는 불필요한 소스코드를 최소화 하면서
# 현실 세계의 사물을 컴퓨터 프호그래밍 상에서
# 쉽게 표현할 수 있도록 해주는 프로그래밍 기술

# 인스턴스: 클래스호 정의된 객체를 ㅠㅡ호그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수, 메소드라고 부릅니다.
class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name #  클래스의 멤버
        self.color = color # 클래스의 멤버
    def show_info(self):
        print("name :", self.name, "/ color : " ,self.color)

Car1 = Car("소나타", "Red")
Car1.show_info()
