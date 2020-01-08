# 사전(Dictionary) : 키(Key)와 값(Value) 산 상을 원소로 가지는 자료형
dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'effort'
dict['안녕'] = 'Hi'
print(dict)
# 제거
del dict['기적']
dict.clear()
print("사전 자료형의 길이", len(dict))
#for i, k in enumerate(dict):
 #  print("[인덱스 :", i, "]한글 :", k , "영어 :" ,dict[k])