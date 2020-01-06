# 반복문 : 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현: range(시작, 끝)

a = 0
sum = 0
while a < 10:

    a = a + 1
    if a % 2  == 0:
        print(a)
        sum = sum + a

print(sum)
add = 0.
for i in range(1,12):
    if i % 2 == 0:
        add = add + i
        print(i)
print(add)

A = 1
B = 0

print(A != B)
print(A == B)
print(A > B)
print(A < B)
print(not B)
if True or False:
    print('안뇽')