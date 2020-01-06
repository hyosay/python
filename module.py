#모듈(module): 미리 작성된 함수 코드를 모아 놓은 파이썬 파일
import keyword
print(keyword.kwlist)

import math
print(math.pow(3, 2)) #제곱
print(math.sqrt(64))
print(math.gcd(72,24))# 최대 공약수

import lib
print(lib.add(3, 2))
from lib import add #크기가 큻떄
print(add(3,2))
import lib as t #lib 모듈의 이름을 t 로 바꾸어서 사용 가능
print(t.add(3,2))

