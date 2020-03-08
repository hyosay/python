
import random
c = 100


for i in range(1, 100):
    d = random.randint(1, 10)
    c = c - d
    if c < 0:
        break

    print(c)




