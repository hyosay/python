#  튜플(Tuple): 리스트(List)와 비슷한 자료형(변경 불가)
'''
tuple = (1, 2, 3)
for i in tuple:
    print(i)
 '''


list1 = [1, 2, 3]
list2 = [4, 5, 6]

tuple = (list1, list2)
tuple[0] = (9, 9, 9) #이런식으로 직접적으로 바꾸지 못함
tuple[0][0] = 7 # list 안에 있는 값은 바꿀 수 있음
print(tuple)
