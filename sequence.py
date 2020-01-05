# 시퀀스(Squence): 문자열, 리스트, 튜플 등의 인덱스(Index)를 가지는 자료형


string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(string[0])
print(list[0])
print(tuple[0])
for i in tuple:
    print(i)
add = 0
for i in list:
    if i == 'l':
        add = add + 1
print(add)