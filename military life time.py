#-*-coding: utf-8-*-
import time
import datetime
from datetime import time,date, datetime,timedelta

#time1 =  현재 시간
time1 = datetime.now()
datetime.now()
print(datetime.now())
#time2 = 전역일
time2 = datetime(int(input("Your Discharge year :")),int(input("Your Discharge month :")),int(input("Your Discharge day :")))


# 남은 군생활
#현재 날짜
print("오늘은:", datetime.strftime(time1,'%Y/ %m/ %d'),"입니다.")
#Discharge = time2 - time1 # 남은 군생화
Discharge = str(time2 - time1)
print("남은 군생화:",time2 - time1)
#전역 전 100일 time3 =  time2 - timnedelta(days = 100)
print(datetime.strftime(time1, "%d"))
time3 = time2 - timedelta(days=100)

if(time2 - time1 < time2 - time3):
    print(Discharge,"일 만 군생활 하면 민간인입니다")
if(time2 - time1 > time2 - time3):
    print(time2 - time1 ,"일 이나 남으셨군요. 힘내십시요")
