# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告註他 比答案大/小

import random
r = random.randint(1, 100)
i = 0
while True:
	num = input('請猜一數字: ')
	i = i + 1
	num = int(num)
	if  r == num:
		print('終於猜對了!')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
print('總共猜了', i ,'次')